# 科目 2 加練｜statsmodels + seaborn + 時間序列

- 科目：`2`
- 優先級：`A`
- 優先級摘要：`A=5 / B=2 / C=0`
- 來源層級：`official-derived`
- 焦點：`Adj. R²、confidence interval、lineplot、resample、rolling mean、TimeSeriesSplit、lag feature`
- 題數：`14` 題
- 建議加做時機：`建議在 Day 07、Day 12、Day 14、Day 18 後加做`
- 作答單：[開啟](../attempts/subject-2-statsmodels-seaborn-timeseries-drill-attempt.md)
- 批改報告：[開啟](../reports/subject-2-statsmodels-seaborn-timeseries-drill-report.md)
- 批改指令：`python .\score_attempt.py --drill subject-2-statsmodels-seaborn-timeseries-drill`
- 使用方式：先做題，再展開 `<details>` 看答案與排錯理由。

## 題源對照

- sources/official-corpus.md｜模型訓練與評估
- sources/scope-weight-map.md｜L22301 模型訓練與效能評估
- sources/official-corpus.md｜假設檢定與統計推論
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論

## 題目

### 題 1｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

閱讀下列 `statsmodels` 程式碼後，哪個敘述最正確？

```python
import pandas as pd
import statsmodels.api as sm

X = pd.DataFrame({
    "tv": [1, 2, 3, 4, 5, 6],
    "radio": [2, 1, 0, 1, 2, 3],
    "noise": [9, 2, 7, 1, 8, 3],
})
y = pd.Series([5, 7, 9, 11, 13, 15])

X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

print(model.rsquared)
print(model.rsquared_adj)
```

- `A` `Adjusted R-squared` 只用於分類模型，線性回歸不會用到。
- `B` `R-squared` 與 `Adjusted R-squared` 一定完全相同，所以保留兩個欄位沒有意義。
- `C` 只要 `R-squared` 高，就代表新增任何特徵都一定有實質幫助。
- `D` `Adjusted R-squared` 會把變數數量納入考量，因此比單純 `R-squared` 更適合比較含不同特徵數量的回歸模型。

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：這題常考你會不會把 `R-squared` 當成唯一指標。`Adjusted R-squared` 會對不必要特徵做懲罰，因此在多變數回歸中更有比較價值。

其餘選項為何錯：
- `A`：`Adjusted R-squared` 就是回歸模型常見評估指標，不是分類限定。
- `B`：兩者只有在少數情況接近，不會保證完全相同。
- `C`：`R-squared` 可能因為加入無效特徵而上升，但不代表模型真的更好。

補強知識點：
- 補強 `R-squared` 與 `Adjusted R-squared` 的差異。
- 補強回歸模型評估時不能只看單一指標。

回看來源：
- sources/official-corpus.md｜模型訓練與評估
- sources/scope-weight-map.md｜L22301 模型訓練與效能評估

</details>

### 題 2｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

如果這題在考 `R-squared` 與 `Adjusted R-squared` 的差異，哪個選項正確？

```python
import pandas as pd
import statsmodels.api as sm

X = pd.DataFrame({
    "tv": [1, 2, 3, 4, 5, 6],
    "radio": [2, 1, 0, 1, 2, 3],
    "noise": [9, 2, 7, 1, 8, 3],
})
y = pd.Series([5, 7, 9, 11, 13, 15])

X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

print(model.rsquared)
print(model.rsquared_adj)
```

- `A` `Adjusted R-squared` 只用於分類模型，線性回歸不會用到。
- `B` `R-squared` 與 `Adjusted R-squared` 一定完全相同，所以保留兩個欄位沒有意義。
- `C` 只要 `R-squared` 高，就代表新增任何特徵都一定有實質幫助。
- `D` `Adjusted R-squared` 會把變數數量納入考量，因此比單純 `R-squared` 更適合比較含不同特徵數量的回歸模型。

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：這題常考你會不會把 `R-squared` 當成唯一指標。`Adjusted R-squared` 會對不必要特徵做懲罰，因此在多變數回歸中更有比較價值。

其餘選項為何錯：
- `A`：`Adjusted R-squared` 就是回歸模型常見評估指標，不是分類限定。
- `B`：兩者只有在少數情況接近，不會保證完全相同。
- `C`：`R-squared` 可能因為加入無效特徵而上升，但不代表模型真的更好。

補強知識點：
- 補強 `R-squared` 與 `Adjusted R-squared` 的差異。
- 補強回歸模型評估時不能只看單一指標。

回看來源：
- sources/official-corpus.md｜模型訓練與評估
- sources/scope-weight-map.md｜L22301 模型訓練與效能評估

</details>

### 題 3｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

閱讀下列 `statsmodels` 輸出片段後，哪個敘述最正確？

```python
import pandas as pd
import statsmodels.api as sm

X = pd.DataFrame({
    "search_ads": [1, 2, 3, 4, 5, 6],
    "coupon": [0, 1, 0, 1, 0, 1],
})
y = pd.Series([10, 13, 15, 18, 19, 23])

X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

print(model.conf_int())
# search_ads  [0.80, 1.45]
# coupon      [-0.90, 1.10]
```

- `A` 信賴區間跨過 0 代表這個變數一定有強烈負向效果。
- `B` 回歸係數的信賴區間只能用來看平均數，不能用來判讀變數效果。
- `C` `search_ads` 的 95% 信賴區間若完全不含 0，可視為其係數在該信賴水準下較可能不是 0；`coupon` 若區間跨過 0，則不宜主張其效果顯著。
- `D` 只要信賴區間比較窄，就一定代表變數顯著，不需要看是否跨過 0。

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：這類題本質上仍是顯著性判讀，只是換成 `conf_int()` 的形式來考。重點不是背表，而是知道『是否包含 0』代表什麼。

其餘選項為何錯：
- `A`：跨過 0 代表方向不穩定或不足以拒絕係數為 0 的可能，不是證明負向效果。
- `B`：回歸係數的信賴區間本來就常用來判讀效果估計的不確定性。
- `D`：區間寬窄和是否顯著不是同一件事，關鍵仍是有沒有跨過 0。

補強知識點：
- 補強用信賴區間判讀係數顯著性。
- 補強『跨 0』與『不跨 0』的實務意義。

回看來源：
- sources/official-corpus.md｜假設檢定與統計推論
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論

</details>

### 題 4｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若這題考的是信賴區間是否跨過 0，哪個選項正確？

```python
import pandas as pd
import statsmodels.api as sm

X = pd.DataFrame({
    "search_ads": [1, 2, 3, 4, 5, 6],
    "coupon": [0, 1, 0, 1, 0, 1],
})
y = pd.Series([10, 13, 15, 18, 19, 23])

X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

print(model.conf_int())
# search_ads  [0.80, 1.45]
# coupon      [-0.90, 1.10]
```

- `A` 信賴區間跨過 0 代表這個變數一定有強烈負向效果。
- `B` 回歸係數的信賴區間只能用來看平均數，不能用來判讀變數效果。
- `C` `search_ads` 的 95% 信賴區間若完全不含 0，可視為其係數在該信賴水準下較可能不是 0；`coupon` 若區間跨過 0，則不宜主張其效果顯著。
- `D` 只要信賴區間比較窄，就一定代表變數顯著，不需要看是否跨過 0。

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：這類題本質上仍是顯著性判讀，只是換成 `conf_int()` 的形式來考。重點不是背表，而是知道『是否包含 0』代表什麼。

其餘選項為何錯：
- `A`：跨過 0 代表方向不穩定或不足以拒絕係數為 0 的可能，不是證明負向效果。
- `B`：回歸係數的信賴區間本來就常用來判讀效果估計的不確定性。
- `D`：區間寬窄和是否顯著不是同一件事，關鍵仍是有沒有跨過 0。

補強知識點：
- 補強用信賴區間判讀係數顯著性。
- 補強『跨 0』與『不跨 0』的實務意義。

回看來源：
- sources/official-corpus.md｜假設檢定與統計推論
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論

</details>

### 題 5｜`L22303`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

閱讀下列 `seaborn` 程式碼後，哪個敘述最正確？

```python
import pandas as pd
import seaborn as sns

df = pd.DataFrame({
    "date": pd.date_range("2026-01-01", periods=5, freq="D"),
    "traffic": [120, 135, 128, 150, 165],
})

sns.lineplot(data=df, x="date", y="traffic")
```

- `A` `lineplot` 的主要用途是顯示每個類別出現次數，和時間趨勢無關。
- `B` 只要 x 軸是日期，圖表一定會自動轉成季節性分解圖，不需要額外分析。
- `C` `lineplot` 適合呈現日期序列隨時間變動的趨勢，因為重點是連續時間上的升降與波動，而不是單純比較幾個不相關類別。
- `D` 只要資料筆數超過 10 筆，就一定要改用 `barplot`，`lineplot` 不適合時間資料。

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：這題的重點是圖表語意。時間序列資料最常見的第一步就是先看趨勢圖，`lineplot` 比 `barplot` 更能表達連續變化。

其餘選項為何錯：
- `A`：顯示類別筆數通常更接近 `countplot` 的用途，不是 `lineplot`。
- `B`：日期軸不會自動變成季節性分解，仍需要額外方法分析季節性。
- `D`：時間資料並沒有『超過 10 筆就不能用 lineplot』這種規則。

補強知識點：
- 補強 `lineplot` 與 `barplot` 在時間資料的選型差異。
- 補強趨勢觀察與類別比較是不同圖表語意。

回看來源：
- sources/official-corpus.md｜數據可視化工具
- sources/scope-weight-map.md｜L22303 數據可視化工具

</details>

### 題 6｜`L22303`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

如果題目在考時間趨勢圖表選型，哪個選項正確？

```python
import pandas as pd
import seaborn as sns

df = pd.DataFrame({
    "date": pd.date_range("2026-01-01", periods=5, freq="D"),
    "traffic": [120, 135, 128, 150, 165],
})

sns.lineplot(data=df, x="date", y="traffic")
```

- `A` 只要 x 軸是日期，圖表一定會自動轉成季節性分解圖，不需要額外分析。
- `B` `lineplot` 適合呈現日期序列隨時間變動的趨勢，因為重點是連續時間上的升降與波動，而不是單純比較幾個不相關類別。
- `C` 只要資料筆數超過 10 筆，就一定要改用 `barplot`，`lineplot` 不適合時間資料。
- `D` `lineplot` 的主要用途是顯示每個類別出現次數，和時間趨勢無關。

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：這題的重點是圖表語意。時間序列資料最常見的第一步就是先看趨勢圖，`lineplot` 比 `barplot` 更能表達連續變化。

其餘選項為何錯：
- `A`：日期軸不會自動變成季節性分解，仍需要額外方法分析季節性。
- `C`：時間資料並沒有『超過 10 筆就不能用 lineplot』這種規則。
- `D`：顯示類別筆數通常更接近 `countplot` 的用途，不是 `lineplot`。

補強知識點：
- 補強 `lineplot` 與 `barplot` 在時間資料的選型差異。
- 補強趨勢觀察與類別比較是不同圖表語意。

回看來源：
- sources/official-corpus.md｜數據可視化工具
- sources/scope-weight-map.md｜L22303 數據可視化工具

</details>

### 題 7｜`L22203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

閱讀下列程式碼後，哪個敘述最正確？

```python
import pandas as pd

df = pd.DataFrame({
    "date": pd.date_range("2026-01-28", periods=6, freq="D"),
    "sales": [10, 12, 11, 30, 28, 35],
}).set_index("date")

monthly = df.resample("M").sum()
print(monthly)
```

- `A` 只要寫 `resample('M')`，就會自動計算月平均，和後面接什麼方法無關。
- `B` `resample('M')` 可以直接套在任何字串索引上，不需要日期型態也能正確做月份聚合。
- `C` `resample('M').sum()` 會把日資料依月份重新聚合成每月總 sales；前提是索引已經是日期型態。
- `D` `resample('M')` 只會重新排序資料，不會做任何聚合。

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：時間序列題常用 `resample` 考頻率轉換。重點是知道它不是單獨完成所有事，而是先按時間頻率分組，再接 `sum()`、`mean()` 等聚合。

其餘選項為何錯：
- `A`：月總和、月平均要看後面接的聚合函式，不是固定月平均。
- `B`：若索引不是日期型態，`resample` 通常無法按時間頻率正確運作。
- `D`：`resample` 本身不是單純排序，它是依時間頻率重分組。

補強知識點：
- 補強 `resample` 與聚合函式的搭配關係。
- 補強時間索引與日期型態的基本前提。

回看來源：
- sources/official-corpus.md｜數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具

</details>

### 題 8｜`L22203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若這題在考 `resample('M')` 的意義，哪個選項正確？

```python
import pandas as pd

df = pd.DataFrame({
    "date": pd.date_range("2026-01-28", periods=6, freq="D"),
    "sales": [10, 12, 11, 30, 28, 35],
}).set_index("date")

monthly = df.resample("M").sum()
print(monthly)
```

- `A` `resample('M').sum()` 會把日資料依月份重新聚合成每月總 sales；前提是索引已經是日期型態。
- `B` `resample('M')` 只會重新排序資料，不會做任何聚合。
- `C` 只要寫 `resample('M')`，就會自動計算月平均，和後面接什麼方法無關。
- `D` `resample('M')` 可以直接套在任何字串索引上，不需要日期型態也能正確做月份聚合。

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：時間序列題常用 `resample` 考頻率轉換。重點是知道它不是單獨完成所有事，而是先按時間頻率分組，再接 `sum()`、`mean()` 等聚合。

其餘選項為何錯：
- `B`：`resample` 本身不是單純排序，它是依時間頻率重分組。
- `C`：月總和、月平均要看後面接的聚合函式，不是固定月平均。
- `D`：若索引不是日期型態，`resample` 通常無法按時間頻率正確運作。

補強知識點：
- 補強 `resample` 與聚合函式的搭配關係。
- 補強時間索引與日期型態的基本前提。

回看來源：
- sources/official-corpus.md｜數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具

</details>

### 題 9｜`L22302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

閱讀下列程式碼後，哪個敘述最正確？

```python
import pandas as pd

s = pd.Series([100, 160, 120, 180, 140, 200])
ma3 = s.rolling(window=3).mean()
print(ma3.tolist())
```

- `A` 移動平均只會保留原始尖峰，不會改變任何波動程度。
- `B` `window=3` 代表每 3 個欄位做平均，不是每 3 筆時間點。
- `C` `rolling(window=3).mean()` 會用最近 3 期資料計算移動平均，常用來平滑短期波動、協助觀察趨勢。
- `D` `rolling(window=3).mean()` 會直接預測未來第 3 期的值，因此屬於預測模型。

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：移動平均是時間序列前處理與視覺化高頻概念。這題要會分清楚『平滑觀察』和『正式預測模型』不是同一件事。

其餘選項為何錯：
- `A`：平滑的目的就是降低局部波動，尖峰影響通常會被稀釋。
- `B`：在這種一維序列場景中，`window=3` 指的是 3 期觀測值。
- `D`：rolling mean 主要是描述與平滑，不是直接做未來預測。

補強知識點：
- 補強 rolling mean 的用途。
- 補強平滑處理與預測模型的差異。

回看來源：
- sources/official-corpus.md｜常見的大數據分析方法
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

### 題 10｜`L22302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

如果這題在考 rolling mean 的用途，哪個選項正確？

```python
import pandas as pd

s = pd.Series([100, 160, 120, 180, 140, 200])
ma3 = s.rolling(window=3).mean()
print(ma3.tolist())
```

- `A` `rolling(window=3).mean()` 會用最近 3 期資料計算移動平均，常用來平滑短期波動、協助觀察趨勢。
- `B` `rolling(window=3).mean()` 會直接預測未來第 3 期的值，因此屬於預測模型。
- `C` 移動平均只會保留原始尖峰，不會改變任何波動程度。
- `D` `window=3` 代表每 3 個欄位做平均，不是每 3 筆時間點。

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：移動平均是時間序列前處理與視覺化高頻概念。這題要會分清楚『平滑觀察』和『正式預測模型』不是同一件事。

其餘選項為何錯：
- `B`：rolling mean 主要是描述與平滑，不是直接做未來預測。
- `C`：平滑的目的就是降低局部波動，尖峰影響通常會被稀釋。
- `D`：在這種一維序列場景中，`window=3` 指的是 3 期觀測值。

補強知識點：
- 補強 rolling mean 的用途。
- 補強平滑處理與預測模型的差異。

回看來源：
- sources/official-corpus.md｜常見的大數據分析方法
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

### 題 11｜`L22302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

閱讀下列程式碼後，哪個敘述最正確？

```python
from sklearn.model_selection import TimeSeriesSplit
import numpy as np

X = np.arange(12).reshape(-1, 1)
tscv = TimeSeriesSplit(n_splits=3)

for train_idx, test_idx in tscv.split(X):
    print(train_idx, test_idx)
```

- `A` `TimeSeriesSplit` 會保留時間順序，讓訓練集先於驗證集，這比隨機打散更適合時間序列資料。
- `B` `TimeSeriesSplit` 的目的和 `shuffle=True` 完全一樣，都是把資料順序打亂後平均分配。
- `C` 時間序列資料最推薦直接用一般 KFold 隨機切分，因為比較平均。
- `D` `TimeSeriesSplit` 只適用於分類資料，回歸型時間序列不能用。

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：時間序列最怕未來資訊滲入過去。這題的重點是知道驗證方式也要符合時間先後，不然評估分數可能過度樂觀。

其餘選項為何錯：
- `B`：`TimeSeriesSplit` 恰恰是不打亂順序，和 `shuffle=True` 方向相反。
- `C`：一般隨機 KFold 容易把未來資料混入訓練，對時間序列不理想。
- `D`：`TimeSeriesSplit` 跟任務是分類或回歸無直接限制，核心在資料順序。

補強知識點：
- 補強時間序列驗證方法與一般 KFold 的差異。
- 補強資料洩漏在時間序列情境下的風險。

回看來源：
- sources/official-corpus.md｜常見的大數據分析方法
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

### 題 12｜`L22302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若這題在考時間序列驗證方法，哪個選項正確？

```python
from sklearn.model_selection import TimeSeriesSplit
import numpy as np

X = np.arange(12).reshape(-1, 1)
tscv = TimeSeriesSplit(n_splits=3)

for train_idx, test_idx in tscv.split(X):
    print(train_idx, test_idx)
```

- `A` 時間序列資料最推薦直接用一般 KFold 隨機切分，因為比較平均。
- `B` `TimeSeriesSplit` 只適用於分類資料，回歸型時間序列不能用。
- `C` `TimeSeriesSplit` 會保留時間順序，讓訓練集先於驗證集，這比隨機打散更適合時間序列資料。
- `D` `TimeSeriesSplit` 的目的和 `shuffle=True` 完全一樣，都是把資料順序打亂後平均分配。

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：時間序列最怕未來資訊滲入過去。這題的重點是知道驗證方式也要符合時間先後，不然評估分數可能過度樂觀。

其餘選項為何錯：
- `A`：一般隨機 KFold 容易把未來資料混入訓練，對時間序列不理想。
- `B`：`TimeSeriesSplit` 跟任務是分類或回歸無直接限制，核心在資料順序。
- `D`：`TimeSeriesSplit` 恰恰是不打亂順序，和 `shuffle=True` 方向相反。

補強知識點：
- 補強時間序列驗證方法與一般 KFold 的差異。
- 補強資料洩漏在時間序列情境下的風險。

回看來源：
- sources/official-corpus.md｜常見的大數據分析方法
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

### 題 13｜`L22203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

閱讀下列程式碼後，哪個敘述最正確？

```python
import pandas as pd

df = pd.DataFrame({
    "sales": [100, 120, 130, 160]
})

df["lag1"] = df["sales"].shift(1)
print(df)
```

- `A` `shift(1)` 會把下一期數值對齊到當前列，所以第一列一定有值。
- `B` `lag1` 代表過去 1 個欄位名稱，不是時間序列特徵。
- `C` 只要建立 `lag1`，模型就一定能正確預測未來，不需要其他處理。
- `D` `shift(1)` 會把前一期的 `sales` 往下對齊到當前列，因此 `lag1` 表示上一期數值，而第一列通常會變成 `NaN`。

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：lag feature 是時間序列建模最常見的基礎題。核心在於你要知道它反映的是過去資訊，並且前幾列常會因為缺少歷史值而出現缺值。

其餘選項為何錯：
- `A`：`shift(1)` 對齊的是上一期，不是下一期，因此第一列通常沒有可對應的歷史值。
- `B`：lag feature 是把過去觀測值轉成特徵，不是欄位名稱操作而已。
- `C`：建立 lag 只是特徵工程的一部分，不會保證模型一定準確。

補強知識點：
- 補強 lag feature 的意義與缺值位置。
- 補強時間序列特徵工程的基本觀念。

回看來源：
- sources/official-corpus.md｜數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具

</details>

### 題 14｜`L22203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

如果這題在考 lag feature 的建立，哪個選項正確？

```python
import pandas as pd

df = pd.DataFrame({
    "sales": [100, 120, 130, 160]
})

df["lag1"] = df["sales"].shift(1)
print(df)
```

- `A` `shift(1)` 會把前一期的 `sales` 往下對齊到當前列，因此 `lag1` 表示上一期數值，而第一列通常會變成 `NaN`。
- `B` `shift(1)` 會把下一期數值對齊到當前列，所以第一列一定有值。
- `C` `lag1` 代表過去 1 個欄位名稱，不是時間序列特徵。
- `D` 只要建立 `lag1`，模型就一定能正確預測未來，不需要其他處理。

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：lag feature 是時間序列建模最常見的基礎題。核心在於你要知道它反映的是過去資訊，並且前幾列常會因為缺少歷史值而出現缺值。

其餘選項為何錯：
- `B`：`shift(1)` 對齊的是上一期，不是下一期，因此第一列通常沒有可對應的歷史值。
- `C`：lag feature 是把過去觀測值轉成特徵，不是欄位名稱操作而已。
- `D`：建立 lag 只是特徵工程的一部分，不會保證模型一定準確。

補強知識點：
- 補強 lag feature 的意義與缺值位置。
- 補強時間序列特徵工程的基本觀念。

回看來源：
- sources/official-corpus.md｜數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具

</details>

## 本組必補

- 補強 `R-squared` 與 `Adjusted R-squared` 的差異
- 補強回歸模型評估時不能只看單一指標
- 補強用信賴區間判讀係數顯著性
- 補強『跨 0』與『不跨 0』的實務意義
- 補強 `lineplot` 與 `barplot` 在時間資料的選型差異
- 補強趨勢觀察與類別比較是不同圖表語意

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
| 13 |  |  |  |
| 14 |  |  |  |
