# Session 012 — Worktree + Task Isolation
**日期**：
**參考**：`reference/series1idea/s12-worktree-task-isolation.md`

> *"Each works in its own directory, no interference"*

## 技術主題
- 雙狀態平面：control plane（.tasks/）管目標，execution plane（.worktrees/）管目錄
- Git worktree 分支命名：wt/{task_name}
- 事件流：events.jsonl 記錄每一步
- 崩潰恢復：從磁碟重建狀態

## RPG 映射
- 平行世界：每個隊友在自己的維度中工作，互不干涉
- 兩個同時編輯同一份地圖的人不會衝突
- 事件水晶球：記錄每一個維度中發生的事，可以回溯
- Series 1 的終極形態：從一根木棍到平行世界的冒險團

## 接龍記錄

（待開始）
