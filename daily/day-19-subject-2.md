# Day 19｜科目 2 反向題單

- 今日焦點：`曾錯主題反向變體`
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

### 題 3｜`L22101`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

使用 IQR 方法做異常值偵測時，哪一個區間外的值會被視為異常？

- `A` 只要超過平均數就算異常
- `B` 低於 `Q1 - 1.5×IQR` 或高於 `Q3 + 1.5×IQR`
- `C` 低於 `Q2 - 2×IQR` 或高於 `Q2 + 2×IQR`
- `D` 低於 `Q1 - 1×IQR` 或高於 `Q3 + 1×IQR`

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：IQR 法的標準 outlier 規則是以四分位數與 1.5 倍 IQR 建界。

其餘選項為何錯：
- `A`：超過平均數不代表異常。
- `C`：Q2 不是 IQR 法的常用邊界中心。
- `D`：1×IQR 不是標準箱型圖常見異常值門檻。

補強知識點：
- 箱型圖、IQR、四分位數的關係要熟。
- 異常值規則常考 1.5×IQR，而不是 2×IQR。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現 IQR
- sources/scope-weight-map.md｜L22101 敘述性統計與資料摘要技術

</details>

### 題 4｜`L22101`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若 Q1 與 Q3 已知，想用箱型圖慣用規則找 outlier，判斷門檻通常是哪一組？

- `A` 只要超過平均數就算異常
- `B` 低於 `Q1 - 1.5×IQR` 或高於 `Q3 + 1.5×IQR`
- `C` 低於 `Q2 - 2×IQR` 或高於 `Q2 + 2×IQR`
- `D` 低於 `Q1 - 1×IQR` 或高於 `Q3 + 1×IQR`

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：IQR 法的標準 outlier 規則是以四分位數與 1.5 倍 IQR 建界。

其餘選項為何錯：
- `A`：超過平均數不代表異常。
- `C`：Q2 不是 IQR 法的常用邊界中心。
- `D`：1×IQR 不是標準箱型圖常見異常值門檻。

補強知識點：
- 箱型圖、IQR、四分位數的關係要熟。
- 異常值規則常考 1.5×IQR，而不是 2×IQR。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現 IQR
- sources/scope-weight-map.md｜L22101 敘述性統計與資料摘要技術

</details>

### 題 5｜`L22203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若模型對特徵尺度敏感，且希望各欄位轉成平均數 0、標準差 1，應選哪種處理方式？

- `A` 刪除所有數值欄位
- `B` 只把欄位改英文名稱
- `C` 標準化（Standardization / Z-score scaling）
- `D` 最小最大正規化（Min-Max Normalization）

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：標準化會把特徵轉成平均數 0、標準差 1，常用於尺度敏感模型。

其餘選項為何錯：
- `A`：刪除數值欄位會損失主要訊息。
- `B`：改欄位名不影響尺度。
- `D`：Min-Max 是壓到指定區間，不是平均數 0、標準差 1。

補強知識點：
- 分清 standardization 與 normalization。
- 題目若明講平均數 0、標準差 1，就選 standardization。

回看來源：
- sources/official-corpus.md｜正式題與樣題多次出現尺度處理
- sources/scope-weight-map.md｜L22203 數據處理技術與工具

</details>

### 題 6｜`L22203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

年齡與收入量級差異很大，若你想讓它們落在共同的標準差尺度而非 0–1 區間，應採哪一種方法？

- `A` 刪除所有數值欄位
- `B` 只把欄位改英文名稱
- `C` 標準化（Standardization / Z-score scaling）
- `D` 最小最大正規化（Min-Max Normalization）

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：標準化會把特徵轉成平均數 0、標準差 1，常用於尺度敏感模型。

其餘選項為何錯：
- `A`：刪除數值欄位會損失主要訊息。
- `B`：改欄位名不影響尺度。
- `D`：Min-Max 是壓到指定區間，不是平均數 0、標準差 1。

補強知識點：
- 分清 standardization 與 normalization。
- 題目若明講平均數 0、標準差 1，就選 standardization。

回看來源：
- sources/official-corpus.md｜正式題與樣題多次出現尺度處理
- sources/scope-weight-map.md｜L22203 數據處理技術與工具

</details>

### 題 7｜`L22301`｜難度：`難`
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

### 題 8｜`L22301`｜難度：`難`
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

### 題 11｜`L22202`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若希望知識圖譜支援語意查詢與關聯推理，哪種資料模型最常見？

- `A` RDF 三元組（subject-predicate-object）
- `B` 只把所有內容塞進單一文字欄位
- `C` 只存成普通 CSV 而不保留關係語意
- `D` 只畫心智圖不建立機器可讀模型

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：RDF 三元組是知識圖譜的常見基礎模型，適合做語意關係與推理。

其餘選項為何錯：
- `B`：單一文字欄位無法表達可機器推理的關係。
- `C`：普通 CSV 缺乏語意連結結構。
- `D`：心智圖若不可機器讀取，無法直接支援推理。

補強知識點：
- RDF、triple、ontology 是知識圖譜高頻詞。
- 知識圖譜題常考『語意查詢與推理』。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 RDF
- sources/scope-weight-map.md｜L22202 數據儲存與管理

</details>

### 題 12｜`L22202`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

企業想把研究報告、專利與專家知識整合成可推理的知識圖譜。若從資料模型來看，哪個方向最對題？

- `A` 只把所有內容塞進單一文字欄位
- `B` 只存成普通 CSV 而不保留關係語意
- `C` 只畫心智圖不建立機器可讀模型
- `D` RDF 三元組（subject-predicate-object）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：RDF 三元組是知識圖譜的常見基礎模型，適合做語意關係與推理。

其餘選項為何錯：
- `A`：單一文字欄位無法表達可機器推理的關係。
- `B`：普通 CSV 缺乏語意連結結構。
- `C`：心智圖若不可機器讀取，無法直接支援推理。

補強知識點：
- RDF、triple、ontology 是知識圖譜高頻詞。
- 知識圖譜題常考『語意查詢與推理』。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 RDF
- sources/scope-weight-map.md｜L22202 數據儲存與管理

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

- 理解 dtype 由內容而非欄位名稱決定，回看 [sources](../sources/) 內對應文件。
- 看到 `float64` 年份欄位時，先檢查 NaN 與原始值格式，回看 [sources](../sources/) 內對應文件。
- 箱型圖、IQR、四分位數的關係要熟，回看 [sources](../sources/) 內對應文件。
- 異常值規則常考 1.5×IQR，而不是 2×IQR，回看 [sources](../sources/) 內對應文件。
- 分清 standardization 與 normalization，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s2d2_standardize_vs_normalize, s2d7_boxcox, s2d9_stratify, s2d13_rdf
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
