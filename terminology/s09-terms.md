# Session 09 技術名詞教學：Agent Teams

> 參考：`reference/series1idea/s09-agent-teams.md`

## 核心概念

**Agent Teams** 讓多個 Agent 以持久身份協作。每個 Persistent Agent 有自己的名字、專長、生命週期（spawn→working→idle→shutdown）。溝通透過 Team Mailbox——基於檔案的非同步信箱，使用 JSONL 日誌確保訊息不遺失。

核心轉變：從「一個人 + 分身」到「一支有固定成員的隊伍」。

## 名詞表

| 名詞 | 詞性 | 技術定義 | 故事類比 |
|------|------|----------|----------|
| Persistent Agent | N | 持續存活於應用生命週期的智能體 | 像是固定隊友（暫定） |
| Team Mailbox | N | 基於檔案的非同步通訊機制 | 隊伍信箱（暫定） |
| Inbox Draining | V | 讀取並清空訊息檔案的操作 | 收信（暫定） |
| Agent Lifecycle | N | 智能體的狀態機：生成→工作→閒置→關閉 | 隊友的一天（暫定） |
| Message Bus | N | 協調多智能體通訊的中樞系統 | 公會的佈告欄（暫定） |

## RPG 世界的理解方式

之前的分身是臨時的——用完就消失。但現在冒險者組了一支正式的隊伍。每個隊友是真實的存在，有名字，有專長，有自己的生活節奏。

隊友之間靠信箱溝通。你在前線打怪的時候，可以往信箱丟一張紙條：「後方有補給需求。」隊友看到了就會去處理。不需要面對面喊話，不需要等對方有空。

## 延伸閱讀

- 原始技術文件：`reference/series1idea/s09-agent-teams.md`
