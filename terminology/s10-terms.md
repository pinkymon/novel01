# Session 10 技術名詞教學：Team Protocols

> 參考：`reference/series1idea/s10-team-protocols.md`

## 核心概念

**Team Protocols** 為團隊溝通建立規則。Request-Response Protocol 用唯一識別碼追蹤每次請求，確保「誰問了什麼」和「誰回了什麼」不會搞混。FSM 管理請求的狀態轉換（pending → approved/rejected）。

特殊協議包括 Plan Approval（執行前需要批准）和 Shutdown Handshake（優雅關閉，確認所有人安全）。

## 名詞表

| 名詞 | 詞性 | 技術定義 | 故事類比 |
|------|------|----------|----------|
| Request-Response Protocol | N | 以唯一識別碼追蹤的非同步協議 | 像是正式的委託書（暫定） |
| FSM (Finite State Machine) | N | 管理請求狀態轉換的有限狀態機 | 委託的流程（暫定） |
| Plan Approval | N | 提交計畫由領導者審查批准的機制 | 作戰計畫需要隊長批准（暫定） |
| Shutdown Handshake | N | 優雅關閉的確認協議 | 撤退的暗號（暫定） |
| Request Correlation | N | 用唯一 ID 將請求與回應綁定 | 委託編號（暫定） |

## RPG 世界的理解方式

隊伍組起來了，但沒有規則的隊伍就是一盤散沙。Protocol 就是隊伍的通訊規矩。

你不能隨便喊一聲「去打左邊那隻」然後就跑。你得寫一張正式的委託書，附上編號。隊長看了，批准或駁回。這樣才不會出現「五個人同時衝向同一隻史萊姆」的混亂。

撤退也是——不能一個人說撤就撤。隊長發出暗號，每個人確認收到，最後一起撤。這就是 Handshake。

## 延伸閱讀

- 原始技術文件：`reference/series1idea/s10-team-protocols.md`
