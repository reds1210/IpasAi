# Day 03｜科目 2 反向題單

- 今日焦點：`t 檢定、ANOVA、卡方、比例檢定`
- 題量：`10` 題
- 建議方式：3–5 小時內完成，先做題、再補點。｜優先級 A｜先刷這份，對過線最有幫助。
- 來源對照：
  - [official-corpus.md](../sources/official-corpus.md)
  - [scope-weight-map.md](../sources/scope-weight-map.md)
  - [question-source-map.md](../sources/question-source-map.md)
  - [question-patterns.md](../sources/question-patterns.md)
  - [book-bridge.md](../sources/book-bridge.md)

## 今日題目

### 題 1｜`L22103`｜難度：`中`
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

### 題 2｜`L22103`｜難度：`中`
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

### 題 3｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若要同時比較三個以上群體的平均數是否存在差異，最適合的檢定是什麼？

- `A` ROC 曲線
- `B` IQR 異常值法
- `C` ANOVA（變異數分析）
- `D` 雙樣本 t 檢定

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：ANOVA 用於三組以上平均數差異檢定，避免多次兩兩比較造成問題。

其餘選項為何錯：
- `A`：ROC 是分類模型評估工具。
- `B`：IQR 用於描述分布與找離群值，不做平均數差異推論。
- `D`：t-test 主要是兩組平均數比較。

補強知識點：
- 題目出現三組以上平均數比較時，優先選 ANOVA。
- 平均數比較與模型評估不要混。

回看來源：
- sources/official-corpus.md｜樣題出現三組平均數差異
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論

</details>

### 題 4｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若題目改成比較一年級、二年級、三年級平均身高是否不同，哪個統計方法最合理？

- `A` ANOVA（變異數分析）
- `B` 雙樣本 t 檢定
- `C` ROC 曲線
- `D` IQR 異常值法

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：ANOVA 用於三組以上平均數差異檢定，避免多次兩兩比較造成問題。

其餘選項為何錯：
- `B`：t-test 主要是兩組平均數比較。
- `C`：ROC 是分類模型評估工具。
- `D`：IQR 用於描述分布與找離群值，不做平均數差異推論。

補強知識點：
- 題目出現三組以上平均數比較時，優先選 ANOVA。
- 平均數比較與模型評估不要混。

回看來源：
- sources/official-corpus.md｜樣題出現三組平均數差異
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論

</details>

### 題 5｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若要檢定兩個類別變數之間是否獨立，最常見的方法是哪一種？

- `A` 卡方檢定（Chi-square test）
- `B` 線性迴歸
- `C` 雙樣本 t 檢定
- `D` K-means 分群

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：卡方檢定適用於類別資料的列聯表與獨立性分析。

其餘選項為何錯：
- `B`：線性迴歸處理的是連續數值關係。
- `C`：t 檢定處理的是平均數差異。
- `D`：K-means 是分群，不做顯著性檢定。

補強知識點：
- 類別對類別的關係先想卡方。
- 列聯表、獨立性、比例分布常一起出現。

回看來源：
- sources/official-corpus.md｜L22103 假設檢定與統計推論
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論

</details>

### 題 6｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

研究者想知道『是否購買會員』與『地區類別』是否相關，最先該選哪個檢定？

- `A` 線性迴歸
- `B` 雙樣本 t 檢定
- `C` K-means 分群
- `D` 卡方檢定（Chi-square test）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：卡方檢定適用於類別資料的列聯表與獨立性分析。

其餘選項為何錯：
- `A`：線性迴歸處理的是連續數值關係。
- `B`：t 檢定處理的是平均數差異。
- `C`：K-means 是分群，不做顯著性檢定。

補強知識點：
- 類別對類別的關係先想卡方。
- 列聯表、獨立性、比例分布常一起出現。

回看來源：
- sources/official-corpus.md｜L22103 假設檢定與統計推論
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論

</details>

### 題 7｜`L22103`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

若要比較兩條生產線良率 95% 與 97% 的差異是否有統計意義，最合理的方法是什麼？

- `A` 雙樣本平均數 t 檢定
- `B` ANOVA
- `C` PCA
- `D` 雙比例 Z 檢定（two-proportion Z-test）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：當目標是比較兩個比例或成功率時，雙比例 Z 檢定最對題。

其餘選項為何錯：
- `A`：t 檢定比較的是平均數，不是比例。
- `B`：ANOVA 也不是比例檢定。
- `C`：PCA 屬於降維方法。

補強知識點：
- 先看目標是平均數還是比例。
- 良率、轉換率、點擊率差異常對應 two-proportion test。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現產線良率比較
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論

</details>

### 題 8｜`L22103`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

工程師各抽樣 100 件產品，比較新舊產線的良率差異是否顯著。這裡最接近哪種檢定？

- `A` 雙樣本平均數 t 檢定
- `B` ANOVA
- `C` PCA
- `D` 雙比例 Z 檢定（two-proportion Z-test）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：當目標是比較兩個比例或成功率時，雙比例 Z 檢定最對題。

其餘選項為何錯：
- `A`：t 檢定比較的是平均數，不是比例。
- `B`：ANOVA 也不是比例檢定。
- `C`：PCA 屬於降維方法。

補強知識點：
- 先看目標是平均數還是比例。
- 良率、轉換率、點擊率差異常對應 two-proportion test。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現產線良率比較
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論

</details>

### 題 9｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

假設檢定中的 p-value 最接近哪一種解讀？

- `A` p-value 與顯著水準無任何關係
- `B` 當 p-value 很小時，表示資料對虛無假設不利
- `C` p-value 就是虛無假設為真的機率
- `D` p-value 很小代表模型一定正確

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：p-value 是在虛無假設為真前提下，得到目前或更極端結果的機率，用來判斷是否拒絕虛無假設。

其餘選項為何錯：
- `A`：p-value 會拿來和顯著水準 alpha 比較。
- `C`：p-value 不是 H0 為真的機率。
- `D`：顯著不代表模型或因果敘事一定正確。

補強知識點：
- p-value 的定義與常見誤解要能區分。
- 拒絕 H0 不等於證明所有其他敘事都成立。

回看來源：
- sources/official-corpus.md｜L22103 假設檢定與統計推論
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論

</details>

### 題 10｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若在虛無假設成立前提下觀察到目前資料或更極端結果的機率很低，通常代表什麼？

- `A` 當 p-value 很小時，表示資料對虛無假設不利
- `B` p-value 就是虛無假設為真的機率
- `C` p-value 很小代表模型一定正確
- `D` p-value 與顯著水準無任何關係

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：p-value 是在虛無假設為真前提下，得到目前或更極端結果的機率，用來判斷是否拒絕虛無假設。

其餘選項為何錯：
- `B`：p-value 不是 H0 為真的機率。
- `C`：顯著不代表模型或因果敘事一定正確。
- `D`：p-value 會拿來和顯著水準 alpha 比較。

補強知識點：
- p-value 的定義與常見誤解要能區分。
- 拒絕 H0 不等於證明所有其他敘事都成立。

回看來源：
- sources/official-corpus.md｜L22103 假設檢定與統計推論
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論

</details>

## 今日必補知識點

- 先判斷要比『平均數』還是『比例 / 類別』，回看 [sources](../sources/) 內對應文件。
- 兩組平均數差異優先想 t-test，回看 [sources](../sources/) 內對應文件。
- 題目出現三組以上平均數比較時，優先選 ANOVA，回看 [sources](../sources/) 內對應文件。
- 平均數比較與模型評估不要混，回看 [sources](../sources/) 內對應文件。
- 類別對類別的關係先想卡方，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s2d3_ttest, s2d3_anova, s2d3_chisquare, s2d3_prop_test, s2d3_hypothesis_logic
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
