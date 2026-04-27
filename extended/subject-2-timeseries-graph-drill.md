# 科目 2 加練｜時間序列與圖分析

- 科目：`2`
- 優先級：`B`
- 優先級摘要：`A=1 / B=3 / C=0`
- 來源層級：`official-derived`
- 焦點：`time split、seasonal naive、centrality、shortest path`
- 題數：`8` 題
- 建議加做時機：`建議在 Day 13、Day 14、Day 18 後加做`
- 作答單：[開啟](../attempts/subject-2-timeseries-graph-drill-attempt.md)
- 批改報告：[開啟](../reports/subject-2-timeseries-graph-drill-report.md)
- 批改指令：`python .\score_attempt.py --drill subject-2-timeseries-graph-drill`
- 使用方式：先做題，再展開 `<details>` 看答案與排錯理由。

## 題源對照

- sources/official-corpus.md｜常見的大數據分析方法
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法
- sources/official-corpus.md｜時間序列分析主題
- sources/official-corpus.md｜圖資料庫與知識圖譜主題

## 題目

### 題 1｜`L22302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若資料是時間序列，做訓練/測試切分時最重要的原則通常是什麼？

- `A` 只留最後一筆做測試即可
- `B` 保留時間順序，避免把未來資訊洩漏到過去
- `C` 一律隨機切分最公平
- `D` 先看測試表現再決定資料切法

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：時間序列的核心是時序依賴，隨機打亂常會讓未來資訊洩漏到訓練資料。

其餘選項為何錯：
- `A`：只留最後一筆樣本太不穩定。
- `C`：隨機切分常破壞時序結構。
- `D`：先看測試再決定切法會造成驗證偏誤。

補強知識點：
- time split 與 leakage 常一起考。
- 時間序列驗證與一般 IID 資料不同。

回看來源：
- sources/official-corpus.md｜常見的大數據分析方法
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

### 題 2｜`L22302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

你要評估銷售預測模型。若把 2026 年資料隨機打亂分到 train 與 test，主要風險是什麼？

- `A` 保留時間順序，避免把未來資訊洩漏到過去
- `B` 一律隨機切分最公平
- `C` 先看測試表現再決定資料切法
- `D` 只留最後一筆做測試即可

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：時間序列的核心是時序依賴，隨機打亂常會讓未來資訊洩漏到訓練資料。

其餘選項為何錯：
- `B`：隨機切分常破壞時序結構。
- `C`：先看測試再決定切法會造成驗證偏誤。
- `D`：只留最後一筆樣本太不穩定。

補強知識點：
- time split 與 leakage 常一起考。
- 時間序列驗證與一般 IID 資料不同。

回看來源：
- sources/official-corpus.md｜常見的大數據分析方法
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

### 題 3｜`L22302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若序列有明顯每週或每月重複型態，建立第一個 baseline 時常見且合理的做法是什麼？

- `A` 直接永遠預測整體平均數
- `B` 只看第一筆資料後固定不變
- `C` 把時間戳欄位刪掉再說
- `D` 使用 seasonal naive，拿上一個相同季節位置的值當預測

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：若季節性很強，seasonal naive 往往是合理 baseline，能提供最低比較基準。

其餘選項為何錯：
- `A`：整體平均數通常忽略季節波動。
- `B`：只看第一筆資料沒有反映近期與週期資訊。
- `C`：刪掉時間欄會失去序列核心結構。

補強知識點：
- time series baseline 題常考 naive / seasonal naive。
- 先有 baseline，才能判斷複雜模型是否真的有幫助。

回看來源：
- sources/official-corpus.md｜時間序列分析主題
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

### 題 4｜`L22302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

面對強季節性資料，若你想先有一個簡單但有意義的基準模型，哪種方向最自然？

- `A` 直接永遠預測整體平均數
- `B` 只看第一筆資料後固定不變
- `C` 把時間戳欄位刪掉再說
- `D` 使用 seasonal naive，拿上一個相同季節位置的值當預測

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：若季節性很強，seasonal naive 往往是合理 baseline，能提供最低比較基準。

其餘選項為何錯：
- `A`：整體平均數通常忽略季節波動。
- `B`：只看第一筆資料沒有反映近期與週期資訊。
- `C`：刪掉時間欄會失去序列核心結構。

補強知識點：
- time series baseline 題常考 naive / seasonal naive。
- 先有 baseline，才能判斷複雜模型是否真的有幫助。

回看來源：
- sources/official-corpus.md｜時間序列分析主題
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

### 題 5｜`L22302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若你想找出社群網路中最有影響力、最值得優先關注的節點，通常會先看哪一類圖分析指標？

- `A` 只比較節點名稱長短
- `B` 只統計資料列數
- `C` 只看節點顏色是否一致
- `D` 中心性（centrality）分析

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：centrality 用來衡量節點在圖中的重要性或位置，是找關鍵節點的常見起點。

其餘選項為何錯：
- `A`：名稱長短不代表網路影響力。
- `B`：資料列數不反映圖結構位置。
- `C`：顏色只是視覺屬性，不是分析方法。

補強知識點：
- 關鍵節點題先想 centrality。
- 不同 centrality 代表不同重要性定義。

回看來源：
- sources/official-corpus.md｜常見的大數據分析方法
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

### 題 6｜`L22302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

企業知識網絡裡，想先定位關鍵專家或關鍵中繼節點，最合理先做哪種分析？

- `A` 只比較節點名稱長短
- `B` 只統計資料列數
- `C` 只看節點顏色是否一致
- `D` 中心性（centrality）分析

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：centrality 用來衡量節點在圖中的重要性或位置，是找關鍵節點的常見起點。

其餘選項為何錯：
- `A`：名稱長短不代表網路影響力。
- `B`：資料列數不反映圖結構位置。
- `C`：顏色只是視覺屬性，不是分析方法。

補強知識點：
- 關鍵節點題先想 centrality。
- 不同 centrality 代表不同重要性定義。

回看來源：
- sources/official-corpus.md｜常見的大數據分析方法
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

### 題 7｜`L22202`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若你想回答『A 透過哪些關係最短連到 B』，圖資料平台最重要的能力是什麼？

- `A` 只支援單欄位排序
- `B` 只支援圖表配色設定
- `C` 只支援匯出成圖片
- `D` 支援 shortest path / path traversal 類查詢

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：圖模型的一大價值就是高效做路徑遍歷與關係鏈查詢。

其餘選項為何錯：
- `A`：單欄位排序不是關係鏈查詢。
- `B`：配色是視覺層，不是資料查詢能力。
- `C`：匯出圖片不等於能回答關係路徑問題。

補強知識點：
- path traversal 是圖資料庫高頻考點。
- 看到『經由哪些關係』時就要想到路徑查詢。

回看來源：
- sources/official-corpus.md｜圖資料庫與知識圖譜主題
- sources/scope-weight-map.md｜L22202 數據儲存與管理

</details>

### 題 8｜`L22202`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

知識圖譜要查某專家如何經由主題、專利與產品問題間接連結到另一節點，哪種查詢能力最對題？

- `A` 支援 shortest path / path traversal 類查詢
- `B` 只支援單欄位排序
- `C` 只支援圖表配色設定
- `D` 只支援匯出成圖片

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：圖模型的一大價值就是高效做路徑遍歷與關係鏈查詢。

其餘選項為何錯：
- `B`：單欄位排序不是關係鏈查詢。
- `C`：配色是視覺層，不是資料查詢能力。
- `D`：匯出圖片不等於能回答關係路徑問題。

補強知識點：
- path traversal 是圖資料庫高頻考點。
- 看到『經由哪些關係』時就要想到路徑查詢。

回看來源：
- sources/official-corpus.md｜圖資料庫與知識圖譜主題
- sources/scope-weight-map.md｜L22202 數據儲存與管理

</details>

## 本組必補

- time split 與 leakage 常一起考
- 時間序列驗證與一般 IID 資料不同
- time series baseline 題常考 naive / seasonal naive
- 先有 baseline，才能判斷複雜模型是否真的有幫助
- 關鍵節點題先想 centrality
- 不同 centrality 代表不同重要性定義

## 自評

| 題號 | 你的答案 | 能否自己解釋 | 備註 |
| --- | --- | --- | --- |
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |
| 6 |  |  |  |
| 7 |  |  |  |
| 8 |  |  |  |
