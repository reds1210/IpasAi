# Day 10｜科目 1 反向題單

- 今日焦點：`Seq2Seq、Word2Vec、資料增強`
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

若任務是把輸入序列轉成另一段輸出序列，例如翻譯或摘要，最合理的模型方向為何？

- `A` 只做關鍵字頻率統計
- `B` 只做圖像分類
- `C` 只做實體名稱標註（NER）
- `D` 序列到序列（Seq2Seq）模型

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：Seq2Seq 適合處理輸入序列到輸出序列的映射，例如翻譯與摘要。

其餘選項為何錯：
- `A`：關鍵字頻率統計不會生成新的序列。
- `B`：圖像分類處理的是整張圖的類別。
- `C`：NER 是序列標註，不等於生成另一段序列。

補強知識點：
- 分清 classification、sequence labeling、sequence generation。
- 看到『翻譯、摘要、改寫』時，優先想 Seq2Seq。

回看來源：
- sources/official-corpus.md｜正式題出現 Seq2Seq
- sources/scope-weight-map.md｜L21101 自然語言處理技術與應用

</details>

### 題 2｜`L21101`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若系統要把輸入文字轉成語意等價的另一段文字，例如自動翻譯或摘要，最合理的模型方向為何？

- `A` 只做實體名稱標註（NER）
- `B` 序列到序列（Seq2Seq）模型
- `C` 只做關鍵字頻率統計
- `D` 只做圖像分類

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：Seq2Seq 適合處理輸入序列到輸出序列的映射，例如翻譯與摘要。

其餘選項為何錯：
- `A`：NER 是序列標註，不等於生成另一段序列。
- `C`：關鍵字頻率統計不會生成新的序列。
- `D`：圖像分類處理的是整張圖的類別。

補強知識點：
- 分清 classification、sequence labeling、sequence generation。
- 看到『翻譯、摘要、改寫』時，優先想 Seq2Seq。

回看來源：
- sources/official-corpus.md｜正式題出現 Seq2Seq
- sources/scope-weight-map.md｜L21101 自然語言處理技術與應用

</details>

### 題 3｜`L21101`｜難度：`難`
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

### 題 4｜`L21101`｜難度：`難`
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

### 題 5｜`L21302`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

下列何者較符合機器學習模型在業界部署的主要趨勢？

- `A` 越來越多地採用 AutoML 與自動化流程
- `B` 全面放棄雲端平台
- `C` 全面改回手動超參數調整
- `D` 盡量改用更少資料與更少監控

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：業界趨勢是把訓練、部署與監控流程自動化，提高效率與可重複性。

其餘選項為何錯：
- `B`：雲端與平台化能力仍是主流基礎設施之一。
- `C`：手動調參仍存在，但不是主要趨勢方向。
- `D`：資料與監控不足通常會提高風險，不是成熟部署方向。

補強知識點：
- AutoML、MLOps、自動化 pipeline 常一起出現。
- 趨勢題通常考『流程自動化』而非『全面手動』。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現 AutoML 趨勢
- sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署

</details>

### 題 6｜`L21302`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若題目問近年企業在部署機器學習時最明顯的共通方向，下列哪個選項最合理？

- `A` 盡量改用更少資料與更少監控
- `B` 越來越多地採用 AutoML 與自動化流程
- `C` 全面放棄雲端平台
- `D` 全面改回手動超參數調整

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：業界趨勢是把訓練、部署與監控流程自動化，提高效率與可重複性。

其餘選項為何錯：
- `A`：資料與監控不足通常會提高風險，不是成熟部署方向。
- `C`：雲端與平台化能力仍是主流基礎設施之一。
- `D`：手動調參仍存在，但不是主要趨勢方向。

補強知識點：
- AutoML、MLOps、自動化 pipeline 常一起出現。
- 趨勢題通常考『流程自動化』而非『全面手動』。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現 AutoML 趨勢
- sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署

</details>

### 題 7｜`L21103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

在資料增強（data augmentation）策略中，哪個做法最能避免模型學到錯誤訊號？

- `A` 維持增強後資料與原任務語意一致
- `B` 只要數量夠大，語意是否一致不重要
- `C` 增強比例越高越安全
- `D` 完全不檢查標註與分布是否改變

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：增強的價值在於增加合理變化，不是破壞原任務定義與標註訊號。

其餘選項為何錯：
- `B`：大量低品質資料只會放大噪音。
- `C`：增強比例沒有固定越高越好的結論。
- `D`：不檢查標註與分布會直接導致模型偏差。

補強知識點：
- augmentation 的第一原則是 semantic consistency。
- 先看資料訊號是否仍對準原任務，再談數量與模型。

回看來源：
- sources/official-corpus.md｜正式題出現 augmentation 分布偏移
- sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用

</details>

### 題 8｜`L21103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若團隊希望利用 augmentation 增加資料量，但又不想讓模型學到與真實任務不一致的樣本，最該守住哪個原則？

- `A` 維持增強後資料與原任務語意一致
- `B` 只要數量夠大，語意是否一致不重要
- `C` 增強比例越高越安全
- `D` 完全不檢查標註與分布是否改變

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：增強的價值在於增加合理變化，不是破壞原任務定義與標註訊號。

其餘選項為何錯：
- `B`：大量低品質資料只會放大噪音。
- `C`：增強比例沒有固定越高越好的結論。
- `D`：不檢查標註與分布會直接導致模型偏差。

補強知識點：
- augmentation 的第一原則是 semantic consistency。
- 先看資料訊號是否仍對準原任務，再談數量與模型。

回看來源：
- sources/official-corpus.md｜正式題出現 augmentation 分布偏移
- sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用

</details>

## 今日必補知識點

- 分清 classification、sequence labeling、sequence generation，回看 [sources](../sources/) 內對應文件。
- 看到『翻譯、摘要、改寫』時，優先想 Seq2Seq，回看 [sources](../sources/) 內對應文件。
- 把 TF-IDF 與 Word2Vec 分清：前者是稀疏權重，後者是嵌入向量，回看 [sources](../sources/) 內對應文件。
- 低頻詞、上下文語意、Skip-gram 這三個關鍵字要連在一起，回看 [sources](../sources/) 內對應文件。
- AutoML、MLOps、自動化 pipeline 常一起出現，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s1d10_seq2seq, s1d10_word2vec, s1d10_automl_trend, s1d10_augmentation_control
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
