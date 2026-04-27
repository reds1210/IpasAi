# Day 02｜科目 1 反向題單

- 今日焦點：`電腦視覺基本任務`
- 題量：`8` 題
- 建議方式：先以 60–75 分鐘完成第一輪，再展開解析。｜優先級 B｜主線刷完後優先補這份。
- 來源對照：
  - [official-corpus.md](../sources/official-corpus.md)
  - [scope-weight-map.md](../sources/scope-weight-map.md)
  - [question-source-map.md](../sources/question-source-map.md)
  - [question-patterns.md](../sources/question-patterns.md)
  - [book-bridge.md](../sources/book-bridge.md)

## 今日題目

### 題 1｜`L21102`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若模型只需判定一張照片中主要物件屬於哪個類別，最符合哪一種電腦視覺任務？

- `A` 物件偵測（Object Detection）
- `B` 語義分割（Semantic Segmentation）
- `C` 實例分割（Instance Segmentation）
- `D` 圖像分類（Image Classification）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：圖像分類只回答整張圖的類別，不要求定位或像素級分割。

其餘選項為何錯：
- `A`：物件偵測還要輸出邊界框與位置。
- `B`：語義分割需要對每個像素標上類別。
- `C`：實例分割除了像素標註，還要區分同類別不同個體。

補強知識點：
- 分類、偵測、語義分割、實例分割的輸出粒度要分清。
- 看到『只要知道是什麼』先想 classification。

回看來源：
- sources/official-corpus.md｜官方樣題曾比較多種 CV 任務
- sources/scope-weight-map.md｜L21102 電腦視覺技術與應用

</details>

### 題 2｜`L21102`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

零售商只想知道商品照片屬於鞋子、包包或外套，不需框出位置，應選哪種 CV 任務？

- `A` 物件偵測（Object Detection）
- `B` 語義分割（Semantic Segmentation）
- `C` 實例分割（Instance Segmentation）
- `D` 圖像分類（Image Classification）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：圖像分類只回答整張圖的類別，不要求定位或像素級分割。

其餘選項為何錯：
- `A`：物件偵測還要輸出邊界框與位置。
- `B`：語義分割需要對每個像素標上類別。
- `C`：實例分割除了像素標註，還要區分同類別不同個體。

補強知識點：
- 分類、偵測、語義分割、實例分割的輸出粒度要分清。
- 看到『只要知道是什麼』先想 classification。

回看來源：
- sources/official-corpus.md｜官方樣題曾比較多種 CV 任務
- sources/scope-weight-map.md｜L21102 電腦視覺技術與應用

</details>

### 題 3｜`L21102`｜難度：`易`
優先級：`B`｜來源層級：`official-derived`

哪一種深度學習架構通常最適合處理影像辨識任務？

- `A` 朴素貝氏分類器（Naive Bayes）
- `B` 單純遞迴神經網路（RNN）
- `C` Apriori 關聯規則演算法
- `D` 卷積神經網路（CNN）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：CNN 能有效抽取局部空間特徵，是影像辨識的標準基礎架構。

其餘選項為何錯：
- `A`：Naive Bayes 可做分類，但不擅長高維影像特徵表示。
- `B`：RNN 較適合序列資料，不是影像辨識主流骨幹。
- `C`：Apriori 用於關聯規則分析，與影像辨識無關。

補強知識點：
- 影像任務先聯想到 CNN；序列任務再考慮 RNN/Transformer。
- 辨識演算法名稱與資料型態的典型搭配。

回看來源：
- sources/official-corpus.md｜科目一評鑑範圍含 CV 技術
- sources/scope-weight-map.md｜L21102 電腦視覺技術與應用

</details>

### 題 4｜`L21102`｜難度：`易`
優先級：`B`｜來源層級：`official-derived`

工廠想用影像自動檢測零件表面瑕疵，若以深度學習為主體，最常見的核心架構是哪一類？

- `A` 卷積神經網路（CNN）
- `B` 朴素貝氏分類器（Naive Bayes）
- `C` 單純遞迴神經網路（RNN）
- `D` Apriori 關聯規則演算法

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：CNN 能有效抽取局部空間特徵，是影像辨識的標準基礎架構。

其餘選項為何錯：
- `B`：Naive Bayes 可做分類，但不擅長高維影像特徵表示。
- `C`：RNN 較適合序列資料，不是影像辨識主流骨幹。
- `D`：Apriori 用於關聯規則分析，與影像辨識無關。

補強知識點：
- 影像任務先聯想到 CNN；序列任務再考慮 RNN/Transformer。
- 辨識演算法名稱與資料型態的典型搭配。

回看來源：
- sources/official-corpus.md｜科目一評鑑範圍含 CV 技術
- sources/scope-weight-map.md｜L21102 電腦視覺技術與應用

</details>

### 題 5｜`L21102`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若企業要把紙本發票中的文字轉成可搜尋的文字資料，最符合哪一種技術應用？

- `A` 語音轉文字（ASR）
- `B` 情緒分析（Sentiment Analysis）
- `C` 推薦系統（Recommendation System）
- `D` 光學字元辨識（OCR）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：OCR 的核心是從影像中辨識文字內容，再轉成結構化或可搜尋文本。

其餘選項為何錯：
- `A`：ASR 處理的是語音，不是影像中的文字。
- `B`：情緒分析是文本理解任務，不負責從影像擷取文字。
- `C`：推薦系統不處理影像文字抽取。

補強知識點：
- 分清 OCR、ASR、NLP 的輸入資料型態差異。
- 看到『影像裡的文字』時，優先想到 OCR。

回看來源：
- sources/official-corpus.md｜L21102 涵蓋 CV 技術應用
- sources/scope-weight-map.md｜L21102 電腦視覺技術與應用

</details>

### 題 6｜`L21102`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

倉儲人員拍攝送貨單影像，想自動擷取影像中的品名與數量，最先應想到哪種 CV/NLP 橋接技術？

- `A` 光學字元辨識（OCR）
- `B` 語音轉文字（ASR）
- `C` 情緒分析（Sentiment Analysis）
- `D` 推薦系統（Recommendation System）

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：OCR 的核心是從影像中辨識文字內容，再轉成結構化或可搜尋文本。

其餘選項為何錯：
- `B`：ASR 處理的是語音，不是影像中的文字。
- `C`：情緒分析是文本理解任務，不負責從影像擷取文字。
- `D`：推薦系統不處理影像文字抽取。

補強知識點：
- 分清 OCR、ASR、NLP 的輸入資料型態差異。
- 看到『影像裡的文字』時，優先想到 OCR。

回看來源：
- sources/official-corpus.md｜L21102 涵蓋 CV 技術應用
- sources/scope-weight-map.md｜L21102 電腦視覺技術與應用

</details>

### 題 7｜`L21102`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

下列哪一種場景最適合優先導入電腦視覺技術？

- `A` 只用手動表單蒐集設備巡檢紀錄的流程系統
- `B` 以影像做瑕疵檢測與物件定位的電腦視覺方案
- `C` 只用文字規則判斷客服情緒的 NLP 系統
- `D` 只靠時間序列做下季營收預測的迴歸模型

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：產線瑕疵檢測的輸入是影像，且常需定位缺陷，電腦視覺是最直接的路線。

其餘選項為何錯：
- `A`：手動表單流程本身不提供自動影像判讀能力。
- `C`：客服情緒是文字任務，不屬於影像檢測。
- `D`：營收預測是數值預測問題，與影像辨識不同。

補強知識點：
- 根據輸入資料型態與業務目的選技術。
- 品質檢測、定位、辨識通常優先落在 CV 範圍。

回看來源：
- sources/official-corpus.md｜L21102 電腦視覺技術與應用
- sources/scope-weight-map.md｜L21102 電腦視覺技術與應用

</details>

### 題 8｜`L21102`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

電子廠想在產線上即時檢查焊點是否缺件或偏移，最合理的 AI 技術起點為何？

- `A` 以影像做瑕疵檢測與物件定位的電腦視覺方案
- `B` 只用文字規則判斷客服情緒的 NLP 系統
- `C` 只靠時間序列做下季營收預測的迴歸模型
- `D` 只用手動表單蒐集設備巡檢紀錄的流程系統

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：產線瑕疵檢測的輸入是影像，且常需定位缺陷，電腦視覺是最直接的路線。

其餘選項為何錯：
- `B`：客服情緒是文字任務，不屬於影像檢測。
- `C`：營收預測是數值預測問題，與影像辨識不同。
- `D`：手動表單流程本身不提供自動影像判讀能力。

補強知識點：
- 根據輸入資料型態與業務目的選技術。
- 品質檢測、定位、辨識通常優先落在 CV 範圍。

回看來源：
- sources/official-corpus.md｜L21102 電腦視覺技術與應用
- sources/scope-weight-map.md｜L21102 電腦視覺技術與應用

</details>

## 今日必補知識點

- 分類、偵測、語義分割、實例分割的輸出粒度要分清，回看 [sources](../sources/) 內對應文件。
- 看到『只要知道是什麼』先想 classification，回看 [sources](../sources/) 內對應文件。
- 影像任務先聯想到 CNN；序列任務再考慮 RNN/Transformer，回看 [sources](../sources/) 內對應文件。
- 辨識演算法名稱與資料型態的典型搭配，回看 [sources](../sources/) 內對應文件。
- 分清 OCR、ASR、NLP 的輸入資料型態差異，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
