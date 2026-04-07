#!/usr/bin/env python3
"""
Claude Quest Builder — Project Visualizer
生成 Mermaid 圖：git 分支、worktree、session 進度
"""

import subprocess
import os
import re
from pathlib import Path

NOVEL_DIR = Path(__file__).parent.parent
SESSIONS_DIR = NOVEL_DIR / "sessions" / "series1"

# Session 主題對照
STATUS_MAP = {
    "✅ 已改寫": "DONE",
    "📝 接龍中": "WIP",
    "🔲 骨架": "SKELETON",
    "🔲 未開始": "TODO",
}

SESSION_TITLES = {
    "001": "What Is an Agent?",
    "002": "Tool Use",
    "003": "TodoWrite",
    "004": "Subagents",
    "005": "Skill Loading",
    "006": "Context Compact",
    "007": "Task System",
    "008": "Background Tasks",
    "009": "Agent Teams",
    "010": "Team Protocols",
    "011": "Autonomous Agents",
    "012": "Worktree Isolation",
}


def run(cmd, cwd=NOVEL_DIR):
    result = subprocess.run(
        cmd, shell=True, capture_output=True, cwd=cwd,
        env={**os.environ, "PYTHONIOENCODING": "utf-8"}
    )
    stdout = result.stdout or b""
    return stdout.decode("utf-8", errors="replace").strip()


def get_worktrees():
    """Parse git worktree list"""
    raw = run("git worktree list --porcelain")
    trees = []
    current = {}
    for line in raw.splitlines():
        if line.startswith("worktree "):
            if current:
                trees.append(current)
            current = {"path": line.split(" ", 1)[1]}
        elif line.startswith("branch "):
            branch = line.split("refs/heads/")[-1]
            current["branch"] = branch
        elif line.startswith("HEAD "):
            current["head"] = line.split(" ", 1)[1][:7]
        elif line == "bare":
            current["bare"] = True
    if current:
        trees.append(current)
    return trees


def get_branches():
    """Get all local branches with latest commit"""
    raw = run('git branch -v --format="%(refname:short)|%(objectname:short)|%(contents:subject)"')
    branches = []
    for line in raw.splitlines():
        parts = line.strip('"').split("|", 2)
        if len(parts) >= 2:
            branches.append({
                "name": parts[0].strip(),
                "hash": parts[1].strip(),
                "subject": parts[2].strip() if len(parts) > 2 else "",
            })
    return branches


def get_commits():
    """Get recent commits on master for gitGraph"""
    raw = run('git log master --oneline --no-walk=unsorted --format="%h|%s" -10')
    commits = []
    for line in raw.splitlines():
        parts = line.strip('"').split("|", 1)
        if len(parts) == 2:
            commits.append({"hash": parts[0], "subject": parts[1]})
    return commits[::-1]  # oldest first


def get_session_status():
    """Check each session file for content status"""
    sessions = []
    for num, title in SESSION_TITLES.items():
        session_file = SESSIONS_DIR / f"session_{num}.md"
        chapter_file = SESSIONS_DIR / f"chapter_{num}.md"
        status = "🔲 未開始"
        if chapter_file.exists():
            status = "✅ 已改寫"
        elif session_file.exists():
            content = session_file.read_text(encoding="utf-8", errors="ignore")
            if "（待開始）" in content or len(content.strip().splitlines()) < 25:
                status = "🔲 骨架"
            else:
                status = "📝 接龍中"
        sessions.append({"num": num, "title": title, "status": status})
    return sessions


def gen_worktree_diagram(trees, branches):
    """Graph TD: worktree + branch 關係"""
    lines = ["```mermaid", "graph TD"]

    # 主 worktree
    lines.append('    MASTER["novel/\\nmaster"]')

    for tree in trees:
        if tree.get("branch") == "master":
            continue
        branch = tree.get("branch", "unknown")
        path = Path(tree["path"]).name
        node_id = branch.replace("-", "_").replace("/", "_")
        lines.append(f'    {node_id}["{path}/\\n{branch}"]')
        lines.append(f'    MASTER -->|worktree| {node_id}')

    # 其他分支（非 worktree）
    worktree_branches = {t.get("branch") for t in trees}
    for b in branches:
        if b["name"] not in worktree_branches and b["name"] != "master":
            node_id = b["name"].replace("-", "_").replace("/", "_")
            name = b["name"]
            h = b["hash"]
            lines.append(f'    {node_id}["branch: {name}\\n{h}"]')
            lines.append(f'    MASTER -.->|branch| {node_id}')

    lines.append("```")
    return "\n".join(lines)


def gen_session_progress(sessions):
    """Graph LR: session 進度條"""
    lines = ["```mermaid", "graph LR"]
    lines.append("    subgraph CQB[Claude Quest Builder Series 1]")

    prev = None
    for s in sessions:
        node_id = f"S{s['num']}"
        status = STATUS_MAP.get(s["status"], s["status"])
        title = s["title"].replace('"', "'").replace("&", "and")
        label = f"s{s['num']} {title}\\n[{status}]"
        lines.append(f'        {node_id}["{label}"]')
        if prev:
            lines.append(f'        {prev} --> {node_id}')
        prev = node_id

    lines.append("    end")
    lines.append("```")
    return "\n".join(lines)


def gen_git_graph():
    """gitGraph: commit 歷史 + branch"""
    raw_log = run(
        'git log --all --oneline --format="%D|%h|%s" -20'
    )

    lines = ["```mermaid", "gitGraph"]
    lines.append('   commit id: "init"')

    # Simplified: just show key commits on master
    master_commits = run('git log master --oneline --format="%h|%s" -6').splitlines()
    for c in reversed(master_commits):
        parts = c.split("|", 1)
        if len(parts) == 2:
            h, subj = parts
            # Shorten subject
            short = subj[:30].replace('"', "'")
            lines.append(f'   commit id: "{short}"')

    # Show session-002 branch
    s002_commits = run('git log session-002 ^master --oneline --format="%h|%s"').splitlines()
    if s002_commits:
        lines.append('   branch session-002')
        lines.append('   checkout session-002')
        for c in reversed(s002_commits):
            parts = c.split("|", 1)
            if len(parts) == 2:
                h, subj = parts
                short = subj[:30].replace('"', "'")
                lines.append(f'   commit id: "{short}"')

    lines.append("```")
    return "\n".join(lines)


def main():
    trees = get_worktrees()
    branches = get_branches()
    sessions = get_session_status()

    output = []
    output.append("# Claude Quest Builder — Project Visualization")
    output.append("")

    output.append("## Git 分支 & Worktree")
    output.append("")
    output.append(gen_worktree_diagram(trees, branches))
    output.append("")

    output.append("## Commit 歷史")
    output.append("")
    output.append(gen_git_graph())
    output.append("")

    output.append("## Session 進度")
    output.append("")
    output.append(gen_session_progress(sessions))
    output.append("")

    output.append("## 當前 Worktrees")
    output.append("")
    output.append("| 路徑 | 分支 | HEAD |")
    output.append("|------|------|------|")
    for t in trees:
        path = Path(t["path"]).name
        branch = t.get("branch", "—")
        head = t.get("head", "—")
        output.append(f"| `{path}/` | `{branch}` | `{head}` |")
    output.append("")

    import sys
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    print("\n".join(output))


if __name__ == "__main__":
    main()
