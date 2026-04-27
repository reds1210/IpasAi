# Day 06｜科目 2 反向題單

- 今日焦點：`groupby、value_counts、melt、視覺化選型`
- 題量：`10` 題
- 建議方式：3–5 小時內完成，先做題、再補點。｜優先級 A｜先刷這份，對過線最有幫助。
- 來源對照：
  - [official-corpus.md](../sources/official-corpus.md)
  - [scope-weight-map.md](../sources/scope-weight-map.md)
  - [question-source-map.md](../sources/question-source-map.md)
  - [question-patterns.md](../sources/question-patterns.md)
  - [book-bridge.md](../sources/book-bridge.md)

## 今日題目

### 題 1｜`L22303`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若想統計每個平台的全球銷售總額並畫長條圖，下列哪種 pandas 思路最正確？

- `A` 只算平均數而非總和
- `B` 直接用 `countplot` 畫原始列數
- `C` 以 `groupby(平台)[銷售額].sum()` 聚合後再畫 bar chart
- `D` 直接 `value_counts()` 平台名稱就好

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：題目要的是銷售總額，因此要先按平台分組，再對銷售額做加總。

其餘選項為何錯：
- `A`：平均數回答的是平均單筆，不是總額。
- `B`：countplot 也是筆數導向，不是金額聚合。
- `D`：`value_counts()` 只會算筆數，不是總銷售額。

補強知識點：
- 看到『總額』先找 sum，不要被 count 誤導。
- 資料聚合與視覺化要先釐清度量是 count、sum 還是 mean。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 `groupby().sum()`
- sources/scope-weight-map.md｜L22303 數據可視化工具

</details>

### 題 2｜`L22303`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

分析師要比較各遊戲平台的總銷售量，而不是遊戲筆數。若先寫一行資料聚合，最合理的方向是什麼？

- `A` 直接用 `countplot` 畫原始列數
- `B` 以 `groupby(平台)[銷售額].sum()` 聚合後再畫 bar chart
- `C` 直接 `value_counts()` 平台名稱就好
- `D` 只算平均數而非總和

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：題目要的是銷售總額，因此要先按平台分組，再對銷售額做加總。

其餘選項為何錯：
- `A`：countplot 也是筆數導向，不是金額聚合。
- `C`：`value_counts()` 只會算筆數，不是總銷售額。
- `D`：平均數回答的是平均單筆，不是總額。

補強知識點：
- 看到『總額』先找 sum，不要被 count 誤導。
- 資料聚合與視覺化要先釐清度量是 count、sum 還是 mean。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 `groupby().sum()`
- sources/scope-weight-map.md｜L22303 數據可視化工具

</details>

### 題 3｜`L22303`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

若要比較多個地區銷售欄位的總額比例，並用 seaborn 長條圖顯示，較合理的資料整理方式為何？

- `A` 先用 `pd.melt()` 轉長表，再以 `barplot(..., estimator=sum)` 繪圖
- `B` 直接 `countplot` 原始欄位名稱
- `C` 直接 `lineplot` 把四個欄位名稱當 y
- `D` 只畫 `histplot` 就能比較總額比例

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：多欄位數值若要用 seaborn 一致地比較總額，常先轉長表再指定聚合函數。

其餘選項為何錯：
- `B`：countplot 主要算類別出現次數，不適合直接比較總銷售額。
- `C`：lineplot 不適合這種欄位到欄位的聚合比較。
- `D`：histplot 用來看分布，不是總額比較的首選。

補強知識點：
- 寬表轉長表是資料視覺化常考轉換。
- melt 與 estimator=sum 要一起記。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 `pd.melt` + seaborn
- sources/scope-weight-map.md｜L22303 數據可視化工具

</details>

### 題 4｜`L22303`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

資料表中 `NA_Sales/EU_Sales/JP_Sales/Other_Sales` 分散在不同欄位。若要先轉成適合 seaborn `barplot` 的長表格式，哪種作法最合理？

- `A` 直接 `countplot` 原始欄位名稱
- `B` 直接 `lineplot` 把四個欄位名稱當 y
- `C` 只畫 `histplot` 就能比較總額比例
- `D` 先用 `pd.melt()` 轉長表，再以 `barplot(..., estimator=sum)` 繪圖

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：多欄位數值若要用 seaborn 一致地比較總額，常先轉長表再指定聚合函數。

其餘選項為何錯：
- `A`：countplot 主要算類別出現次數，不適合直接比較總銷售額。
- `B`：lineplot 不適合這種欄位到欄位的聚合比較。
- `C`：histplot 用來看分布，不是總額比較的首選。

補強知識點：
- 寬表轉長表是資料視覺化常考轉換。
- melt 與 estimator=sum 要一起記。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 `pd.melt` + seaborn
- sources/scope-weight-map.md｜L22303 數據可視化工具

</details>

### 題 5｜`L22303`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若想找出北美銷售最好的前五名遊戲並畫條狀圖，較合理的資料選取方法為何？

- `A` 先 `sort_values()` 由小到大再取前五筆
- `B` 直接 `countplot` 遊戲名稱
- `C` 先用 `nlargest(5, 'NA_Sales')` 取前五筆
- `D` 直接 `head(5)` 原始資料

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：題目要的是銷售最高前五名，因此要依目標欄位排序並選最大值。

其餘選項為何錯：
- `A`：由小到大排序後取前五會得到最小值。
- `B`：countplot 不會反映銷售額大小。
- `D`：`head(5)` 只取前五列，不一定是銷售最高。

補強知識點：
- top-N 題先看排序依據是什麼欄位。
- 視覺化前先把資料子集選對。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 `nlargest`
- sources/scope-weight-map.md｜L22303 數據可視化工具

</details>

### 題 6｜`L22303`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

你要用 `seaborn.barplot` 畫出 `NA_Sales` 最高的 5 款遊戲，最先應怎麼挑資料？

- `A` 先用 `nlargest(5, 'NA_Sales')` 取前五筆
- `B` 直接 `head(5)` 原始資料
- `C` 先 `sort_values()` 由小到大再取前五筆
- `D` 直接 `countplot` 遊戲名稱

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：題目要的是銷售最高前五名，因此要依目標欄位排序並選最大值。

其餘選項為何錯：
- `B`：`head(5)` 只取前五列，不一定是銷售最高。
- `C`：由小到大排序後取前五會得到最小值。
- `D`：countplot 不會反映銷售額大小。

補強知識點：
- top-N 題先看排序依據是什麼欄位。
- 視覺化前先把資料子集選對。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 `nlargest`
- sources/scope-weight-map.md｜L22303 數據可視化工具

</details>

### 題 7｜`L22303`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若你只想知道每個平台出現幾筆資料，而不是總銷售額，較適合的函式是哪一類？

- `A` 直接做 `LinearRegression`
- `B` 使用 `value_counts()` 或分組後 `count()`
- `C` 使用 `sum()` 計算銷售總額
- `D` 使用 `mean()` 計算平均售額

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：當度量是『出現次數』時，`value_counts()` 或 `count()` 比較直接。

其餘選項為何錯：
- `A`：這題重點是 count，不是 predictive modeling。
- `C`：sum 與 mean 都在處理數值聚合，不是筆數。
- `D`：迴歸模型不是用來統計類別筆數。

補強知識點：
- 先分清題目要 count 還是要 measure aggregation。
- 筆數分布和銷售總額常是考試常見陷阱。

回看來源：
- sources/official-corpus.md｜L22303 數據可視化工具
- sources/scope-weight-map.md｜L22303 數據可視化工具

</details>

### 題 8｜`L22303`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

分析師現在不是要比較金額，而是只想看平台資料筆數分布。這時最貼切的 pandas 方法為何？

- `A` 使用 `value_counts()` 或分組後 `count()`
- `B` 使用 `sum()` 計算銷售總額
- `C` 使用 `mean()` 計算平均售額
- `D` 直接做 `LinearRegression`

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：當度量是『出現次數』時，`value_counts()` 或 `count()` 比較直接。

其餘選項為何錯：
- `B`：sum 與 mean 都在處理數值聚合，不是筆數。
- `C`：迴歸模型不是用來統計類別筆數。
- `D`：這題重點是 count，不是 predictive modeling。

補強知識點：
- 先分清題目要 count 還是要 measure aggregation。
- 筆數分布和銷售總額常是考試常見陷阱。

回看來源：
- sources/official-corpus.md｜L22303 數據可視化工具
- sources/scope-weight-map.md｜L22303 數據可視化工具

</details>

### 題 9｜`L22303`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若想比較不同類別之間的總量高低，最直觀的圖表通常是哪一種？

- `A` 散佈圖（scatter plot）
- `B` 熱力圖（heatmap）
- `C` 長條圖（bar chart）
- `D` 折線圖（line chart）

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：類別間高低比較最直觀的通常是長條圖。

其餘選項為何錯：
- `A`：散佈圖強調兩數值變數關係。
- `B`：熱力圖較適合矩陣關係或密度概覽。
- `D`：折線圖較適合強調時間或有序序列變化。

補強知識點：
- 先判斷資料型態：類別比較常用 bar。
- 時間趨勢才優先考慮 line。

回看來源：
- sources/official-corpus.md｜L22303 數據可視化工具
- sources/scope-weight-map.md｜L22303 數據可視化工具

</details>

### 題 10｜`L22303`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

主管想快速比較不同遊戲平台的總銷售量高低，不強調時間連續性。此時最適合優先畫哪種圖？

- `A` 折線圖（line chart）
- `B` 散佈圖（scatter plot）
- `C` 熱力圖（heatmap）
- `D` 長條圖（bar chart）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：類別間高低比較最直觀的通常是長條圖。

其餘選項為何錯：
- `A`：折線圖較適合強調時間或有序序列變化。
- `B`：散佈圖強調兩數值變數關係。
- `C`：熱力圖較適合矩陣關係或密度概覽。

補強知識點：
- 先判斷資料型態：類別比較常用 bar。
- 時間趨勢才優先考慮 line。

回看來源：
- sources/official-corpus.md｜L22303 數據可視化工具
- sources/scope-weight-map.md｜L22303 數據可視化工具

</details>

## 今日必補知識點

- 看到『總額』先找 sum，不要被 count 誤導，回看 [sources](../sources/) 內對應文件。
- 資料聚合與視覺化要先釐清度量是 count、sum 還是 mean，回看 [sources](../sources/) 內對應文件。
- 寬表轉長表是資料視覺化常考轉換，回看 [sources](../sources/) 內對應文件。
- melt 與 estimator=sum 要一起記，回看 [sources](../sources/) 內對應文件。
- top-N 題先看排序依據是什麼欄位，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s2d6_groupby_sum, s2d6_melt_barplot, s2d6_nlargest, s2d6_valuecounts, s2d6_chart_selection
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
