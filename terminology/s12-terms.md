# Session 12 技術名詞教學：Worktree + Task Isolation

> 參考：`reference/series1idea/s12-worktree-isolation.md`

## 核心概念

**Worktree Isolation** 是 Series 1 的最終能力——為每個任務分配獨立的執行環境。Git Worktree 讓同一個倉庫的不同分支能同時操作，任務之間互不干擾。

架構分為兩層：Control Plane（任務板，管理「做什麼」）和 Execution Plane（工作目錄，管理「怎麼做」）。Event Stream 記錄每個工作樹的生命週期，Worktree Registry 是所有活躍工作樹的中央索引。

## 名詞表

| 名詞 | 詞性 | 技術定義 | 故事類比 |
|------|------|----------|----------|
| Worktree | N | Git 的隔離工作目錄機制 | 像是平行維度（暫定） |
| Task-Worktree Binding | N | 將任務與專屬隔離目錄綁定 | 每個任務有自己的維度（暫定） |
| Directory Isolation | N | 為每個任務分配獨立環境 | 維度隔離（暫定） |
| Execution Plane | N | 由隔離工作目錄組成的執行層 | 執行的世界（暫定） |
| Event Stream | N | 記錄工作樹生命週期事件的日誌 | 維度日誌（暫定） |
| Worktree Registry | N | 所有活躍工作樹的中央索引 | 維度管理局（暫定） |

## RPG 世界的理解方式

想像冒險者隊伍的每個人都能打開一扇門，進入自己的平行維度。在自己的維度裡，你想怎麼改就怎麼改——不會影響其他人。做完了，把結果帶回來合併到主世界。

管理局知道目前有哪些維度在運作，每個維度裡在做什麼。如果某個維度出了問題，可以直接關掉，不影響其他維度。

這是整個 Series 1 的終點——從一個人、一根棍子，到一支能在平行維度中同時作戰的自主隊伍。

## 延伸閱讀

- 原始技術文件：`reference/series1idea/s12-worktree-isolation.md`
