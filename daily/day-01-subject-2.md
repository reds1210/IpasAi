# Day 01｜科目 2 反向題單

- 今日焦點：`資料型態、NaN、dtype、敘述統計`
- 題量：`10` 題
- 建議方式：3–5 小時內完成，先做題、再補點。｜優先級 B｜主線刷完後優先補這份。
- 來源對照：
  - [official-corpus.md](../sources/official-corpus.md)
  - [scope-weight-map.md](../sources/scope-weight-map.md)
  - [question-source-map.md](../sources/question-source-map.md)
  - [question-patterns.md](../sources/question-patterns.md)
  - [book-bridge.md](../sources/book-bridge.md)

## 今日題目

### 題 1｜`L22201`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

讀入 CSV 後發現 `Year` 欄位是 `float64` 而不是整數，下列哪個原因最合理？

- `A` 只要欄位名稱叫 Year 就一定會轉成字串
- `B` 資料只要超過 100 筆就會自動升成浮點數
- `C` 欄位中含有 NaN 或帶小數格式的值
- `D` Pandas 會把所有數值欄位強制讀成 float64

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：含 NaN 的整數欄位在傳統 `numpy` 型態下常被升成浮點數，或原始資料本來就含 `2006.0` 類值。

其餘選項為何錯：
- `A`：欄位名稱不會決定資料型態。
- `B`：筆數多寡與是否升成浮點數無直接關係。
- `D`：Pandas 會依內容推斷型態，不會把所有數值欄位都強制轉成 float64。

補強知識點：
- 理解 dtype 由內容而非欄位名稱決定。
- 看到 `float64` 年份欄位時，先檢查 NaN 與原始值格式。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 Year float64 情境
- sources/scope-weight-map.md｜L22201 數據收集與清理

</details>

### 題 2｜`L22201`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

資料分析師發現年份欄位變成 `float64`，若原始欄位理應是年份，最先應懷疑哪種狀況？

- `A` 只要欄位名稱叫 Year 就一定會轉成字串
- `B` 資料只要超過 100 筆就會自動升成浮點數
- `C` 欄位中含有 NaN 或帶小數格式的值
- `D` Pandas 會把所有數值欄位強制讀成 float64

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：含 NaN 的整數欄位在傳統 `numpy` 型態下常被升成浮點數，或原始資料本來就含 `2006.0` 類值。

其餘選項為何錯：
- `A`：欄位名稱不會決定資料型態。
- `B`：筆數多寡與是否升成浮點數無直接關係。
- `D`：Pandas 會依內容推斷型態，不會把所有數值欄位都強制轉成 float64。

補強知識點：
- 理解 dtype 由內容而非欄位名稱決定。
- 看到 `float64` 年份欄位時，先檢查 NaN 與原始值格式。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 Year float64 情境
- sources/scope-weight-map.md｜L22201 數據收集與清理

</details>

### 題 3｜`L22201`｜難度：`中`
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

### 題 4｜`L22201`｜難度：`中`
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

### 題 5｜`L22201`｜難度：`易`
優先級：`B`｜來源層級：`official-derived`

在 pandas 中，要統計每個欄位 NaN 個數，最標準的寫法是哪一類？

- `A` 使用 `isnan().sum()` 在 DataFrame 直接呼叫
- `B` 使用 `missing().count()`
- `C` 使用 `isna().sum()` 或 `isnull().sum()`
- `D` 使用 `isNaN().sum()`

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：在 pandas 裡，`isna()` 與 `isnull()` 是等價的常用缺值檢查方法。

其餘選項為何錯：
- `A`：`isnan()` 不是 DataFrame 物件的通用方法。
- `B`：`missing()` 不是 pandas 的標準 API。
- `D`：`isNaN()` 不是 pandas DataFrame 的標準方法名稱。

補強知識點：
- 記住 pandas 缺值檢查常用 API：`isna` / `isnull`。
- 不要把 numpy 或其他語言的命名直接套進 pandas。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 `isna()` / `isnull()`
- sources/scope-weight-map.md｜L22201 數據收集與清理

</details>

### 題 6｜`L22201`｜難度：`易`
優先級：`B`｜來源層級：`official-derived`

若你想快速檢查資料各欄位缺失值數量，哪個 pandas 方法組合最可靠？

- `A` 使用 `isna().sum()` 或 `isnull().sum()`
- `B` 使用 `isNaN().sum()`
- `C` 使用 `isnan().sum()` 在 DataFrame 直接呼叫
- `D` 使用 `missing().count()`

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：在 pandas 裡，`isna()` 與 `isnull()` 是等價的常用缺值檢查方法。

其餘選項為何錯：
- `B`：`isNaN()` 不是 pandas DataFrame 的標準方法名稱。
- `C`：`isnan()` 不是 DataFrame 物件的通用方法。
- `D`：`missing()` 不是 pandas 的標準 API。

補強知識點：
- 記住 pandas 缺值檢查常用 API：`isna` / `isnull`。
- 不要把 numpy 或其他語言的命名直接套進 pandas。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 `isna()` / `isnull()`
- sources/scope-weight-map.md｜L22201 數據收集與清理

</details>

### 題 7｜`L22101`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若資料分布可能有極端值，描述中心趨勢時哪個統計量通常比平均數更穩健？

- `A` 平均數（mean）一定更穩健
- `B` 標準差（standard deviation）
- `C` 樣本數（count）
- `D` 中位數（median）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：中位數較不受極端值影響，對偏態資料通常比平均數穩健。

其餘選項為何錯：
- `A`：平均數容易被極端值拉動。
- `B`：標準差描述離散程度，不是中心趨勢。
- `C`：樣本數只描述資料量，不描述典型位置。

補強知識點：
- 中心趨勢與離散程度要分清。
- 偏態與極端值情境優先想 median。

回看來源：
- sources/official-corpus.md｜L22101 敘述性統計與資料摘要技術
- sources/scope-weight-map.md｜L22101 敘述性統計與資料摘要技術

</details>

### 題 8｜`L22101`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

銷售資料右偏且有少數超高值，若主管只想知道『典型值』，你較優先報告哪個統計量？

- `A` 平均數（mean）一定更穩健
- `B` 標準差（standard deviation）
- `C` 樣本數（count）
- `D` 中位數（median）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：中位數較不受極端值影響，對偏態資料通常比平均數穩健。

其餘選項為何錯：
- `A`：平均數容易被極端值拉動。
- `B`：標準差描述離散程度，不是中心趨勢。
- `C`：樣本數只描述資料量，不描述典型位置。

補強知識點：
- 中心趨勢與離散程度要分清。
- 偏態與極端值情境優先想 median。

回看來源：
- sources/official-corpus.md｜L22101 敘述性統計與資料摘要技術
- sources/scope-weight-map.md｜L22101 敘述性統計與資料摘要技術

</details>

### 題 9｜`L22201`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

下列哪一項最符合資料型態清理（dtype cleanup）的主要目的？

- `A` 只是為了讓資料列數變少
- `B` 只是為了讓圖表顏色更好看
- `C` 讓後續計算、過濾與視覺化建立在正確資料語意上
- `D` 只為了讓檔案看起來整齊

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：dtype 正確與否會直接影響排序、比較、聚合與繪圖結果。

其餘選項為何錯：
- `A`：型態修正不一定會改變列數。
- `B`：圖表顏色屬視覺設計，非 dtype cleanup 核心。
- `D`：型態清理不只是版面問題。

補強知識點：
- 把 dtype cleanup 視為分析正確性的前置條件。
- 數值、類別、日期、文字欄位要各自用對型態。

回看來源：
- sources/official-corpus.md｜L22201 數據收集與清理
- sources/scope-weight-map.md｜L22201 數據收集與清理

</details>

### 題 10｜`L22201`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若分析流程常在合併、排序、計算時出錯，而原因是欄位型態混亂，最核心的修正方向為何？

- `A` 只為了讓檔案看起來整齊
- `B` 只是為了讓資料列數變少
- `C` 只是為了讓圖表顏色更好看
- `D` 讓後續計算、過濾與視覺化建立在正確資料語意上

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：dtype 正確與否會直接影響排序、比較、聚合與繪圖結果。

其餘選項為何錯：
- `A`：型態清理不只是版面問題。
- `B`：型態修正不一定會改變列數。
- `C`：圖表顏色屬視覺設計，非 dtype cleanup 核心。

補強知識點：
- 把 dtype cleanup 視為分析正確性的前置條件。
- 數值、類別、日期、文字欄位要各自用對型態。

回看來源：
- sources/official-corpus.md｜L22201 數據收集與清理
- sources/scope-weight-map.md｜L22201 數據收集與清理

</details>

## 今日必補知識點

- 理解 dtype 由內容而非欄位名稱決定，回看 [sources](../sources/) 內對應文件。
- 看到 `float64` 年份欄位時，先檢查 NaN 與原始值格式，回看 [sources](../sources/) 內對應文件。
- 區分 Python / numpy 的整數型態與 pandas nullable integer，回看 [sources](../sources/) 內對應文件。
- 看到『保留 NaN 又想是整數』就先想 `Int64`，回看 [sources](../sources/) 內對應文件。
- 記住 pandas 缺值檢查常用 API：`isna` / `isnull`，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
