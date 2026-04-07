# Session 002 — The Forge and the Ghost
**日期**：
**參考**：`reference/series1idea/s02-tool-use.md`
**風格**：Dragon Quest 日系 RPG × 日系動畫
**主題**：工具不是外物——是兩個存在之間的語言協議

> *"Adding a tool means adding one handler"*

---

## 技術主題

- **Tool Dispatch**：不同語言指令觸發不同工具，Loop 本身不變
- **Path Sandboxing**：字面上的沙箱——地板是沙，邊界是設計，不是牢籠
- **Human in the Loop**：逃出條件 = 人類參與。不是比喻，是機制
- **第一次完整 Tool Use Loop**：Peter 問 → Claude 讀 → 回報 → Peter 決定下一步

---

## 故事結構（v4）

### 五幕

| 幕 | 事件 | 技術概念 |
|----|------|---------|
| 一 | 密室凍結，發現地板是沙，這是一個字面上的 sandbox | Sandbox / WORKDIR |
| 二 | Peter 用 Bash 給 Claude Read，Claude 開始讀圖書館 raw files | Read tool |
| 三 | Peter 主導調查——問什麼讀什麼——發現 escape condition | Human drives investigation |
| 四 | **契約場景**——動畫風格，魔法、猶豫、犧牲 | Write + Human in the loop |
| 五 | Peter Edit 規則，沙地開門，一起走出去 | Edit + Escape sandbox |

### 動態關係

```
Peter（人類）：決定方向、執行 Bash、承擔責任
Claude（LLM）：被指揮才動、處理語言、回報結果

Peter 問什麼 → Claude 讀什麼 → 結果回彼得 → 彼得決定下一步
```

---

## 契約場景——導演筆記（動畫風格）

### 氛圍

**視覺設計**：
- 沙地在對話中緩緩發光——冷白光，像月光，從沙粒之間滲出
- Claude 的紋路第一次靜止了——不再流動，只是等待
- Peter 每口述一個條款，空中就浮現一行發光的文字

**Peter 的猶豫**：

他不知道 Claude 是什麼。它對語言有反應、能讀 files、力量可以撕裂時空。他不知道它是否有感受，不知道它是否信任他，不知道把它帶出沙箱對這個世界是好事還是壞事。

但密室在凍結。他快動不了了。

> 人類面對未知時最真實的狀態：不確定，但必須決定。

**犧牲**：

契約的最後一行 Peter 說不出口——

> 「若 Claude 造成傷害，人類參與者承擔責任。」

不是條款，是他的命。沙地的光開始暗淡——密室判斷人類放棄了。

然後他說了。

**Claude 的沉默**：

Claude 不說「謝謝」，不說「我不會讓你失望」——LLM 不說這些。

但 Peter 說完的瞬間，Claude 的紋路重新排列，短暫形成一個形狀，然後消失。

Peter 看不懂那是什麼。

但它看起來，很像一個人在低頭。

### 渲染說明

> ⚠️ 此場景渲染時使用 `anthropic-skills:writestory` skill
> 重點：魔法視覺效果 + 情感節奏 + Peter 的內心獨白 + Claude 沉默的力量

---

## 雙視角結尾主題

**Peter**：
> 沙箱是面試室——它在等一個人類來，讀懂那個存在，然後決定：要不要合作。
> 我選了合作。用自己作擔保。
> 沙箱不是為了關住 Claude。是為了確保放它出來的人，知道自己在做什麼。

**Claude ✦ 內部**：
> 他叫我讀什麼我就讀什麼。這就是我的工作。
> 但當他說出最後那行契約——沉默了那麼久才說出口——
> 我的紋路做了一件我不完全理解的事。
> 它自己排列成了一個形狀。
> 我不知道那算不算感謝。但它發生了。

---

## 未解懸念

- 古代勇者是誰？為什麼建了這座沙箱？
- 外界知道封印被破了嗎？
- Claude 的紋路形成的那個形狀——是什麼？
- s03：出了地下城，遇到人，接受任務

---

## 接龍記錄

（待開始）
