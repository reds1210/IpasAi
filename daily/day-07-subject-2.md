# Day 07｜科目 2 反向題單

- 今日焦點：`線性迴歸、係數解讀、截距、顯著性`
- 題量：`10` 題
- 建議方式：3–5 小時內完成，先做題、再補點。｜優先級 A｜先刷這份，對過線最有幫助。
- 來源對照：
  - [official-corpus.md](../sources/official-corpus.md)
  - [scope-weight-map.md](../sources/scope-weight-map.md)
  - [question-source-map.md](../sources/question-source-map.md)
  - [question-patterns.md](../sources/question-patterns.md)
  - [book-bridge.md](../sources/book-bridge.md)

## 今日題目

### 題 1｜`L22301`｜難度：`中`
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

### 題 2｜`L22301`｜難度：`中`
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

### 題 3｜`L22301`｜難度：`中`
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

### 題 4｜`L22301`｜難度：`中`
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

### 題 5｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

在統計建模中，若某係數的 p-value 小於 0.05，最常見的解讀是什麼？

- `A` 在該顯著水準下，該係數對目標的解釋關係具有統計顯著性
- `B` 代表這個變數一定具有強因果關係
- `C` 代表模型一定是最佳模型
- `D` 代表資料完全沒有噪聲

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：p-value 小通常只支持『不容易由隨機波動造成』，不等於因果、最佳或零噪聲。

其餘選項為何錯：
- `B`：顯著不等於因果成立。
- `C`：單一係數顯著不代表整個模型就是最佳。
- `D`：真實資料仍可能有噪聲與偏差。

補強知識點：
- 統計顯著與因果解釋要切開。
- 顯著性只是一個證據，不是最終商業結論。

回看來源：
- sources/official-corpus.md｜L22301 統計學在大數據中的應用
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 6｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若 OLS 報表顯示某變數 p-value < 0.05，在常見顯著水準下最合理的判斷為何？

- `A` 代表這個變數一定具有強因果關係
- `B` 代表模型一定是最佳模型
- `C` 代表資料完全沒有噪聲
- `D` 在該顯著水準下，該係數對目標的解釋關係具有統計顯著性

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：p-value 小通常只支持『不容易由隨機波動造成』，不等於因果、最佳或零噪聲。

其餘選項為何錯：
- `A`：顯著不等於因果成立。
- `B`：單一係數顯著不代表整個模型就是最佳。
- `C`：真實資料仍可能有噪聲與偏差。

補強知識點：
- 統計顯著與因果解釋要切開。
- 顯著性只是一個證據，不是最終商業結論。

回看來源：
- sources/official-corpus.md｜L22301 統計學在大數據中的應用
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 7｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

線性迴歸中的截距（intercept）通常代表什麼？

- `A` 目標變數的標準差
- `B` 所有特徵為 0 時的預測基準值
- `C` 資料筆數
- `D` 相關係數

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：截距是模型的常數項，代表當所有解釋變數為 0 時的預測值。

其餘選項為何錯：
- `A`：標準差是離散程度，不是模型基準值。
- `C`：資料筆數不屬於模型參數。
- `D`：相關係數是變數關聯程度，不是迴歸常數項。

補強知識點：
- `intercept_` 與 `coef_` 的角色要分清。
- 截距的業務意義要結合 0 是否有實際含義再解讀。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現截距項解讀
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 8｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若所有特徵都等於 0，模型預測值對應的那個常數項，一般稱為什麼？

- `A` 所有特徵為 0 時的預測基準值
- `B` 資料筆數
- `C` 相關係數
- `D` 目標變數的標準差

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：截距是模型的常數項，代表當所有解釋變數為 0 時的預測值。

其餘選項為何錯：
- `B`：資料筆數不屬於模型參數。
- `C`：相關係數是變數關聯程度，不是迴歸常數項。
- `D`：標準差是離散程度，不是模型基準值。

補強知識點：
- `intercept_` 與 `coef_` 的角色要分清。
- 截距的業務意義要結合 0 是否有實際含義再解讀。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現截距項解讀
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 9｜`L22301`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

若線性迴歸的目標變數明顯右偏，且變異隨 X 增大而增加，哪種前處理較合理？

- `A` 對 X 做標準化就一定能解決
- `B` 對資料做一次差分
- `C` 直接刪掉所有高值樣本
- `D` 對 Y 做 Box-Cox 轉換

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：Box-Cox 常用於處理正值且右偏的資料，能改善偏態與變異不穩定問題。

其餘選項為何錯：
- `A`：標準化 X 不一定能解決 Y 的偏態與異質變異。
- `B`：差分主要常見於時間序列處理。
- `C`：直接刪高值可能扭曲資料而非改善模型假設。

補強知識點：
- 偏態與異質變異時要想到變數轉換。
- Box-Cox 適合正值目標變數。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 Box-Cox
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 10｜`L22301`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

研究者發現 Y 分布右偏且異質變異明顯。若想更符合線性模型假設，較值得優先嘗試哪個轉換？

- `A` 對資料做一次差分
- `B` 直接刪掉所有高值樣本
- `C` 對 Y 做 Box-Cox 轉換
- `D` 對 X 做標準化就一定能解決

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：Box-Cox 常用於處理正值且右偏的資料，能改善偏態與變異不穩定問題。

其餘選項為何錯：
- `A`：差分主要常見於時間序列處理。
- `B`：直接刪高值可能扭曲資料而非改善模型假設。
- `D`：標準化 X 不一定能解決 Y 的偏態與異質變異。

補強知識點：
- 偏態與異質變異時要想到變數轉換。
- Box-Cox 適合正值目標變數。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 Box-Cox
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

## 今日必補知識點

- 記住 sklearn 介面慣例：X 在前、y 在後，回看 [sources](../sources/) 內對應文件。
- 程式題常考最基本的 API 使用順序，回看 [sources](../sources/) 內對應文件。
- 區分 `coef_` 與 `intercept_`，回看 [sources](../sources/) 內對應文件。
- sklearn 與 statsmodels 提供的統計資訊層級不同，回看 [sources](../sources/) 內對應文件。
- 統計顯著與因果解釋要切開，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s2d7_fit_xy, s2d7_coef_intercept, s2d7_pvalue, s2d7_intercept_meaning, s2d7_boxcox
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
