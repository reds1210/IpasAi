# 科目 2 加練｜pandas + sklearn 程式強化

- 科目：`2`
- 優先級：`A`
- 優先級摘要：`A=7 / B=1 / C=0`
- 來源層級：`official-derived`
- 焦點：`缺值補值、one-hot、stratify、Pipeline、cross validation、PCA、feature importance、group transform`
- 題數：`16` 題
- 建議加做時機：`建議在 Day 06、Day 08、Day 17、Day 18 後加做`
- 作答單：[開啟](../attempts/subject-2-pandas-sklearn-intensive-drill-attempt.md)
- 批改報告：[開啟](../reports/subject-2-pandas-sklearn-intensive-drill-report.md)
- 批改指令：`python .\score_attempt.py --drill subject-2-pandas-sklearn-intensive-drill`
- 使用方式：先做題，再展開 `<details>` 看答案與排錯理由。

## 題源對照

- sources/official-corpus.md｜數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具
- sources/official-corpus.md｜模型優化與調校
- sources/scope-weight-map.md｜L22401 模型優化與調校

## 題目

### 題 1｜`L22203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

閱讀下列程式碼後，哪個敘述最正確？

```python
import pandas as pd

df = pd.DataFrame({
    "income": [50000, None, 60000, 90000]
})

filled = df["income"].fillna(df["income"].median())
print(filled.tolist())
print(filled.loc[1])
```

- `A` 程式會用平均數補值，所以缺值會被補成 65000。
- `B` `fillna` 只能處理字串欄位，這段程式會報錯。
- `C` 補值後 `filled` 與原始 `df` 完全相同，缺值不會改變。
- `D` `income` 欄位中的缺值會被中位數補上；在這組資料中中位數是 60000，因此 `filled.loc[1, "income"]` 會是 60000。

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：`median()` 與 `mean()` 常被混淆。這題的核心是看懂 `fillna(df[col].median())` 的意義，以及為什麼偏態或離群值明顯時，中位數常比平均數穩定。

其餘選項為何錯：
- `A`：程式明確使用 `median()`，不是 `mean()`。
- `B`：數值欄位是 `fillna` 的典型使用場景，不會因為是數值就報錯。
- `C`：補值完成後該欄位的 `NaN` 會被替換，不會和原始缺值狀態完全相同。

補強知識點：
- 補強 `mean` 與 `median` 的補值差異。
- 補強 `fillna` 與缺值處理的高頻寫法。

回看來源：
- sources/official-corpus.md｜數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具

</details>

### 題 2｜`L22203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

如果這題考的是缺值補值策略與輸出判讀，哪個選項正確？

```python
import pandas as pd

df = pd.DataFrame({
    "income": [50000, None, 60000, 90000]
})

filled = df["income"].fillna(df["income"].median())
print(filled.tolist())
print(filled.loc[1])
```

- `A` `income` 欄位中的缺值會被中位數補上；在這組資料中中位數是 60000，因此 `filled.loc[1, "income"]` 會是 60000。
- `B` 程式會用平均數補值，所以缺值會被補成 65000。
- `C` `fillna` 只能處理字串欄位，這段程式會報錯。
- `D` 補值後 `filled` 與原始 `df` 完全相同，缺值不會改變。

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：`median()` 與 `mean()` 常被混淆。這題的核心是看懂 `fillna(df[col].median())` 的意義，以及為什麼偏態或離群值明顯時，中位數常比平均數穩定。

其餘選項為何錯：
- `B`：程式明確使用 `median()`，不是 `mean()`。
- `C`：數值欄位是 `fillna` 的典型使用場景，不會因為是數值就報錯。
- `D`：補值完成後該欄位的 `NaN` 會被替換，不會和原始缺值狀態完全相同。

補強知識點：
- 補強 `mean` 與 `median` 的補值差異。
- 補強 `fillna` 與缺值處理的高頻寫法。

回看來源：
- sources/official-corpus.md｜數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具

</details>

### 題 3｜`L22203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

閱讀下列程式碼後，哪個敘述最正確？

```python
import pandas as pd

df = pd.DataFrame({
    "city": ["Taipei", "Taichung", "Kaohsiung", "Taipei"]
})

out = pd.get_dummies(df, columns=["city"], drop_first=True)
print(out.columns.tolist())
```

- `A` 因為用了 `drop_first=True`，`city` 只會展開成 2 個虛擬變數欄位，而不是 3 個全部保留。
- `B` `get_dummies` 會把 `city` 直接改成單一整數欄位，效果等同 label encoding。
- `C` 只要做 one-hot encoding，就一定要保留所有類別欄位，不能 drop first。
- `D` `drop_first=True` 只會刪除資料表的第一列，不會影響 dummy 欄位數量。

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：`drop_first=True` 常用在避免完全共線性或簡化線性模型輸入。題目重點是辨識 one-hot encoding 與 label encoding 的差別，以及 `drop_first` 真正影響的是欄位，不是列。

其餘選項為何錯：
- `B`：`get_dummies` 產生的是多個 0/1 欄位，不是單一整數標籤欄。
- `C`：保留全部欄位不是唯一做法；`drop_first=True` 是常見選項。
- `D`：`drop_first=True` 處理的是類別展開後的欄位，不是刪資料列。

補強知識點：
- 補強 one-hot encoding 與 label encoding 的差異。
- 補強 `drop_first=True` 對虛擬變數欄位數量的影響。

回看來源：
- sources/official-corpus.md｜數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具

</details>

### 題 4｜`L22203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

如果這題在考 one-hot encoding 的輸出欄位，哪個選項正確？

```python
import pandas as pd

df = pd.DataFrame({
    "city": ["Taipei", "Taichung", "Kaohsiung", "Taipei"]
})

out = pd.get_dummies(df, columns=["city"], drop_first=True)
print(out.columns.tolist())
```

- `A` 只要做 one-hot encoding，就一定要保留所有類別欄位，不能 drop first。
- `B` `drop_first=True` 只會刪除資料表的第一列，不會影響 dummy 欄位數量。
- `C` 因為用了 `drop_first=True`，`city` 只會展開成 2 個虛擬變數欄位，而不是 3 個全部保留。
- `D` `get_dummies` 會把 `city` 直接改成單一整數欄位，效果等同 label encoding。

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：`drop_first=True` 常用在避免完全共線性或簡化線性模型輸入。題目重點是辨識 one-hot encoding 與 label encoding 的差別，以及 `drop_first` 真正影響的是欄位，不是列。

其餘選項為何錯：
- `A`：保留全部欄位不是唯一做法；`drop_first=True` 是常見選項。
- `B`：`drop_first=True` 處理的是類別展開後的欄位，不是刪資料列。
- `D`：`get_dummies` 產生的是多個 0/1 欄位，不是單一整數標籤欄。

補強知識點：
- 補強 one-hot encoding 與 label encoding 的差異。
- 補強 `drop_first=True` 對虛擬變數欄位數量的影響。

回看來源：
- sources/official-corpus.md｜數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具

</details>

### 題 5｜`L22401`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

閱讀下列程式碼後，哪個敘述最正確？

```python
from sklearn.model_selection import train_test_split

X = [[i] for i in range(20)]
y = [1, 1, 1, 1] + [0] * 16

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

print(sum(y_train), len(y_train))
print(sum(y_test), len(y_test))
```

- `A` `stratify=y` 只適用於回歸，分類資料不能用。
- `B` 使用 `stratify=y` 的目的是讓訓練集與測試集盡量維持與原始資料相近的類別比例，這在不平衡分類問題特別重要。
- `C` `stratify=y` 會自動完成 SMOTE，因此少數類會被複製到和多數類一樣多。
- `D` 只要用了 `random_state=42`，就不需要 `stratify`，兩者作用完全相同。

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：`stratify` 是切分時維持比例，不是重抽樣。這題常見干擾就是把 `stratify`、`random_state`、`SMOTE` 混在一起考。

其餘選項為何錯：
- `A`：`stratify=y` 典型用於分類資料，不是回歸限定功能。
- `C`：`stratify` 不會生成新樣本；SMOTE 才是重抽樣方法。
- `D`：`random_state` 只負責可重現，不能保證類別比例。

補強知識點：
- 補強 `stratify`、`random_state`、`SMOTE` 的功能差異。
- 補強不平衡分類切分時的基本原則。

回看來源：
- sources/official-corpus.md｜模型優化與調校
- sources/scope-weight-map.md｜L22401 模型優化與調校

</details>

### 題 6｜`L22401`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

如果這題在考不平衡資料切分策略，哪個選項正確？

```python
from sklearn.model_selection import train_test_split

X = [[i] for i in range(20)]
y = [1, 1, 1, 1] + [0] * 16

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

print(sum(y_train), len(y_train))
print(sum(y_test), len(y_test))
```

- `A` 只要用了 `random_state=42`，就不需要 `stratify`，兩者作用完全相同。
- `B` `stratify=y` 只適用於回歸，分類資料不能用。
- `C` 使用 `stratify=y` 的目的是讓訓練集與測試集盡量維持與原始資料相近的類別比例，這在不平衡分類問題特別重要。
- `D` `stratify=y` 會自動完成 SMOTE，因此少數類會被複製到和多數類一樣多。

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：`stratify` 是切分時維持比例，不是重抽樣。這題常見干擾就是把 `stratify`、`random_state`、`SMOTE` 混在一起考。

其餘選項為何錯：
- `A`：`random_state` 只負責可重現，不能保證類別比例。
- `B`：`stratify=y` 典型用於分類資料，不是回歸限定功能。
- `D`：`stratify` 不會生成新樣本；SMOTE 才是重抽樣方法。

補強知識點：
- 補強 `stratify`、`random_state`、`SMOTE` 的功能差異。
- 補強不平衡分類切分時的基本原則。

回看來源：
- sources/official-corpus.md｜模型優化與調校
- sources/scope-weight-map.md｜L22401 模型優化與調校

</details>

### 題 7｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

閱讀下列程式碼後，哪個敘述最正確？

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
import numpy as np

X = np.array([[1, 100], [2, 120], [3, 80], [4, 200], [5, 220], [6, 210]])
y = np.array([0, 0, 0, 1, 1, 1])

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

scores = cross_val_score(pipe, X, y, cv=3)
print(scores)
```

- `A` `Pipeline` 的主要作用是讓模型一定變成非線性，和資料洩漏無關。
- `B` 只要先在全資料做 `fit_transform`，再交叉驗證會更穩定，這是推薦做法。
- `C` `StandardScaler` 只改變欄位名稱，不會影響任何模型輸入分布。
- `D` 把縮放與模型一起放進 `Pipeline`，可以讓每個交叉驗證切分只用訓練折來估計縮放參數，降低資料洩漏風險。

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：`Pipeline` 是 Subject 2 很常見的工程化題。核心不是語法本身，而是理解 preprocessing 也必須被包含在驗證流程裡，否則容易把測試資訊偷帶進訓練。

其餘選項為何錯：
- `A`：`Pipeline` 不會自動讓模型變非線性；它的重點是串接前處理與模型流程。
- `B`：先在全資料上 `fit_transform` 再做交叉驗證，反而容易造成資料洩漏。
- `C`：`StandardScaler` 會改變數值尺度與分布中心，不只是改欄位名稱。

補強知識點：
- 補強 `Pipeline` 與資料洩漏的關係。
- 補強 `StandardScaler` 在模型流程中的正確位置。

回看來源：
- sources/official-corpus.md｜模型訓練與評估
- sources/scope-weight-map.md｜L22301 模型訓練與效能評估

</details>

### 題 8｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若考題在問為什麼要把 `StandardScaler` 放進 `Pipeline`，哪個選項正確？

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
import numpy as np

X = np.array([[1, 100], [2, 120], [3, 80], [4, 200], [5, 220], [6, 210]])
y = np.array([0, 0, 0, 1, 1, 1])

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

scores = cross_val_score(pipe, X, y, cv=3)
print(scores)
```

- `A` 只要先在全資料做 `fit_transform`，再交叉驗證會更穩定，這是推薦做法。
- `B` `StandardScaler` 只改變欄位名稱，不會影響任何模型輸入分布。
- `C` 把縮放與模型一起放進 `Pipeline`，可以讓每個交叉驗證切分只用訓練折來估計縮放參數，降低資料洩漏風險。
- `D` `Pipeline` 的主要作用是讓模型一定變成非線性，和資料洩漏無關。

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：`Pipeline` 是 Subject 2 很常見的工程化題。核心不是語法本身，而是理解 preprocessing 也必須被包含在驗證流程裡，否則容易把測試資訊偷帶進訓練。

其餘選項為何錯：
- `A`：先在全資料上 `fit_transform` 再做交叉驗證，反而容易造成資料洩漏。
- `B`：`StandardScaler` 會改變數值尺度與分布中心，不只是改欄位名稱。
- `D`：`Pipeline` 不會自動讓模型變非線性；它的重點是串接前處理與模型流程。

補強知識點：
- 補強 `Pipeline` 與資料洩漏的關係。
- 補強 `StandardScaler` 在模型流程中的正確位置。

回看來源：
- sources/official-corpus.md｜模型訓練與評估
- sources/scope-weight-map.md｜L22301 模型訓練與效能評估

</details>

### 題 9｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

閱讀下列程式碼後，哪個敘述最正確？

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([3, 5, 7, 9, 11, 13])

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3, scoring="neg_mean_absolute_error")
print(scores)
print(scores.mean())
```

- `A` 因為是 `mean_absolute_error`，分數一定是正值，所以越大越好。
- `B` `cross_val_score` 看到 `neg_` 會自動把結果取絕對值，因此不用管正負號。
- `C` 只要是回歸任務，`cross_val_score` 都只能用 accuracy 做比較。
- `D` `scoring="neg_mean_absolute_error"` 會回傳負值；比較模型時，數值越接近 0 通常代表 MAE 越小、表現越好。

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：`neg_*` 分數是 sklearn 的常見陷阱。這題不是要你背 API，而是要知道 regression loss 轉成 score 時常會帶負號，解讀時不能直接當成越大越差。

其餘選項為何錯：
- `A`：這個 scoring 名稱就明確表示會回傳負的 MAE。
- `B`：sklearn 不會自動幫你轉絕對值；你必須自己理解其意義。
- `C`：accuracy 不是回歸任務常用指標，MAE、MSE、R² 才是高頻。

補強知識點：
- 補強 `neg_mean_absolute_error` 的解讀。
- 補強回歸指標與分類指標的區分。

回看來源：
- sources/official-corpus.md｜模型訓練與評估
- sources/scope-weight-map.md｜L22301 模型訓練與效能評估

</details>

### 題 10｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

如果這題在考 `cross_val_score` 的 regression scoring，哪個選項正確？

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([3, 5, 7, 9, 11, 13])

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3, scoring="neg_mean_absolute_error")
print(scores)
print(scores.mean())
```

- `A` `scoring="neg_mean_absolute_error"` 會回傳負值；比較模型時，數值越接近 0 通常代表 MAE 越小、表現越好。
- `B` 因為是 `mean_absolute_error`，分數一定是正值，所以越大越好。
- `C` `cross_val_score` 看到 `neg_` 會自動把結果取絕對值，因此不用管正負號。
- `D` 只要是回歸任務，`cross_val_score` 都只能用 accuracy 做比較。

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：`neg_*` 分數是 sklearn 的常見陷阱。這題不是要你背 API，而是要知道 regression loss 轉成 score 時常會帶負號，解讀時不能直接當成越大越差。

其餘選項為何錯：
- `B`：這個 scoring 名稱就明確表示會回傳負的 MAE。
- `C`：sklearn 不會自動幫你轉絕對值；你必須自己理解其意義。
- `D`：accuracy 不是回歸任務常用指標，MAE、MSE、R² 才是高頻。

補強知識點：
- 補強 `neg_mean_absolute_error` 的解讀。
- 補強回歸指標與分類指標的區分。

回看來源：
- sources/official-corpus.md｜模型訓練與評估
- sources/scope-weight-map.md｜L22301 模型訓練與效能評估

</details>

### 題 11｜`L22203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

閱讀下列程式碼後，哪個敘述最正確？

```python
import pandas as pd

df = pd.DataFrame({
    "dept": ["A", "A", "B", "B"],
    "sales": [30, 70, 20, 80]
})

df["dept_total"] = df.groupby("dept")["sales"].transform("sum")
df["share"] = df["sales"] / df["dept_total"]
print(df)
```

- `A` `transform("sum")` 會把每個部門的總 sales 對齊回原始列，因此 `share` 是每一列在自己部門總量中的占比。
- `B` `transform("sum")` 會把資料縮成每部門一列，因此 `share` 只會有 2 筆。
- `C` 這段程式是在算全公司總 sales 的占比，和部門分組無關。
- `D` `transform` 只能搭配字串欄位，不能用在數值欄位。

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：`agg` 與 `transform` 很容易混。`agg` 會彙總成較少列，`transform` 則把分組結果對齊回原始列，這是程式題很常出的差異點。

其餘選項為何錯：
- `B`：`transform` 的特性就是維持原始列數，不會縮成每群一列。
- `C`：這題明確以 `dept` 分組，因此占比是部門內占比，不是全體占比。
- `D`：`transform` 可以常見地搭配數值欄位計算 sum、mean、max 等。

補強知識點：
- 補強 `agg` 與 `transform` 的差異。
- 補強分組後回填原始列的輸出判讀。

回看來源：
- sources/official-corpus.md｜數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具

</details>

### 題 12｜`L22203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

如果這題在考 `groupby().transform()` 的用途，哪個選項正確？

```python
import pandas as pd

df = pd.DataFrame({
    "dept": ["A", "A", "B", "B"],
    "sales": [30, 70, 20, 80]
})

df["dept_total"] = df.groupby("dept")["sales"].transform("sum")
df["share"] = df["sales"] / df["dept_total"]
print(df)
```

- `A` 這段程式是在算全公司總 sales 的占比，和部門分組無關。
- `B` `transform` 只能搭配字串欄位，不能用在數值欄位。
- `C` `transform("sum")` 會把每個部門的總 sales 對齊回原始列，因此 `share` 是每一列在自己部門總量中的占比。
- `D` `transform("sum")` 會把資料縮成每部門一列，因此 `share` 只會有 2 筆。

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：`agg` 與 `transform` 很容易混。`agg` 會彙總成較少列，`transform` 則把分組結果對齊回原始列，這是程式題很常出的差異點。

其餘選項為何錯：
- `A`：這題明確以 `dept` 分組，因此占比是部門內占比，不是全體占比。
- `B`：`transform` 可以常見地搭配數值欄位計算 sum、mean、max 等。
- `D`：`transform` 的特性就是維持原始列數，不會縮成每群一列。

補強知識點：
- 補強 `agg` 與 `transform` 的差異。
- 補強分組後回填原始列的輸出判讀。

回看來源：
- sources/official-corpus.md｜數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具

</details>

### 題 13｜`L22302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

閱讀下列程式碼後，哪個敘述最正確？

```python
from sklearn.decomposition import PCA
import numpy as np

X = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5],
    [4, 5, 6]
])

pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)
print(X_reduced.shape)
print(pca.explained_variance_ratio_)
```

- `A` `PCA(n_components=2)` 代表模型只會保留前 2 筆資料列，和特徵維度無關。
- `B` `explained_variance_ratio_` 是每個原始欄位的 p-value，所以可以拿來做顯著性檢定。
- `C` PCA 的主要目的就是直接提高分類 accuracy，不需要考慮降維或資訊保留。
- `D` `explained_variance_ratio_` 用來看各主成分解釋了多少變異；設定 `n_components=2` 代表把原始 3 個特徵壓縮成 2 個主成分。

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：PCA 常見考點是降維意義與輸出欄位解讀，不是把它誤當成顯著性工具。這題要能分清楚『主成分數量』和『資料筆數』是不同概念。

其餘選項為何錯：
- `A`：`n_components` 控制的是保留的主成分維度，不是保留幾筆資料。
- `B`：`explained_variance_ratio_` 反映變異解釋比例，不是 p-value。
- `C`：PCA 可能幫助模型，但主要目的仍是降維、去冗餘與壓縮資訊。

補強知識點：
- 補強 PCA 的降維意義與 `explained_variance_ratio_` 解讀。
- 補強主成分數量與資料筆數的區別。

回看來源：
- sources/official-corpus.md｜常見的大數據分析方法
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

### 題 14｜`L22302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

如果這題在考 PCA 輸出判讀，哪個選項正確？

```python
from sklearn.decomposition import PCA
import numpy as np

X = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5],
    [4, 5, 6]
])

pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)
print(X_reduced.shape)
print(pca.explained_variance_ratio_)
```

- `A` `PCA(n_components=2)` 代表模型只會保留前 2 筆資料列，和特徵維度無關。
- `B` `explained_variance_ratio_` 是每個原始欄位的 p-value，所以可以拿來做顯著性檢定。
- `C` PCA 的主要目的就是直接提高分類 accuracy，不需要考慮降維或資訊保留。
- `D` `explained_variance_ratio_` 用來看各主成分解釋了多少變異；設定 `n_components=2` 代表把原始 3 個特徵壓縮成 2 個主成分。

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：PCA 常見考點是降維意義與輸出欄位解讀，不是把它誤當成顯著性工具。這題要能分清楚『主成分數量』和『資料筆數』是不同概念。

其餘選項為何錯：
- `A`：`n_components` 控制的是保留的主成分維度，不是保留幾筆資料。
- `B`：`explained_variance_ratio_` 反映變異解釋比例，不是 p-value。
- `C`：PCA 可能幫助模型，但主要目的仍是降維、去冗餘與壓縮資訊。

補強知識點：
- 補強 PCA 的降維意義與 `explained_variance_ratio_` 解讀。
- 補強主成分數量與資料筆數的區別。

回看來源：
- sources/official-corpus.md｜常見的大數據分析方法
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

### 題 15｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

閱讀下列程式碼後，哪個敘述最正確？

```python
from sklearn.ensemble import RandomForestClassifier
import numpy as np

X = np.array([
    [20, 1, 0],
    [22, 1, 1],
    [35, 0, 1],
    [40, 0, 1],
    [28, 1, 0],
    [50, 0, 1],
])
y = np.array([0, 0, 1, 1, 0, 1])

model = RandomForestClassifier(random_state=42, n_estimators=50)
model.fit(X, y)
print(model.feature_importances_)
```

- `A` 只要看到 importance 比較高，就代表該特徵一定和目標變數有因果關係。
- `B` `RandomForestClassifier` 訓練後不會有任何特徵重要性資訊，必須另外手算。
- `C` `feature_importances_` 反映各特徵對樹模型分裂決策的重要程度；它不是線性模型的斜率，也不能直接解讀成『增加 1 單位會增加多少預測值』。
- `D` `feature_importances_` 就等同線性回歸的 `coef_`，可以直接看正負方向與增加量。

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：樹模型的重要性與線性係數是兩種不同概念。這題常用來測試你會不會把 `coef_` 的解讀硬套到 ensemble tree 模型上。

其餘選項為何錯：
- `A`：重要性高不等於因果關係成立，只代表模型決策時較常依賴該特徵。
- `B`：隨機森林本身就能提供 `feature_importances_`。
- `D`：`feature_importances_` 不提供線性方向與單位變化解讀，不能等同 `coef_`。

補強知識點：
- 補強樹模型重要性與線性係數的差異。
- 補強特徵重要性不等於因果推論。

回看來源：
- sources/official-corpus.md｜模型訓練與評估
- sources/scope-weight-map.md｜L22301 模型訓練與效能評估

</details>

### 題 16｜`L22301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

如果這題在考樹模型的 `feature_importances_`，哪個選項正確？

```python
from sklearn.ensemble import RandomForestClassifier
import numpy as np

X = np.array([
    [20, 1, 0],
    [22, 1, 1],
    [35, 0, 1],
    [40, 0, 1],
    [28, 1, 0],
    [50, 0, 1],
])
y = np.array([0, 0, 1, 1, 0, 1])

model = RandomForestClassifier(random_state=42, n_estimators=50)
model.fit(X, y)
print(model.feature_importances_)
```

- `A` `feature_importances_` 反映各特徵對樹模型分裂決策的重要程度；它不是線性模型的斜率，也不能直接解讀成『增加 1 單位會增加多少預測值』。
- `B` `feature_importances_` 就等同線性回歸的 `coef_`，可以直接看正負方向與增加量。
- `C` 只要看到 importance 比較高，就代表該特徵一定和目標變數有因果關係。
- `D` `RandomForestClassifier` 訓練後不會有任何特徵重要性資訊，必須另外手算。

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：樹模型的重要性與線性係數是兩種不同概念。這題常用來測試你會不會把 `coef_` 的解讀硬套到 ensemble tree 模型上。

其餘選項為何錯：
- `B`：`feature_importances_` 不提供線性方向與單位變化解讀，不能等同 `coef_`。
- `C`：重要性高不等於因果關係成立，只代表模型決策時較常依賴該特徵。
- `D`：隨機森林本身就能提供 `feature_importances_`。

補強知識點：
- 補強樹模型重要性與線性係數的差異。
- 補強特徵重要性不等於因果推論。

回看來源：
- sources/official-corpus.md｜模型訓練與評估
- sources/scope-weight-map.md｜L22301 模型訓練與效能評估

</details>

## 本組必補

- 補強 `mean` 與 `median` 的補值差異
- 補強 `fillna` 與缺值處理的高頻寫法
- 補強 one-hot encoding 與 label encoding 的差異
- 補強 `drop_first=True` 對虛擬變數欄位數量的影響
- 補強 `stratify`、`random_state`、`SMOTE` 的功能差異
- 補強不平衡分類切分時的基本原則

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
| 15 |  |  |  |
| 16 |  |  |  |
