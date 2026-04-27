# Day 11｜科目 2 反向題單

- 今日焦點：`第一次統計與程式回鍋`
- 題量：`10` 題
- 建議方式：3–5 小時內完成，先做題、再補點。｜優先級 A｜先刷這份，對過線最有幫助。
- 來源對照：
  - [official-corpus.md](../sources/official-corpus.md)
  - [scope-weight-map.md](../sources/scope-weight-map.md)
  - [question-source-map.md](../sources/question-source-map.md)
  - [question-patterns.md](../sources/question-patterns.md)
  - [book-bridge.md](../sources/book-bridge.md)

## 今日題目

### 題 1｜`L22201`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

讀入 CSV 後發現 `Year` 欄位是 `float64` 而不是整數，下列哪個原因最合理？

- `A` 只要欄位名稱叫 Year 就一定會轉成字串
- `B` 資料只要超過 100 筆就會自動升成浮點數
- `C` 欄位中含有 NaN 或帶小數格式的值
- `D` Pandas 會把所有數值欄位強制讀成 float64

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：含 NaN 的整數欄位在傳統 `numpy` 型態下常被升成浮點數，或原始資料本來就含 `2006.0` 類值。

其餘選項為何錯：
- `A`：欄位名稱不會決定資料型態。
- `B`：筆數多寡與是否升成浮點數無直接關係。
- `D`：Pandas 會依內容推斷型態，不會把所有數值欄位都強制轉成 float64。

補強知識點：
- 理解 dtype 由內容而非欄位名稱決定。
- 看到 `float64` 年份欄位時，先檢查 NaN 與原始值格式。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 Year float64 情境
- sources/scope-weight-map.md｜L22201 數據收集與清理

</details>

### 題 2｜`L22201`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

資料分析師發現年份欄位變成 `float64`，若原始欄位理應是年份，最先應懷疑哪種狀況？

- `A` 只要欄位名稱叫 Year 就一定會轉成字串
- `B` 資料只要超過 100 筆就會自動升成浮點數
- `C` 欄位中含有 NaN 或帶小數格式的值
- `D` Pandas 會把所有數值欄位強制讀成 float64

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：含 NaN 的整數欄位在傳統 `numpy` 型態下常被升成浮點數，或原始資料本來就含 `2006.0` 類值。

其餘選項為何錯：
- `A`：欄位名稱不會決定資料型態。
- `B`：筆數多寡與是否升成浮點數無直接關係。
- `D`：Pandas 會依內容推斷型態，不會把所有數值欄位都強制轉成 float64。

補強知識點：
- 理解 dtype 由內容而非欄位名稱決定。
- 看到 `float64` 年份欄位時，先檢查 NaN 與原始值格式。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 Year float64 情境
- sources/scope-weight-map.md｜L22201 數據收集與清理

</details>

### 題 3｜`L22201`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若年份欄位包含 NaN，但你仍想保留整數語意，最合適的轉型方式為何？

- `A` 先全部轉成 `str`
- `B` 把所有 NaN 都改成 1900 再轉 `int`
- `C` 使用 pandas 的 `Int64` nullable integer 型態
- `D` 直接 `astype(int)`

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：`Int64` 可在保留缺值的同時維持整數語意，是 pandas 常見解法。

其餘選項為何錯：
- `A`：轉字串會失去數值操作便利性。
- `B`：用 1900 等假值硬補會污染分析結果。
- `D`：`astype(int)` 遇到 NaN 會失敗。

補強知識點：
- 區分 Python / numpy 的整數型態與 pandas nullable integer。
- 看到『保留 NaN 又想是整數』就先想 `Int64`。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 `astype('Int64')`
- sources/scope-weight-map.md｜L22201 數據收集與清理

</details>

### 題 4｜`L22201`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

資料中 `Year` 有缺值，你又不想把缺值硬補成 0 或 1。若還要維持整數欄位，最合理的 pandas 型態為何？

- `A` 先全部轉成 `str`
- `B` 把所有 NaN 都改成 1900 再轉 `int`
- `C` 使用 pandas 的 `Int64` nullable integer 型態
- `D` 直接 `astype(int)`

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：`Int64` 可在保留缺值的同時維持整數語意，是 pandas 常見解法。

其餘選項為何錯：
- `A`：轉字串會失去數值操作便利性。
- `B`：用 1900 等假值硬補會污染分析結果。
- `D`：`astype(int)` 遇到 NaN 會失敗。

補強知識點：
- 區分 Python / numpy 的整數型態與 pandas nullable integer。
- 看到『保留 NaN 又想是整數』就先想 `Int64`。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 `astype('Int64')`
- sources/scope-weight-map.md｜L22201 數據收集與清理

</details>

### 題 5｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

要檢定兩個獨立群體的平均數是否有差異，最常見的統計方法是哪一種？

- `A` 卡方檢定（Chi-square test）
- `B` 變異數分析（ANOVA）
- `C` 主成分分析（PCA）
- `D` 雙樣本 t 檢定（two-sample t-test）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：兩組平均數比較且資料近似常態時，雙樣本 t 檢定是標準起點。

其餘選項為何錯：
- `A`：卡方檢定主要處理類別資料或次數分配。
- `B`：ANOVA 常用於三組以上平均數比較。
- `C`：PCA 是降維方法，不是顯著性檢定。

補強知識點：
- 先判斷要比『平均數』還是『比例 / 類別』。
- 兩組平均數差異優先想 t-test。

回看來源：
- sources/official-corpus.md｜樣題出現一年級與二年級平均數比較
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論

</details>

### 題 6｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若你想比較一年級與二年級平均身高是否不同，且資料近似常態，最先該選哪種檢定？

- `A` 卡方檢定（Chi-square test）
- `B` 變異數分析（ANOVA）
- `C` 主成分分析（PCA）
- `D` 雙樣本 t 檢定（two-sample t-test）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：兩組平均數比較且資料近似常態時，雙樣本 t 檢定是標準起點。

其餘選項為何錯：
- `A`：卡方檢定主要處理類別資料或次數分配。
- `B`：ANOVA 常用於三組以上平均數比較。
- `C`：PCA 是降維方法，不是顯著性檢定。

補強知識點：
- 先判斷要比『平均數』還是『比例 / 類別』。
- 兩組平均數差異優先想 t-test。

回看來源：
- sources/official-corpus.md｜樣題出現一年級與二年級平均數比較
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論

</details>

### 題 7｜`L22301`｜難度：`中`
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

### 題 8｜`L22301`｜難度：`中`
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

### 題 9｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

在 `LinearRegression().fit()` 中，哪個參數順序才是正確的？

- `A` `fit(y)` 後模型會自己找特徵
- `B` `fit(X, y)`
- `C` `fit(y, X)`
- `D` `fit(X)` 就足夠

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：`sklearn` 的監督式模型介面通常是 `fit(features, target)`。

其餘選項為何錯：
- `A`：只給 y 不會讓模型自動知道特徵。
- `C`：把 y 放前面會把目標與特徵顛倒。
- `D`：監督式迴歸需要特徵與目標。

補強知識點：
- 記住 sklearn 介面慣例：X 在前、y 在後。
- 程式題常考最基本的 API 使用順序。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 `fit(X, y)`
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 10｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若你要用 `sklearn` 建立線性迴歸模型，X 與 y 的輸入位置應如何安排？

- `A` `fit(X, y)`
- `B` `fit(y, X)`
- `C` `fit(X)` 就足夠
- `D` `fit(y)` 後模型會自己找特徵

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：`sklearn` 的監督式模型介面通常是 `fit(features, target)`。

其餘選項為何錯：
- `B`：把 y 放前面會把目標與特徵顛倒。
- `C`：監督式迴歸需要特徵與目標。
- `D`：只給 y 不會讓模型自動知道特徵。

補強知識點：
- 記住 sklearn 介面慣例：X 在前、y 在後。
- 程式題常考最基本的 API 使用順序。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 `fit(X, y)`
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

## 今日必補知識點

- 理解 dtype 由內容而非欄位名稱決定，回看 [sources](../sources/) 內對應文件。
- 看到 `float64` 年份欄位時，先檢查 NaN 與原始值格式，回看 [sources](../sources/) 內對應文件。
- 區分 Python / numpy 的整數型態與 pandas nullable integer，回看 [sources](../sources/) 內對應文件。
- 看到『保留 NaN 又想是整數』就先想 `Int64`，回看 [sources](../sources/) 內對應文件。
- 先判斷要比『平均數』還是『比例 / 類別』，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s2d3_ttest, s2d4_roc, s2d7_fit_xy
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
