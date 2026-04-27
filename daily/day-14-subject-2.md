# Day 14｜科目 2 反向題單

- 今日焦點：`時間序列、ARIMA、ACF、殘差診斷`
- 題量：`12` 題
- 建議方式：3–5 小時內完成，先做題、再補點。｜優先級 B｜主線刷完後優先補這份。
- 來源對照：
  - [official-corpus.md](../sources/official-corpus.md)
  - [scope-weight-map.md](../sources/scope-weight-map.md)
  - [question-source-map.md](../sources/question-source-map.md)
  - [question-patterns.md](../sources/question-patterns.md)
  - [book-bridge.md](../sources/book-bridge.md)

## 今日題目

### 題 1｜`L22302`｜難度：`難`
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

### 題 2｜`L22302`｜難度：`難`
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

### 題 3｜`L22102`｜難度：`中`
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

### 題 4｜`L22102`｜難度：`中`
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

### 題 5｜`L22302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若時間序列存在趨勢而不平穩，常見的基本處理方式之一是什麼？

- `A` 把所有值都取絕對值
- `B` 只把欄位名稱改成 t
- `C` 直接 one-hot encoding 時間索引
- `D` 做差分（differencing）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：差分常用來移除趨勢，幫助序列更接近平穩。

其餘選項為何錯：
- `A`：取絕對值不會系統性處理趨勢。
- `B`：改欄位名不影響資料性質。
- `C`：one-hot 時間索引與平穩化是不同問題。

補強知識點：
- 非平穩序列與差分處理要成對記。
- ARIMA 的 I 就是 integrated / differencing。

回看來源：
- sources/official-corpus.md｜L22302 常見的大數據分析方法
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

### 題 6｜`L22302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

你懷疑序列平均數隨時間漂移，不符合平穩假設。若先做一個基本轉換，較合理的是什麼？

- `A` 直接 one-hot encoding 時間索引
- `B` 做差分（differencing）
- `C` 把所有值都取絕對值
- `D` 只把欄位名稱改成 t

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：差分常用來移除趨勢，幫助序列更接近平穩。

其餘選項為何錯：
- `A`：one-hot 時間索引與平穩化是不同問題。
- `C`：取絕對值不會系統性處理趨勢。
- `D`：改欄位名不影響資料性質。

補強知識點：
- 非平穩序列與差分處理要成對記。
- ARIMA 的 I 就是 integrated / differencing。

回看來源：
- sources/official-corpus.md｜L22302 常見的大數據分析方法
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

### 題 7｜`L22302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

在時間序列模型診斷中，『殘差接近白噪音』通常代表什麼？

- `A` 未來預測值保證不會出錯
- `B` 模型已捕捉大部分可解釋的時間結構
- `C` 模型一定 100% 正確
- `D` 資料集完全沒有外部干擾

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：殘差近白噪音表示剩餘誤差較接近隨機波動，是模型診斷的好訊號之一。

其餘選項為何錯：
- `A`：任何預測都不可能保證零錯誤。
- `C`：白噪音不等於模型完美無誤。
- `D`：外部干擾仍可能存在。

補強知識點：
- 白噪音是『較理想』，不是『完美』。
- 診斷題要避免過度解讀。

回看來源：
- sources/official-corpus.md｜時間序列殘差診斷
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

### 題 8｜`L22302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若模型殘差不再顯示明顯自相關結構，最常見的正向解讀為何？

- `A` 未來預測值保證不會出錯
- `B` 模型已捕捉大部分可解釋的時間結構
- `C` 模型一定 100% 正確
- `D` 資料集完全沒有外部干擾

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：殘差近白噪音表示剩餘誤差較接近隨機波動，是模型診斷的好訊號之一。

其餘選項為何錯：
- `A`：任何預測都不可能保證零錯誤。
- `C`：白噪音不等於模型完美無誤。
- `D`：外部干擾仍可能存在。

補強知識點：
- 白噪音是『較理想』，不是『完美』。
- 診斷題要避免過度解讀。

回看來源：
- sources/official-corpus.md｜時間序列殘差診斷
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

### 題 9｜`L22302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若每週或每月都出現固定重複波動，下列哪個概念最貼近這種現象？

- `A` 正規化（normalization）
- `B` 季節性（seasonality）
- `C` 缺失值（missingness）
- `D` 共線性（multicollinearity）

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：規律重複的週期波動通常稱為季節性，是時間序列的重要結構之一。

其餘選項為何錯：
- `A`：正規化是前處理方法。
- `C`：缺失值是資料缺漏。
- `D`：共線性是多變數之間的線性關聯問題。

補強知識點：
- 時間序列的趨勢、季節性、殘差要拆開記。
- 固定週期波動不是隨機噪聲。

回看來源：
- sources/official-corpus.md｜時間序列分析主題
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

### 題 10｜`L22302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

銷售資料在每個月初都會固定飆升，這種可重複的週期結構最常稱為什麼？

- `A` 缺失值（missingness）
- `B` 共線性（multicollinearity）
- `C` 正規化（normalization）
- `D` 季節性（seasonality）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：規律重複的週期波動通常稱為季節性，是時間序列的重要結構之一。

其餘選項為何錯：
- `A`：缺失值是資料缺漏。
- `B`：共線性是多變數之間的線性關聯問題。
- `C`：正規化是前處理方法。

補強知識點：
- 時間序列的趨勢、季節性、殘差要拆開記。
- 固定週期波動不是隨機噪聲。

回看來源：
- sources/official-corpus.md｜時間序列分析主題
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

### 題 11｜`L22302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

在 ACF 圖中提到的 lag，最接近哪個意思？

- `A` 目前值與往前 3 個時間步之間的延遲關係
- `B` 第三個特徵欄位的名稱
- `C` 第三個模型版本
- `D` 第三種資料型態

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：lag 描述的是時間序列向後回看的延遲步數。

其餘選項為何錯：
- `B`：lag 與特徵欄位編號無關。
- `C`：模型版本不是時間延遲。
- `D`：資料型態也與 lag 無關。

補強知識點：
- 時間序列的 lag 是延遲，不是欄位序號。
- ACF/PACF 題常用 lag 當關鍵詞。

回看來源：
- sources/official-corpus.md｜時間序列分析主題
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

### 題 12｜`L22302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若說某序列在 lag 3 上仍有明顯自相關，這裡的 lag 3 通常指什麼？

- `A` 第三個特徵欄位的名稱
- `B` 第三個模型版本
- `C` 第三種資料型態
- `D` 目前值與往前 3 個時間步之間的延遲關係

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：lag 描述的是時間序列向後回看的延遲步數。

其餘選項為何錯：
- `A`：lag 與特徵欄位編號無關。
- `B`：模型版本不是時間延遲。
- `C`：資料型態也與 lag 無關。

補強知識點：
- 時間序列的 lag 是延遲，不是欄位序號。
- ACF/PACF 題常用 lag 當關鍵詞。

回看來源：
- sources/official-corpus.md｜時間序列分析主題
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

## 今日必補知識點

- 時間序列診斷常看殘差是否近白噪音，回看 [sources](../sources/) 內對應文件。
- ACF 顯著不為 0 常暗示 underfitting 或規格不完整，回看 [sources](../sources/) 內對應文件。
- Poisson 關鍵字：count、independent events、fixed rate，回看 [sources](../sources/) 內對應文件。
- 看到『每小時幾次』常先想 Poisson，回看 [sources](../sources/) 內對應文件。
- 非平穩序列與差分處理要成對記，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
