# Day 20｜科目 2 反向題單

- 今日焦點：`最終過線題單`
- 題量：`14` 題
- 建議方式：3–5 小時內完成，先做題、再補點。｜優先級 A｜先刷這份，對過線最有幫助。
- 來源對照：
  - [official-corpus.md](../sources/official-corpus.md)
  - [scope-weight-map.md](../sources/scope-weight-map.md)
  - [question-source-map.md](../sources/question-source-map.md)
  - [question-patterns.md](../sources/question-patterns.md)
  - [book-bridge.md](../sources/book-bridge.md)

## 今日題目

### 題 1｜`L22201`｜難度：`易`
優先級：`B`｜來源層級：`official-derived`

在 pandas 中，要統計每個欄位 NaN 個數，最標準的寫法是哪一類？

- `A` 使用 `isnan().sum()` 在 DataFrame 直接呼叫
- `B` 使用 `missing().count()`
- `C` 使用 `isna().sum()` 或 `isnull().sum()`
- `D` 使用 `isNaN().sum()`

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：在 pandas 裡，`isna()` 與 `isnull()` 是等價的常用缺值檢查方法。

其餘選項為何錯：
- `A`：`isnan()` 不是 DataFrame 物件的通用方法。
- `B`：`missing()` 不是 pandas 的標準 API。
- `D`：`isNaN()` 不是 pandas DataFrame 的標準方法名稱。

補強知識點：
- 記住 pandas 缺值檢查常用 API：`isna` / `isnull`。
- 不要把 numpy 或其他語言的命名直接套進 pandas。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 `isna()` / `isnull()`
- sources/scope-weight-map.md｜L22201 數據收集與清理

</details>

### 題 2｜`L22201`｜難度：`易`
優先級：`B`｜來源層級：`official-derived`

若你想快速檢查資料各欄位缺失值數量，哪個 pandas 方法組合最可靠？

- `A` 使用 `isna().sum()` 或 `isnull().sum()`
- `B` 使用 `isNaN().sum()`
- `C` 使用 `isnan().sum()` 在 DataFrame 直接呼叫
- `D` 使用 `missing().count()`

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：在 pandas 裡，`isna()` 與 `isnull()` 是等價的常用缺值檢查方法。

其餘選項為何錯：
- `B`：`isNaN()` 不是 pandas DataFrame 的標準方法名稱。
- `C`：`isnan()` 不是 DataFrame 物件的通用方法。
- `D`：`missing()` 不是 pandas 的標準 API。

補強知識點：
- 記住 pandas 缺值檢查常用 API：`isna` / `isnull`。
- 不要把 numpy 或其他語言的命名直接套進 pandas。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 `isna()` / `isnull()`
- sources/scope-weight-map.md｜L22201 數據收集與清理

</details>

### 題 3｜`L22302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

主成分分析（PCA）最主要的用途為何？

- `A` 直接做時間序列預測
- `B` 生成更多標註資料
- `C` 降維並保留主要變異資訊
- `D` 做監督式分類

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：PCA 透過線性組合形成主成分，常用來降低維度與去除共線性。

其餘選項為何錯：
- `A`：時間序列預測有其他專門方法。
- `B`：PCA 不會憑空生成標註資料。
- `D`：PCA 本身不是分類器。

補強知識點：
- 把 PCA 與 regression / classification 分清。
- 看到『高維、降維、主成分』就先選 PCA。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現 PCA
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

### 題 4｜`L22302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若高維資料太多欄位，你想在盡量保留變異資訊下壓縮維度，最合理的方法為何？

- `A` 降維並保留主要變異資訊
- `B` 做監督式分類
- `C` 直接做時間序列預測
- `D` 生成更多標註資料

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：PCA 透過線性組合形成主成分，常用來降低維度與去除共線性。

其餘選項為何錯：
- `B`：PCA 本身不是分類器。
- `C`：時間序列預測有其他專門方法。
- `D`：PCA 不會憑空生成標註資料。

補強知識點：
- 把 PCA 與 regression / classification 分清。
- 看到『高維、降維、主成分』就先選 PCA。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現 PCA
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

### 題 5｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若想降低單次切分造成的評估波動，最常見的模型驗證方法是哪一種？

- `A` 只隨機挑一筆做測試
- `B` K-fold 交叉驗證
- `C` 只看訓練集分數
- `D` 完全不切驗證集

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：K-fold 會反覆切分資料並平均結果，比單次 hold-out 更穩定。

其餘選項為何錯：
- `A`：單筆測試完全不穩定。
- `C`：只看訓練集會過度樂觀。
- `D`：沒有驗證集無法評估泛化。

補強知識點：
- 交叉驗證的重點是反覆切分與平均。
- 穩定評估通常優先想到 K-fold。

回看來源：
- sources/official-corpus.md｜L22301 統計學在大數據中的應用
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 6｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

當資料量不算太小，且你想更穩定評估模型泛化能力，哪種驗證方式通常最合適？

- `A` 只看訓練集分數
- `B` 完全不切驗證集
- `C` 只隨機挑一筆做測試
- `D` K-fold 交叉驗證

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：K-fold 會反覆切分資料並平均結果，比單次 hold-out 更穩定。

其餘選項為何錯：
- `A`：只看訓練集會過度樂觀。
- `B`：沒有驗證集無法評估泛化。
- `C`：單筆測試完全不穩定。

補強知識點：
- 交叉驗證的重點是反覆切分與平均。
- 穩定評估通常優先想到 K-fold。

回看來源：
- sources/official-corpus.md｜L22301 統計學在大數據中的應用
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 7｜`L22401`｜難度：`難`
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

### 題 8｜`L22401`｜難度：`難`
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

### 題 11｜`L22302`｜難度：`中`
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

### 題 12｜`L22302`｜難度：`中`
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

### 題 13｜`L22302`｜難度：`中`
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

### 題 14｜`L22302`｜難度：`中`
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

- 記住 pandas 缺值檢查常用 API：`isna` / `isnull`，回看 [sources](../sources/) 內對應文件。
- 不要把 numpy 或其他語言的命名直接套進 pandas，回看 [sources](../sources/) 內對應文件。
- 把 PCA 與 regression / classification 分清，回看 [sources](../sources/) 內對應文件。
- 看到『高維、降維、主成分』就先選 PCA，回看 [sources](../sources/) 內對應文件。
- 交叉驗證的重點是反覆切分與平均，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s2d9_kfold, s2d10_smote, s2d10_class_weight
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
