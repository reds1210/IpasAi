# Day 15｜科目 1 反向題單

- 今日焦點：`易混概念對抗題`
- 題量：`10` 題
- 建議方式：先以 60–75 分鐘完成第一輪，再展開解析。｜優先級 A｜先刷這份，對過線最有幫助。
- 來源對照：
  - [official-corpus.md](../sources/official-corpus.md)
  - [scope-weight-map.md](../sources/scope-weight-map.md)
  - [question-source-map.md](../sources/question-source-map.md)
  - [question-patterns.md](../sources/question-patterns.md)
  - [book-bridge.md](../sources/book-bridge.md)

## 今日題目

### 題 1｜`L21103`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

建立高效能 RAG 系統時，在檢索階段最關鍵的挑戰通常是什麼？

- `A` 一律提高溫度（temperature）讓回答更有創意
- `B` 只增加輸出字數上限而不調整檢索品質
- `C` 能否找回語意相關且可信的文件
- `D` 把所有文件一次塞進 context window

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：RAG 成敗首先取決於找回的文件是否相關且可信，生成器再強也難以修正錯誤檢索。

其餘選項為何錯：
- `A`：提高 temperature 影響生成風格，不會改善檢索精準度。
- `B`：只增加輸出長度無法彌補檢索來源不對的問題。
- `D`：把不相關文件全塞進上下文會增加噪音。

補強知識點：
- 把『檢索品質』與『生成品質』拆開看。
- 看到 RAG 錯誤時，先查 embedding、索引與召回文件品質。

回看來源：
- sources/official-corpus.md｜官方正式題與樣題都偏好 RAG 情境判斷
- sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用

</details>

### 題 2｜`L21103`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

若生成式 AI 明明可讀很多 token，但檢索回來的文件與問題常常不夠相關，系統品質仍差，最先該檢查哪一段？

- `A` 把所有文件一次塞進 context window
- `B` 一律提高溫度（temperature）讓回答更有創意
- `C` 只增加輸出字數上限而不調整檢索品質
- `D` 能否找回語意相關且可信的文件

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：RAG 成敗首先取決於找回的文件是否相關且可信，生成器再強也難以修正錯誤檢索。

其餘選項為何錯：
- `A`：把不相關文件全塞進上下文會增加噪音。
- `B`：提高 temperature 影響生成風格，不會改善檢索精準度。
- `C`：只增加輸出長度無法彌補檢索來源不對的問題。

補強知識點：
- 把『檢索品質』與『生成品質』拆開看。
- 看到 RAG 錯誤時，先查 embedding、索引與召回文件品質。

回看來源：
- sources/official-corpus.md｜官方正式題與樣題都偏好 RAG 情境判斷
- sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用

</details>

### 題 3｜`L21203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

在 AI 治理脈絡下，透明性（Transparency）通常指什麼？

- `A` 系統只要速度夠快就算透明
- `B` 只要模型有商業價值，就不需要說明原理
- `C` 決策流程與依據具可理解性與可追溯性
- `D` 所有模型都必須完全開源

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：透明性重點在可解釋與可追溯，不等於所有細節都要公開原始碼。

其餘選項為何錯：
- `A`：速度快與是否透明是不同維度。
- `B`：有商業價值不代表可以忽略說明責任。
- `D`：開源與否是治理手段選項，不是透明性的唯一條件。

補強知識點：
- 記住 transparency、explainability、traceability 是一組常連動的治理概念。
- 不要把『透明』誤解成『全部開源』。

回看來源：
- sources/official-corpus.md｜L21203 AI 風險管理與治理
- sources/scope-weight-map.md｜L21203 AI 風險管理

</details>

### 題 4｜`L21203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若企業要讓審查單位能追蹤 AI 如何得出決策、使用何種資料與規則，最符合哪項治理原則？

- `A` 只要模型有商業價值，就不需要說明原理
- `B` 決策流程與依據具可理解性與可追溯性
- `C` 所有模型都必須完全開源
- `D` 系統只要速度夠快就算透明

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：透明性重點在可解釋與可追溯，不等於所有細節都要公開原始碼。

其餘選項為何錯：
- `A`：有商業價值不代表可以忽略說明責任。
- `C`：開源與否是治理手段選項，不是透明性的唯一條件。
- `D`：速度快與是否透明是不同維度。

補強知識點：
- 記住 transparency、explainability、traceability 是一組常連動的治理概念。
- 不要把『透明』誤解成『全部開源』。

回看來源：
- sources/official-corpus.md｜L21203 AI 風險管理與治理
- sources/scope-weight-map.md｜L21203 AI 風險管理

</details>

### 題 5｜`L21301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

資料中若特徵尺度差異極大，最常見的前處理解法是什麼？

- `A` 完全不處理尺度差異
- `B` 對特徵做標準化或正規化
- `C` 直接刪除尺度較小的欄位
- `D` 把所有欄位都加上一個常數

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：對尺度敏感的模型常需先做標準化或正規化，避免某些欄位因量級大而主導學習。

其餘選項為何錯：
- `A`：忽略尺度差異會讓模型學習不穩定。
- `C`：刪欄位可能損失有效訊息，且不是解決尺度問題的標準做法。
- `D`：加常數不會改變相對尺度關係。

補強知識點：
- 標準化、正規化與模型敏感度要建立連結。
- 尺度問題通常先補 preprocessing，而不是先換演算法。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現標準化情境
- sources/scope-weight-map.md｜L21301 數據準備與模型選擇

</details>

### 題 6｜`L21301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

當年齡範圍是 0–100、收入範圍是 0–1,000,000，模型容易偏向高尺度欄位。若要先穩定模型，最合理的做法為何？

- `A` 把所有欄位都加上一個常數
- `B` 完全不處理尺度差異
- `C` 對特徵做標準化或正規化
- `D` 直接刪除尺度較小的欄位

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：對尺度敏感的模型常需先做標準化或正規化，避免某些欄位因量級大而主導學習。

其餘選項為何錯：
- `A`：加常數不會改變相對尺度關係。
- `B`：忽略尺度差異會讓模型學習不穩定。
- `D`：刪欄位可能損失有效訊息，且不是解決尺度問題的標準做法。

補強知識點：
- 標準化、正規化與模型敏感度要建立連結。
- 尺度問題通常先補 preprocessing，而不是先換演算法。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現標準化情境
- sources/scope-weight-map.md｜L21301 數據準備與模型選擇

</details>

### 題 7｜`L21302`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若企業想降低新模型上線事故對全部使用者的衝擊，最適合的部署策略為何？

- `A` 只在簡報中宣告模型已準備好
- `B` 採小流量試放的 canary 或分階段部署策略
- `C` 直接 100% 切到新版本
- `D` 先停掉舊服務再部署新版本

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：canary deployment 能在有限流量下觀察風險，便於回退。

其餘選項為何錯：
- `A`：文件宣告無法取代真實流量驗證。
- `C`：直接全量切換會把風險一次擴散到所有使用者。
- `D`：先停舊服務會增加停機與失敗風險。

補強知識點：
- 部署策略要跟風險控制綁在一起理解。
- 看到『小流量、先驗證、可回退』時，優先選 canary / phased rollout。

回看來源：
- sources/official-corpus.md｜L21302 系統部署與更新管理
- sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署

</details>

### 題 8｜`L21302`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

團隊準備替換線上模型，但擔心新版本會在真實流量下出現未預期錯誤。若要先在小流量驗證，應採哪種思路？

- `A` 直接 100% 切到新版本
- `B` 先停掉舊服務再部署新版本
- `C` 只在簡報中宣告模型已準備好
- `D` 採小流量試放的 canary 或分階段部署策略

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：canary deployment 能在有限流量下觀察風險，便於回退。

其餘選項為何錯：
- `A`：直接全量切換會把風險一次擴散到所有使用者。
- `B`：先停舊服務會增加停機與失敗風險。
- `C`：文件宣告無法取代真實流量驗證。

補強知識點：
- 部署策略要跟風險控制綁在一起理解。
- 看到『小流量、先驗證、可回退』時，優先選 canary / phased rollout。

回看來源：
- sources/official-corpus.md｜L21302 系統部署與更新管理
- sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署

</details>

### 題 9｜`L21101`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

資料量大且希望更有效捕捉罕見詞語意關聯時，Word2Vec 較適合採哪種訓練策略？

- `A` 採用 CBOW 並假設它對罕見詞一定更有利
- `B` 完全不做詞向量，只保留原始字串
- `C` 採用 Skip-gram 架構
- `D` 採用只靠詞頻排序的 TF-IDF

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：Skip-gram 以中心詞預測周邊詞，對低頻詞的表示通常更有優勢。

其餘選項為何錯：
- `A`：CBOW 訓練較快，但對低頻詞的語意關聯通常不如 Skip-gram 穩定。
- `B`：不做向量化無法讓模型有效利用詞的語意鄰近關係。
- `D`：TF-IDF 是加權方法，不是分散式詞向量模型。

補強知識點：
- 把 TF-IDF 與 Word2Vec 分清：前者是稀疏權重，後者是嵌入向量。
- 低頻詞、上下文語意、Skip-gram 這三個關鍵字要連在一起。

回看來源：
- sources/official-corpus.md｜正式題出現 Word2Vec / Skip-gram
- sources/scope-weight-map.md｜L21101 自然語言處理技術與應用

</details>

### 題 10｜`L21101`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

客服語料中有大量低頻專有名詞，若想讓詞向量更能學到罕見詞的上下文關係，較合理的選擇為何？

- `A` 完全不做詞向量，只保留原始字串
- `B` 採用 Skip-gram 架構
- `C` 採用只靠詞頻排序的 TF-IDF
- `D` 採用 CBOW 並假設它對罕見詞一定更有利

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：Skip-gram 以中心詞預測周邊詞，對低頻詞的表示通常更有優勢。

其餘選項為何錯：
- `A`：不做向量化無法讓模型有效利用詞的語意鄰近關係。
- `C`：TF-IDF 是加權方法，不是分散式詞向量模型。
- `D`：CBOW 訓練較快，但對低頻詞的語意關聯通常不如 Skip-gram 穩定。

補強知識點：
- 把 TF-IDF 與 Word2Vec 分清：前者是稀疏權重，後者是嵌入向量。
- 低頻詞、上下文語意、Skip-gram 這三個關鍵字要連在一起。

回看來源：
- sources/official-corpus.md｜正式題出現 Word2Vec / Skip-gram
- sources/scope-weight-map.md｜L21101 自然語言處理技術與應用

</details>

## 今日必補知識點

- 把『檢索品質』與『生成品質』拆開看，回看 [sources](../sources/) 內對應文件。
- 看到 RAG 錯誤時，先查 embedding、索引與召回文件品質，回看 [sources](../sources/) 內對應文件。
- 記住 transparency、explainability、traceability 是一組常連動的治理概念，回看 [sources](../sources/) 內對應文件。
- 不要把『透明』誤解成『全部開源』，回看 [sources](../sources/) 內對應文件。
- 標準化、正規化與模型敏感度要建立連結，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s1d3_retrieval_stage, s1d7_transparency, s1d8_scaling, s1d9_canary, s1d10_word2vec
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
