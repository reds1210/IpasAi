# Day 16｜科目 2 反向題單

- 今日焦點：`第二輪半模擬`
- 題量：`12` 題
- 建議方式：3–5 小時內完成，先做題、再補點。｜優先級 A｜先刷這份，對過線最有幫助。
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

### 題 3｜`L22303`｜難度：`中`
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

### 題 4｜`L22303`｜難度：`中`
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

### 題 8｜`L22301`｜難度：`中`
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

### 題 9｜`L22301`｜難度：`難`
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

### 題 10｜`L22301`｜難度：`難`
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

### 題 11｜`L22102`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

卜瓦松分布（Poisson distribution）較適合描述哪一類事件？

- `A` 固定時間或空間內稀有事件的發生次數
- `B` 連續型測量值的精準高度
- `C` 只有類別標籤的比例值
- `D` 影像像素顏色的 RGB 三通道值

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：Poisson 常用於描述在固定區間內獨立事件的計數資料。

其餘選項為何錯：
- `B`：連續型高度常不直接以 Poisson 描述。
- `C`：比例值與 Poisson 的計數本質不同。
- `D`：RGB 三通道不是事件次數模型。

補強知識點：
- Poisson 關鍵字：count、independent events、fixed rate。
- 看到『每小時幾次』常先想 Poisson。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 Poisson
- sources/scope-weight-map.md｜L22102 機率分佈與資料分佈模型

</details>

### 題 12｜`L22102`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若題目說『每小時瑕疵品個數、平均發生率固定、事件彼此獨立』，最可能對應哪一種分布？

- `A` 固定時間或空間內稀有事件的發生次數
- `B` 連續型測量值的精準高度
- `C` 只有類別標籤的比例值
- `D` 影像像素顏色的 RGB 三通道值

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：Poisson 常用於描述在固定區間內獨立事件的計數資料。

其餘選項為何錯：
- `B`：連續型高度常不直接以 Poisson 描述。
- `C`：比例值與 Poisson 的計數本質不同。
- `D`：RGB 三通道不是事件次數模型。

補強知識點：
- Poisson 關鍵字：count、independent events、fixed rate。
- 看到『每小時幾次』常先想 Poisson。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 Poisson
- sources/scope-weight-map.md｜L22102 機率分佈與資料分佈模型

</details>

## 今日必補知識點

- 熟記 Z-score 公式與意義，回看 [sources](../sources/) 內對應文件。
- 標準化分數常用來比較不同量尺資料的位置，回看 [sources](../sources/) 內對應文件。
- 看到『總額』先找 sum，不要被 count 誤導，回看 [sources](../sources/) 內對應文件。
- 資料聚合與視覺化要先釐清度量是 count、sum 還是 mean，回看 [sources](../sources/) 內對應文件。
- 統計顯著與因果解釋要切開，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s2d6_groupby_sum, s2d7_pvalue, s2d9_kfold, s2d9_bootstrap
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
