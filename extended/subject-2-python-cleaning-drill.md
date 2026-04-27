# 科目 2 加練｜Python 資料清理

- 科目：`2`
- 優先級：`A`
- 優先級摘要：`A=3 / B=1 / C=0`
- 來源層級：`official-derived`
- 焦點：`merge、重複值、日期轉型、transform`
- 題數：`8` 題
- 建議加做時機：`建議在 Day 05、Day 06、Day 17 後加做`
- 作答單：[開啟](../attempts/subject-2-python-cleaning-drill-attempt.md)
- 批改報告：[開啟](../reports/subject-2-python-cleaning-drill-report.md)
- 批改指令：`python .\score_attempt.py --drill subject-2-python-cleaning-drill`
- 使用方式：先做題，再展開 `<details>` 看答案與排錯理由。

## 題源對照

- sources/official-corpus.md｜數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具
- sources/official-corpus.md｜數據收集與清理
- sources/scope-weight-map.md｜L22201 數據收集與清理

## 題目

### 題 1｜`L22203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若你要把會員主表接上交易摘要，但不希望因沒有交易紀錄而把會員列弄丟，較合理的 join 是哪一種？

- `A` 只用 concat 不看 key
- `B` left join，保留左表全部列
- `C` inner join，因為最乾淨
- `D` cross join，因為資料最多

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：left join 的核心就是保留左表所有列，右表對不到時以缺值補上。

其餘選項為何錯：
- `A`：concat 只是拼接，不等於按 key 關聯。
- `C`：inner join 會丟掉對不到 key 的左表列。
- `D`：cross join 會產生笛卡兒積，不符合主鍵合併需求。

補強知識點：
- join 題先判斷『哪些列一定要留下』。
- left / inner / outer 的差異要熟。

回看來源：
- sources/official-corpus.md｜數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具

</details>

### 題 2｜`L22203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

分析師希望合併兩張表時保留左表全部資料列，即使右表有些 key 對不到也沒關係。最適合用哪種 join？

- `A` 只用 concat 不看 key
- `B` left join，保留左表全部列
- `C` inner join，因為最乾淨
- `D` cross join，因為資料最多

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：left join 的核心就是保留左表所有列，右表對不到時以缺值補上。

其餘選項為何錯：
- `A`：concat 只是拼接，不等於按 key 關聯。
- `C`：inner join 會丟掉對不到 key 的左表列。
- `D`：cross join 會產生笛卡兒積，不符合主鍵合併需求。

補強知識點：
- join 題先判斷『哪些列一定要留下』。
- left / inner / outer 的差異要熟。

回看來源：
- sources/official-corpus.md｜數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具

</details>

### 題 3｜`L22201`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若同一客戶可能有多筆重複資料，但你想依 `customer_id` 去重並保留第一筆，最常見的 pandas 作法為何？

- `A` 把整個 DataFrame 轉成字串再比對
- `B` 使用 `drop_duplicates(subset=['customer_id'], keep='first')`
- `C` 直接 `sort_values()` 就會自動去重
- `D` 只要 `reset_index()` 就會消失重複列

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：`drop_duplicates` 可依指定欄位判定重複，並控制保留第一筆或最後一筆。

其餘選項為何錯：
- `A`：轉字串比對不是 pandas 的標準清理流程。
- `C`：排序不會自動刪除重複。
- `D`：重設索引不會改變資料重複性。

補強知識點：
- subset 與 keep 是去重題常考參數。
- 先想重複判定依據是哪個 key。

回看來源：
- sources/official-corpus.md｜數據收集與清理
- sources/scope-weight-map.md｜L22201 數據收集與清理

</details>

### 題 4｜`L22201`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

資料表裡同一個主鍵出現重複列。若你只想留下第一筆紀錄，哪種操作方向最合理？

- `A` 把整個 DataFrame 轉成字串再比對
- `B` 使用 `drop_duplicates(subset=['customer_id'], keep='first')`
- `C` 直接 `sort_values()` 就會自動去重
- `D` 只要 `reset_index()` 就會消失重複列

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：`drop_duplicates` 可依指定欄位判定重複，並控制保留第一筆或最後一筆。

其餘選項為何錯：
- `A`：轉字串比對不是 pandas 的標準清理流程。
- `C`：排序不會自動刪除重複。
- `D`：重設索引不會改變資料重複性。

補強知識點：
- subset 與 keep 是去重題常考參數。
- 先想重複判定依據是哪個 key。

回看來源：
- sources/official-corpus.md｜數據收集與清理
- sources/scope-weight-map.md｜L22201 數據收集與清理

</details>

### 題 5｜`L22203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若欄位目前是字串日期，例如 `2026-04-27`，而你接下來要萃取年月或計算時間差，最合理的第一步是什麼？

- `A` 先轉成 category 以加速時間差運算
- `B` 先用 `pd.to_datetime()` 轉成 datetime 型態
- `C` 直接對字串做平均數
- `D` 只把欄位名稱改成 date

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：日期分析前通常先把字串轉成 datetime，後續才能穩定做時間屬性與差值運算。

其餘選項為何錯：
- `A`：category 不適合作為日期運算主型態。
- `C`：字串無法直接做合理的日期平均。
- `D`：改欄位名不會改變資料型態。

補強知識點：
- date parsing 是資料清理常考基本功。
- 看到 object 日期欄，先想到 `to_datetime`。

回看來源：
- sources/official-corpus.md｜數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具

</details>

### 題 6｜`L22203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

資料欄位看起來像日期，但 dtype 仍是 `object`。若後續要做時間分析，最值得先做哪個轉換？

- `A` 先用 `pd.to_datetime()` 轉成 datetime 型態
- `B` 直接對字串做平均數
- `C` 只把欄位名稱改成 date
- `D` 先轉成 category 以加速時間差運算

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：日期分析前通常先把字串轉成 datetime，後續才能穩定做時間屬性與差值運算。

其餘選項為何錯：
- `B`：字串無法直接做合理的日期平均。
- `C`：改欄位名不會改變資料型態。
- `D`：category 不適合作為日期運算主型態。

補強知識點：
- date parsing 是資料清理常考基本功。
- 看到 object 日期欄，先想到 `to_datetime`。

回看來源：
- sources/official-corpus.md｜數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具

</details>

### 題 7｜`L22203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若你想把『每個部門的平均薪資』回填到原始每一列，之後再計算個人薪資與部門平均的差距，較合理的方法方向為何？

- `A` 使用 `groupby(...).transform(...)` 把群組統計回填原列
- `B` 只用 `groupby().agg()` 然後假設列數不會改變
- `C` 只用 `value_counts()`
- `D` 直接把整張表 `dropna()`

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：`transform` 會回傳與原表等長的結果，適合把群組統計量貼回每列。

其餘選項為何錯：
- `B`：`agg()` 通常會產生彙總表，不一定保持原列數。
- `C`：`value_counts()` 是計數，不是通用群組回填工具。
- `D`：`dropna()` 與群組統計回填無關。

補強知識點：
- transform 與 agg 的輸出形狀差異要熟。
- 需要保留原列數時先想 transform。

回看來源：
- sources/official-corpus.md｜數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具

</details>

### 題 8｜`L22203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

分析師需要把群組統計量保留在原表同樣列數上，而不是變成彙總表。這時最常想到哪個 pandas 方法？

- `A` 只用 `groupby().agg()` 然後假設列數不會改變
- `B` 只用 `value_counts()`
- `C` 直接把整張表 `dropna()`
- `D` 使用 `groupby(...).transform(...)` 把群組統計回填原列

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：`transform` 會回傳與原表等長的結果，適合把群組統計量貼回每列。

其餘選項為何錯：
- `A`：`agg()` 通常會產生彙總表，不一定保持原列數。
- `B`：`value_counts()` 是計數，不是通用群組回填工具。
- `C`：`dropna()` 與群組統計回填無關。

補強知識點：
- transform 與 agg 的輸出形狀差異要熟。
- 需要保留原列數時先想 transform。

回看來源：
- sources/official-corpus.md｜數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具

</details>

## 本組必補

- join 題先判斷『哪些列一定要留下』
- left / inner / outer 的差異要熟
- subset 與 keep 是去重題常考參數
- 先想重複判定依據是哪個 key
- date parsing 是資料清理常考基本功
- 看到 object 日期欄，先想到 `to_datetime`

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
