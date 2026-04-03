# Session 08 技術名詞教學：Background Tasks

> 參考：`reference/series1idea/s08-background-tasks.md`

## 核心概念

**Background Tasks** 讓 Agent 能同時做多件事。長時間操作（如等待回應、執行安裝）在 Daemon Thread 中後台運行，主線程繼續思考和工作。完成結果放入 Notification Queue，在下次 LLM 調用前清空。

核心轉變：從「做一件事→等→做下一件事」（Blocking）到「同時做多件事」（Non-blocking）。

## 名詞表

| 名詞 | 詞性 | 技術定義 | 故事類比 |
|------|------|----------|----------|
| Background Execution | N | 在後台線程中運行長時間操作 | 像是派出信鴿（暫定） |
| Daemon Thread | N | 不阻擋主執行迴圈的後台線程 | 影子分身（暫定） |
| Notification Queue | N | 存儲後台完成結果的線程安全佇列 | 信箱（暫定） |
| Blocking vs Non-blocking | Adj | 站著等 vs 邊走邊等的兩種執行方式 | 兩種做事方式（暫定） |
| Task Spawning | V | 啟動後台任務並立即返回 | 放出信鴿（暫定） |

## RPG 世界的理解方式

之前的分身術（Subagent）是「派出去，等他回來」。Background Task 不一樣——你派出信鴿送信，然後立刻去做下一件事。信鴿回來的時候會把結果放在信箱裡，你空閒了再去看。

冒險者不再需要站在原地等。送出三隻信鴿，自己繼續往前走，等走到下個路口再檢查信箱裡有沒有回信。

## 延伸閱讀

- 原始技術文件：`reference/series1idea/s08-background-tasks.md`
