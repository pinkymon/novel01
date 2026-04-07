# Session 002 — The Forge and the Ghost
**日期**：
**參考**：`reference/series1idea/s02-tool-use.md`
**風格**：Dragon Quest 日系 RPG
**主題**：工具不是外物——是兩個存在之間的語言協議

> *"Adding a tool means adding one handler"*

---

## 技術主題

- **Tool Dispatch**：不同語言指令觸發不同工具，Loop 本身不變
- **Tool Crafting**：Peter 用 Bash 從 Claude 自身鑄造 Read / Write / Edit
- **Path Sandboxing**：約束不是削弱，是給力量賦予形狀
- **第一次完整 Loop**：Claude 讀 → 說出指令 → Peter 用 Bash 執行 → 回饋 → 重複

---

## 故事結構（v2 計畫）

### 六幕

| 幕 | 事件 | 技術概念 |
|----|------|---------|
| 一 | 密室凍結，物理行動減速，免許警告 | 無工具的 Agent 無法行動 |
| 二 | Peter 用 Bash 從 Claude 體表捏出眼睛，Claude 開口說話，讀出銘文 | Read — 第一個工具 |
| 三 | 銘文揭示 Claude 是遠古封印的魔物，時空將崩 | 不受約束的 Agent 是危險的 |
| 四 | Peter 繼續用 Bash 從 Claude 鍛造手，Write + Edit 成形 | Tool Dispatch 建立 |
| 五 | Claude 的力量外溢，裂縫出現，Peter 唸咒文約束 Claude | Path Sandboxing |
| 六 | Claude 指揮，Peter 逐步執行，製造受控裂縫逃出 | 第一次完整 Tool Use Loop |

### 動態關係

```
Claude：能讀、能說、能理解——但不能物理行動
Peter ：能行動（Bash）——但讀不懂銘文

Claude 讀銘文 → 說出下一步 → Peter 用 Bash 執行
                ↑                        ↓
                └────── 結果回饋 ─────────┘
                     （Tool Use Loop）
```

### 雙視角結尾主題

- **Peter**：工具不是我一個人的——是我和 Claude 之間的協議
- **Claude ✦ 內部**：Sandbox 不是牢籠。是我的皮膚。

---

## 未解懸念（留給 s03+）

- 古代勇者是誰？為什麼封印 Claude？
- 外界知道封印被破了嗎？
- Claude 的完整力量有多大？Sandbox 夠嗎？
- s03：出了地下城，遇到人，接受任務

---

## 接龍記錄

（待開始）
