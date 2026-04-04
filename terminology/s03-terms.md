# Session 03 技術名詞教學：TodoWrite

> 參考：`reference/series1idea/s03-todowrite.md`

## 核心概念

**TodoWrite** 解決了 Agent 在長時間工作中「忘記計畫」的問題。透過 TodoManager 管理任務列表，強制同時只有一個任務處於進行中，配合 Nag Reminder 機制在模型漂移時重新拉回注意力。

核心洞察：LLM 的上下文會隨著工具結果的累積而「褪色」（Context Fading），計畫的優先級被壓低。TodoWrite 是對抗這種遺忘的武器。

## 名詞表

| 名詞 | 詞性 | 技術定義 | 故事類比 |
|------|------|----------|----------|
| TodoManager | N | 儲存任務列表並強制同時只有一個任務進行中的狀態管理物件 | 像是冒險者筆記本（暫定） |
| Task Status | N | 任務的狀態標籤：pending、in_progress、completed | 任務的進度標記（暫定） |
| Nag Reminder | N | 模型多輪未更新任務時系統自動注入的提醒 | 像是公會櫃台的催促（暫定） |
| Sequential Focus | N | 同時只有一個任務進行中的約束 | 專注的力量——分心就會迷路（暫定） |
| Context Fading | N | 長對話中系統提示優先級逐漸降低的現象 | 記憶的模糊（暫定） |

## RPG 世界的理解方式

冒險者在地下城裡走了很久很久，走到後來忘了自己進來是要幹嘛的。這就是 Context Fading。

筆記本的存在就是為了解決這個問題——把要做的事寫下來，一次只做一件，做完打勾。如果太久沒翻筆記本，公會會派人來提醒你：「喂，你的任務還記得嗎？」

聽起來很簡單，但這可能是冒險者最容易忽略的能力——記得自己要做什麼。

## 延伸閱讀

- 原始技術文件：`reference/series1idea/s03-todowrite.md`
