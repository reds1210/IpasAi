# Day 19｜科目 1 反向題單

- 今日焦點：`曾錯主題反向變體`
- 題量：`12` 題
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

### 題 2｜`L21103`｜難度：`中`
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

### 題 3｜`L21103`｜難度：`難`
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

### 題 4｜`L21103`｜難度：`難`
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

### 題 5｜`L21203`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

若模型容易被對抗樣本騙過，從模型層面最直接的補強做法通常是什麼？

- `A` 導入對抗訓練（adversarial training）
- `B` 只增加輸出字數上限
- `C` 只把訓練資料做欄位重新命名
- `D` 只在簡報中加入風險聲明而不調整模型

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：對抗訓練是直接把擾動樣本納入訓練，提升模型對惡意擾動的穩健性。

其餘選項為何錯：
- `B`：輸出字數與對抗韌性無直接關聯。
- `C`：重新命名欄位不會改變模型面對對抗擾動的能力。
- `D`：風險聲明屬治理措施，不是模型層補強。

補強知識點：
- 把技術補強與流程治理分開看。
- 只要題目強調『惡意擾動輸入』，優先想到 adversarial training 或 robust training。

回看來源：
- sources/official-corpus.md｜正式題出現對抗攻擊情境
- sources/scope-weight-map.md｜L21203 AI 風險管理

</details>

### 題 6｜`L21203`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

金融風控模型被駭客透過微小特徵擾動成功誤導。若你想優先提升模型對這類攻擊的辨識韌性，較合理的技術方向為何？

- `A` 只增加輸出字數上限
- `B` 只把訓練資料做欄位重新命名
- `C` 只在簡報中加入風險聲明而不調整模型
- `D` 導入對抗訓練（adversarial training）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：對抗訓練是直接把擾動樣本納入訓練，提升模型對惡意擾動的穩健性。

其餘選項為何錯：
- `A`：輸出字數與對抗韌性無直接關聯。
- `B`：重新命名欄位不會改變模型面對對抗擾動的能力。
- `C`：風險聲明屬治理措施，不是模型層補強。

補強知識點：
- 把技術補強與流程治理分開看。
- 只要題目強調『惡意擾動輸入』，優先想到 adversarial training 或 robust training。

回看來源：
- sources/official-corpus.md｜正式題出現對抗攻擊情境
- sources/scope-weight-map.md｜L21203 AI 風險管理

</details>

### 題 7｜`L21302`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

模型上線後，若想監控輸入特徵分布是否偏離訓練資料，哪一類指標最有代表性？

- `A` 只看 commit 次數是否增加
- `B` 資料分布漂移指標，例如 PSI（Population Stability Index）
- `C` 只看 CPU 使用率
- `D` 只看 API 回應字數長短

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：當標籤尚未回收時，先看輸入分布是否偏移，是線上監控常見做法。

其餘選項為何錯：
- `A`：commit 次數與線上資料分布無直接關係。
- `C`：CPU 使用率是系統資源指標，不是資料漂移指標。
- `D`：回應字數無法直接代表資料分布是否偏移。

補強知識點：
- 把 model drift 與 system metrics 區分開。
- PSI、KL divergence、feature distribution monitoring 是常見 drift 訊號。

回看來源：
- sources/official-corpus.md｜正式題出現 PSI 類 drift 概念
- sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署

</details>

### 題 8｜`L21302`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

若你懷疑業務資料分布已改變，導致模型精度下降，但標籤回收還很慢，最先可用哪類監控訊號判斷 drift？

- `A` 只看 commit 次數是否增加
- `B` 資料分布漂移指標，例如 PSI（Population Stability Index）
- `C` 只看 CPU 使用率
- `D` 只看 API 回應字數長短

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：當標籤尚未回收時，先看輸入分布是否偏移，是線上監控常見做法。

其餘選項為何錯：
- `A`：commit 次數與線上資料分布無直接關係。
- `C`：CPU 使用率是系統資源指標，不是資料漂移指標。
- `D`：回應字數無法直接代表資料分布是否偏移。

補強知識點：
- 把 model drift 與 system metrics 區分開。
- PSI、KL divergence、feature distribution monitoring 是常見 drift 訊號。

回看來源：
- sources/official-corpus.md｜正式題出現 PSI 類 drift 概念
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

### 題 11｜`L21203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若企業擔心模型受到惡意格式輸入或極端異常值衝擊，上線前最實務的第一層保護通常是什麼？

- `A` 加強輸入驗證與資料前處理檢查
- `B` 把所有異常輸入都直接當成正常樣本餵進模型
- `C` 只提高 GPU 數量
- `D` 只增加輸出長度上限

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：入口檢查能在模型看到資料前先過濾明顯錯誤或惡意輸入，是低成本有效的第一層防線。

其餘選項為何錯：
- `B`：把異常資料當正常資料只會放大風險。
- `C`：GPU 數量與輸入安全性無直接關聯。
- `D`：輸出長度不會改善入口資料品質。

補強知識點：
- 風險管理要分成入口、模型、流程三層看。
- 看到『格式不符、極端值』先想 input validation。

回看來源：
- sources/official-corpus.md｜正式題出現對抗攻擊與資料前處理
- sources/scope-weight-map.md｜L21203 AI 風險管理

</details>

### 題 12｜`L21203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

除了從模型本身補強外，若要先在系統入口擋掉格式異常與極端輸入，最合理的做法為何？

- `A` 只提高 GPU 數量
- `B` 只增加輸出長度上限
- `C` 加強輸入驗證與資料前處理檢查
- `D` 把所有異常輸入都直接當成正常樣本餵進模型

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：入口檢查能在模型看到資料前先過濾明顯錯誤或惡意輸入，是低成本有效的第一層防線。

其餘選項為何錯：
- `A`：GPU 數量與輸入安全性無直接關聯。
- `B`：輸出長度不會改善入口資料品質。
- `D`：把異常資料當正常資料只會放大風險。

補強知識點：
- 風險管理要分成入口、模型、流程三層看。
- 看到『格式不符、極端值』先想 input validation。

回看來源：
- sources/official-corpus.md｜正式題出現對抗攻擊與資料前處理
- sources/scope-weight-map.md｜L21203 AI 風險管理

</details>

## 今日必補知識點

- 區分 rule-based automation 與 ML system 的邊界，回看 [sources](../sources/) 內對應文件。
- 看到『固定規則、無訓練資料』時，先排除 ML，回看 [sources](../sources/) 內對應文件。
- 資料增強不是越多越好，關鍵是語意一致與分布合理，回看 [sources](../sources/) 內對應文件。
- 先檢查 augmentation strategy，再調 learning rate 或模型大小，回看 [sources](../sources/) 內對應文件。
- 把技術補強與流程治理分開看，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s1d1_rule_based_boundary, s1d3_augmentation_semantics, s1d7_adversarial_training, s1d9_drift_monitoring, s1d10_word2vec
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
