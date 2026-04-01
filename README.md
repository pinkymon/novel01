# 小說創作專案

## 協作規則

1. **使用者主導** — 故事方向、劇情走向由使用者決定
2. **開放性設計** — 隨時加入新元素（世界觀、物件、名詞）
3. **Claude 負責研究與生成** — 世界觀/物件/名詞需查資料後產出
4. **模式切換** — 導演 / 演員 / 改寫 / 系統 四種模式
5. **每日產出** — 每天生成 brief（進度摘要）和 log（詳細記錄）

## 目錄結構

```
novel/
├── sessions/
│   └── series1/         # Series 1: The Loop Awakens（12 sessions）
│       ├── session_001.md
│       ├── ...
│       └── session_012.md
├── drafts/              # 改寫草稿（小說體）
├── worldbuilding/       # 世界觀設定
├── items/               # 物件設定
├── glossary/            # 名詞解釋（故事內）
├── terminology/         # 技術名詞教學（用 RPG 類比解釋真實技術）
├── reference/           # 參考資料（.gitignore，不進 repo）
├── logs/                # 每日 brief & log
├── outline.md           # 總體大綱
├── outline-series1.md   # Series 1 大綱（12 session 對照表）
├── characters.md        # 角色設定
├── CLAUDE.md            # 協作工作指引
└── README.md            # 本說明
```

## Series 概念

故事以 **Series** 為單位組織，每個 Series 包含多個 Session。

### Series 1: The Loop Awakens
- **風格：Dragon Quest 日系 RPG**
- 12 個 sessions，每個對應一個技術概念
- 技術概念映射為 DQ 風格 RPG 故事元素
- 參考資料：`reference/series1idea/s01~s12`
- 大綱：`outline-series1.md`

## 工作流程

### 🎬 導演模式 — 提供素材，Claude 生成設定
### 🎭 演員模式 — Claude 下場接龍或對手戲
### ✍️ 改寫模式 — 素材改寫成正式小說
### ⚙️ 系統模式 — 處理專案設定、規則、目錄

### 素材生成
- 世界觀 → `worldbuilding/主題名.md`
- 物件 → `items/物件名.md`
- 名詞 → `glossary/名詞.md`
- 技術教學 → `terminology/term-name.md`（用 RPG 類比教學真實技術）
- Claude 會查資料確保合理性

### Session 結束規則
- 導演可根據故事節奏建議結束，或使用者直接下令
- 結束時：儲存記錄、更新大綱、commit & push

### 每日記錄
- `logs/YYYY-MM-DD_brief.md` — 當日進度摘要
- `logs/YYYY-MM-DD_log.md` — 詳細記錄
