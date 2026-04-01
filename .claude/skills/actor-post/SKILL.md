---
name: actor-post
description: 每次 Actor 模式接龍後，自動執行風格對齊工作流程
disable-model-invocation: true
allowed-tools: Read, Edit, Write, Grep, Glob, Bash
argument-hint: [session-number]
---

# /actor-post — 接龍後自動對齊

使用者剛完成一段 Actor 模式的接龍。請依序執行以下步驟：

## 步驟 1：蒐集原話

1. 讀取最新的 session 檔案：`sessions/series1/session_$ARGUMENTS.md`
   - 如果未提供 session 編號，讀取最近修改的 session 檔案
2. 找出使用者（Peter）的所有 Actor 原話段落（標記為【Peter —】的區塊）
3. 讀取 `peter-voice.md`
4. 將**新增的**原話追加到 `peter-voice.md` 對應 session 區塊下
   - 僅收錄使用者原文，**不收錄 Claude 生成的內容**

## 步驟 2：檢查風格指南

1. 讀取 `style-guide.md`
2. 比對新收錄的原話，確認風格分析是否仍準確
3. 如有新的語感特徵（新的標點習慣、新的句式模式、新的詞彙偏好），更新 `style-guide.md`
4. 如無變化，跳過此步驟並告知使用者「風格指南無需更新」

## 步驟 3：對齊 Claude 段落

1. 在同一 session 檔案中，找出所有【Claude —】區塊
2. 逐段檢查是否符合 `style-guide.md` 的規則：
   - ✅ 第一人稱「我」（非「他」「Peter」）
   - ✅ 口語、自嘲、短句、逗號串接
   - ✅ 描寫量不超過 Peter 的 1.5 倍
   - ✅ 技術類比自然嵌入
   - ✅ 符號習慣一致（`~`、`...`、`!`、`?`）
3. 如有偏離，直接修正並列出修改摘要
4. 如完全對齊，告知使用者「所有段落已對齊」

## 輸出格式

完成後輸出摘要：

```
📝 原話更新：新增 X 段至 peter-voice.md
📖 風格指南：[已更新 / 無需更新]
🎯 段落對齊：修正 Y 處 / 全部對齊
```
