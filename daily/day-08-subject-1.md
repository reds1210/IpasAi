# Day 08｜科目 1 反向題單

- 今日焦點：`數據準備與模型選擇`
- 題量：`8` 題
- 建議方式：先以 60–75 分鐘完成第一輪，再展開解析。｜優先級 A｜先刷這份，對過線最有幫助。
- 來源對照：
  - [official-corpus.md](../sources/official-corpus.md)
  - [scope-weight-map.md](../sources/scope-weight-map.md)
  - [question-source-map.md](../sources/question-source-map.md)
  - [question-patterns.md](../sources/question-patterns.md)
  - [book-bridge.md](../sources/book-bridge.md)

## 今日題目

### 題 1｜`L21301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若目標是根據歷史銷售資料預測下一季銷售額，下列哪種模型類型最適合？

- `A` 分群模型（Clustering）
- `B` 分類模型（Classification）
- `C` 關聯規則分析（Association Rules）
- `D` 迴歸模型（Regression）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：預測連續數值目標時，首選應是迴歸模型。

其餘選項為何錯：
- `A`：分群用於找群組，不直接輸出連續預測值。
- `B`：分類輸出類別標籤，不是連續數值。
- `C`：關聯規則用來找共現模式，不是數值預測。

補強知識點：
- 先辨識目標變數型態：連續值選 regression，離散標籤選 classification。
- 看到『預測金額、銷量、工時』時，優先想回歸。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現回歸任務選型
- sources/scope-weight-map.md｜L21301 數據準備與模型選擇

</details>

### 題 2｜`L21301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

電商老闆想依過去產品銷量預估下季數量，以便調整庫存，最合理的第一個模型方向為何？

- `A` 迴歸模型（Regression）
- `B` 分群模型（Clustering）
- `C` 分類模型（Classification）
- `D` 關聯規則分析（Association Rules）

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：預測連續數值目標時，首選應是迴歸模型。

其餘選項為何錯：
- `B`：分群用於找群組，不直接輸出連續預測值。
- `C`：分類輸出類別標籤，不是連續數值。
- `D`：關聯規則用來找共現模式，不是數值預測。

補強知識點：
- 先辨識目標變數型態：連續值選 regression，離散標籤選 classification。
- 看到『預測金額、銷量、工時』時，優先想回歸。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現回歸任務選型
- sources/scope-weight-map.md｜L21301 數據準備與模型選擇

</details>

### 題 3｜`L21301`｜難度：`中`
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

### 題 4｜`L21301`｜難度：`中`
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

### 題 5｜`L21301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若事前沒有定義用戶類型，想先把相似用戶自動分群，最合理的模型方向為何？

- `A` 強化學習（Reinforcement Learning）
- `B` 規則式專家系統
- `C` 非監督式學習（Unsupervised Learning）
- `D` 監督式學習（Supervised Learning）

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：沒有標籤時，先用非監督式方法探索群組或資料結構最合理。

其餘選項為何錯：
- `A`：強化學習需要回饋訊號與互動環境。
- `B`：規則式系統無法自動從資料中學出群組結構。
- `D`：監督式學習需要既有標籤作為訓練目標。

補強知識點：
- 標籤有無，是分 supervised / unsupervised 的第一判斷點。
- 看到『事前沒有定義類型』，優先找 clustering 或密度方法。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現 DBSCAN 分群情境
- sources/scope-weight-map.md｜L21301 數據準備與模型選擇

</details>

### 題 6｜`L21301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

音樂平台只有使用者聽歌與搜尋行為，沒有既定標籤，卻想先找出使用者類型輪廓，應先選哪一種學習範式？

- `A` 規則式專家系統
- `B` 非監督式學習（Unsupervised Learning）
- `C` 監督式學習（Supervised Learning）
- `D` 強化學習（Reinforcement Learning）

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：沒有標籤時，先用非監督式方法探索群組或資料結構最合理。

其餘選項為何錯：
- `A`：規則式系統無法自動從資料中學出群組結構。
- `C`：監督式學習需要既有標籤作為訓練目標。
- `D`：強化學習需要回饋訊號與互動環境。

補強知識點：
- 標籤有無，是分 supervised / unsupervised 的第一判斷點。
- 看到『事前沒有定義類型』，優先找 clustering 或密度方法。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現 DBSCAN 分群情境
- sources/scope-weight-map.md｜L21301 數據準備與模型選擇

</details>

### 題 7｜`L21301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

對於低結構化的文本或圖像資料，下列哪種特徵工程方向通常最適用？

- `A` 特徵學習（Feature Learning）
- `B` 只做手工特徵挑選
- `C` 只做人工資料輸入格式化
- `D` 只依人工規則固定欄位值

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：非結構化資料常由模型自行學習表徵，比純手工欄位設計更有效。

其餘選項為何錯：
- `B`：手工特徵挑選對非結構化資料通常不夠彈性。
- `C`：格式化只是清理資料，不等於學到有用表徵。
- `D`：固定規則欄位難以覆蓋複雜語意或視覺特徵。

補強知識點：
- 結構化資料常做人工特徵；非結構化資料常做 representation learning。
- 看到文本/圖像原始輸入時，先想 embedding 或 deep feature learning。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現特徵學習
- sources/scope-weight-map.md｜L21301 數據準備與模型選擇

</details>

### 題 8｜`L21301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若資料多為原始圖像與長文本，不想手工設計大量欄位，較合理的方向為何？

- `A` 特徵學習（Feature Learning）
- `B` 只做手工特徵挑選
- `C` 只做人工資料輸入格式化
- `D` 只依人工規則固定欄位值

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：非結構化資料常由模型自行學習表徵，比純手工欄位設計更有效。

其餘選項為何錯：
- `B`：手工特徵挑選對非結構化資料通常不夠彈性。
- `C`：格式化只是清理資料，不等於學到有用表徵。
- `D`：固定規則欄位難以覆蓋複雜語意或視覺特徵。

補強知識點：
- 結構化資料常做人工特徵；非結構化資料常做 representation learning。
- 看到文本/圖像原始輸入時，先想 embedding 或 deep feature learning。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現特徵學習
- sources/scope-weight-map.md｜L21301 數據準備與模型選擇

</details>

## 今日必補知識點

- 先辨識目標變數型態：連續值選 regression，離散標籤選 classification，回看 [sources](../sources/) 內對應文件。
- 看到『預測金額、銷量、工時』時，優先想回歸，回看 [sources](../sources/) 內對應文件。
- 標準化、正規化與模型敏感度要建立連結，回看 [sources](../sources/) 內對應文件。
- 尺度問題通常先補 preprocessing，而不是先換演算法，回看 [sources](../sources/) 內對應文件。
- 標籤有無，是分 supervised / unsupervised 的第一判斷點，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s1d8_regression_fit, s1d8_scaling, s1d8_unsupervised_grouping, s1d8_feature_learning
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
