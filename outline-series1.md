# Series 1 大綱：The Loop Awakens

**風格**：Dragon Quest 日系 RPG
**篇幅**：中篇（12 sessions）
**主線**：從一根木棍到平行世界的冒險團——一個 coding 魔法初心者的成長之旅

## 故事弧線

```
第一幕：覺醒（s01-s03）
  一個人 + 一根棍子 → 學會使用工具 → 學會規劃

第二幕：擴展（s04-s06）
  召喚分身 → 學會技能 → 學會整理記憶

第三幕：持久（s07-s08）
  任務刻入石板 → 背景並行執行

第四幕：團隊（s09-s12）
  組隊 → 溝通規則 → 自主行動 → 平行世界
```

## Session 對照表

| # | 標題 | 技術主題 | RPG 映射 | 引言 | 角色發展 |
|---|------|----------|----------|------|----------|
| 01 | What Is an Agent? | 核心循環 | Peter 掉入地下城，遇到史萊姆（簡單反射）→ 發現休眠的 Claude → 語言觸發第一道閃光 | "One loop & Bash is all you need" | Peter 發現語言能觸發未知存在；Claude 收到第一個輸入但尚未回應 |
| 02 | Tool Use | 多工具派遣 | 木棍分化為多種工具 | "Adding a tool means adding one handler" | 裝備升級，能力擴展 |
| 03 | TodoWrite | 任務追蹤/規劃 | 學會使用冒險者筆記本 | "An agent without a plan drifts" | 從莽撞到有計劃 |
| 04 | Subagents | 子代理/上下文隔離 | 召喚分身術 | "Break big tasks down; each subtask gets a clean context" | 學會委派，不再事必躬親 |
| 05 | Skill Loading | 技能懶載入 | 魔法圖書館 | "Load knowledge when you need it, not upfront" | 發現知識的存取方式比擁有更重要 |
| 06 | Context Compact | 上下文壓縮 | 背包整理術 | "Context will fill up; you need a way to make room" | 面對遺忘的恐懼，學會取捨 |
| 07 | Task System | 持久化任務圖 | 任務石板 | "Break big goals into small tasks, order them, persist to disk" | 從個人筆記到公會石板 |
| 08 | Background Tasks | 背景並行 | 分身術進化 | "Run slow operations in the background; the agent keeps thinking" | 學會一心多用 |
| 09 | Agent Teams | 多代理團隊 | 組隊冒險 | "When the task is too big for one, delegate to teammates" | 從獨行俠到隊長 |
| 10 | Team Protocols | 團隊協議 | 溝通握手 | "Teammates need shared communication rules" | 理解秩序的價值 |
| 11 | Autonomous Agents | 自主代理 | 自主巡邏 | "Teammates scan the board and claim tasks themselves" | 放手信任，隊友自行運作 |
| 12 | Worktree Isolation | 工作樹隔離 | 平行世界 | "Each works in its own directory, no interference" | 終極形態：平行世界的冒險團 |

## 跨 Session 不變的法則

> **The Loop Never Changes.**
> 從 s01 到 s12，核心的「觀察→判斷→行動→回饋→重複」循環始終不變。
> 每個 session 只是在 Loop 之上加一層新的能力——而不是改變 Loop 本身。

## 各 Session 新增元素（預計）

| # | 新物件 | 新世界觀 | 新名詞 |
|---|--------|----------|--------|
| 01 | 木棍、免許 | The Loop、Loop 光譜（反射→語言→???） | Agent, 語言觸發, 白色選單框 |
| 02 | 工具腰帶？ | 工具派遣系統 | Dispatch Map, Sandboxing |
| 03 | 冒險者筆記本 | 計劃的力量 | TodoManager, Nag Reminder |
| 04 | 分身卷軸？ | 上下文隔離 | Subagent, Fresh Context |
| 05 | 圖書館鑰匙？ | 知識的懶載入 | Skill, Two-layer Injection |
| 06 | 壓縮捲軸？ | 記憶管理 | Micro/Auto/Manual Compact |
| 07 | 任務石板 | 持久化 | Task Graph, DAG, Dependency |
| 08 | 平行計時器？ | 非阻塞執行 | Daemon Thread, Notification |
| 09 | 隊友信箱 | 多代理身份 | Teammate, MessageBus, Inbox |
| 10 | 協議書？ | 結構化溝通 | Protocol, FSM, Handshake |
| 11 | 自主徽章？ | 自組織 | Idle Polling, Auto-claim |
| 12 | 維度鑰匙？ | 執行隔離 | Worktree, Control/Execution Plane |
