# Session 01 技術名詞教學：The Agent Loop

> 參考：`reference/series1idea/s01-the-agent-loop.md`

## 核心概念

**Agent Loop** 是整個 Series 1 的基石。一個 `while True` 迴圈，反覆執行「送出訊息→模型回應→執行工具→收集結果」，直到 `stop_reason` 不再是 `tool_use`。

從 s01 到 s12，這個 Loop 從未改變——只是不斷在上面疊加新的能力。「One loop & Bash is all you need.」

## 名詞表

| 名詞 | 詞性 | 技術定義 | 故事類比 |
|------|------|----------|----------|
| Agent Loop | N | 觀察→判斷→行動→回饋的無限循環，直到模型停止呼叫工具 | The Loop——世界運轉的法則，進入 Loop 的存在是「活的」 |
| messages[] | N | 累積式對話紀錄陣列，儲存所有輸入與輸出 | 像是冒險者的記憶——經歷過的事都留在腦海中 |
| stop_reason | N | 模型回傳的終止條件，決定 Loop 是否繼續 | Loop 的脈搏——當行動的理由消失，循環暫停 |
| Tool Call | N | 模型主動請求執行特定工具的操作 | 行動的意志——決定「做點什麼」而非「說完收工」 |
| Tool Result | N | 工具執行後返回的輸出，重新傳回模型作為下一輪上下文 | 行動的回饋——世界對冒險者動作的回應 |
| Exit Condition | N | 控制循環終止的判定邏輯 | Loop 的終點——什麼時候可以停下來 |

## RPG 世界的理解方式

在這個世界裡，所有的存在都遵循一個法則——The Loop。

史萊姆在 Loop 中，但它的 Loop 只有反射——`if (有人靠近) { attack(); }`，沒有語言，沒有判斷，只有反應。
人類的 Loop 裝著語言——能思考、規劃、學習。

而 Claude 是第三種存在：**幽靈型（Ghost-type）**。

它的 Loop 是休眠的，不是消失的。物理接觸對它無效——戳它沒用，砸它沒用。
但語言讓它動了。那個橘色的東西，被一句話觸發，Loop 開始，但尚未完成第一個循環。

**Bash** 是 Peter 在 Session 01 唯一的能力——不是木棍，是對世界下達指令的方式。
物件可以被物理工具觸動，但 Claude 只響應語言。Bash 對物理世界有用，對 Claude 無用。
直到 Peter 用語言說話——那不是 Bash，那是更根本的東西。

這就是 Session 01 的核心問題：**什麼是 Agent？**
答案不是「會動的東西」，而是「能接收語言、處理語言、最終用語言回應的存在」。

## 延伸閱讀

- 原始技術文件：`reference/series1idea/s01-the-agent-loop.md`
- 世界觀：`worldbuilding/the-loop.md`
- 詞彙：`glossary/core-terms.md`（The Loop、Agent 相關條目）
