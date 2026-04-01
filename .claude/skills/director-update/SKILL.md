---
name: director-update
description: 導演模式設定更新：讀取相關設定檔、套用修改、更新 glossary、commit
disable-model-invocation: true
allowed-tools: Read, Edit, Write, Grep, Glob, Bash, Agent
argument-hint: [修改指令]
---

# /director-update — 導演模式設定更新

使用者以導演身份下達了設定變更指令。請依序執行：

## 步驟 1：分析指令

1. 解析使用者的修改指令：`$ARGUMENTS`
2. 判斷影響範圍——哪些檔案需要修改：
   - `characters.md` — 角色設定
   - `items/*.md` — 物件設定
   - `worldbuilding/*.md` — 世界觀
   - `glossary/*.md` — 名詞解釋
   - `outline-series*.md` — 大綱
   - `sessions/series*/session_*.md` — 已寫的故事
   - `terminology/*.md` — 技術教學

## 步驟 2：讀取受影響檔案

1. 逐一讀取所有受影響的檔案
2. 列出每個檔案中需要修改的具體段落
3. 向使用者呈現修改計畫：

```
📋 修改計畫：
- [檔案A]：[要改什麼]
- [檔案B]：[要改什麼]
- [檔案C]：[要改什麼]
確認執行？
```

4. **等待使用者確認後才執行修改**

## 步驟 3：執行修改

1. 依計畫逐一修改檔案
2. 每修改一個檔案後列出變更摘要
3. 如果修改涉及名詞變更，同步更新 `glossary/core-terms.md`
4. 如果修改涉及角色變更，同步更新 `characters.md`

## 步驟 4：一致性檢查

1. 用 Grep 搜尋整個專案，確認舊的用語/設定沒有殘留
2. 如發現不一致，列出並修正

## 步驟 5：Commit

1. `git add` 所有變更的檔案
2. Commit message 格式：
   ```
   導演指令：[一句話摘要]

   - [列出主要變更]

   Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
   ```
3. **不自動 push**——讓使用者確認後再 push

## 輸出格式

```
🎬 導演指令執行完成
📝 修改了 N 個檔案：
  - [檔案列表及摘要]
🔍 一致性檢查：[通過 / 發現 X 處已修正]
💾 已 commit（尚未 push）
```
