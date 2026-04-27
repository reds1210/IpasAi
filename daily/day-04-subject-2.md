# Day 04｜科目 2 反向題單

- 今日焦點：`ROC、AUC、PCA、分群基礎`
- 題量：`10` 題
- 建議方式：3–5 小時內完成，先做題、再補點。｜優先級 A｜先刷這份，對過線最有幫助。
- 來源對照：
  - [official-corpus.md](../sources/official-corpus.md)
  - [scope-weight-map.md](../sources/scope-weight-map.md)
  - [question-source-map.md](../sources/question-source-map.md)
  - [question-patterns.md](../sources/question-patterns.md)
  - [book-bridge.md](../sources/book-bridge.md)

## 今日題目

### 題 1｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

ROC 曲線主要描繪哪兩個量之間的關係？

- `A` 精確率（Precision）與召回率（Recall）
- `B` 平均數與標準差
- `C` 截距與斜率
- `D` 真陽性率（TPR）與假陽性率（FPR）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：ROC 的橫軸通常是假陽性率，縱軸是真陽性率，用來評估分類器在不同閾值下的表現。

其餘選項為何錯：
- `A`：Precision-Recall 是另一種曲線，不是 ROC 的定義。
- `B`：平均數與標準差屬描述統計。
- `C`：截距與斜率是迴歸概念。

補強知識點：
- ROC 與 PR curve 不要混。
- AUC-ROC 常配二元分類一起出現。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現 ROC
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 2｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若你要解釋 AUC-ROC 的基礎圖形，最核心的兩個座標軸是什麼？

- `A` 截距與斜率
- `B` 真陽性率（TPR）與假陽性率（FPR）
- `C` 精確率（Precision）與召回率（Recall）
- `D` 平均數與標準差

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：ROC 的橫軸通常是假陽性率，縱軸是真陽性率，用來評估分類器在不同閾值下的表現。

其餘選項為何錯：
- `A`：截距與斜率是迴歸概念。
- `C`：Precision-Recall 是另一種曲線，不是 ROC 的定義。
- `D`：平均數與標準差屬描述統計。

補強知識點：
- ROC 與 PR curve 不要混。
- AUC-ROC 常配二元分類一起出現。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現 ROC
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

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

### 題 5｜`L22302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若事前沒有定義群體類型，且資料中可能有雜訊點，較適合哪一種分群方法？

- `A` DBSCAN
- `B` 邏輯迴歸
- `C` 線性迴歸
- `D` 決策樹分類

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：DBSCAN 是密度式分群方法，可處理未知群數與雜訊點。

其餘選項為何錯：
- `B`：邏輯迴歸是監督式分類。
- `C`：線性迴歸處理連續值預測。
- `D`：決策樹分類需要標籤。

補強知識點：
- 沒有標籤又有噪聲時，先想到 DBSCAN。
- 把 clustering 與 supervised models 的輸入前提分開。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現 DBSCAN 情境
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

### 題 6｜`L22302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

音樂平台想根據使用者行為自動分出類型，還希望把離群用戶當作噪聲處理。下列哪種方法較合理？

- `A` 決策樹分類
- `B` DBSCAN
- `C` 邏輯迴歸
- `D` 線性迴歸

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：DBSCAN 是密度式分群方法，可處理未知群數與雜訊點。

其餘選項為何錯：
- `A`：決策樹分類需要標籤。
- `C`：邏輯迴歸是監督式分類。
- `D`：線性迴歸處理連續值預測。

補強知識點：
- 沒有標籤又有噪聲時，先想到 DBSCAN。
- 把 clustering 與 supervised models 的輸入前提分開。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現 DBSCAN 情境
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

### 題 7｜`L22302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若一段虛擬程式碼描述『隨機初始化中心點、計算距離、重新更新中心點直到收斂』，最可能是哪種演算法？

- `A` Apriori 關聯規則
- `B` K-means 分群
- `C` 高斯混合模型
- `D` 階層式分群

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：K-means 的核心流程就是分配到最近中心，再更新中心點並重複迭代。

其餘選項為何錯：
- `A`：Apriori 不屬於分群演算法。
- `C`：高斯混合模型多了機率分布假設。
- `D`：階層式分群不是以重算 centroid 為核心。

補強知識點：
- K-means 的關鍵字：centroid、最近中心、反覆更新。
- 看到『收斂前重算中心點』時要快速聯想到 K-means。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 K-means pseudocode
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

### 題 8｜`L22302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若題目描述重複執行『分配樣本到最近中心』與『更新群中心』的流程，最符合哪一種分群方法？

- `A` 階層式分群
- `B` Apriori 關聯規則
- `C` K-means 分群
- `D` 高斯混合模型

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：K-means 的核心流程就是分配到最近中心，再更新中心點並重複迭代。

其餘選項為何錯：
- `A`：階層式分群不是以重算 centroid 為核心。
- `B`：Apriori 不屬於分群演算法。
- `D`：高斯混合模型多了機率分布假設。

補強知識點：
- K-means 的關鍵字：centroid、最近中心、反覆更新。
- 看到『收斂前重算中心點』時要快速聯想到 K-means。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 K-means pseudocode
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

### 題 9｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

下列哪個敘述最符合 AUC-ROC 的一般解讀？

- `A` 模型只適用於回歸問題
- `B` AUC 一定只能是 1 或 0
- `C` 模型在不同閾值下區分正負類的整體能力較強
- `D` 模型的準確率一定等於 100%

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：AUC-ROC 衡量的是分類器跨閾值的整體區辨能力，不等於單一閾值下的準確率。

其餘選項為何錯：
- `A`：ROC 主要用在分類，不是回歸。
- `B`：AUC 介於 0 到 1 之間，通常不是只有 0 或 1。
- `D`：AUC 高不代表準確率一定滿分。

補強知識點：
- AUC 與 accuracy 的意義要分清。
- 評估指標題常考『跨閾值整體能力』這句話。

回看來源：
- sources/official-corpus.md｜ROC/AUC 類型題
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 10｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若模型的 AUC-ROC 越高，最常代表什麼？

- `A` 模型在不同閾值下區分正負類的整體能力較強
- `B` 模型的準確率一定等於 100%
- `C` 模型只適用於回歸問題
- `D` AUC 一定只能是 1 或 0

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：AUC-ROC 衡量的是分類器跨閾值的整體區辨能力，不等於單一閾值下的準確率。

其餘選項為何錯：
- `B`：AUC 高不代表準確率一定滿分。
- `C`：ROC 主要用在分類，不是回歸。
- `D`：AUC 介於 0 到 1 之間，通常不是只有 0 或 1。

補強知識點：
- AUC 與 accuracy 的意義要分清。
- 評估指標題常考『跨閾值整體能力』這句話。

回看來源：
- sources/official-corpus.md｜ROC/AUC 類型題
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

## 今日必補知識點

- ROC 與 PR curve 不要混，回看 [sources](../sources/) 內對應文件。
- AUC-ROC 常配二元分類一起出現，回看 [sources](../sources/) 內對應文件。
- 把 PCA 與 regression / classification 分清，回看 [sources](../sources/) 內對應文件。
- 看到『高維、降維、主成分』就先選 PCA，回看 [sources](../sources/) 內對應文件。
- 沒有標籤又有噪聲時，先想到 DBSCAN，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s2d4_roc, s2d4_auc_interpret
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
