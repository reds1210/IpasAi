# Day 09｜科目 2 反向題單

- 今日焦點：`交叉驗證、Bootstrap、模型驗證方法`
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

若想降低單次切分造成的評估波動，最常見的模型驗證方法是哪一種？

- `A` 只隨機挑一筆做測試
- `B` K-fold 交叉驗證
- `C` 只看訓練集分數
- `D` 完全不切驗證集

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：K-fold 會反覆切分資料並平均結果，比單次 hold-out 更穩定。

其餘選項為何錯：
- `A`：單筆測試完全不穩定。
- `C`：只看訓練集會過度樂觀。
- `D`：沒有驗證集無法評估泛化。

補強知識點：
- 交叉驗證的重點是反覆切分與平均。
- 穩定評估通常優先想到 K-fold。

回看來源：
- sources/official-corpus.md｜L22301 統計學在大數據中的應用
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 2｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

當資料量不算太小，且你想更穩定評估模型泛化能力，哪種驗證方式通常最合適？

- `A` 只看訓練集分數
- `B` 完全不切驗證集
- `C` 只隨機挑一筆做測試
- `D` K-fold 交叉驗證

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：K-fold 會反覆切分資料並平均結果，比單次 hold-out 更穩定。

其餘選項為何錯：
- `A`：只看訓練集會過度樂觀。
- `B`：沒有驗證集無法評估泛化。
- `C`：單筆測試完全不穩定。

補強知識點：
- 交叉驗證的重點是反覆切分與平均。
- 穩定評估通常優先想到 K-fold。

回看來源：
- sources/official-corpus.md｜L22301 統計學在大數據中的應用
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 3｜`L22301`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

若資料有限，且想估計模型表現或統計量的不確定性，哪種方法常被採用？

- `A` 只做一次平均數計算
- `B` 只調高學習率
- `C` 只用 `value_counts()` 看筆數
- `D` Bootstrap 重抽樣

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：Bootstrap 透過有放回重抽樣來估計指標或統計量的變異與不確定性。

其餘選項為何錯：
- `A`：一次平均數無法反映估計不確定性。
- `B`：學習率是模型訓練參數，不是重抽樣方法。
- `C`：筆數統計無法替代不確定性估計。

補強知識點：
- Bootstrap 的核心是『有放回重抽樣』。
- 當題目談不確定性或抽樣變異時，可優先想到 bootstrap。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 bootstrap
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 4｜`L22301`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

你想多次重抽樣資料來觀察指標波動範圍，而不是固定切 K 份。這時較合理的方法為何？

- `A` Bootstrap 重抽樣
- `B` 只做一次平均數計算
- `C` 只調高學習率
- `D` 只用 `value_counts()` 看筆數

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：Bootstrap 透過有放回重抽樣來估計指標或統計量的變異與不確定性。

其餘選項為何錯：
- `B`：一次平均數無法反映估計不確定性。
- `C`：學習率是模型訓練參數，不是重抽樣方法。
- `D`：筆數統計無法替代不確定性估計。

補強知識點：
- Bootstrap 的核心是『有放回重抽樣』。
- 當題目談不確定性或抽樣變異時，可優先想到 bootstrap。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 bootstrap
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 5｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

為何單次 hold-out 驗證常被認為不如交叉驗證穩定？

- `A` 它不需要任何隨機種子或資料分層
- `B` 結果容易受到特定切分方式影響
- `C` 它完全不能用於任何任務
- `D` 它會自動避免所有過擬合

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：單次切分若剛好抽到偏樣本，評估結果可能高估或低估模型能力。

其餘選項為何錯：
- `A`：切分策略與 random state 仍然重要。
- `C`：hold-out 仍可用，只是穩定性較差。
- `D`：單次切分不會自動消除過擬合。

補強知識點：
- validation method 的重點在穩定性與偏差。
- 單次切分不是錯，而是風險較高。

回看來源：
- sources/official-corpus.md｜L22301 統計學在大數據中的應用
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 6｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若你只做一次 train/test split，模型評估最主要的風險是什麼？

- `A` 它完全不能用於任何任務
- `B` 它會自動避免所有過擬合
- `C` 它不需要任何隨機種子或資料分層
- `D` 結果容易受到特定切分方式影響

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：單次切分若剛好抽到偏樣本，評估結果可能高估或低估模型能力。

其餘選項為何錯：
- `A`：hold-out 仍可用，只是穩定性較差。
- `B`：單次切分不會自動消除過擬合。
- `C`：切分策略與 random state 仍然重要。

補強知識點：
- validation method 的重點在穩定性與偏差。
- 單次切分不是錯，而是風險較高。

回看來源：
- sources/official-corpus.md｜L22301 統計學在大數據中的應用
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 7｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

在一般訓練流程中，驗證集（validation set）的主要用途為何？

- `A` 用來調整模型與超參數，而非作最終公正測試
- `B` 用來取代所有訓練資料
- `C` 用來永久當正式上線資料
- `D` 用來當唯一的商業 KPI 報表來源

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：validation set 主要支援 model selection 與 tuning，final test 則負責較公正的最後評估。

其餘選項為何錯：
- `B`：validation 不是訓練資料的替代品。
- `C`：上線資料與驗證集角色不同。
- `D`：商業 KPI 報表來源不應只依賴 validation。

補強知識點：
- train/validation/test 三者角色要分清。
- 調參看 validation，最終報告看 test。

回看來源：
- sources/official-corpus.md｜L22301 統計學在大數據中的應用
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 8｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若團隊要調超參數、挑模型版本，但不想偷看最終測試集，這時應主要依賴哪個資料切分？

- `A` 用來取代所有訓練資料
- `B` 用來永久當正式上線資料
- `C` 用來當唯一的商業 KPI 報表來源
- `D` 用來調整模型與超參數，而非作最終公正測試

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：validation set 主要支援 model selection 與 tuning，final test 則負責較公正的最後評估。

其餘選項為何錯：
- `A`：validation 不是訓練資料的替代品。
- `B`：上線資料與驗證集角色不同。
- `C`：商業 KPI 報表來源不應只依賴 validation。

補強知識點：
- train/validation/test 三者角色要分清。
- 調參看 validation，最終報告看 test。

回看來源：
- sources/official-corpus.md｜L22301 統計學在大數據中的應用
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 9｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若分類資料類別極不平衡，在切分 train/test 時常見的安全作法是什麼？

- `A` 採用分層切分（stratified split）
- `B` 完全不打亂資料直接切
- `C` 只依索引奇偶切分
- `D` 先刪除少數類再切分

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：分層切分可讓各子集維持接近原始類別比例。

其餘選項為何錯：
- `B`：不打亂可能引入順序偏差。
- `C`：奇偶切分沒有保證類別比例。
- `D`：刪掉少數類會讓問題更嚴重。

補強知識點：
- 不平衡分類題除了 SMOTE，也常考 stratified split。
- 先保住分布，再談建模。

回看來源：
- sources/official-corpus.md｜L22301 統計學在大數據中的應用
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 10｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

資料集中 95% 是正常類、5% 是異常類。若想避免測試集幾乎抽不到異常類，較合理的切分策略為何？

- `A` 只依索引奇偶切分
- `B` 先刪除少數類再切分
- `C` 採用分層切分（stratified split）
- `D` 完全不打亂資料直接切

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：分層切分可讓各子集維持接近原始類別比例。

其餘選項為何錯：
- `A`：奇偶切分沒有保證類別比例。
- `B`：刪掉少數類會讓問題更嚴重。
- `D`：不打亂可能引入順序偏差。

補強知識點：
- 不平衡分類題除了 SMOTE，也常考 stratified split。
- 先保住分布，再談建模。

回看來源：
- sources/official-corpus.md｜L22301 統計學在大數據中的應用
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

## 今日必補知識點

- 交叉驗證的重點是反覆切分與平均，回看 [sources](../sources/) 內對應文件。
- 穩定評估通常優先想到 K-fold，回看 [sources](../sources/) 內對應文件。
- Bootstrap 的核心是『有放回重抽樣』，回看 [sources](../sources/) 內對應文件。
- 當題目談不確定性或抽樣變異時，可優先想到 bootstrap，回看 [sources](../sources/) 內對應文件。
- validation method 的重點在穩定性與偏差，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s2d9_kfold, s2d9_bootstrap, s2d9_holdout_limits, s2d9_train_val_test, s2d9_stratify
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
