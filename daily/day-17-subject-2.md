# Day 17｜科目 2 反向題單

- 今日焦點：`高密度程式判讀與回歸解讀`
- 題量：`14` 題
- 建議方式：3–5 小時內完成，先做題、再補點。｜優先級 A｜先刷這份，對過線最有幫助。
- 來源對照：
  - [official-corpus.md](../sources/official-corpus.md)
  - [scope-weight-map.md](../sources/scope-weight-map.md)
  - [question-source-map.md](../sources/question-source-map.md)
  - [question-patterns.md](../sources/question-patterns.md)
  - [book-bridge.md](../sources/book-bridge.md)

## 今日題目

### 題 1｜`L22201`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若年份欄位包含 NaN，但你仍想保留整數語意，最合適的轉型方式為何？

- `A` 先全部轉成 `str`
- `B` 把所有 NaN 都改成 1900 再轉 `int`
- `C` 使用 pandas 的 `Int64` nullable integer 型態
- `D` 直接 `astype(int)`

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：`Int64` 可在保留缺值的同時維持整數語意，是 pandas 常見解法。

其餘選項為何錯：
- `A`：轉字串會失去數值操作便利性。
- `B`：用 1900 等假值硬補會污染分析結果。
- `D`：`astype(int)` 遇到 NaN 會失敗。

補強知識點：
- 區分 Python / numpy 的整數型態與 pandas nullable integer。
- 看到『保留 NaN 又想是整數』就先想 `Int64`。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 `astype('Int64')`
- sources/scope-weight-map.md｜L22201 數據收集與清理

</details>

### 題 2｜`L22201`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

資料中 `Year` 有缺值，你又不想把缺值硬補成 0 或 1。若還要維持整數欄位，最合理的 pandas 型態為何？

- `A` 先全部轉成 `str`
- `B` 把所有 NaN 都改成 1900 再轉 `int`
- `C` 使用 pandas 的 `Int64` nullable integer 型態
- `D` 直接 `astype(int)`

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：`Int64` 可在保留缺值的同時維持整數語意，是 pandas 常見解法。

其餘選項為何錯：
- `A`：轉字串會失去數值操作便利性。
- `B`：用 1900 等假值硬補會污染分析結果。
- `D`：`astype(int)` 遇到 NaN 會失敗。

補強知識點：
- 區分 Python / numpy 的整數型態與 pandas nullable integer。
- 看到『保留 NaN 又想是整數』就先想 `Int64`。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 `astype('Int64')`
- sources/scope-weight-map.md｜L22201 數據收集與清理

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

### 題 5｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

在 `LinearRegression().fit()` 中，哪個參數順序才是正確的？

- `A` `fit(y)` 後模型會自己找特徵
- `B` `fit(X, y)`
- `C` `fit(y, X)`
- `D` `fit(X)` 就足夠

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：`sklearn` 的監督式模型介面通常是 `fit(features, target)`。

其餘選項為何錯：
- `A`：只給 y 不會讓模型自動知道特徵。
- `C`：把 y 放前面會把目標與特徵顛倒。
- `D`：監督式迴歸需要特徵與目標。

補強知識點：
- 記住 sklearn 介面慣例：X 在前、y 在後。
- 程式題常考最基本的 API 使用順序。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 `fit(X, y)`
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 6｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若你要用 `sklearn` 建立線性迴歸模型，X 與 y 的輸入位置應如何安排？

- `A` `fit(X, y)`
- `B` `fit(y, X)`
- `C` `fit(X)` 就足夠
- `D` `fit(y)` 後模型會自己找特徵

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：`sklearn` 的監督式模型介面通常是 `fit(features, target)`。

其餘選項為何錯：
- `B`：把 y 放前面會把目標與特徵顛倒。
- `C`：監督式迴歸需要特徵與目標。
- `D`：只給 y 不會讓模型自動知道特徵。

補強知識點：
- 記住 sklearn 介面慣例：X 在前、y 在後。
- 程式題常考最基本的 API 使用順序。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 `fit(X, y)`
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

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

### 題 11｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若任務重點是盡量抓到少數類，不希望漏判，較應優先關注哪一項指標？

- `A` 召回率（Recall）
- `B` 只看整體準確率（Accuracy）
- `C` 只看資料筆數
- `D` 只看訓練時間長短

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：當漏判成本高時，召回率比單純準確率更重要。

其餘選項為何錯：
- `B`：在高度不平衡資料中，accuracy 可能誤導。
- `C`：資料筆數不是模型性能指標。
- `D`：訓練時間不是任務目標指標。

補強知識點：
- 任務成本決定你優先的 metric。
- 偵測少數類場景常優先 recall 或 PR 指標。

回看來源：
- sources/official-corpus.md｜L22301 統計學在大數據中的應用
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 12｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

在疾病偵測或詐欺攔截場景中，若漏掉真正異常代價最高，調整模型時最優先看的通常是哪個方向？

- `A` 只看資料筆數
- `B` 只看訓練時間長短
- `C` 召回率（Recall）
- `D` 只看整體準確率（Accuracy）

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：當漏判成本高時，召回率比單純準確率更重要。

其餘選項為何錯：
- `A`：資料筆數不是模型性能指標。
- `B`：訓練時間不是任務目標指標。
- `D`：在高度不平衡資料中，accuracy 可能誤導。

補強知識點：
- 任務成本決定你優先的 metric。
- 偵測少數類場景常優先 recall 或 PR 指標。

回看來源：
- sources/official-corpus.md｜L22301 統計學在大數據中的應用
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 13｜`L22302`｜難度：`難`
優先級：`B`｜來源層級：`official-derived`

ARIMA 模型建立後，若殘差 ACF 在多個 lag 上仍顯著不為 0，最合理的診斷是什麼？

- `A` 代表殘差一定是白噪音
- `B` 代表模型完全不需要再調整
- `C` 代表只能改成分類模型
- `D` 模型仍未充分捕捉時間依賴，存在配適不足

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：若殘差仍有結構，表示資訊還留在誤差中，模型尚未充分擬合。

其餘選項為何錯：
- `A`：白噪音應接近無系統自相關。
- `B`：有殘差結構時通常需要再調整模型。
- `C`：時間序列配適不足不會直接推出改做分類。

補強知識點：
- 時間序列診斷常看殘差是否近白噪音。
- ACF 顯著不為 0 常暗示 underfitting 或規格不完整。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 ARIMA 殘差診斷
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

### 題 14｜`L22302`｜難度：`難`
優先級：`B`｜來源層級：`official-derived`

若時間序列模型的誤差仍呈現週期性、自相關顯著，表示模型最可能有什麼問題？

- `A` 代表殘差一定是白噪音
- `B` 代表模型完全不需要再調整
- `C` 代表只能改成分類模型
- `D` 模型仍未充分捕捉時間依賴，存在配適不足

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：若殘差仍有結構，表示資訊還留在誤差中，模型尚未充分擬合。

其餘選項為何錯：
- `A`：白噪音應接近無系統自相關。
- `B`：有殘差結構時通常需要再調整模型。
- `C`：時間序列配適不足不會直接推出改做分類。

補強知識點：
- 時間序列診斷常看殘差是否近白噪音。
- ACF 顯著不為 0 常暗示 underfitting 或規格不完整。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 ARIMA 殘差診斷
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

## 今日必補知識點

- 區分 Python / numpy 的整數型態與 pandas nullable integer，回看 [sources](../sources/) 內對應文件。
- 看到『保留 NaN 又想是整數』就先想 `Int64`，回看 [sources](../sources/) 內對應文件。
- 寬表轉長表是資料視覺化常考轉換，回看 [sources](../sources/) 內對應文件。
- melt 與 estimator=sum 要一起記，回看 [sources](../sources/) 內對應文件。
- 記住 sklearn 介面慣例：X 在前、y 在後，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s2d6_melt_barplot, s2d7_fit_xy, s2d7_coef_intercept, s2d10_smote, s2d10_recall_threshold
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
