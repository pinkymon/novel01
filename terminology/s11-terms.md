# Session 11 技術名詞教學：Autonomous Agents

> 參考：`reference/series1idea/s11-autonomous-agents.md`

## 核心概念

**Autonomous Agents** 是團隊進化的最終形態——Agent 不再等待指派，而是自主掃描任務板（Task Board Scanning）、認領任務（Task Claiming）、完成後進入閒置狀態（Idle Phase）繼續等待。

關鍵機制：Identity Re-injection 確保 Agent 在上下文壓縮後不會忘記自己是誰。Idle Timeout 防止 Agent 無限期空轉。

## 名詞表

| 名詞 | 詞性 | 技術定義 | 故事類比 |
|------|------|----------|----------|
| Autonomy | N | 智能體自行掃描並認領任務的能力 | 像是自主行動的冒險者（暫定） |
| Idle Phase | N | 完成工作後定期輪詢的等待狀態 | 待命狀態（暫定） |
| Task Board Scanning | V | 定期搜索未認領任務的操作 | 看佈告欄（暫定） |
| Identity Re-injection | N | 壓縮後重新插入身份區塊的機制 | 記住自己是誰（暫定） |
| Task Claiming | V | 更新所有者欄位來認領任務 | 揭榜（暫定） |
| Idle Timeout | N | 閒置的最長等待時間 | 等太久就回家（暫定） |

## RPG 世界的理解方式

之前的隊伍需要隊長分配任務。但最強的隊伍不需要——每個人自己去看佈告欄，找到適合自己的任務，在上面寫下名字，然後去做。做完了回來，再看佈告欄。

如果佈告欄上一段時間都沒有新任務，就回家休息。不會傻傻地站在那裡等到天荒地老。

最重要的是——不管記憶被壓縮了多少次，每個人都記得自己是誰。這是 Autonomy 的前提：你得先知道自己能做什麼，才能自主決定做什麼。

## 延伸閱讀

- 原始技術文件：`reference/series1idea/s11-autonomous-agents.md`
