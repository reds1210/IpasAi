# 科目 2 加練｜公開題型轉寫混合題

- 科目：`2`
- 優先級：`B`
- 優先級摘要：`A=0 / B=4 / C=0`
- 來源層級：`public-pattern-derived`
- 焦點：`pandas 輸出判讀、Q-Q plot、箱型圖、門檻與指標選型`
- 題數：`8` 題
- 建議加做時機：`Day 06、Day 12、Day 17 後加做`
- 作答單：[開啟](../attempts/subject-2-public-patterns-mixed-drill-attempt.md)
- 批改報告：[開啟](../reports/subject-2-public-patterns-mixed-drill-report.md)
- 批改指令：`python .\score_attempt.py --drill subject-2-public-patterns-mixed-drill`
- 使用方式：先做題，再展開 `<details>` 看答案與排錯理由。

## 題源對照

- sources/question-source-map.md｜AITerms、S 測驗、CCChen 題型整理
- sources/question-patterns.md｜公開題型轉寫規則

## 題目

### 題 1｜`L22203`｜難度：`中`
優先級：`B`｜來源層級：`public-pattern-derived`

觀察下列程式後，哪個敘述最可能正確？

```python
summary = (
    df.groupby('dept', as_index=False)['salary']
      .mean()
      .sort_values('salary', ascending=False)
)
```

- `A` 先把缺值全部刪除，再展開欄位
- `B` 把每一列都轉成字串
- `C` 只計算每個部門的筆數，不會算平均
- `D` 先按部門聚合平均值，再依平均薪資由高到低排序

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`public-pattern-derived`

說明：程式中先做 groupby 與 mean，再接 sort_values，典型目的是算部門平均後排序。

其餘選項為何錯：
- `A`：題幹沒有 dropna 或欄位展開操作。
- `B`：astype(str) 才會做字串轉換，這裡沒有。
- `C`：若指定的是平均聚合，就不是只算筆數。

補強知識點：
- 熟悉 groupby、agg/mean、sort_values 的常見組合。
- 不要把聚合函式與計數函式混淆。

回看來源：
- sources/question-source-map.md｜AITerms Python 題攻略
- sources/question-patterns.md｜程式判讀題模板

</details>

### 題 2｜`L22203`｜難度：`中`
優先級：`B`｜來源層級：`public-pattern-derived`

若資料表中同一個部門有多筆資料，下列程式最終想達成什麼效果？

```python
summary = (
    df.groupby('dept', as_index=False)['salary']
      .mean()
      .sort_values('salary', ascending=False)
)
```

- `A` 只計算每個部門的筆數，不會算平均
- `B` 先按部門聚合平均值，再依平均薪資由高到低排序
- `C` 先把缺值全部刪除，再展開欄位
- `D` 把每一列都轉成字串

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`public-pattern-derived`

說明：程式中先做 groupby 與 mean，再接 sort_values，典型目的是算部門平均後排序。

其餘選項為何錯：
- `A`：若指定的是平均聚合，就不是只算筆數。
- `C`：題幹沒有 dropna 或欄位展開操作。
- `D`：astype(str) 才會做字串轉換，這裡沒有。

補強知識點：
- 熟悉 groupby、agg/mean、sort_values 的常見組合。
- 不要把聚合函式與計數函式混淆。

回看來源：
- sources/question-source-map.md｜AITerms Python 題攻略
- sources/question-patterns.md｜程式判讀題模板

</details>

### 題 3｜`L22203`｜難度：`中`
優先級：`B`｜來源層級：`public-pattern-derived`

若 `left merge` 後發現右表沒有對上的資料，結果表最常出現哪種現象？

- `A` Pandas 會自動改成 inner join
- `B` 右表對不上 key 的欄位會出現 NaN
- `C` 整列一定會被刪除
- `D` 所有欄位都會自動補成 0

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`public-pattern-derived`

說明：left join 會保留左表列，右表對不上的欄位以 NaN 表示。

其餘選項為何錯：
- `A`：join 類型不會自動改成 inner join。
- `C`：left join 不會因為右表缺值而直接刪掉左表整列。
- `D`：Pandas 不會自動把所有缺值補成 0。

補強知識點：
- 熟悉 left merge 的保留規則。
- 知道 NaN 常出現在合併後的未對應欄位。

回看來源：
- sources/question-source-map.md｜AITerms Python 題攻略
- sources/question-source-map.md｜S 測驗科目 2 模擬題

</details>

### 題 4｜`L22203`｜難度：`中`
優先級：`B`｜來源層級：`public-pattern-derived`

A 表保留所有列去接 B 表，某些 key 在 B 表不存在。這時合併結果最常如何呈現？

- `A` 右表對不上 key 的欄位會出現 NaN
- `B` 整列一定會被刪除
- `C` 所有欄位都會自動補成 0
- `D` Pandas 會自動改成 inner join

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`public-pattern-derived`

說明：left join 會保留左表列，右表對不上的欄位以 NaN 表示。

其餘選項為何錯：
- `B`：left join 不會因為右表缺值而直接刪掉左表整列。
- `C`：Pandas 不會自動把所有缺值補成 0。
- `D`：join 類型不會自動改成 inner join。

補強知識點：
- 熟悉 left merge 的保留規則。
- 知道 NaN 常出現在合併後的未對應欄位。

回看來源：
- sources/question-source-map.md｜AITerms Python 題攻略
- sources/question-source-map.md｜S 測驗科目 2 模擬題

</details>

### 題 5｜`L22303`｜難度：`中`
優先級：`B`｜來源層級：`public-pattern-derived`

若你想快速檢查各門市交易金額的中位數、四分位距與離群值，最貼近目的的圖表是什麼？

- `A` 圓餅圖（pie chart）
- `B` 雷達圖（radar chart）
- `C` 箱型圖（box plot）
- `D` 長條圖（bar chart）

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`public-pattern-derived`

說明：箱型圖能直接顯示中位數、四分位距與離群值，是這類分布檢查的標準選型。

其餘選項為何錯：
- `A`：圓餅圖用來看比例結構，不適合分布檢查。
- `B`：雷達圖不適合呈現 IQR 與離群值。
- `D`：長條圖適合比較彙總值，不擅長展示分布與離群值。

補強知識點：
- 把圖表選型綁回分析目的。
- IQR、median、outlier 通常先想到 box plot。

回看來源：
- sources/question-source-map.md｜S 測驗科目 2 模擬題
- sources/question-patterns.md｜視覺化題模板

</details>

### 題 6｜`L22303`｜難度：`中`
優先級：`B`｜來源層級：`public-pattern-derived`

資料分析會議上，主管要你一張圖同時看出分布位置、IQR 與離群值。你應先選哪種圖？

- `A` 箱型圖（box plot）
- `B` 長條圖（bar chart）
- `C` 圓餅圖（pie chart）
- `D` 雷達圖（radar chart）

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`public-pattern-derived`

說明：箱型圖能直接顯示中位數、四分位距與離群值，是這類分布檢查的標準選型。

其餘選項為何錯：
- `B`：長條圖適合比較彙總值，不擅長展示分布與離群值。
- `C`：圓餅圖用來看比例結構，不適合分布檢查。
- `D`：雷達圖不適合呈現 IQR 與離群值。

補強知識點：
- 把圖表選型綁回分析目的。
- IQR、median、outlier 通常先想到 box plot。

回看來源：
- sources/question-source-map.md｜S 測驗科目 2 模擬題
- sources/question-patterns.md｜視覺化題模板

</details>

### 題 7｜`L22401`｜難度：`中`
優先級：`B`｜來源層級：`public-pattern-derived`

詐欺偵測模型若目標是盡量少漏掉真詐欺案例，調整分類閾值時最應優先觀察哪類指標？

- `A` 只看 accuracy 即可
- `B` 只看訓練集損失最小即可
- `C` 只看 R² 是否提高
- `D` 優先提高召回率（recall），再權衡 precision

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`public-pattern-derived`

說明：詐欺偵測偏重少漏判，通常先看 recall；之後再評估 precision 與業務成本。

其餘選項為何錯：
- `A`：accuracy 在類別不平衡時常失真。
- `B`：訓練集損失不能直接代表部署風險。
- `C`：R² 是迴歸指標，不是分類閾值調整指標。

補強知識點：
- 辨識不平衡分類情境。
- 知道 recall、precision、threshold 三者的取捨。

回看來源：
- sources/question-source-map.md｜CCChen 科目 2 模擬題
- sources/question-patterns.md｜指標選型與情境題

</details>

### 題 8｜`L22401`｜難度：`中`
優先級：`B`｜來源層級：`public-pattern-derived`

在高風險風控情境下，團隊寧可多抓一些可疑交易，也不想漏掉真正詐欺。這時評估應優先看哪個方向？

- `A` 只看訓練集損失最小即可
- `B` 只看 R² 是否提高
- `C` 優先提高召回率（recall），再權衡 precision
- `D` 只看 accuracy 即可

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`public-pattern-derived`

說明：詐欺偵測偏重少漏判，通常先看 recall；之後再評估 precision 與業務成本。

其餘選項為何錯：
- `A`：訓練集損失不能直接代表部署風險。
- `B`：R² 是迴歸指標，不是分類閾值調整指標。
- `D`：accuracy 在類別不平衡時常失真。

補強知識點：
- 辨識不平衡分類情境。
- 知道 recall、precision、threshold 三者的取捨。

回看來源：
- sources/question-source-map.md｜CCChen 科目 2 模擬題
- sources/question-patterns.md｜指標選型與情境題

</details>

## 本組必補

- 熟悉 groupby、agg/mean、sort_values 的常見組合
- 不要把聚合函式與計數函式混淆
- 熟悉 left merge 的保留規則
- 知道 NaN 常出現在合併後的未對應欄位
- 把圖表選型綁回分析目的
- IQR、median、outlier 通常先想到 box plot

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
