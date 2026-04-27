# 科目 2 加練｜程式碼題型

- 科目：`2`
- 優先級：`A`
- 優先級摘要：`A=6 / B=0 / C=0`
- 來源層級：`official-derived`
- 焦點：`pandas、seaborn、sklearn、statsmodels code block 判讀`
- 題數：`12` 題
- 建議加做時機：`建議在 Day 06、Day 08、Day 17 後加做`
- 作答單：[開啟](../attempts/subject-2-code-practice-drill-attempt.md)
- 批改報告：[開啟](../reports/subject-2-code-practice-drill-report.md)
- 批改指令：`python .\score_attempt.py --drill subject-2-code-practice-drill`
- 使用方式：先做題，再展開 `<details>` 看答案與排錯理由。

## 題源對照

- sources/official-corpus.md｜數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具
- sources/official-corpus.md｜模型訓練與評估
- sources/scope-weight-map.md｜L22301 模型訓練與效能評估

## 題目

### 題 1｜`L22203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

閱讀下列程式碼後，哪個敘述最正確？

```python
import pandas as pd

df = pd.DataFrame({
    "team": ["A", "A", "B", "B", "B"],
    "sales": [10, 15, 7, 8, 20],
    "region": ["N", "S", "N", "S", "N"],
})

out = (
    df.groupby("team", as_index=False)["sales"]
    .sum()
    .sort_values("sales", ascending=False)
)
print(out)
```

- `A` 程式先依 `team` 分組加總 `sales`，再依總銷售額由大到小排序，因此 `B` 會排在 `A` 前面，且總 sales 為 35。
- `B` `A` 的總 sales 為 35，因此輸出會先看到 `A`。
- `C` 這段程式是在計算每個 `region` 的平均 sales，而不是依 `team` 加總。
- `D` 因為用了 `as_index=False`，所以結果不會真的做分組，只會保留原始列順序。

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：`groupby(...)[col].sum()` 先做分組彙總，`sort_values(..., ascending=False)` 再把總量大的群組排在前面。這是 Subject 2 很常見的資料處理與輸出判讀題型。

其餘選項為何錯：
- `B`：`A` 的 sales 是 10 + 15 = 25，不是 35；35 是 `B` 的總和。
- `C`：程式明確是 `groupby("team")["sales"].sum()`，不是對 `region` 做平均。
- `D`：`as_index=False` 的作用是讓 `team` 保留為一般欄位，不是取消分組。

補強知識點：
- 補強 `groupby`、`sum`、`sort_values` 的基本輸出判讀。
- 補強 `as_index=False` 與彙總表結構的差異。

回看來源：
- sources/official-corpus.md｜數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具

</details>

### 題 2｜`L22203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若你要根據這段輸出快速判斷哪個 team 的總 sales 最高，哪個選項正確？

```python
import pandas as pd

df = pd.DataFrame({
    "team": ["A", "A", "B", "B", "B"],
    "sales": [10, 15, 7, 8, 20],
    "region": ["N", "S", "N", "S", "N"],
})

out = (
    df.groupby("team", as_index=False)["sales"]
    .sum()
    .sort_values("sales", ascending=False)
)
print(out)
```

- `A` 因為用了 `as_index=False`，所以結果不會真的做分組，只會保留原始列順序。
- `B` 程式先依 `team` 分組加總 `sales`，再依總銷售額由大到小排序，因此 `B` 會排在 `A` 前面，且總 sales 為 35。
- `C` `A` 的總 sales 為 35，因此輸出會先看到 `A`。
- `D` 這段程式是在計算每個 `region` 的平均 sales，而不是依 `team` 加總。

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：`groupby(...)[col].sum()` 先做分組彙總，`sort_values(..., ascending=False)` 再把總量大的群組排在前面。這是 Subject 2 很常見的資料處理與輸出判讀題型。

其餘選項為何錯：
- `A`：`as_index=False` 的作用是讓 `team` 保留為一般欄位，不是取消分組。
- `C`：`A` 的 sales 是 10 + 15 = 25，不是 35；35 是 `B` 的總和。
- `D`：程式明確是 `groupby("team")["sales"].sum()`，不是對 `region` 做平均。

補強知識點：
- 補強 `groupby`、`sum`、`sort_values` 的基本輸出判讀。
- 補強 `as_index=False` 與彙總表結構的差異。

回看來源：
- sources/official-corpus.md｜數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具

</details>

### 題 3｜`L22203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

閱讀下列程式碼後，哪個敘述最正確？

```python
import pandas as pd

orders = pd.DataFrame({
    "customer_id": [101, 102, 103],
    "amount": [200, 150, 300],
})
vip_map = pd.DataFrame({
    "customer_id": [101, 102],
    "vip": ["Y", "N"],
})

merged = orders.merge(vip_map, on="customer_id", how="left")
print(merged)
print(merged["vip"].isna().sum())
```

- `A` 這段程式等同於 `inner join`，所以只會留下兩筆有對到 `customer_id` 的資料。
- `B` 因為使用 `how="left"`，所以 `orders` 的列都會保留；`customer_id=103` 在 `vip_map` 找不到對應值，因此 `vip` 會出現 1 個 `NaN`。
- `C` 因為 `merge` 預設會丟掉對不到 key 的列，所以結果中不會看到 `customer_id=103`。
- `D` `vip` 欄位不會出現缺值，因為 pandas 會自動把找不到的值補成 `False`。

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：`left join` 是最常考的資料整併觀念之一。左表所有列都保留，右表只提供能對上的欄位值；對不到的部分會變成缺值，必須後續再判斷是否 `fillna` 或另做處理。

其餘選項為何錯：
- `A`：題目明確寫了 `how="left"`，所以不會退化成 `inner join`。
- `C`：會丟掉對不到 key 的列的是 `inner join`，不是 `left join`。
- `D`：pandas 不會自行把找不到的類別補成 `False`；找不到就是 `NaN`。

補強知識點：
- 補強 `left / inner / outer join` 的保留列差異。
- 補強 merge 後缺值來源與 `NaN` 判讀。

回看來源：
- sources/official-corpus.md｜數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具

</details>

### 題 4｜`L22203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

如果這題出成 merge 後缺值判讀題，哪個選項是正解？

```python
import pandas as pd

orders = pd.DataFrame({
    "customer_id": [101, 102, 103],
    "amount": [200, 150, 300],
})
vip_map = pd.DataFrame({
    "customer_id": [101, 102],
    "vip": ["Y", "N"],
})

merged = orders.merge(vip_map, on="customer_id", how="left")
print(merged)
print(merged["vip"].isna().sum())
```

- `A` `vip` 欄位不會出現缺值，因為 pandas 會自動把找不到的值補成 `False`。
- `B` 這段程式等同於 `inner join`，所以只會留下兩筆有對到 `customer_id` 的資料。
- `C` 因為使用 `how="left"`，所以 `orders` 的列都會保留；`customer_id=103` 在 `vip_map` 找不到對應值，因此 `vip` 會出現 1 個 `NaN`。
- `D` 因為 `merge` 預設會丟掉對不到 key 的列，所以結果中不會看到 `customer_id=103`。

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：`left join` 是最常考的資料整併觀念之一。左表所有列都保留，右表只提供能對上的欄位值；對不到的部分會變成缺值，必須後續再判斷是否 `fillna` 或另做處理。

其餘選項為何錯：
- `A`：pandas 不會自行把找不到的類別補成 `False`；找不到就是 `NaN`。
- `B`：題目明確寫了 `how="left"`，所以不會退化成 `inner join`。
- `D`：會丟掉對不到 key 的列的是 `inner join`，不是 `left join`。

補強知識點：
- 補強 `left / inner / outer join` 的保留列差異。
- 補強 merge 後缺值來源與 `NaN` 判讀。

回看來源：
- sources/official-corpus.md｜數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具

</details>

### 題 5｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

閱讀下列 `sklearn` 程式碼後，哪個敘述最正確？

```python
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4]])
y = np.array([7, 9, 11, 13])  # y = 5 + 2x

model = LinearRegression()
model.fit(X, y)

print(model.coef_)
print(model.intercept_)
```

- `A` `y = 5 + 2x`，因此模型訓練後的 `coef_` 會接近 2，`intercept_` 會接近 5。這代表 `x` 每增加 1，預測值平均增加約 2。
- `B` `coef_` 會接近 5，`intercept_` 會接近 2，因為截距與斜率在 sklearn 會顛倒儲存。
- `C` `coef_` 會是 0，因為資料筆數太少，線性回歸無法估計參數。
- `D` `intercept_` 一定是 0，因為 `LinearRegression()` 預設不估計截距。

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：`coef_` 對應斜率，`intercept_` 對應截距，這是 Subject 2 高頻程式題。考法通常不是要你手算，而是要你理解參數對模型的意義與方向。

其餘選項為何錯：
- `B`：sklearn 不會顛倒儲存斜率與截距；`coef_` 就是斜率，`intercept_` 就是截距。
- `C`：線性回歸不會因為只有 4 筆資料就無法估計；只要資料形狀正確就能擬合。
- `D`：`LinearRegression()` 預設 `fit_intercept=True`，會估計截距。

補強知識點：
- 補強 `coef_`、`intercept_` 與線性關係的對應。
- 補強 `fit(X, y)` 後常見輸出欄位的判讀。

回看來源：
- sources/official-corpus.md｜模型訓練與評估
- sources/scope-weight-map.md｜L22301 模型訓練與效能評估

</details>

### 題 6｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若考題要你判讀 `coef_` 與 `intercept_`，哪個選項正確？

```python
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4]])
y = np.array([7, 9, 11, 13])  # y = 5 + 2x

model = LinearRegression()
model.fit(X, y)

print(model.coef_)
print(model.intercept_)
```

- `A` `coef_` 會接近 5，`intercept_` 會接近 2，因為截距與斜率在 sklearn 會顛倒儲存。
- `B` `coef_` 會是 0，因為資料筆數太少，線性回歸無法估計參數。
- `C` `intercept_` 一定是 0，因為 `LinearRegression()` 預設不估計截距。
- `D` `y = 5 + 2x`，因此模型訓練後的 `coef_` 會接近 2，`intercept_` 會接近 5。這代表 `x` 每增加 1，預測值平均增加約 2。

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：`coef_` 對應斜率，`intercept_` 對應截距，這是 Subject 2 高頻程式題。考法通常不是要你手算，而是要你理解參數對模型的意義與方向。

其餘選項為何錯：
- `A`：sklearn 不會顛倒儲存斜率與截距；`coef_` 就是斜率，`intercept_` 就是截距。
- `B`：線性回歸不會因為只有 4 筆資料就無法估計；只要資料形狀正確就能擬合。
- `C`：`LinearRegression()` 預設 `fit_intercept=True`，會估計截距。

補強知識點：
- 補強 `coef_`、`intercept_` 與線性關係的對應。
- 補強 `fit(X, y)` 後常見輸出欄位的判讀。

回看來源：
- sources/official-corpus.md｜模型訓練與評估
- sources/scope-weight-map.md｜L22301 模型訓練與效能評估

</details>

### 題 7｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

閱讀下列 `statsmodels` 輸出片段後，哪個敘述最正確？

```python
import pandas as pd
import statsmodels.api as sm

X = pd.DataFrame({
    "ad_spend": [1, 2, 3, 4, 5, 6],
    "discount": [0, 0, 1, 1, 0, 1],
})
y = pd.Series([11, 13, 16, 18, 19, 22])

X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

print(model.pvalues)
# const       0.002
# ad_spend    0.010
# discount    0.410
```

- `A` `const` 的 `p-value` 顯著，就代表所有自變數都一定顯著。
- `B` 在顯著水準 0.05 下，`ad_spend` 的 `p-value = 0.010`，可視為對 `y` 有顯著關聯；`discount` 的 `p-value = 0.410`，則不能說有顯著效果。
- `C` `discount` 比 `ad_spend` 更顯著，因為它的係數比較小。
- `D` 只要 `p-value` 大於 0.05，就代表變數一定對 `y` 有正向效果。

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：`p-value` 的核心是顯著性判讀，不是看係數大小。這題常搭配 `OLS`、`add_constant` 與表格輸出一起考，重點是知道哪些變數能支持「存在統計上顯著關聯」的說法。

其餘選項為何錯：
- `A`：截距顯著不代表所有自變數都顯著，變數要各自判讀。
- `C`：顯著性不是看係數絕對值大小，而是看對應的 `p-value` 是否低於顯著水準。
- `D`：`p-value` 大於 0.05 通常表示沒有足夠證據拒絕虛無假設，不是證明正向效果。

補強知識點：
- 補強 OLS 輸出中 `p-value` 的判讀。
- 補強「顯著」與「效果大小」是不同概念。

回看來源：
- sources/official-corpus.md｜假設檢定與統計推論
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論

</details>

### 題 8｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若題目要你判讀 OLS 的 `p-value`，哪個選項是合理結論？

```python
import pandas as pd
import statsmodels.api as sm

X = pd.DataFrame({
    "ad_spend": [1, 2, 3, 4, 5, 6],
    "discount": [0, 0, 1, 1, 0, 1],
})
y = pd.Series([11, 13, 16, 18, 19, 22])

X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

print(model.pvalues)
# const       0.002
# ad_spend    0.010
# discount    0.410
```

- `A` 只要 `p-value` 大於 0.05，就代表變數一定對 `y` 有正向效果。
- `B` `const` 的 `p-value` 顯著，就代表所有自變數都一定顯著。
- `C` 在顯著水準 0.05 下，`ad_spend` 的 `p-value = 0.010`，可視為對 `y` 有顯著關聯；`discount` 的 `p-value = 0.410`，則不能說有顯著效果。
- `D` `discount` 比 `ad_spend` 更顯著，因為它的係數比較小。

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：`p-value` 的核心是顯著性判讀，不是看係數大小。這題常搭配 `OLS`、`add_constant` 與表格輸出一起考，重點是知道哪些變數能支持「存在統計上顯著關聯」的說法。

其餘選項為何錯：
- `A`：`p-value` 大於 0.05 通常表示沒有足夠證據拒絕虛無假設，不是證明正向效果。
- `B`：截距顯著不代表所有自變數都顯著，變數要各自判讀。
- `D`：顯著性不是看係數絕對值大小，而是看對應的 `p-value` 是否低於顯著水準。

補強知識點：
- 補強 OLS 輸出中 `p-value` 的判讀。
- 補強「顯著」與「效果大小」是不同概念。

回看來源：
- sources/official-corpus.md｜假設檢定與統計推論
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論

</details>

### 題 9｜`L22303`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

閱讀下列 `seaborn` 程式碼後，哪個敘述最正確？

```python
import pandas as pd
import seaborn as sns

df = pd.DataFrame({
    "channel": ["web", "web", "store", "store", "app"],
    "orders": [120, 80, 90, 70, 60],
})

sns.barplot(data=df, x="channel", y="orders", estimator=sum)
```

- `A` 這段程式會畫出各 `channel` 的 `orders` 總量比較圖；因為使用 `barplot(..., estimator=sum)`，重點是加總值，不是每個通路出現了幾筆資料。
- `B` 這會等同於 `countplot`，所以柱高只代表每個 `channel` 的筆數。
- `C` 因為 `estimator=sum`，圖上會直接顯示每筆資料的原始折線，不會做彙總。
- `D` 這段程式無法執行，因為 `barplot` 不接受 `y` 欄位。

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：`countplot` 與 `barplot` 的差別是 Subject 2 很常見的干擾點。只要看到 `estimator=sum` 或 `mean`，就要想到這是聚合後的數值比較，而不是單純筆數統計。

其餘選項為何錯：
- `B`：`countplot` 看的是筆數；這題明確用 `barplot` 加總 `orders`。
- `C`：`barplot` 會先按類別聚合 `y`，不是把每筆資料直接畫成折線。
- `D`：`barplot` 當然可以接受 `x` 與 `y` 欄位，這正是其常見用法。

補強知識點：
- 補強 `countplot`、`barplot`、`estimator` 的差異。
- 補強圖表選型時要先確認是在比較筆數還是聚合值。

回看來源：
- sources/official-corpus.md｜數據可視化工具
- sources/scope-weight-map.md｜L22303 數據可視化工具

</details>

### 題 10｜`L22303`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

如果這題考的是圖表函式選型與輸出意義，哪個選項正確？

```python
import pandas as pd
import seaborn as sns

df = pd.DataFrame({
    "channel": ["web", "web", "store", "store", "app"],
    "orders": [120, 80, 90, 70, 60],
})

sns.barplot(data=df, x="channel", y="orders", estimator=sum)
```

- `A` 這會等同於 `countplot`，所以柱高只代表每個 `channel` 的筆數。
- `B` 因為 `estimator=sum`，圖上會直接顯示每筆資料的原始折線，不會做彙總。
- `C` 這段程式無法執行，因為 `barplot` 不接受 `y` 欄位。
- `D` 這段程式會畫出各 `channel` 的 `orders` 總量比較圖；因為使用 `barplot(..., estimator=sum)`，重點是加總值，不是每個通路出現了幾筆資料。

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：`countplot` 與 `barplot` 的差別是 Subject 2 很常見的干擾點。只要看到 `estimator=sum` 或 `mean`，就要想到這是聚合後的數值比較，而不是單純筆數統計。

其餘選項為何錯：
- `A`：`countplot` 看的是筆數；這題明確用 `barplot` 加總 `orders`。
- `B`：`barplot` 會先按類別聚合 `y`，不是把每筆資料直接畫成折線。
- `C`：`barplot` 當然可以接受 `x` 與 `y` 欄位，這正是其常見用法。

補強知識點：
- 補強 `countplot`、`barplot`、`estimator` 的差異。
- 補強圖表選型時要先確認是在比較筆數還是聚合值。

回看來源：
- sources/official-corpus.md｜數據可視化工具
- sources/scope-weight-map.md｜L22303 數據可視化工具

</details>

### 題 11｜`L22401`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

閱讀下列程式碼後，若團隊最在意少漏抓正類，哪個敘述最正確？

```python
y_true = [1, 1, 1, 0, 0]
prob = [0.92, 0.81, 0.63, 0.44, 0.31]

pred_05 = [1 if p >= 0.5 else 0 for p in prob]
pred_03 = [1 if p >= 0.3 else 0 for p in prob]

print(pred_05)
print(pred_03)
```

- `A` 只要降低 threshold，precision 與 recall 一定會同時上升。
- `B` threshold 只影響顯示格式，不會改變任何預測類別。
- `C` 把門檻從 `0.5` 降到 `0.3`，通常會讓更多樣本被判成正類，因此 recall 常會上升或至少不下降，但 false positive 也可能增加。
- `D` 把門檻從 `0.5` 降到 `0.3`，recall 一定下降，因為模型會更保守。

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：不平衡資料題常考 threshold tuning。考點不是背公式，而是理解門檻下修會放寬正類判定條件，於是較容易抓到真正例，同時也更容易引入假陽性。

其餘選項為何錯：
- `A`：precision 與 recall 經常存在 trade-off，不會保證同時上升。
- `B`：threshold 直接影響最終 `pred` 類別，是分類決策的一部分。
- `D`：降低 threshold 不是更保守，而是更容易判成正類，所以 recall 通常不會下降。

補強知識點：
- 補強 threshold tuning 對 recall / precision 的影響。
- 補強不平衡資料時以商業目標決定評估指標。

回看來源：
- sources/official-corpus.md｜不平衡資料與模型調整
- sources/scope-weight-map.md｜L22401 模型優化與調校

</details>

### 題 12｜`L22401`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

如果這題考的是 threshold 調整效果判讀，哪個選項正確？

```python
y_true = [1, 1, 1, 0, 0]
prob = [0.92, 0.81, 0.63, 0.44, 0.31]

pred_05 = [1 if p >= 0.5 else 0 for p in prob]
pred_03 = [1 if p >= 0.3 else 0 for p in prob]

print(pred_05)
print(pred_03)
```

- `A` 把門檻從 `0.5` 降到 `0.3`，recall 一定下降，因為模型會更保守。
- `B` 只要降低 threshold，precision 與 recall 一定會同時上升。
- `C` threshold 只影響顯示格式，不會改變任何預測類別。
- `D` 把門檻從 `0.5` 降到 `0.3`，通常會讓更多樣本被判成正類，因此 recall 常會上升或至少不下降，但 false positive 也可能增加。

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：不平衡資料題常考 threshold tuning。考點不是背公式，而是理解門檻下修會放寬正類判定條件，於是較容易抓到真正例，同時也更容易引入假陽性。

其餘選項為何錯：
- `A`：降低 threshold 不是更保守，而是更容易判成正類，所以 recall 通常不會下降。
- `B`：precision 與 recall 經常存在 trade-off，不會保證同時上升。
- `C`：threshold 直接影響最終 `pred` 類別，是分類決策的一部分。

補強知識點：
- 補強 threshold tuning 對 recall / precision 的影響。
- 補強不平衡資料時以商業目標決定評估指標。

回看來源：
- sources/official-corpus.md｜不平衡資料與模型調整
- sources/scope-weight-map.md｜L22401 模型優化與調校

</details>

## 本組必補

- 補強 `groupby`、`sum`、`sort_values` 的基本輸出判讀
- 補強 `as_index=False` 與彙總表結構的差異
- 補強 `left / inner / outer join` 的保留列差異
- 補強 merge 後缺值來源與 `NaN` 判讀
- 補強 `coef_`、`intercept_` 與線性關係的對應
- 補強 `fit(X, y)` 後常見輸出欄位的判讀

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
| 9 |  |  |  |
| 10 |  |  |  |
| 11 |  |  |  |
| 12 |  |  |  |
