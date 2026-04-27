# Day 03｜科目 1 反向題單

- 今日焦點：`生成式 AI 與 RAG`
- 題量：`8` 題
- 建議方式：先以 60–75 分鐘完成第一輪，再展開解析。｜優先級 A｜先刷這份，對過線最有幫助。
- 來源對照：
  - [official-corpus.md](../sources/official-corpus.md)
  - [scope-weight-map.md](../sources/scope-weight-map.md)
  - [question-source-map.md](../sources/question-source-map.md)
  - [question-patterns.md](../sources/question-patterns.md)
  - [book-bridge.md](../sources/book-bridge.md)

## 今日題目

### 題 1｜`L21103`｜難度：`中`
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

### 題 2｜`L21103`｜難度：`中`
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

### 題 3｜`L21103`｜難度：`難`
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

### 題 4｜`L21103`｜難度：`難`
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

### 題 5｜`L21103`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

訓練生成式 AI 時導入資料增強後，模型效能反而下降，下列哪個原因最合理？

- `A` 提高增強比例必然能修正所有過擬合問題
- `B` 把增強資料混入後，不需要再確認語意一致性
- `C` 增強後資料分布偏離原任務語意，破壞了泛化基礎
- `D` 只要資料量變多，模型一定會變好

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：資料增強若破壞原始語意或讓分布偏離真實資料，可能直接傷害模型學習。

其餘選項為何錯：
- `A`：過高比例的低品質增強資料可能讓模型學到偏差模式。
- `B`：augmentation 仍需維持語意一致性，否則標註訊號會失真。
- `D`：資料量增加不等於訊號品質提升。

補強知識點：
- 資料增強不是越多越好，關鍵是語意一致與分布合理。
- 先檢查 augmentation strategy，再調 learning rate 或模型大小。

回看來源：
- sources/official-corpus.md｜正式題曾出現 Data Augmentation 情境
- sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用

</details>

### 題 6｜`L21103`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

團隊把原始影像或文本做大量 augmentation 後，發現模型泛化能力變差。若要先抓最可能的根因，應優先懷疑什麼？

- `A` 增強後資料分布偏離原任務語意，破壞了泛化基礎
- `B` 只要資料量變多，模型一定會變好
- `C` 提高增強比例必然能修正所有過擬合問題
- `D` 把增強資料混入後，不需要再確認語意一致性

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：資料增強若破壞原始語意或讓分布偏離真實資料，可能直接傷害模型學習。

其餘選項為何錯：
- `B`：資料量增加不等於訊號品質提升。
- `C`：過高比例的低品質增強資料可能讓模型學到偏差模式。
- `D`：augmentation 仍需維持語意一致性，否則標註訊號會失真。

補強知識點：
- 資料增強不是越多越好，關鍵是語意一致與分布合理。
- 先檢查 augmentation strategy，再調 learning rate 或模型大小。

回看來源：
- sources/official-corpus.md｜正式題曾出現 Data Augmentation 情境
- sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用

</details>

### 題 7｜`L21302`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

企業導入生成式 AI 時，若希望在不大幅犧牲效果下減少模型記憶體占用，最常見的壓縮方法是哪一種？

- `A` 只提高 batch size 不改模型結構
- `B` 參數剪枝（Pruning）
- `C` 增加模型層數
- `D` 把訓練資料維度做得更高

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：參數剪枝會移除低重要性的權重，是常見的模型壓縮技術。

其餘選項為何錯：
- `A`：batch size 影響訓練批次，不是主要的模型壓縮手段。
- `C`：增加模型層數通常會提高記憶體需求。
- `D`：提高資料維度反而增加計算與儲存負擔。

補強知識點：
- 區分模型壓縮、訓練策略調整、資料工程三種不同問題。
- 記住 pruning、quantization、distillation 都是常見壓縮家族。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現模型壓縮
- sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署

</details>

### 題 8｜`L21302`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若邊緣設備無法承載完整模型權重，團隊希望先從模型壓縮著手，最合理的第一步為何？

- `A` 增加模型層數
- `B` 把訓練資料維度做得更高
- `C` 只提高 batch size 不改模型結構
- `D` 參數剪枝（Pruning）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：參數剪枝會移除低重要性的權重，是常見的模型壓縮技術。

其餘選項為何錯：
- `A`：增加模型層數通常會提高記憶體需求。
- `B`：提高資料維度反而增加計算與儲存負擔。
- `C`：batch size 影響訓練批次，不是主要的模型壓縮手段。

補強知識點：
- 區分模型壓縮、訓練策略調整、資料工程三種不同問題。
- 記住 pruning、quantization、distillation 都是常見壓縮家族。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現模型壓縮
- sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署

</details>

## 今日必補知識點

- 理解 RAG 的核心價值：檢索可信內容再生成，回看 [sources](../sources/) 內對應文件。
- 區分『更新知識』與『重訓模型』兩條不同路線，回看 [sources](../sources/) 內對應文件。
- 把『檢索品質』與『生成品質』拆開看，回看 [sources](../sources/) 內對應文件。
- 看到 RAG 錯誤時，先查 embedding、索引與召回文件品質，回看 [sources](../sources/) 內對應文件。
- 資料增強不是越多越好，關鍵是語意一致與分布合理，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s1d3_rag_core, s1d3_retrieval_stage, s1d3_augmentation_semantics, s1d3_pruning
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
