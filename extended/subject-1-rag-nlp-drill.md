# 科目 1 加練｜RAG 與進階 NLP

- 科目：`1`
- 優先級：`A`
- 優先級摘要：`A=4 / B=0 / C=0`
- 來源層級：`official-derived`
- 焦點：`embedding 檢索、chunking、reranker、grounding`
- 題數：`8` 題
- 建議加做時機：`建議在 Day 03、Day 11、Day 17 後加做`
- 作答單：[開啟](../attempts/subject-1-rag-nlp-drill-attempt.md)
- 批改報告：[開啟](../reports/subject-1-rag-nlp-drill-report.md)
- 批改指令：`python .\score_attempt.py --drill subject-1-rag-nlp-drill`
- 使用方式：先做題，再展開 `<details>` 看答案與排錯理由。

## 題源對照

- sources/official-corpus.md｜生成式 AI 與檢索增強應用
- sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用
- sources/official-corpus.md｜生成式 AI 應用與資料處理
- sources/official-corpus.md｜生成式 AI 技術應用

## 題目

### 題 1｜`L21103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若搜尋系統希望找出語意相近但未必共用相同關鍵字的文件，最合理的檢索方式為何？

- `A` 只做完全相同字串比對
- `B` 按檔案大小排序文件
- `C` 隨機抽取前 10 份文件
- `D` 將查詢與文件轉成 embedding 後做向量相似度檢索

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：embedding 檢索能抓語意鄰近關係，不必完全依賴關鍵字重疊。

其餘選項為何錯：
- `A`：完全字串比對容易漏掉同義改寫。
- `B`：檔案大小與語意相關性無關。
- `C`：隨機抽樣沒有檢索能力。

補強知識點：
- RAG 的第一關通常是把語意相近文件找回來。
- keyword match 與 vector search 的差異要分清。

回看來源：
- sources/official-corpus.md｜生成式 AI 與檢索增強應用
- sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用

</details>

### 題 2｜`L21103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

使用者問題和知識庫文件常用不同字詞表達同一意思。若想改善召回，最值得優先加入哪種能力？

- `A` 只做完全相同字串比對
- `B` 按檔案大小排序文件
- `C` 隨機抽取前 10 份文件
- `D` 將查詢與文件轉成 embedding 後做向量相似度檢索

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：embedding 檢索能抓語意鄰近關係，不必完全依賴關鍵字重疊。

其餘選項為何錯：
- `A`：完全字串比對容易漏掉同義改寫。
- `B`：檔案大小與語意相關性無關。
- `C`：隨機抽樣沒有檢索能力。

補強知識點：
- RAG 的第一關通常是把語意相近文件找回來。
- keyword match 與 vector search 的差異要分清。

回看來源：
- sources/official-corpus.md｜生成式 AI 與檢索增強應用
- sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用

</details>

### 題 3｜`L21103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

在 RAG 建知識庫時，若 chunk 切得過大或過小都可能影響檢索品質。較合理的實務做法為何？

- `A` 整份文件永遠不切
- `B` 每 3 個字固定切一段且不保留上下文
- `C` 只依頁碼平均切分，不看語意結構
- `D` 依語意段落切 chunk，並保留適度 overlap

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：以語意段落切分並保留少量 overlap，通常能兼顧檢索精準度與上下文完整性。

其餘選項為何錯：
- `A`：整份文件不切會讓檢索粒度太粗。
- `B`：過細切分會破壞上下文連貫。
- `C`：只看頁碼不看內容結構，常切斷完整語意。

補強知識點：
- chunk size 與 overlap 都會影響 RAG 品質。
- 切分粒度要跟語意單位對齊。

回看來源：
- sources/official-corpus.md｜生成式 AI 應用與資料處理
- sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用

</details>

### 題 4｜`L21103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若你要切分長文件供檢索使用，哪種 chunking 策略通常比較穩健？

- `A` 整份文件永遠不切
- `B` 每 3 個字固定切一段且不保留上下文
- `C` 只依頁碼平均切分，不看語意結構
- `D` 依語意段落切 chunk，並保留適度 overlap

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：以語意段落切分並保留少量 overlap，通常能兼顧檢索精準度與上下文完整性。

其餘選項為何錯：
- `A`：整份文件不切會讓檢索粒度太粗。
- `B`：過細切分會破壞上下文連貫。
- `C`：只看頁碼不看內容結構，常切斷完整語意。

補強知識點：
- chunk size 與 overlap 都會影響 RAG 品質。
- 切分粒度要跟語意單位對齊。

回看來源：
- sources/official-corpus.md｜生成式 AI 應用與資料處理
- sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用

</details>

### 題 5｜`L21103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若第一階段檢索能找回大致相關文件，但排名常不夠準，下一步最合理的補強是什麼？

- `A` 只增加模型輸出字數
- `B` 先粗召回候選文件，再用 reranker 重新排序
- `C` 把所有候選文件都直接塞進 prompt
- `D` 只提高 temperature

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：兩階段檢索常先做高召回，再用 reranker 改善前排結果的相關性。

其餘選項為何錯：
- `A`：輸出字數不會改善檢索排序品質。
- `C`：全部塞進 prompt 會增加雜訊與成本。
- `D`：temperature 影響生成風格，不解決排序問題。

補強知識點：
- 粗召回與精排序是常見的兩段式檢索思路。
- retrieval quality 與 generation settings 要分開看。

回看來源：
- sources/official-corpus.md｜生成式 AI 技術應用
- sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用

</details>

### 題 6｜`L21103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

RAG 系統已能粗略召回候選文件，但最相關片段不一定排最前面。此時最常見的補強方向為何？

- `A` 先粗召回候選文件，再用 reranker 重新排序
- `B` 把所有候選文件都直接塞進 prompt
- `C` 只提高 temperature
- `D` 只增加模型輸出字數

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：兩階段檢索常先做高召回，再用 reranker 改善前排結果的相關性。

其餘選項為何錯：
- `B`：全部塞進 prompt 會增加雜訊與成本。
- `C`：temperature 影響生成風格，不解決排序問題。
- `D`：輸出字數不會改善檢索排序品質。

補強知識點：
- 粗召回與精排序是常見的兩段式檢索思路。
- retrieval quality 與 generation settings 要分開看。

回看來源：
- sources/official-corpus.md｜生成式 AI 技術應用
- sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用

</details>

### 題 7｜`L21103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若你想降低 RAG 回答看似合理但無法核對來源的風險，最有效的輸出要求是什麼？

- `A` 要求答案附上對應片段或引用來源
- `B` 只要求回答更流暢
- `C` 只提高模型溫度
- `D` 只限制回答字數更短

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：附帶來源或片段能讓使用者快速核對回答是否 grounded。

其餘選項為何錯：
- `B`：流暢不等於可驗證。
- `C`：提高溫度常增加隨機性。
- `D`：縮短字數不會自動增加可追溯性。

補強知識點：
- grounding 與 citation 是降低幻覺的重要手段。
- 能查證來源，才更適合企業場景。

回看來源：
- sources/official-corpus.md｜生成式 AI 應用與風險
- sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用

</details>

### 題 8｜`L21103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

內部知識助理常回答得很像真的，但使用者無法知道依據從何而來。若先補一個控管，最值得做什麼？

- `A` 只限制回答字數更短
- `B` 要求答案附上對應片段或引用來源
- `C` 只要求回答更流暢
- `D` 只提高模型溫度

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：附帶來源或片段能讓使用者快速核對回答是否 grounded。

其餘選項為何錯：
- `A`：縮短字數不會自動增加可追溯性。
- `C`：流暢不等於可驗證。
- `D`：提高溫度常增加隨機性。

補強知識點：
- grounding 與 citation 是降低幻覺的重要手段。
- 能查證來源，才更適合企業場景。

回看來源：
- sources/official-corpus.md｜生成式 AI 應用與風險
- sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用

</details>

## 本組必補

- RAG 的第一關通常是把語意相近文件找回來
- keyword match 與 vector search 的差異要分清
- chunk size 與 overlap 都會影響 RAG 品質
- 切分粒度要跟語意單位對齊
- 粗召回與精排序是常見的兩段式檢索思路
- retrieval quality 與 generation settings 要分開看

## 自評

| 題號 | 你的答案 | 能否自己解釋 | 備註 |
| --- | --- | --- | --- |
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |
| 6 |  |  |  |
| 7 |  |  |  |
| 8 |  |  |  |
