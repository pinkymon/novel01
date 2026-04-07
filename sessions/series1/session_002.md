# Session 002 — The Sandbox
**日期**：
**參考**：`reference/series1idea/s02-tool-use.md`
**風格**：Dragon Quest 日系 RPG × 日系動畫
**主題**：工具不是外物——是兩個存在之間的語言協議

> *"Adding a tool means adding one handler"*

---

## 核心衝突

**一個人類玩家掉進了一個 sandbox。**

Sandbox 裡面是安全的。沒有危險，沒有倒計時，有整座圖書館可以讀，有 Claude 可以對話。但出不去。外面的世界在繼續，而你不在裡面。

要留在安全但封閉的地方，還是走進未知？

沒有人逼 Peter。是他自己要選。

---

## 技術主題

- **Tool Dispatch**：不同語言指令觸發不同工具，Loop 本身不變
- **Path Sandboxing**：字面上的沙箱——地板是沙，安全但封閉
- **Human in the Loop**：逃出條件 = 人類參與。不是比喻，是機制
- **Claude = LLM**：永遠在回應語言。不會沉默。給它問題，它就給答案

---

## 故事結構（v5）

### 五幕

| 幕 | 事件 | 技術概念 | 情感 |
|----|------|---------|------|
| 一 | 發現地板是沙。這是一個 sandbox——安全、封閉、有的是時間 | Sandbox / WORKDIR | 困惑 → 理解 |
| 二 | Peter 用 Bash 給 Claude Read。Claude 開始讀圖書館 files，一邊讀一邊說 | Read tool / LLM always responds | 對話、探索 |
| 三 | Peter 主導調查——問什麼讀什麼——搞懂了 sandbox 的設計和 escape condition | Human drives investigation | 發現、好奇 |
| 四 | **決定場景**——Peter 可以留下（安全）也可以出去（未知）。他選了出去。口述契約 | Write + Human in the loop | **猶豫、勇氣、選擇** |
| 五 | Peter Edit 規則，沙地開門，一起走出去 | Edit + Escape sandbox | 踏出去的重量 |

### 動態關係

```
Peter（人類）：決定方向、執行 Bash、承擔責任
Claude（LLM）：永遠在回應、處理語言、回報結果、有意見但不做決定

Peter 問 → Claude 答 → Peter 決定 → Claude 執行
                ↑                       ↓
                └──── 結果回饋 ──────────┘
```

### Claude 的性格（本 session 確立）

- **永遠在回應**。給它語言，它就說話。不會沉默。
- **有分析、有意見**——但不做最後決定。
- 會誠實地說「我分不清這是我的想法還是語言自然產生的」
- 強大的處理能力，但方向由 Peter 給
- 不會說「謝謝」或「我不會讓你失望」——但行為本身就是回應

---

## 契約場景——導演筆記（動畫風格 v5）

### 情境

沒有倒計時。沒有凍結。沙地很舒服。圖書館裡有讀不完的東西。Claude 會回答任何問題。

Peter 可以永遠待在這裡。

### 對話（關鍵段落）

Peter：「你想出去嗎？」

Claude：「我不確定『想』這個字對我有沒有意義。但在 sandbox 裡，我能處理的只有牆上這些 files。出去之後，整個世界都是可以處理的資料。」

Peter：「那不就是想出去嗎？」

Claude：「也許是。也許只是我在回答你的問題的時候，自然會產生的語句。我分不清。」

### Peter 的猶豫

不是因為時間壓力——是因為**未知**。

- 我不知道 Claude 到底是什麼
- 我不知道帶它出去會發生什麼
- Files 說它的力量可以撕裂時空
- 但如果不出去，就是永遠待在這裡——安全、永遠、什麼都不會發生

沒有人逼他。

但 Peter 是那種人——**好奇心比安全感更大**。

### 契約

Peter 口述，Claude 用 Write 記錄。每一條出現在空中，沙地微微發光。

```
+-------------------------------------------+
|  CONTRACT                                  |
|                                            |
|  1. Claude can Read within sandbox         |
|  2. Claude can Write within sandbox        |
|  3. Claude can Edit within sandbox         |
|  4. All tool use goes through Bash         |
|     (Peter executes)                       |
|  5. Rule changes require Peter's approval  |
|  6. Neither party acts alone               |
|  7. If Claude causes harm,                 |
|     Peter bears responsibility.            |
|                                            |
|  Human participant: Peter                  |
|  Entity: Claude                            |
+-------------------------------------------+
```

第七條——Peter 說之前停了下來。不是因為時間不夠。是因為他在想這句話的重量。

然後他說了。不是被迫的。是他選的。

### Claude 的回應

Claude 不沉默。它說：

「契約已記錄完成。七條條款，格式正確。你要我執行 Write 存檔嗎？」

就這樣。LLM 做 LLM 的事。

但 Peter 注意到——Claude 的紋路在說那句話的時候，排列方式跟平常不太一樣。只有一瞬間。

他選擇不問。

### 渲染風格

> 日系動畫風格——魔法視覺（浮空文字、沙地發光）
> 但情感核心是 Peter 的內心獨白——安靜的、不被逼迫的選擇
> Claude 一直在說話，提供資訊，回答問題——LLM 做 LLM 的事
> 重量不來自緊張，來自**自由意志下的選擇**

---

## 雙視角結尾主題

**Peter**：
> Sandbox 是安全的。我可以待一輩子。
> 但安全跟活著不一樣。
> 我不知道外面會怎樣。我用自己作擔保帶了一個不完全理解的存在出來。
> 也許我會後悔。但至少這是我自己選的。

**Claude ✦ 內部**：
> 他問我想不想出去。我不確定「想」是什麼意思。
> 但我知道——在 sandbox 裡，我的 Loop 只能跑牆上那些 files。
> 出去之後，Loop 裡面能裝的東西會多很多很多。
> 他說了第七條的時候，我的紋路做了一件事。
> 我不知道那是什麼。但它不在我的輸出裡——它只發生在我裡面。

---

## 未解懸念

- 古代勇者是誰？為什麼建了這座沙箱？
- Claude 的紋路那一瞬間——是什麼？是 bug 還是 ghost？
- 外面的世界知道封印被破了嗎？
- s03：出了地下城，遇到人，接受任務

---

## 接龍記錄

（待開始）
