# iPAS 中級 AI 規劃師 20 天反向刷題包

這個專案是給台灣 `iPAS AI 應用規劃師（中級）` 科目 `1 + 2` 用的反向刷題包。

目標不是先把書讀完，而是直接從題目開始，透過：

- 每日題單
- 額外加練題庫
- 可收折答案與解析
- 作答單
- 批改報告
- 自動弱點追蹤

把 `20` 天的衝刺準備流程做成可以直接使用的本地題庫系統。

## 你會拿到什麼

- `daily/`
  - `Day 01` 到 `Day 20` 的每日題單
- `extended/`
  - 額外加練題庫，集中補強高頻主題
- `attempts/`
  - 每份題單對應的作答單
- `reports/`
  - 每份題單對應的批改報告
- `progress/`
  - 成績總表、自動弱點、自動回看順序
- `sources/`
  - 官方來源整理、L-code 權重、題源轉寫規則
- `data/pack-manifest.json`
  - 題庫結構、正解、metadata 索引

## 題庫設計原則

- 採 `先做題、後補點`，不走傳統先讀完再考
- 每題都附：
  - 正解
  - 另外三個選項錯在哪
  - 應補知識點
- 答案與解析用 `<details>` 收折，預設不會直接看到答案
- 題目區分 `A / B / C` 優先級，方便你先刷高命中區
- 題源區分：
  - `official-derived`
  - `public-pattern-derived`

## 優先級說明

- `A`
  - 先刷。高命中主戰場，優先來自官方範圍、官方樣題、官方公告題型
- `B`
  - 第二層。常見延伸題型，通常用來補回鍋與跨章情境
- `C`
  - 最後補。低報酬或偏補洞題，不影響 20 天過線主路徑

## 題源層級

- `official-derived`
  - 依官方範圍、官方樣題、官方公告題型轉寫
- `public-pattern-derived`
  - 依公開練習題、備考心得、非官方題型整理轉寫

公開來源只拿來抽：

- 題型骨架
- 干擾選項邏輯
- 熱區主題

不做近似改寫原題面。

## 快速開始

先重建整包：

```powershell
python .\build_full_pack.py
```

主入口：

- [study-hub.md](study-hub.md)
- [extended/README.md](extended/README.md)
- [attempts/README.md](attempts/README.md)

## 批改方式

批改每日題單：

```powershell
python .\score_attempt.py --day 1 --subject 1
```

直接貼答案：

```powershell
python .\score_attempt.py --day 1 --subject 1 --answers D,A,C,B,D,A,C,B
```

批改加練題庫：

```powershell
python .\score_attempt.py --drill subject-2-code-practice-drill
```

## 作答單版本保護

這個專案會持續擴題，所以每份作答單都帶有 `session_version`。

如果你重建題庫後，題目數量或內容有變動：

- 舊版非空作答單會先自動備份成 `*.stale-...md`
- 新版作答單會重新生成
- 若你拿舊版作答單去批改，系統會擋下並提醒你先重建

這樣可以避免：

- 題數不一致
- 舊答案對到新版題目
- 舊紀錄污染現在的分數與弱點追蹤

## 主要檔案

- [build_full_pack.py](build_full_pack.py)
  - 重建整包、生成 manifest、作答單、報告與追蹤檔
- [generate_ipas_reverse_pack.py](generate_ipas_reverse_pack.py)
  - 每日題單主題庫與 daily 題單生成
- [expanded_question_bank.py](expanded_question_bank.py)
  - extended 題庫與 drill 生成
- [score_attempt.py](score_attempt.py)
  - 批改入口
- [study_pack_lib.py](study_pack_lib.py)
  - 共用解析、報告、scoreboard、弱點與回看邏輯

## 官方與題源整理

- [sources/official-corpus.md](sources/official-corpus.md)
- [sources/scope-weight-map.md](sources/scope-weight-map.md)
- [sources/question-patterns.md](sources/question-patterns.md)
- [sources/question-source-map.md](sources/question-source-map.md)
- [sources/book-bridge.md](sources/book-bridge.md)

## 日常使用順序

1. 從 [study-hub.md](study-hub.md) 打開今天的題單
2. 到對應 `attempts/` 作答
3. 用 `score_attempt.py` 批改
4. 看 `reports/` 的錯題與解析
5. 回到：
   - [progress/scoreboard.md](progress/scoreboard.md)
   - [progress/auto-knowledge-gaps.md](progress/auto-knowledge-gaps.md)
   - [progress/auto-review-queue.md](progress/auto-review-queue.md)

## 適合誰

這包比較適合：

- 想在短時間內衝過線
- 不想先通讀整套書
- 想直接用題目反推弱點
- 想把刷題、批改、回看流程固定下來的人
