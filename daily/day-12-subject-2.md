# Day 12｜科目 2 反向題單

- 今日焦點：`半模擬跨章整合`
- 題量：`10` 題
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

若要同時比較三個以上群體的平均數是否存在差異，最適合的檢定是什麼？

- `A` ROC 曲線
- `B` IQR 異常值法
- `C` ANOVA（變異數分析）
- `D` 雙樣本 t 檢定

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：ANOVA 用於三組以上平均數差異檢定，避免多次兩兩比較造成問題。

其餘選項為何錯：
- `A`：ROC 是分類模型評估工具。
- `B`：IQR 用於描述分布與找離群值，不做平均數差異推論。
- `D`：t-test 主要是兩組平均數比較。

補強知識點：
- 題目出現三組以上平均數比較時，優先選 ANOVA。
- 平均數比較與模型評估不要混。

回看來源：
- sources/official-corpus.md｜樣題出現三組平均數差異
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論

</details>

### 題 2｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若題目改成比較一年級、二年級、三年級平均身高是否不同，哪個統計方法最合理？

- `A` ANOVA（變異數分析）
- `B` 雙樣本 t 檢定
- `C` ROC 曲線
- `D` IQR 異常值法

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：ANOVA 用於三組以上平均數差異檢定，避免多次兩兩比較造成問題。

其餘選項為何錯：
- `B`：t-test 主要是兩組平均數比較。
- `C`：ROC 是分類模型評估工具。
- `D`：IQR 用於描述分布與找離群值，不做平均數差異推論。

補強知識點：
- 題目出現三組以上平均數比較時，優先選 ANOVA。
- 平均數比較與模型評估不要混。

回看來源：
- sources/official-corpus.md｜樣題出現三組平均數差異
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

### 題 5｜`L22303`｜難度：`難`
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

### 題 6｜`L22303`｜難度：`難`
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

### 題 7｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

在 `sklearn` 線性迴歸中，`coef_` 主要代表什麼？

- `A` 包含截距在內的所有係數
- `B` 模型的 p-value 清單
- `C` 每個欄位的缺失值數量
- `D` 各特徵對目標變數的迴歸係數，不包含截距

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：`coef_` 反映各特徵的斜率係數；截距通常在 `intercept_`。

其餘選項為何錯：
- `A`：截距通常另存在 `intercept_`。
- `B`：p-value 不是 sklearn `LinearRegression` 直接提供的欄位。
- `C`：缺失值數量與迴歸係數無關。

補強知識點：
- 區分 `coef_` 與 `intercept_`。
- sklearn 與 statsmodels 提供的統計資訊層級不同。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 `coef_` 解讀
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 8｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若你在 `LinearRegression` 訓練後印出 `reg.coef_`，最合理的解讀是什麼？

- `A` 模型的 p-value 清單
- `B` 每個欄位的缺失值數量
- `C` 各特徵對目標變數的迴歸係數，不包含截距
- `D` 包含截距在內的所有係數

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：`coef_` 反映各特徵的斜率係數；截距通常在 `intercept_`。

其餘選項為何錯：
- `A`：p-value 不是 sklearn `LinearRegression` 直接提供的欄位。
- `B`：缺失值數量與迴歸係數無關。
- `D`：截距通常另存在 `intercept_`。

補強知識點：
- 區分 `coef_` 與 `intercept_`。
- sklearn 與 statsmodels 提供的統計資訊層級不同。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 `coef_` 解讀
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 9｜`L22401`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

在少數類樣本極少、又想提升少數類偵測能力時，下列哪一種策略最合理？

- `A` 使用 SMOTE 生成合成少數類樣本
- `B` 只隨機刪掉大量多數類而不評估代價
- `C` 完全不處理不平衡問題
- `D` 只提高決策閾值卻不檢查整體泛化

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：SMOTE 能在特徵空間中合成少數類樣本，常用於不平衡分類前處理。

其餘選項為何錯：
- `B`：欠採樣有時可行，但粗暴刪資料可能損失太多資訊。
- `C`：完全不處理通常會讓模型偏向多數類。
- `D`：只調閾值不能替代資料層補強。

補強知識點：
- SMOTE、class weight、threshold tuning 是不平衡分類三個高頻補救方向。
- 先看題目要的是資料層、模型層還是決策層補強。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 SMOTE
- sources/scope-weight-map.md｜L22401 大數據與機器學習

</details>

### 題 10｜`L22401`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

罕見疾病分類中，確診樣本不到 1%，又短期內拿不到更多標註資料。若想先提升少數類學習效果，哪個方法較對題？

- `A` 使用 SMOTE 生成合成少數類樣本
- `B` 只隨機刪掉大量多數類而不評估代價
- `C` 完全不處理不平衡問題
- `D` 只提高決策閾值卻不檢查整體泛化

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：SMOTE 能在特徵空間中合成少數類樣本，常用於不平衡分類前處理。

其餘選項為何錯：
- `B`：欠採樣有時可行，但粗暴刪資料可能損失太多資訊。
- `C`：完全不處理通常會讓模型偏向多數類。
- `D`：只調閾值不能替代資料層補強。

補強知識點：
- SMOTE、class weight、threshold tuning 是不平衡分類三個高頻補救方向。
- 先看題目要的是資料層、模型層還是決策層補強。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 SMOTE
- sources/scope-weight-map.md｜L22401 大數據與機器學習

</details>

## 今日必補知識點

- 題目出現三組以上平均數比較時，優先選 ANOVA，回看 [sources](../sources/) 內對應文件。
- 平均數比較與模型評估不要混，回看 [sources](../sources/) 內對應文件。
- 先看目標是平均數還是比例，回看 [sources](../sources/) 內對應文件。
- 良率、轉換率、點擊率差異常對應 two-proportion test，回看 [sources](../sources/) 內對應文件。
- 寬表轉長表是資料視覺化常考轉換，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s2d3_anova, s2d3_prop_test, s2d6_melt_barplot, s2d7_coef_intercept, s2d10_smote
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
