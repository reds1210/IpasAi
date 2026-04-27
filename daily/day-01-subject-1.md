# Day 01｜科目 1 反向題單

- 今日焦點：`NLP 基礎與 AI/ML 邊界`
- 題量：`8` 題
- 建議方式：先以 60–75 分鐘完成第一輪，再展開解析。｜優先級 A｜先刷這份，對過線最有幫助。
- 來源對照：
  - [official-corpus.md](../sources/official-corpus.md)
  - [scope-weight-map.md](../sources/scope-weight-map.md)
  - [question-source-map.md](../sources/question-source-map.md)
  - [question-patterns.md](../sources/question-patterns.md)
  - [book-bridge.md](../sources/book-bridge.md)

## 今日題目

### 題 1｜`L21101`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

在文本前處理中，將連續文字切成可供模型處理的詞彙單位，這個步驟稱為何者？

- `A` 詞形還原（Lemmatization）
- `B` 停用詞移除（Stopword Removal）
- `C` 詞頻逆文件頻率（TF-IDF）
- `D` 斷詞（Tokenization）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：斷詞的目的就是把連續文本切成 token，通常是 NLP 前處理的起點。

其餘選項為何錯：
- `A`：詞形還原是把單字轉回原型，不負責切分字串。
- `B`：停用詞移除是在切詞之後刪掉低資訊量詞語。
- `C`：TF-IDF 是權重計算方法，不是切詞步驟。

補強知識點：
- 區分 tokenization、lemmatization、stopword removal、TF-IDF 的先後次序。
- 記住 NLP 前處理常見管線：切詞、清理、向量化。

回看來源：
- sources/official-corpus.md｜114.09 樣題曾出現 tokenization 類題
- sources/scope-weight-map.md｜L21101 自然語言處理技術與應用

</details>

### 題 2｜`L21101`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

客服團隊想先把抱怨訊息拆成模型可處理的 token，再做後續分析，最先應執行哪個技術？

- `A` 斷詞（Tokenization）
- `B` 詞形還原（Lemmatization）
- `C` 停用詞移除（Stopword Removal）
- `D` 詞頻逆文件頻率（TF-IDF）

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：斷詞的目的就是把連續文本切成 token，通常是 NLP 前處理的起點。

其餘選項為何錯：
- `B`：詞形還原是把單字轉回原型，不負責切分字串。
- `C`：停用詞移除是在切詞之後刪掉低資訊量詞語。
- `D`：TF-IDF 是權重計算方法，不是切詞步驟。

補強知識點：
- 區分 tokenization、lemmatization、stopword removal、TF-IDF 的先後次序。
- 記住 NLP 前處理常見管線：切詞、清理、向量化。

回看來源：
- sources/official-corpus.md｜114.09 樣題曾出現 tokenization 類題
- sources/scope-weight-map.md｜L21101 自然語言處理技術與應用

</details>

### 題 3｜`L21101`｜難度：`易`
優先級：`A`｜來源層級：`official-derived`

下列何者最符合自然語言處理在機器學習中的典型用途？

- `A` 預測性維護（Predictive Maintenance）
- `B` 供應鏈優化（Supply Chain Optimization）
- `C` 情緒分析（Sentiment Analysis）
- `D` 圖像分類（Image Classification）

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：情緒分析直接處理文字的語意與情緒極性，是 NLP 的典型應用。

其餘選項為何錯：
- `A`：預測性維護通常依賴感測器或設備紀錄，不是文字情緒任務。
- `B`：供應鏈優化偏向營運分析，並非文字理解任務。
- `D`：圖像分類屬於電腦視覺，不處理文字語意。

補強知識點：
- 建立文字任務與 NLP、影像任務與 CV 的快速對應。
- 看到『留言、評論、客服紀錄』時，優先想到文本分析。

回看來源：
- sources/official-corpus.md｜官方樣題有 NLP 情緒分析類型
- sources/scope-weight-map.md｜L21101 自然語言處理技術與應用

</details>

### 題 4｜`L21101`｜難度：`易`
優先級：`A`｜來源層級：`official-derived`

銀行想分析客服留言的正負向傾向，若資料主要是文字，最適合先導入哪一類 AI 任務？

- `A` 預測性維護（Predictive Maintenance）
- `B` 供應鏈優化（Supply Chain Optimization）
- `C` 情緒分析（Sentiment Analysis）
- `D` 圖像分類（Image Classification）

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：情緒分析直接處理文字的語意與情緒極性，是 NLP 的典型應用。

其餘選項為何錯：
- `A`：預測性維護通常依賴感測器或設備紀錄，不是文字情緒任務。
- `B`：供應鏈優化偏向營運分析，並非文字理解任務。
- `D`：圖像分類屬於電腦視覺，不處理文字語意。

補強知識點：
- 建立文字任務與 NLP、影像任務與 CV 的快速對應。
- 看到『留言、評論、客服紀錄』時，優先想到文本分析。

回看來源：
- sources/official-corpus.md｜官方樣題有 NLP 情緒分析類型
- sources/scope-weight-map.md｜L21101 自然語言處理技術與應用

</details>

### 題 5｜`L21103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

下列哪一種情境最不屬於使用 AI 或機器學習能力的系統？

- `A` 透過資料訓練改善準確率的影像辨識模型
- `B` 使用固定規則決定行為的傳統程式
- `C` 透過深度神經網路進行語音辨識的系統
- `D` 使用 NLP 理解用戶查詢的聊天機器人

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：只有固定規則、沒有從資料中學習或泛化能力的系統，不應被誤判成機器學習系統。

其餘選項為何錯：
- `A`：影像辨識若依資料訓練改善效能，屬於機器學習。
- `C`：語音辨識常使用深度學習模型，屬於 AI/ML。
- `D`：聊天機器人若理解文本與生成回覆，屬於 NLP 應用。

補強知識點：
- 區分 rule-based automation 與 ML system 的邊界。
- 看到『固定規則、無訓練資料』時，先排除 ML。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現 AI/ML 邊界判斷
- sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用

</details>

### 題 6｜`L21103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若一個象棋程式只依預先寫死的規則枚舉下一步，沒有依資料學習，最合理的判斷為何？

- `A` 使用 NLP 理解用戶查詢的聊天機器人
- `B` 透過資料訓練改善準確率的影像辨識模型
- `C` 使用固定規則決定行為的傳統程式
- `D` 透過深度神經網路進行語音辨識的系統

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：只有固定規則、沒有從資料中學習或泛化能力的系統，不應被誤判成機器學習系統。

其餘選項為何錯：
- `A`：聊天機器人若理解文本與生成回覆，屬於 NLP 應用。
- `B`：影像辨識若依資料訓練改善效能，屬於機器學習。
- `D`：語音辨識常使用深度學習模型，屬於 AI/ML。

補強知識點：
- 區分 rule-based automation 與 ML system 的邊界。
- 看到『固定規則、無訓練資料』時，先排除 ML。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現 AI/ML 邊界判斷
- sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用

</details>

### 題 7｜`L21101`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若企業要從大量 FAQ 與客服逐字稿中自動找出常見問題與關鍵主題，最先應考慮哪一類技術？

- `A` 只做規則式關鍵字比對且不建立語意表示
- `B` 自然語言處理技術（NLP）
- `C` 電腦視覺技術（CV）
- `D` 單純關聯式資料庫正規化

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：任務核心是理解文字內容、主題與語意，因此應先選 NLP 技術。

其餘選項為何錯：
- `A`：純關鍵字規則缺乏語意泛化能力，面對同義表達容易失效。
- `C`：CV 主要處理影像與影片，不處理文本語意。
- `D`：資料庫正規化是資料儲存設計，無法直接理解文本語意。

補強知識點：
- 從問題的輸入資料型態判斷技術路線。
- 文字理解任務優先想 NLP，而不是存儲或純規則方案。

回看來源：
- sources/official-corpus.md｜官方範圍將 NLP 列在 L21101
- sources/scope-weight-map.md｜L21101 自然語言處理技術與應用

</details>

### 題 8｜`L21101`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

製造商累積大量維修文字紀錄，想讓系統先理解文本內容再做分類與摘要，最適合的起點為何？

- `A` 電腦視覺技術（CV）
- `B` 單純關聯式資料庫正規化
- `C` 只做規則式關鍵字比對且不建立語意表示
- `D` 自然語言處理技術（NLP）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：任務核心是理解文字內容、主題與語意，因此應先選 NLP 技術。

其餘選項為何錯：
- `A`：CV 主要處理影像與影片，不處理文本語意。
- `B`：資料庫正規化是資料儲存設計，無法直接理解文本語意。
- `C`：純關鍵字規則缺乏語意泛化能力，面對同義表達容易失效。

補強知識點：
- 從問題的輸入資料型態判斷技術路線。
- 文字理解任務優先想 NLP，而不是存儲或純規則方案。

回看來源：
- sources/official-corpus.md｜官方範圍將 NLP 列在 L21101
- sources/scope-weight-map.md｜L21101 自然語言處理技術與應用

</details>

## 今日必補知識點

- 區分 tokenization、lemmatization、stopword removal、TF-IDF 的先後次序，回看 [sources](../sources/) 內對應文件。
- 記住 NLP 前處理常見管線：切詞、清理、向量化，回看 [sources](../sources/) 內對應文件。
- 建立文字任務與 NLP、影像任務與 CV 的快速對應，回看 [sources](../sources/) 內對應文件。
- 看到『留言、評論、客服紀錄』時，優先想到文本分析，回看 [sources](../sources/) 內對應文件。
- 區分 rule-based automation 與 ML system 的邊界，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s1d1_tokenization, s1d1_sentiment, s1d1_rule_based_boundary, s1d1_language_model_fit
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
