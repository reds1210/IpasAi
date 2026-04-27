# Day 11｜科目 1 反向題單

- 今日焦點：`第一次高頻回鍋`
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

### 題 3｜`L21103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

檢索增強生成（RAG）最主要想解決大型語言模型的哪一類問題？

- `A` 讓模型完全不需要任何外部資料
- `B` 讓模型只依隨機生成內容作答
- `C` 把所有回應限制為固定規則模板
- `D` 降低知識過時與幻覺風險

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：RAG 透過外部檢索補入最新或可信文件，能降低知識過時與幻覺。

其餘選項為何錯：
- `A`：RAG 的目的正是引入外部知識，而不是移除外部資料。
- `B`：隨機生成不會提升正確性，反而增加不穩定性。
- `C`：固定模板會降低表達能力，也無法解決知識更新問題。

補強知識點：
- 理解 RAG 的核心價值：檢索可信內容再生成。
- 區分『更新知識』與『重訓模型』兩條不同路線。

回看來源：
- sources/official-corpus.md｜評鑑範圍含生成式 AI 技術與應用
- sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用

</details>

### 題 4｜`L21103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

法務團隊抱怨內部生成式 AI 會引用過時資料並偶爾胡亂編造答案，若先不重訓模型，最合理的補強方向為何？

- `A` 降低知識過時與幻覺風險
- `B` 讓模型完全不需要任何外部資料
- `C` 讓模型只依隨機生成內容作答
- `D` 把所有回應限制為固定規則模板

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：RAG 透過外部檢索補入最新或可信文件，能降低知識過時與幻覺。

其餘選項為何錯：
- `B`：RAG 的目的正是引入外部知識，而不是移除外部資料。
- `C`：隨機生成不會提升正確性，反而增加不穩定性。
- `D`：固定模板會降低表達能力，也無法解決知識更新問題。

補強知識點：
- 理解 RAG 的核心價值：檢索可信內容再生成。
- 區分『更新知識』與『重訓模型』兩條不同路線。

回看來源：
- sources/official-corpus.md｜評鑑範圍含生成式 AI 技術與應用
- sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用

</details>

### 題 5｜`L21203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

企業部署生成式 AI 協助行銷內容產出，若要降低著作權侵權風險，最有效的預防策略為何？

- `A` 只看點擊率，不必檢查引用來源與授權
- `B` 建立資料來源審查、輸出覆核與授權檢查流程
- `C` 只要模型夠大，就不會有著作權風險
- `D` 把所有輸出都自動發布，避免人工拖慢速度

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：著作權風險主要來自訓練來源、輸出近似與使用流程，因此要建立審查與覆核機制。

其餘選項為何錯：
- `A`：只看商業指標會忽略法律風險。
- `C`：模型大小與侵權風險沒有必然反比關係。
- `D`：自動發布會放大錯誤輸出與侵權責任。

補強知識點：
- 生成式 AI 法務風險通常要從流程治理，而非只從模型參數處理。
- 看到『侵權』優先想到授權、來源、覆核、紀錄。

回看來源：
- sources/official-corpus.md｜正式題出現生成式 AI 著作權風險
- sources/scope-weight-map.md｜L21203 AI 風險管理

</details>

### 題 6｜`L21203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

內容團隊常把 AI 生成文案直接外發。若你要從流程面先降風險，最優先的安排應是什麼？

- `A` 把所有輸出都自動發布，避免人工拖慢速度
- `B` 只看點擊率，不必檢查引用來源與授權
- `C` 建立資料來源審查、輸出覆核與授權檢查流程
- `D` 只要模型夠大，就不會有著作權風險

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：著作權風險主要來自訓練來源、輸出近似與使用流程，因此要建立審查與覆核機制。

其餘選項為何錯：
- `A`：自動發布會放大錯誤輸出與侵權責任。
- `B`：只看商業指標會忽略法律風險。
- `D`：模型大小與侵權風險沒有必然反比關係。

補強知識點：
- 生成式 AI 法務風險通常要從流程治理，而非只從模型參數處理。
- 看到『侵權』優先想到授權、來源、覆核、紀錄。

回看來源：
- sources/official-corpus.md｜正式題出現生成式 AI 著作權風險
- sources/scope-weight-map.md｜L21203 AI 風險管理

</details>

### 題 7｜`L21302`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

Kubernetes 在 AI 模型部署與運行中的核心角色最接近下列何者？

- `A` 直接負責所有 GPU 推論計算本身
- `B` 管理與協調模型服務的部署、擴展與運行環境
- `C` 自動幫模型做超參數調整
- `D` 提供資料倉儲與版本控管的全部功能

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：Kubernetes 主要處理容器化服務的部署、調度、擴縮與穩定運行。

其餘選項為何錯：
- `A`：Kubernetes 會調度資源，但不等於 GPU 推論演算法本身。
- `C`：超參數調整屬訓練與實驗管理，不是 Kubernetes 的核心職責。
- `D`：資料倉儲與版本控管需要其他工具配合。

補強知識點：
- Kubernetes 是 orchestration，不是 model training tool。
- 分清部署平台、實驗平台、資料平台的責任。

回看來源：
- sources/official-corpus.md｜正式題出現 Kubernetes
- sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署

</details>

### 題 8｜`L21302`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若團隊想讓模型服務能自動部署、擴縮與管理執行環境，最符合 Kubernetes 價值的描述為何？

- `A` 管理與協調模型服務的部署、擴展與運行環境
- `B` 自動幫模型做超參數調整
- `C` 提供資料倉儲與版本控管的全部功能
- `D` 直接負責所有 GPU 推論計算本身

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：Kubernetes 主要處理容器化服務的部署、調度、擴縮與穩定運行。

其餘選項為何錯：
- `B`：超參數調整屬訓練與實驗管理，不是 Kubernetes 的核心職責。
- `C`：資料倉儲與版本控管需要其他工具配合。
- `D`：Kubernetes 會調度資源，但不等於 GPU 推論演算法本身。

補強知識點：
- Kubernetes 是 orchestration，不是 model training tool。
- 分清部署平台、實驗平台、資料平台的責任。

回看來源：
- sources/official-corpus.md｜正式題出現 Kubernetes
- sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署

</details>

## 今日必補知識點

- 區分 tokenization、lemmatization、stopword removal、TF-IDF 的先後次序，回看 [sources](../sources/) 內對應文件。
- 記住 NLP 前處理常見管線：切詞、清理、向量化，回看 [sources](../sources/) 內對應文件。
- 理解 RAG 的核心價值：檢索可信內容再生成，回看 [sources](../sources/) 內對應文件。
- 區分『更新知識』與『重訓模型』兩條不同路線，回看 [sources](../sources/) 內對應文件。
- 生成式 AI 法務風險通常要從流程治理，而非只從模型參數處理，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s1d1_tokenization, s1d3_rag_core, s1d7_copyright_prevention, s1d9_kubernetes
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
