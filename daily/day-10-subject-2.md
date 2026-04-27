# Day 10｜科目 2 反向題單

- 今日焦點：`不平衡資料、SMOTE、召回率與閾值`
- 題量：`10` 題
- 建議方式：3–5 小時內完成，先做題、再補點。｜優先級 A｜先刷這份，對過線最有幫助。
- 來源對照：
  - [official-corpus.md](../sources/official-corpus.md)
  - [scope-weight-map.md](../sources/scope-weight-map.md)
  - [question-source-map.md](../sources/question-source-map.md)
  - [question-patterns.md](../sources/question-patterns.md)
  - [book-bridge.md](../sources/book-bridge.md)

## 今日題目

### 題 1｜`L22401`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

在少數類樣本極少、又想提升少數類偵測能力時，下列哪一種策略最合理？

- `A` 使用 SMOTE 生成合成少數類樣本
- `B` 只隨機刪掉大量多數類而不評估代價
- `C` 完全不處理不平衡問題
- `D` 只提高決策閾值卻不檢查整體泛化

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：SMOTE 能在特徵空間中合成少數類樣本，常用於不平衡分類前處理。

其餘選項為何錯：
- `B`：欠採樣有時可行，但粗暴刪資料可能損失太多資訊。
- `C`：完全不處理通常會讓模型偏向多數類。
- `D`：只調閾值不能替代資料層補強。

補強知識點：
- SMOTE、class weight、threshold tuning 是不平衡分類三個高頻補救方向。
- 先看題目要的是資料層、模型層還是決策層補強。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 SMOTE
- sources/scope-weight-map.md｜L22401 大數據與機器學習

</details>

### 題 2｜`L22401`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

罕見疾病分類中，確診樣本不到 1%，又短期內拿不到更多標註資料。若想先提升少數類學習效果，哪個方法較對題？

- `A` 使用 SMOTE 生成合成少數類樣本
- `B` 只隨機刪掉大量多數類而不評估代價
- `C` 完全不處理不平衡問題
- `D` 只提高決策閾值卻不檢查整體泛化

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：SMOTE 能在特徵空間中合成少數類樣本，常用於不平衡分類前處理。

其餘選項為何錯：
- `B`：欠採樣有時可行，但粗暴刪資料可能損失太多資訊。
- `C`：完全不處理通常會讓模型偏向多數類。
- `D`：只調閾值不能替代資料層補強。

補強知識點：
- SMOTE、class weight、threshold tuning 是不平衡分類三個高頻補救方向。
- 先看題目要的是資料層、模型層還是決策層補強。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 SMOTE
- sources/scope-weight-map.md｜L22401 大數據與機器學習

</details>

### 題 3｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若任務重點是盡量抓到少數類，不希望漏判，較應優先關注哪一項指標？

- `A` 召回率（Recall）
- `B` 只看整體準確率（Accuracy）
- `C` 只看資料筆數
- `D` 只看訓練時間長短

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：當漏判成本高時，召回率比單純準確率更重要。

其餘選項為何錯：
- `B`：在高度不平衡資料中，accuracy 可能誤導。
- `C`：資料筆數不是模型性能指標。
- `D`：訓練時間不是任務目標指標。

補強知識點：
- 任務成本決定你優先的 metric。
- 偵測少數類場景常優先 recall 或 PR 指標。

回看來源：
- sources/official-corpus.md｜L22301 統計學在大數據中的應用
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 4｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

在疾病偵測或詐欺攔截場景中，若漏掉真正異常代價最高，調整模型時最優先看的通常是哪個方向？

- `A` 只看資料筆數
- `B` 只看訓練時間長短
- `C` 召回率（Recall）
- `D` 只看整體準確率（Accuracy）

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：當漏判成本高時，召回率比單純準確率更重要。

其餘選項為何錯：
- `A`：資料筆數不是模型性能指標。
- `B`：訓練時間不是任務目標指標。
- `D`：在高度不平衡資料中，accuracy 可能誤導。

補強知識點：
- 任務成本決定你優先的 metric。
- 偵測少數類場景常優先 recall 或 PR 指標。

回看來源：
- sources/official-corpus.md｜L22301 統計學在大數據中的應用
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 5｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若模型機率輸出已存在，但你想在不重訓模型的前提下提升召回率，哪個調整方向最直接？

- `A` 只改欄位名稱
- `B` 只提高 batch size
- `C` 只增加訓練輪數而不重新驗證
- `D` 調整分類決策閾值（decision threshold）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：閾值調整直接影響 precision / recall 取捨，是不重訓下最直接的方法之一。

其餘選項為何錯：
- `A`：欄位名稱與分類邏輯無關。
- `B`：batch size 主要影響訓練流程。
- `C`：增加訓練輪數不一定能朝你要的 error trade-off 前進。

補強知識點：
- threshold tuning 是決策層調整，不是資料層。
- 題目若說『不重訓』，常先想 threshold。

回看來源：
- sources/official-corpus.md｜不平衡資料與召回率題型
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 6｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

你想讓模型抓到更多異常案例，且允許多一些誤報。若先不重建資料或改演算法，較合理的做法為何？

- `A` 調整分類決策閾值（decision threshold）
- `B` 只改欄位名稱
- `C` 只提高 batch size
- `D` 只增加訓練輪數而不重新驗證

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：閾值調整直接影響 precision / recall 取捨，是不重訓下最直接的方法之一。

其餘選項為何錯：
- `B`：欄位名稱與分類邏輯無關。
- `C`：batch size 主要影響訓練流程。
- `D`：增加訓練輪數不一定能朝你要的 error trade-off 前進。

補強知識點：
- threshold tuning 是決策層調整，不是資料層。
- 題目若說『不重訓』，常先想 threshold。

回看來源：
- sources/official-corpus.md｜不平衡資料與召回率題型
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 7｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

下列哪個敘述最符合 precision 與 recall 的常見取捨？

- `A` 召回率可能提升，但誤報也可能增加
- `B` 準確率一定同步提高
- `C` 資料量會自動翻倍
- `D` 模型就不再需要驗證

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：降低閾值常讓模型抓到更多正類，同時也更可能把負類誤判成正類。

其餘選項為何錯：
- `B`：不同指標不會自動同向改善。
- `C`：調閾值不會改變資料量。
- `D`：任何閾值調整後都仍需要重新驗證。

補強知識點：
- precision/recall 是 trade-off，不是一起無條件上升。
- 閾值題常考『抓更多正類』的代價。

回看來源：
- sources/official-corpus.md｜L22301 統計學在大數據中的應用
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 8｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若你把分類閾值調低，通常更容易發生哪一類現象？

- `A` 資料量會自動翻倍
- `B` 模型就不再需要驗證
- `C` 召回率可能提升，但誤報也可能增加
- `D` 準確率一定同步提高

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：降低閾值常讓模型抓到更多正類，同時也更可能把負類誤判成正類。

其餘選項為何錯：
- `A`：調閾值不會改變資料量。
- `B`：任何閾值調整後都仍需要重新驗證。
- `D`：不同指標不會自動同向改善。

補強知識點：
- precision/recall 是 trade-off，不是一起無條件上升。
- 閾值題常考『抓更多正類』的代價。

回看來源：
- sources/official-corpus.md｜L22301 統計學在大數據中的應用
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 9｜`L22401`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若資料極不平衡，但你不想先改動樣本分布，還有哪些模型層常見作法？

- `A` 只把欄位排序改掉
- `B` 完全不理會類別比例
- `C` 調整 class weight 或成本敏感學習
- `D` 把所有樣本權重都設成一樣

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：class weight 會讓模型在訓練時對少數類錯誤給更高代價，是不平衡分類常見手段。

其餘選項為何錯：
- `A`：欄位排序與類別偏誤無關。
- `B`：不理會比例常讓模型只學會多數類。
- `D`：權重全相同無法處理不平衡。

補強知識點：
- SMOTE 是資料層，class weight 是模型層。
- 同一題要先判斷它在問哪一層補強。

回看來源：
- sources/official-corpus.md｜L22401 大數據與機器學習
- sources/scope-weight-map.md｜L22401 大數據與機器學習

</details>

### 題 10｜`L22401`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

團隊不希望先做過採樣，而是想在訓練時讓模型更重視少數類。較合理的方向為何？

- `A` 完全不理會類別比例
- `B` 調整 class weight 或成本敏感學習
- `C` 把所有樣本權重都設成一樣
- `D` 只把欄位排序改掉

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：class weight 會讓模型在訓練時對少數類錯誤給更高代價，是不平衡分類常見手段。

其餘選項為何錯：
- `A`：不理會比例常讓模型只學會多數類。
- `C`：權重全相同無法處理不平衡。
- `D`：欄位排序與類別偏誤無關。

補強知識點：
- SMOTE 是資料層，class weight 是模型層。
- 同一題要先判斷它在問哪一層補強。

回看來源：
- sources/official-corpus.md｜L22401 大數據與機器學習
- sources/scope-weight-map.md｜L22401 大數據與機器學習

</details>

## 今日必補知識點

- SMOTE、class weight、threshold tuning 是不平衡分類三個高頻補救方向，回看 [sources](../sources/) 內對應文件。
- 先看題目要的是資料層、模型層還是決策層補強，回看 [sources](../sources/) 內對應文件。
- 任務成本決定你優先的 metric，回看 [sources](../sources/) 內對應文件。
- 偵測少數類場景常優先 recall 或 PR 指標，回看 [sources](../sources/) 內對應文件。
- threshold tuning 是決策層調整，不是資料層，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s2d10_smote, s2d10_recall_threshold, s2d10_threshold_tuning, s2d10_precision_recall_tradeoff, s2d10_class_weight
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
