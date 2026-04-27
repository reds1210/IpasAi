# Day 08｜科目 2 反向題單

- 今日焦點：`LinearRegression.fit、OLS、coef_、p-value`
- 題量：`10` 題
- 建議方式：3–5 小時內完成，先做題、再補點。｜優先級 A｜先刷這份，對過線最有幫助。
- 來源對照：
  - [official-corpus.md](../sources/official-corpus.md)
  - [scope-weight-map.md](../sources/scope-weight-map.md)
  - [question-source-map.md](../sources/question-source-map.md)
  - [question-patterns.md](../sources/question-patterns.md)
  - [book-bridge.md](../sources/book-bridge.md)

## 今日題目

### 題 1｜`L22301`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

使用 `statsmodels` 建立 OLS 模型時，較正確的呼叫方向為何？

- `A` `OLS(y).fit(X)`
- `B` `OLS(y, X_with_constant).fit()`
- `C` `OLS(X, y).fit()`
- `D` `OLS(X).fit(y)`

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：在 statsmodels 中，第一個位置通常是目標 y，第二個是設計矩陣 X。

其餘選項為何錯：
- `A`：只給單邊參數不構成完整 OLS 模型。
- `C`：把 X 與 y 顛倒會把資料語意反轉。
- `D`：fit 不接受這種拆開方式。

補強知識點：
- sklearn 與 statsmodels 的介面習慣要分清。
- statsmodels 題常考 y、X 的順序與常數項。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 OLS 呼叫方向
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 2｜`L22301`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

若你要用 `statsmodels.api.OLS` 建立線性模型，下列哪個概念順序最合理？

- `A` `OLS(y, X_with_constant).fit()`
- `B` `OLS(X, y).fit()`
- `C` `OLS(X).fit(y)`
- `D` `OLS(y).fit(X)`

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：在 statsmodels 中，第一個位置通常是目標 y，第二個是設計矩陣 X。

其餘選項為何錯：
- `B`：把 X 與 y 顛倒會把資料語意反轉。
- `C`：fit 不接受這種拆開方式。
- `D`：只給單邊參數不構成完整 OLS 模型。

補強知識點：
- sklearn 與 statsmodels 的介面習慣要分清。
- statsmodels 題常考 y、X 的順序與常數項。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 OLS 呼叫方向
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 3｜`L22301`｜難度：`中`
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

### 題 4｜`L22301`｜難度：`中`
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

### 題 5｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

線性迴歸中的殘差（residual）最接近哪個定義？

- `A` 資料列數與欄位數的差
- `B` 實際值減去預測值的差
- `C` 各特徵之間的相關係數
- `D` 模型的截距項

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：殘差反映單筆樣本的預測誤差，是模型診斷的重要基礎。

其餘選項為何錯：
- `A`：資料形狀與殘差定義無關。
- `C`：相關係數衡量變數關聯，不是單筆誤差。
- `D`：截距是模型參數，不是單筆預測誤差。

補強知識點：
- 殘差診斷與整體指標（R²、RMSE）要一起看。
- 單筆誤差與整體模型品質不是同一層次。

回看來源：
- sources/official-corpus.md｜L22301 統計學在大數據中的應用
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 6｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

如果你想檢查模型是否系統性低估或高估，最直接會看的量是什麼？

- `A` 實際值減去預測值的差
- `B` 各特徵之間的相關係數
- `C` 模型的截距項
- `D` 資料列數與欄位數的差

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：殘差反映單筆樣本的預測誤差，是模型診斷的重要基礎。

其餘選項為何錯：
- `B`：相關係數衡量變數關聯，不是單筆誤差。
- `C`：截距是模型參數，不是單筆預測誤差。
- `D`：資料形狀與殘差定義無關。

補強知識點：
- 殘差診斷與整體指標（R²、RMSE）要一起看。
- 單筆誤差與整體模型品質不是同一層次。

回看來源：
- sources/official-corpus.md｜L22301 統計學在大數據中的應用
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 7｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

當兩個變數高度相關時，下列哪個敘述最嚴謹？

- `A` 相關高代表不用做驗證與實驗設計
- `B` 相關性不自動代表因果關係
- `C` 只要相關高就代表有直接因果
- `D` 相關高代表模型一定無偏

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：相關只描述同時變動，是否因果仍需更多設計、控制與領域證據。

其餘選項為何錯：
- `A`：驗證與設計仍然必要。
- `C`：相關高可能來自混雜因素。
- `D`：相關高不保證模型無偏。

補強知識點：
- 考試常拿 correlation vs causation 當判斷陷阱。
- 看到『高度相關』不要自動跳到『因果成立』。

回看來源：
- sources/official-corpus.md｜L22301 統計學在大數據中的應用
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 8｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若你在回歸分析中看到某特徵與銷售高度正相關，最安全的結論應是什麼？

- `A` 相關高代表模型一定無偏
- `B` 相關高代表不用做驗證與實驗設計
- `C` 相關性不自動代表因果關係
- `D` 只要相關高就代表有直接因果

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：相關只描述同時變動，是否因果仍需更多設計、控制與領域證據。

其餘選項為何錯：
- `A`：相關高不保證模型無偏。
- `B`：驗證與設計仍然必要。
- `D`：相關高可能來自混雜因素。

補強知識點：
- 考試常拿 correlation vs causation 當判斷陷阱。
- 看到『高度相關』不要自動跳到『因果成立』。

回看來源：
- sources/official-corpus.md｜L22301 統計學在大數據中的應用
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 9｜`L22203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若要避免資料前處理與模型訓練步驟在實驗與部署間不一致，較佳的工程做法是什麼？

- `A` 把前處理與模型包進同一條 pipeline
- `B` 每次手動重打一遍前處理
- `C` 只在簡報中描述前處理步驟
- `D` 把標準化留到使用者自行處理

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：把 scaler 與 model 放在同一 pipeline 能降低訓練/推論不一致。

其餘選項為何錯：
- `B`：手動重做容易出現人為偏差。
- `C`：簡報無法保證系統實作一致。
- `D`：把責任丟給使用者會提高線上錯誤率。

補強知識點：
- 工程一致性也是資料分析能力的一部分。
- preprocessing drift 不只在數值，也可能在流程。

回看來源：
- sources/official-corpus.md｜L22203 數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具

</details>

### 題 10｜`L22203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

團隊擔心訓練時做了標準化，但上線推論忘記套同樣規則。若想降低這類錯誤，較好的作法為何？

- `A` 把前處理與模型包進同一條 pipeline
- `B` 每次手動重打一遍前處理
- `C` 只在簡報中描述前處理步驟
- `D` 把標準化留到使用者自行處理

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：把 scaler 與 model 放在同一 pipeline 能降低訓練/推論不一致。

其餘選項為何錯：
- `B`：手動重做容易出現人為偏差。
- `C`：簡報無法保證系統實作一致。
- `D`：把責任丟給使用者會提高線上錯誤率。

補強知識點：
- 工程一致性也是資料分析能力的一部分。
- preprocessing drift 不只在數值，也可能在流程。

回看來源：
- sources/official-corpus.md｜L22203 數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具

</details>

## 今日必補知識點

- sklearn 與 statsmodels 的介面習慣要分清，回看 [sources](../sources/) 內對應文件。
- statsmodels 題常考 y、X 的順序與常數項，回看 [sources](../sources/) 內對應文件。
- `add_constant` 是 statsmodels 題的高頻 API，回看 [sources](../sources/) 內對應文件。
- sklearn 與 statsmodels 對截距的預設行為不同，回看 [sources](../sources/) 內對應文件。
- 殘差診斷與整體指標（R²、RMSE）要一起看，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s2d8_ols_order, s2d8_add_constant, s2d8_residuals, s2d8_corr_causation, s2d8_scaler_pipeline
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
