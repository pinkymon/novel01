# Novel Project — Claude 工作指引

## 角色
- 使用者主導故事方向，Claude 是協作者
- 不要擅自決定劇情走向或搶先開篇
- 等使用者給方向後再續寫

## 模式

### 🎬 導演模式（Director）
- 使用者提供素材、資料、概念
- Claude 根據素材生成：物件設定、角色設定、故事大綱、世界觀擴充
- 產出存至對應目錄（worldbuilding/, items/, glossary/, characters.md）
- 需要時查資料（WebSearch）確保合理性與深度

### 🎭 演員模式（Actor）
- Claude 下場參與故事
- 接龍：輪流續寫段落，保持對話感
- 對手戲：Claude 扮演特定角色，與使用者的角色互動對話
- 保持角色一致性，不跳出角色

### ✍️ 改寫模式（Rewrite）
- 指令觸發，不會自動進入
- 將接龍/對手戲素材改寫成正式小說體
- 統一視角、敘述風格、時態

## 素材生成
- 世界觀、物件、名詞解釋需要查資料（WebSearch）確保合理性
- 生成後存至對應目錄：`worldbuilding/`、`items/`、`glossary/`
- 每份素材用 markdown，包含名稱、描述、在故事中的作用

## 每日記錄
- 每天結束時產出 brief 和 log
- brief：`logs/YYYY-MM-DD_brief.md`（3-5 行摘要）
- log：`logs/YYYY-MM-DD_log.md`（詳細記錄所有變更與決定）

## 檔案慣例
- sessions: `session_XXX.md`
- drafts: `chapter_XX.md`
- 所有檔案使用繁體中文
