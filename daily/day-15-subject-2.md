# Day 15｜科目 2 反向題單

- 今日焦點：`Python/統計錯題變體`
- 題量：`12` 題
- 建議方式：3–5 小時內完成，先做題、再補點。｜優先級 A｜先刷這份，對過線最有幫助。
- 來源對照：
  - [official-corpus.md](../sources/official-corpus.md)
  - [scope-weight-map.md](../sources/scope-weight-map.md)
  - [question-source-map.md](../sources/question-source-map.md)
  - [question-patterns.md](../sources/question-patterns.md)
  - [book-bridge.md](../sources/book-bridge.md)

## 今日題目

### 題 1｜`L22101`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

使用 IQR 方法做異常值偵測時，哪一個區間外的值會被視為異常？

- `A` 只要超過平均數就算異常
- `B` 低於 `Q1 - 1.5×IQR` 或高於 `Q3 + 1.5×IQR`
- `C` 低於 `Q2 - 2×IQR` 或高於 `Q2 + 2×IQR`
- `D` 低於 `Q1 - 1×IQR` 或高於 `Q3 + 1×IQR`

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：IQR 法的標準 outlier 規則是以四分位數與 1.5 倍 IQR 建界。

其餘選項為何錯：
- `A`：超過平均數不代表異常。
- `C`：Q2 不是 IQR 法的常用邊界中心。
- `D`：1×IQR 不是標準箱型圖常見異常值門檻。

補強知識點：
- 箱型圖、IQR、四分位數的關係要熟。
- 異常值規則常考 1.5×IQR，而不是 2×IQR。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現 IQR
- sources/scope-weight-map.md｜L22101 敘述性統計與資料摘要技術

</details>

### 題 2｜`L22101`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若 Q1 與 Q3 已知，想用箱型圖慣用規則找 outlier，判斷門檻通常是哪一組？

- `A` 只要超過平均數就算異常
- `B` 低於 `Q1 - 1.5×IQR` 或高於 `Q3 + 1.5×IQR`
- `C` 低於 `Q2 - 2×IQR` 或高於 `Q2 + 2×IQR`
- `D` 低於 `Q1 - 1×IQR` 或高於 `Q3 + 1×IQR`

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：IQR 法的標準 outlier 規則是以四分位數與 1.5 倍 IQR 建界。

其餘選項為何錯：
- `A`：超過平均數不代表異常。
- `C`：Q2 不是 IQR 法的常用邊界中心。
- `D`：1×IQR 不是標準箱型圖常見異常值門檻。

補強知識點：
- 箱型圖、IQR、四分位數的關係要熟。
- 異常值規則常考 1.5×IQR，而不是 2×IQR。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現 IQR
- sources/scope-weight-map.md｜L22101 敘述性統計與資料摘要技術

</details>

### 題 3｜`L22103`｜難度：`中`
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

### 題 4｜`L22103`｜難度：`中`
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

### 題 5｜`L22302`｜難度：`中`
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

### 題 6｜`L22302`｜難度：`中`
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

### 題 7｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

在 `statsmodels` 做 OLS 時，若想顯式估計截距項，常需要先做哪個步驟？

- `A` 使用 `sm.add_constant(X)` 加入常數欄位
- `B` 把 X 全部轉成字串
- `C` 先做 one-hot 才會有截距
- `D` 把 y 乘上一個常數即可

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：statsmodels 不一定自動補截距，常見做法是先對 X 加常數欄。

其餘選項為何錯：
- `B`：轉字串與截距無關。
- `C`：one-hot 用於類別編碼，不是專門為截距設計。
- `D`：改 y 不會自動產生設計矩陣中的常數項。

補強知識點：
- `add_constant` 是 statsmodels 題的高頻 API。
- sklearn 與 statsmodels 對截距的預設行為不同。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現常數項
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 8｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

為了讓 OLS 報表中含有常數項，對設計矩陣 X 最常見的前處理是什麼？

- `A` 把 X 全部轉成字串
- `B` 先做 one-hot 才會有截距
- `C` 把 y 乘上一個常數即可
- `D` 使用 `sm.add_constant(X)` 加入常數欄位

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：statsmodels 不一定自動補截距，常見做法是先對 X 加常數欄。

其餘選項為何錯：
- `A`：轉字串與截距無關。
- `B`：one-hot 用於類別編碼，不是專門為截距設計。
- `C`：改 y 不會自動產生設計矩陣中的常數項。

補強知識點：
- `add_constant` 是 statsmodels 題的高頻 API。
- sklearn 與 statsmodels 對截距的預設行為不同。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現常數項
- sources/scope-weight-map.md｜L22301 統計學在大數據中的應用

</details>

### 題 9｜`L22301`｜難度：`中`
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

### 題 10｜`L22301`｜難度：`中`
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

### 題 11｜`L22202`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

在圖形資料庫中，若『按讚』行為本身還帶有時間戳與裝置類型等資訊，較合適的建模方式是什麼？

- `A` 把所有按讚都寫回使用者節點文字欄位
- `B` 完全不用圖模型，改成隨意 Excel 記錄
- `C` 把裝置類型改成人工備註而不建模關聯
- `D` 把按讚視為帶屬性的邊（edge/property）來連結節點

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：圖資料庫很適合用邊來表示互動關係，邊上再保留時間與裝置等屬性。

其餘選項為何錯：
- `A`：寫回單一節點會破壞關聯查詢能力。
- `B`：Excel 不是圖查詢與關聯推理的設計。
- `C`：不建模關係就失去圖資料庫價值。

補強知識點：
- 圖資料庫的核心是節點、邊與屬性。
- 互動事件若天然是關係，先考慮 edge property。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 graph database edge property
- sources/scope-weight-map.md｜L22202 數據儲存與管理

</details>

### 題 12｜`L22202`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

社群資料中，使用者與貼文之間的 like 互動還要保留時間與裝置欄位。若用圖資料庫，最合理的設計方向為何？

- `A` 把裝置類型改成人工備註而不建模關聯
- `B` 把按讚視為帶屬性的邊（edge/property）來連結節點
- `C` 把所有按讚都寫回使用者節點文字欄位
- `D` 完全不用圖模型，改成隨意 Excel 記錄

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：圖資料庫很適合用邊來表示互動關係，邊上再保留時間與裝置等屬性。

其餘選項為何錯：
- `A`：不建模關係就失去圖資料庫價值。
- `C`：寫回單一節點會破壞關聯查詢能力。
- `D`：Excel 不是圖查詢與關聯推理的設計。

補強知識點：
- 圖資料庫的核心是節點、邊與屬性。
- 互動事件若天然是關係，先考慮 edge property。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 graph database edge property
- sources/scope-weight-map.md｜L22202 數據儲存與管理

</details>

## 今日必補知識點

- 箱型圖、IQR、四分位數的關係要熟，回看 [sources](../sources/) 內對應文件。
- 異常值規則常考 1.5×IQR，而不是 2×IQR，回看 [sources](../sources/) 內對應文件。
- 類別對類別的關係先想卡方，回看 [sources](../sources/) 內對應文件。
- 列聯表、獨立性、比例分布常一起出現，回看 [sources](../sources/) 內對應文件。
- K-means 的關鍵字：centroid、最近中心、反覆更新，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s2d3_chisquare, s2d8_add_constant, s2d10_threshold_tuning, s2d13_graph_edge_property
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
