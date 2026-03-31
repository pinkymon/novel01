# 小說創作專案

## 協作規則

1. **使用者主導** — 故事方向、劇情走向由使用者決定
2. **開放性設計** — 隨時加入新元素（世界觀、物件、名詞）
3. **Claude 負責研究與生成** — 世界觀/物件/名詞需查資料後產出
4. **模式切換** — 預設為對話/接龍模式，收到指令時改寫成小說體
5. **每日產出** — 每天生成 brief（進度摘要）和 log（詳細記錄）

## 目錄結構

```
novel/
├── sessions/        # 接龍紀錄
├── drafts/          # 改寫草稿（小說體）
├── worldbuilding/   # 世界觀設定
├── items/           # 物件設定
├── glossary/        # 名詞解釋
├── logs/            # 每日 brief & log
├── outline.md       # 故事大綱
├── characters.md    # 角色設定
└── README.md        # 本說明
```

## 工作流程

### 對話/接龍模式（預設）
- 使用者給方向或起頭，Claude 續接
- 每次接龍存至 `sessions/session_XXX.md`

### 改寫模式（指令觸發）
- 使用者下指令後，將接龍素材改寫成正式小說
- 存至 `drafts/chapter_XX.md`

### 素材生成
- 世界觀 → `worldbuilding/主題名.md`
- 物件 → `items/物件名.md`
- 名詞 → `glossary/名詞.md`
- Claude 會查資料確保合理性

### 每日記錄
- `logs/YYYY-MM-DD_brief.md` — 當日進度摘要
- `logs/YYYY-MM-DD_log.md` — 詳細記錄

## 待補充設定

- [ ] 小說類型
- [ ] 故事背景與世界觀
- [ ] 主角設定
- [ ] 預計長度
