# 科目 2 加練｜回歸與評估補強

- 科目：`2`
- 優先級：`A`
- 優先級摘要：`A=4 / B=0 / C=0`
- 來源層級：`official-derived`
- 焦點：`資料洩漏、VIF、RMSE/MAE、Adjusted R²`
- 題數：`8` 題
- 建議加做時機：`建議在 Day 07、Day 08、Day 17 後加做`
- 作答單：[開啟](../attempts/subject-2-regression-eval-drill-attempt.md)
- 批改報告：[開啟](../reports/subject-2-regression-eval-drill-report.md)
- 批改指令：`python .\score_attempt.py --drill subject-2-regression-eval-drill`
- 使用方式：先做題，再展開 `<details>` 看答案與排錯理由。

## 題源對照

- sources/official-corpus.md｜模型驗證與統計應用
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用
- sources/official-corpus.md｜回歸與統計分析應用
- sources/official-corpus.md｜模型評估方法

## 題目

### 題 1｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若你在做監督式學習時需要標準化特徵，為避免資料洩漏，最合理的流程是什麼？

- `A` 先看 test 再決定 train 的縮放方式
- `B` 完全不切資料，直接在全資料上報分數
- `C` 先切分 train/test，再只用 train fit scaler，最後套到 test
- `D` 先對全資料 fit scaler 才最公平

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：若先看過全資料分布再縮放，測試集資訊就提前滲入訓練流程。

其餘選項為何錯：
- `A`：先看 test 決定轉換更是直接洩漏。
- `B`：不切資料無法評估泛化。
- `D`：全資料先 fit 會造成 leakage。

補強知識點：
- preprocessing 也可能 leakage，不只模型本身。
- fit 在 train，transform 套到 test 是標準流程。

回看來源：
- sources/official-corpus.md｜模型驗證與統計應用
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 2｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

團隊先對整份資料 `fit_transform` 再切 train/test。這個做法的主要問題是什麼？

- `A` 先對全資料 fit scaler 才最公平
- `B` 先看 test 再決定 train 的縮放方式
- `C` 完全不切資料，直接在全資料上報分數
- `D` 先切分 train/test，再只用 train fit scaler，最後套到 test

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：若先看過全資料分布再縮放，測試集資訊就提前滲入訓練流程。

其餘選項為何錯：
- `A`：全資料先 fit 會造成 leakage。
- `B`：先看 test 決定轉換更是直接洩漏。
- `C`：不切資料無法評估泛化。

補強知識點：
- preprocessing 也可能 leakage，不只模型本身。
- fit 在 train，transform 套到 test 是標準流程。

回看來源：
- sources/official-corpus.md｜模型驗證與統計應用
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 3｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若線性迴歸中多個特徵高度相關，想量化多重共線性的程度，最常見的指標是哪一個？

- `A` Lift chart
- `B` VIF（Variance Inflation Factor）
- `C` AUC
- `D` Silhouette score

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：VIF 是多重共線性的常見診斷指標，值高代表該特徵可被其他特徵高度解釋。

其餘選項為何錯：
- `A`：Lift chart 多見於分類/行銷排序評估。
- `C`：AUC 是分類辨識能力指標。
- `D`：Silhouette score 用於分群評估。

補強知識點：
- 共線性題優先想到 VIF。
- 高 VIF 不一定要刪欄，但代表係數解讀要小心。

回看來源：
- sources/official-corpus.md｜回歸與統計分析應用
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 4｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

你懷疑特徵之間彼此太像，導致係數不穩。若想先看一個經典診斷量，最合理的是什麼？

- `A` AUC
- `B` Silhouette score
- `C` Lift chart
- `D` VIF（Variance Inflation Factor）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：VIF 是多重共線性的常見診斷指標，值高代表該特徵可被其他特徵高度解釋。

其餘選項為何錯：
- `A`：AUC 是分類辨識能力指標。
- `B`：Silhouette score 用於分群評估。
- `C`：Lift chart 多見於分類/行銷排序評估。

補強知識點：
- 共線性題優先想到 VIF。
- 高 VIF 不一定要刪欄，但代表係數解讀要小心。

回看來源：
- sources/official-corpus.md｜回歸與統計分析應用
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 5｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若你特別不希望模型出現少數非常大的預測誤差，評估時通常會偏向哪一種指標？

- `A` RMSE，因為它對大誤差懲罰更重
- `B` MAE，因為它永遠比 RMSE 更嚴格
- `C` Accuracy，因為任何任務都可用
- `D` 只看平均數，不需要誤差指標

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：RMSE 會平方誤差，因此對少數大錯誤更敏感。

其餘選項為何錯：
- `B`：MAE 較線性，對極端大誤差懲罰沒 RMSE 那麼重。
- `C`：Accuracy 不是回歸主指標。
- `D`：只看平均數無法評估預測誤差。

補強知識點：
- MAE 線性、RMSE 重罰大誤差，這是高頻比較題。
- 先看業務在意的是穩定還是避免大錯。

回看來源：
- sources/official-corpus.md｜模型評估方法
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 6｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

兩個模型平均表現差不多，但其中一個偶爾會犯很大的錯。若你想更重懲大誤差，應優先看哪種指標？

- `A` Accuracy，因為任何任務都可用
- `B` 只看平均數，不需要誤差指標
- `C` RMSE，因為它對大誤差懲罰更重
- `D` MAE，因為它永遠比 RMSE 更嚴格

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：RMSE 會平方誤差，因此對少數大錯誤更敏感。

其餘選項為何錯：
- `A`：Accuracy 不是回歸主指標。
- `B`：只看平均數無法評估預測誤差。
- `D`：MAE 較線性，對極端大誤差懲罰沒 RMSE 那麼重。

補強知識點：
- MAE 線性、RMSE 重罰大誤差，這是高頻比較題。
- 先看業務在意的是穩定還是避免大錯。

回看來源：
- sources/official-corpus.md｜模型評估方法
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 7｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若你想比較不同特徵數量的線性迴歸模型，並避免因亂加欄位而誤以為表現變好，較適合看的指標是哪個？

- `A` 單看訓練集 Accuracy
- `B` 只看資料列數
- `C` 只看欄位名稱長度
- `D` Adjusted R²

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：Adjusted R² 會考慮特徵數量，避免單純因增加欄位而讓指標看起來變好。

其餘選項為何錯：
- `A`：Accuracy 不是回歸主指標。
- `B`：資料列數不是模型擬合品質指標。
- `C`：欄位名稱長度與模型評估無關。

補強知識點：
- R² 與 Adjusted R² 的用途差異要分清。
- 比較不同欄位數模型時，Adjusted R² 更有參考價值。

回看來源：
- sources/official-corpus.md｜回歸與模型評估
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 8｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

一般 R² 加特徵後常不下降。若你要在比較模型時對多餘特徵做一些懲罰，應優先參考哪個量？

- `A` Adjusted R²
- `B` 單看訓練集 Accuracy
- `C` 只看資料列數
- `D` 只看欄位名稱長度

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：Adjusted R² 會考慮特徵數量，避免單純因增加欄位而讓指標看起來變好。

其餘選項為何錯：
- `B`：Accuracy 不是回歸主指標。
- `C`：資料列數不是模型擬合品質指標。
- `D`：欄位名稱長度與模型評估無關。

補強知識點：
- R² 與 Adjusted R² 的用途差異要分清。
- 比較不同欄位數模型時，Adjusted R² 更有參考價值。

回看來源：
- sources/official-corpus.md｜回歸與模型評估
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

## 本組必補

- preprocessing 也可能 leakage，不只模型本身
- fit 在 train，transform 套到 test 是標準流程
- 共線性題優先想到 VIF
- 高 VIF 不一定要刪欄，但代表係數解讀要小心
- MAE 線性、RMSE 重罰大誤差，這是高頻比較題
- 先看業務在意的是穩定還是避免大錯

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
