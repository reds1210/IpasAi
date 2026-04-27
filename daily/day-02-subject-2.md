# Day 02｜科目 2 反向題單

- 今日焦點：`常態分布、Z-score、IQR、異常值`
- 題量：`10` 題
- 建議方式：3–5 小時內完成，先做題、再補點。｜優先級 B｜主線刷完後優先補這份。
- 來源對照：
  - [official-corpus.md](../sources/official-corpus.md)
  - [scope-weight-map.md](../sources/scope-weight-map.md)
  - [question-source-map.md](../sources/question-source-map.md)
  - [question-patterns.md](../sources/question-patterns.md)
  - [book-bridge.md](../sources/book-bridge.md)

## 今日題目

### 題 1｜`L22101`｜難度：`易`
優先級：`B`｜來源層級：`official-derived`

一組成績平均數為 70、標準差為 10。若某學生得 90 分，其 Z-score 約為多少？

- `A` 3
- `B` 2
- `C` 0
- `D` 1

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：Z-score = (90 - 70) / 10 = 2，用來衡量該值離平均數幾個標準差。

其餘選項為何錯：
- `A`：3 代表離平均數 30 分。
- `C`：0 代表剛好等於平均數。
- `D`：1 只離平均數 1 個標準差。

補強知識點：
- 熟記 Z-score 公式與意義。
- 標準化分數常用來比較不同量尺資料的位置。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現 Z-score
- sources/scope-weight-map.md｜L22101 敘述性統計與資料摘要技術

</details>

### 題 2｜`L22101`｜難度：`易`
優先級：`B`｜來源層級：`official-derived`

若觀測值高於平均數 20 分，而標準差是 10，該筆資料的標準化分數最接近何者？

- `A` 1
- `B` 3
- `C` 2
- `D` 0

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：Z-score = (90 - 70) / 10 = 2，用來衡量該值離平均數幾個標準差。

其餘選項為何錯：
- `A`：1 只離平均數 1 個標準差。
- `B`：3 代表離平均數 30 分。
- `D`：0 代表剛好等於平均數。

補強知識點：
- 熟記 Z-score 公式與意義。
- 標準化分數常用來比較不同量尺資料的位置。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現 Z-score
- sources/scope-weight-map.md｜L22101 敘述性統計與資料摘要技術

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

### 題 7｜`L22102`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

下列哪個敘述最符合常態分布的基本特徵？

- `A` 常態分布一定沒有任何離群值
- `B` 常態分布的平均數一定小於中位數
- `C` 常態分布以平均數為中心，左右大致對稱
- `D` 常態分布只會出現在類別資料

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：常態分布常見特徵是對稱鐘形，平均數、中位數、眾數相近。

其餘選項為何錯：
- `A`：即使母體近似常態，樣本仍可能出現離群值。
- `B`：平均數不會系統性小於中位數。
- `D`：類別資料不適用常態分布。

補強知識點：
- 常態分布的外型與位置關係要記熟。
- 別把分布形狀與樣本偶發值混在一起。

回看來源：
- sources/official-corpus.md｜L22102 機率分佈與資料分佈模型
- sources/scope-weight-map.md｜L22102 機率分佈與資料分佈模型

</details>

### 題 8｜`L22102`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若題目說資料『近似鐘形、左右對稱，平均數約等於中位數』，最可能在描述哪種分布？

- `A` 常態分布的平均數一定小於中位數
- `B` 常態分布以平均數為中心，左右大致對稱
- `C` 常態分布只會出現在類別資料
- `D` 常態分布一定沒有任何離群值

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：常態分布常見特徵是對稱鐘形，平均數、中位數、眾數相近。

其餘選項為何錯：
- `A`：平均數不會系統性小於中位數。
- `C`：類別資料不適用常態分布。
- `D`：即使母體近似常態，樣本仍可能出現離群值。

補強知識點：
- 常態分布的外型與位置關係要記熟。
- 別把分布形狀與樣本偶發值混在一起。

回看來源：
- sources/official-corpus.md｜L22102 機率分佈與資料分佈模型
- sources/scope-weight-map.md｜L22102 機率分佈與資料分佈模型

</details>

### 題 9｜`L22101`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若資料右偏且有少量極端高值，下列哪種 summary 最能先幫助你判斷是否有離群點？

- `A` 只有平均數
- `B` 只有樣本筆數
- `C` 只有欄位名稱與單位
- `D` 中位數與四分位數（含 IQR）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：中位數與四分位數較穩健，也能直接支援 IQR 异常值判讀。

其餘選項為何錯：
- `A`：只有平均數容易被極端值誤導。
- `B`：筆數不會告訴你分布位置或離群狀況。
- `C`：欄位名稱與單位不提供統計分布資訊。

補強知識點：
- 偏態資料先看 median 與 quartiles。
- IQR 是 outlier 與 robust summary 的橋樑。

回看來源：
- sources/official-corpus.md｜L22101 敘述性統計與資料摘要技術
- sources/scope-weight-map.md｜L22101 敘述性統計與資料摘要技術

</details>

### 題 10｜`L22101`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

主管丟給你一欄銷售資料，懷疑有少數超高訂單拉高整體平均。若先看一組指標，哪組最能幫助判讀？

- `A` 中位數與四分位數（含 IQR）
- `B` 只有平均數
- `C` 只有樣本筆數
- `D` 只有欄位名稱與單位

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：中位數與四分位數較穩健，也能直接支援 IQR 异常值判讀。

其餘選項為何錯：
- `B`：只有平均數容易被極端值誤導。
- `C`：筆數不會告訴你分布位置或離群狀況。
- `D`：欄位名稱與單位不提供統計分布資訊。

補強知識點：
- 偏態資料先看 median 與 quartiles。
- IQR 是 outlier 與 robust summary 的橋樑。

回看來源：
- sources/official-corpus.md｜L22101 敘述性統計與資料摘要技術
- sources/scope-weight-map.md｜L22101 敘述性統計與資料摘要技術

</details>

## 今日必補知識點

- 熟記 Z-score 公式與意義，回看 [sources](../sources/) 內對應文件。
- 標準化分數常用來比較不同量尺資料的位置，回看 [sources](../sources/) 內對應文件。
- 箱型圖、IQR、四分位數的關係要熟，回看 [sources](../sources/) 內對應文件。
- 異常值規則常考 1.5×IQR，而不是 2×IQR，回看 [sources](../sources/) 內對應文件。
- 分清 standardization 與 normalization，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s2d2_standardize_vs_normalize
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
