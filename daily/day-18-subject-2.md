# Day 18｜科目 2 反向題單

- 今日焦點：`檢定、視覺化、資料處理混題`
- 題量：`14` 題
- 建議方式：3–5 小時內完成，先做題、再補點。｜優先級 A｜先刷這份，對過線最有幫助。
- 來源對照：
  - [official-corpus.md](../sources/official-corpus.md)
  - [scope-weight-map.md](../sources/scope-weight-map.md)
  - [question-source-map.md](../sources/question-source-map.md)
  - [question-patterns.md](../sources/question-patterns.md)
  - [book-bridge.md](../sources/book-bridge.md)

## 今日題目

### 題 1｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

要檢定兩個獨立群體的平均數是否有差異，最常見的統計方法是哪一種？

- `A` 卡方檢定（Chi-square test）
- `B` 變異數分析（ANOVA）
- `C` 主成分分析（PCA）
- `D` 雙樣本 t 檢定（two-sample t-test）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：兩組平均數比較且資料近似常態時，雙樣本 t 檢定是標準起點。

其餘選項為何錯：
- `A`：卡方檢定主要處理類別資料或次數分配。
- `B`：ANOVA 常用於三組以上平均數比較。
- `C`：PCA 是降維方法，不是顯著性檢定。

補強知識點：
- 先判斷要比『平均數』還是『比例 / 類別』。
- 兩組平均數差異優先想 t-test。

回看來源：
- sources/official-corpus.md｜樣題出現一年級與二年級平均數比較
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論

</details>

### 題 2｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若你想比較一年級與二年級平均身高是否不同，且資料近似常態，最先該選哪種檢定？

- `A` 卡方檢定（Chi-square test）
- `B` 變異數分析（ANOVA）
- `C` 主成分分析（PCA）
- `D` 雙樣本 t 檢定（two-sample t-test）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：兩組平均數比較且資料近似常態時，雙樣本 t 檢定是標準起點。

其餘選項為何錯：
- `A`：卡方檢定主要處理類別資料或次數分配。
- `B`：ANOVA 常用於三組以上平均數比較。
- `C`：PCA 是降維方法，不是顯著性檢定。

補強知識點：
- 先判斷要比『平均數』還是『比例 / 類別』。
- 兩組平均數差異優先想 t-test。

回看來源：
- sources/official-corpus.md｜樣題出現一年級與二年級平均數比較
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論

</details>

### 題 3｜`L22103`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

若要比較兩條生產線良率 95% 與 97% 的差異是否有統計意義，最合理的方法是什麼？

- `A` 雙樣本平均數 t 檢定
- `B` ANOVA
- `C` PCA
- `D` 雙比例 Z 檢定（two-proportion Z-test）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：當目標是比較兩個比例或成功率時，雙比例 Z 檢定最對題。

其餘選項為何錯：
- `A`：t 檢定比較的是平均數，不是比例。
- `B`：ANOVA 也不是比例檢定。
- `C`：PCA 屬於降維方法。

補強知識點：
- 先看目標是平均數還是比例。
- 良率、轉換率、點擊率差異常對應 two-proportion test。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現產線良率比較
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論

</details>

### 題 4｜`L22103`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

工程師各抽樣 100 件產品，比較新舊產線的良率差異是否顯著。這裡最接近哪種檢定？

- `A` 雙樣本平均數 t 檢定
- `B` ANOVA
- `C` PCA
- `D` 雙比例 Z 檢定（two-proportion Z-test）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：當目標是比較兩個比例或成功率時，雙比例 Z 檢定最對題。

其餘選項為何錯：
- `A`：t 檢定比較的是平均數，不是比例。
- `B`：ANOVA 也不是比例檢定。
- `C`：PCA 屬於降維方法。

補強知識點：
- 先看目標是平均數還是比例。
- 良率、轉換率、點擊率差異常對應 two-proportion test。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現產線良率比較
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論

</details>

### 題 5｜`L22303`｜難度：`中`
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

### 題 6｜`L22303`｜難度：`中`
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

### 題 7｜`L22303`｜難度：`中`
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

### 題 8｜`L22303`｜難度：`中`
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

### 題 9｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

在 `statsmodels` 做 OLS 時，若想顯式估計截距項，常需要先做哪個步驟？

- `A` 使用 `sm.add_constant(X)` 加入常數欄位
- `B` 把 X 全部轉成字串
- `C` 先做 one-hot 才會有截距
- `D` 把 y 乘上一個常數即可

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：statsmodels 不一定自動補截距，常見做法是先對 X 加常數欄。

其餘選項為何錯：
- `B`：轉字串與截距無關。
- `C`：one-hot 用於類別編碼，不是專門為截距設計。
- `D`：改 y 不會自動產生設計矩陣中的常數項。

補強知識點：
- `add_constant` 是 statsmodels 題的高頻 API。
- sklearn 與 statsmodels 對截距的預設行為不同。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現常數項
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 10｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

為了讓 OLS 報表中含有常數項，對設計矩陣 X 最常見的前處理是什麼？

- `A` 把 X 全部轉成字串
- `B` 先做 one-hot 才會有截距
- `C` 把 y 乘上一個常數即可
- `D` 使用 `sm.add_constant(X)` 加入常數欄位

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：statsmodels 不一定自動補截距，常見做法是先對 X 加常數欄。

其餘選項為何錯：
- `A`：轉字串與截距無關。
- `B`：one-hot 用於類別編碼，不是專門為截距設計。
- `C`：改 y 不會自動產生設計矩陣中的常數項。

補強知識點：
- `add_constant` 是 statsmodels 題的高頻 API。
- sklearn 與 statsmodels 對截距的預設行為不同。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現常數項
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 11｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若模型機率輸出已存在，但你想在不重訓模型的前提下提升召回率，哪個調整方向最直接？

- `A` 只改欄位名稱
- `B` 只提高 batch size
- `C` 只增加訓練輪數而不重新驗證
- `D` 調整分類決策閾值（decision threshold）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：閾值調整直接影響 precision / recall 取捨，是不重訓下最直接的方法之一。

其餘選項為何錯：
- `A`：欄位名稱與分類邏輯無關。
- `B`：batch size 主要影響訓練流程。
- `C`：增加訓練輪數不一定能朝你要的 error trade-off 前進。

補強知識點：
- threshold tuning 是決策層調整，不是資料層。
- 題目若說『不重訓』，常先想 threshold。

回看來源：
- sources/official-corpus.md｜不平衡資料與召回率題型
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 12｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

你想讓模型抓到更多異常案例，且允許多一些誤報。若先不重建資料或改演算法，較合理的做法為何？

- `A` 調整分類決策閾值（decision threshold）
- `B` 只改欄位名稱
- `C` 只提高 batch size
- `D` 只增加訓練輪數而不重新驗證

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：閾值調整直接影響 precision / recall 取捨，是不重訓下最直接的方法之一。

其餘選項為何錯：
- `B`：欄位名稱與分類邏輯無關。
- `C`：batch size 主要影響訓練流程。
- `D`：增加訓練輪數不一定能朝你要的 error trade-off 前進。

補強知識點：
- threshold tuning 是決策層調整，不是資料層。
- 題目若說『不重訓』，常先想 threshold。

回看來源：
- sources/official-corpus.md｜不平衡資料與召回率題型
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 13｜`L22202`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

在圖形資料庫中，若『按讚』行為本身還帶有時間戳與裝置類型等資訊，較合適的建模方式是什麼？

- `A` 把所有按讚都寫回使用者節點文字欄位
- `B` 完全不用圖模型，改成隨意 Excel 記錄
- `C` 把裝置類型改成人工備註而不建模關聯
- `D` 把按讚視為帶屬性的邊（edge/property）來連結節點

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：圖資料庫很適合用邊來表示互動關係，邊上再保留時間與裝置等屬性。

其餘選項為何錯：
- `A`：寫回單一節點會破壞關聯查詢能力。
- `B`：Excel 不是圖查詢與關聯推理的設計。
- `C`：不建模關係就失去圖資料庫價值。

補強知識點：
- 圖資料庫的核心是節點、邊與屬性。
- 互動事件若天然是關係，先考慮 edge property。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 graph database edge property
- sources/scope-weight-map.md｜L22202 數據儲存與管理

</details>

### 題 14｜`L22202`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

社群資料中，使用者與貼文之間的 like 互動還要保留時間與裝置欄位。若用圖資料庫，最合理的設計方向為何？

- `A` 把裝置類型改成人工備註而不建模關聯
- `B` 把按讚視為帶屬性的邊（edge/property）來連結節點
- `C` 把所有按讚都寫回使用者節點文字欄位
- `D` 完全不用圖模型，改成隨意 Excel 記錄

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：圖資料庫很適合用邊來表示互動關係，邊上再保留時間與裝置等屬性。

其餘選項為何錯：
- `A`：不建模關係就失去圖資料庫價值。
- `C`：寫回單一節點會破壞關聯查詢能力。
- `D`：Excel 不是圖查詢與關聯推理的設計。

補強知識點：
- 圖資料庫的核心是節點、邊與屬性。
- 互動事件若天然是關係，先考慮 edge property。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 graph database edge property
- sources/scope-weight-map.md｜L22202 數據儲存與管理

</details>

## 今日必補知識點

- 先判斷要比『平均數』還是『比例 / 類別』，回看 [sources](../sources/) 內對應文件。
- 兩組平均數差異優先想 t-test，回看 [sources](../sources/) 內對應文件。
- 先看目標是平均數還是比例，回看 [sources](../sources/) 內對應文件。
- 良率、轉換率、點擊率差異常對應 two-proportion test，回看 [sources](../sources/) 內對應文件。
- 看到『總額』先找 sum，不要被 count 誤導，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s2d3_ttest, s2d3_prop_test, s2d6_groupby_sum, s2d6_nlargest, s2d8_add_constant
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
