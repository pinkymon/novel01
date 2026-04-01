# Session 011 — Autonomous Agents
**日期**：
**參考**：`reference/series1idea/s11-autonomous-agents.md`

> *"Teammates scan the board and claim tasks themselves"*

## 技術主題
- 自主生命週期：WORK → IDLE（輪詢信箱/任務板）→ shutdown 或繼續
- scan_unclaimed_tasks()：找到待認領的任務
- 身份重注入：壓縮後可能忘記自己是誰

## RPG 映射
- 隊友自己去任務板找工作——不再需要隊長逐一指派
- 閒置的隊友會主動巡邏、認領任務
- 「我是誰」的危機：壓縮記憶後，隊友可能忘記自己的身份

## 接龍記錄

（待開始）
