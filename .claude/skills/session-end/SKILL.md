---
name: session-end
description: Session 結束時自動打包：儲存記錄、更新大綱、生成 brief & log、commit & push
disable-model-invocation: true
allowed-tools: Read, Edit, Write, Grep, Glob, Bash
argument-hint: [session-number]
---

# /session-end — Session 結束打包

Session 結束了。請依序執行以下打包流程：

## 步驟 1：確認 Session 檔案

1. 確認目標 session：`sessions/series1/session_$ARGUMENTS.md`
   - 如果未提供編號，找出最近修改的 session 檔案
2. 讀取 session 檔案，確認接龍記錄完整

## 步驟 2：執行 /actor-post

1. 先執行風格對齊流程（同 /actor-post 的步驟 1-3）
2. 確保 peter-voice.md 和 style-guide.md 是最新的

## 步驟 3：更新大綱

1. 讀取 `outline-series1.md`
2. 根據本 session 的實際內容，更新對應行的：
   - 角色發展欄
   - 新物件欄
   - 新世界觀欄
3. 如果 session 中出現了新名詞，更新 `glossary/core-terms.md`

## 步驟 4：導演筆記

1. 確認 session 檔案底部有「## 導演筆記」區塊
2. 如果沒有，根據 session 內容生成：
   - 核心探索主題
   - 技術映射（隱含）
   - 未解懸念

## 步驟 5：生成 Brief & Log

讀取今天日期 !`date +%Y-%m-%d`

1. 生成 **brief**：`logs/$DATE_brief.md`
   ```
   # Brief — YYYY-MM-DD
   - Session XXX 完成
   - [3-5 行摘要：發生了什麼、推進了什麼、決定了什麼]
   ```

2. 生成 **log**：`logs/$DATE_log.md`
   ```
   # Log — YYYY-MM-DD
   ## 變更記錄
   - [列出所有新增/修改的檔案及原因]
   ## 決定事項
   - [列出本 session 做出的所有設定/劇情決定]
   ## 下一步
   - [列出未解懸念或下次要做的事]
   ```

## 步驟 6：Commit & Push

1. `git add` 所有變更的檔案（逐一列出，不用 -A）
2. Commit message 格式：
   ```
   Session XXX 完成：[一句話摘要]

   - [列出主要變更]

   Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
   ```
3. `git push`

## 輸出格式

```
✅ Session XXX 打包完成
📝 原話/風格：已更新
📋 大綱：已更新
📓 Brief & Log：已生成
🔄 Git：已 commit & push
```
