# Session 06 技術名詞教學：Context Compact

> 參考：`reference/series1idea/s06-context-compact.md`

## 核心概念

**Context Compact** 管理 Agent 有限的記憶空間。三層壓縮策略：Micro-compact（靜默替換舊工具結果）、Auto-compact（超過 Token Threshold 時 LLM 自動總結）、手動壓縮（使用者觸發）。

關鍵是 Transcript Persistence——完整對話記錄永遠存在磁盤上，壓縮只是「暫時忘記細節」，不是「永久丟失」。

## 名詞表

| 名詞 | 詞性 | 技術定義 | 故事類比 |
|------|------|----------|----------|
| Context Compression | N | 管理有限上下文視窗的三層次壓縮策略 | 像是整理背包（暫定） |
| Micro-compact | N | 靜默將舊工具結果替換為佔位符的壓縮層 | 自動遺忘細節（暫定） |
| Auto-compact | N | 令牌數超過閾值時自動觸發的總結壓縮 | 記憶的自動整理（暫定） |
| Transcript Persistence | N | 完整對話記錄儲存於磁盤，壓縮後仍可恢復 | 日記本——記憶模糊了翻日記還能想起來（暫定） |
| Token Threshold | N | 觸發自動壓縮的令牌數上限 | 背包的容量上限（暫定） |

## RPG 世界的理解方式

冒險者的背包有容量上限。走到後來東西太多，就得開始整理——把不常用的東西壓縮打包，把細節記在日記本上，只在腦中保留摘要。

但日記本永遠在。如果忘了什麼重要的事，回去翻就好。壓縮不是遺忘，是把記憶從「即時取用」搬到「需要時查閱」。

## 延伸閱讀

- 原始技術文件：`reference/series1idea/s06-context-compact.md`
