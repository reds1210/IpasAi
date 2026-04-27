# Day 05｜科目 2 反向題單

- 今日焦點：`資料清理、缺值處理、型別轉換`
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

若欄位包含缺失值，但不能隨便用 0 或 1 亂補，最合理的清理原則為何？

- `A` 完全忽略缺值直接建模
- `B` 依欄位意義與分析目的決定補值或保留缺失
- `C` 一律補 0，這樣最方便
- `D` 一律刪掉所有含缺值列

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：缺值處理沒有單一萬用答案，應依欄位意義、缺失機制與後續模型需求決定。

其餘選項為何錯：
- `A`：忽略缺值常使模型或統計結果失真。
- `C`：補 0 可能引入不存在的實際意義。
- `D`：全部刪除可能犧牲太多資料。

補強知識點：
- 缺值處理要結合欄位語意與缺失機制。
- 清理策略不應只追求方便。

回看來源：
- sources/official-corpus.md｜L22201 數據收集與清理
- sources/scope-weight-map.md｜L22201 數據收集與清理

</details>

### 題 2｜`L22201`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

資料欄位有 NaN，若硬補成 0 會扭曲商業意義。這種情況下，先做哪種判斷最重要？

- `A` 一律刪掉所有含缺值列
- `B` 完全忽略缺值直接建模
- `C` 依欄位意義與分析目的決定補值或保留缺失
- `D` 一律補 0，這樣最方便

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：缺值處理沒有單一萬用答案，應依欄位意義、缺失機制與後續模型需求決定。

其餘選項為何錯：
- `A`：全部刪除可能犧牲太多資料。
- `B`：忽略缺值常使模型或統計結果失真。
- `D`：補 0 可能引入不存在的實際意義。

補強知識點：
- 缺值處理要結合欄位語意與缺失機制。
- 清理策略不應只追求方便。

回看來源：
- sources/official-corpus.md｜L22201 數據收集與清理
- sources/scope-weight-map.md｜L22201 數據收集與清理

</details>

### 題 3｜`L22201`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

資料清理時若懷疑同一筆交易被重複匯入，最應先檢查哪一類問題？

- `A` 先把所有欄位轉成字串
- `B` 檢查重複資料與主鍵/唯一鍵一致性
- `C` 直接把所有數值乘以 0.5
- `D` 只重畫圖表不看原始資料

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：若資料重複匯入，先從 duplicates 與唯一鍵檢查著手最直接。

其餘選項為何錯：
- `A`：全轉字串不會解決重複匯入。
- `C`：直接縮小數值是掩蓋問題，不是修正根因。
- `D`：只重畫圖無法修復原始資料品質。

補強知識點：
- 資料品質問題先找根因，不要直接修數字。
- 主鍵、時間戳、交易編號常是 dedup 的線索。

回看來源：
- sources/official-corpus.md｜L22201 數據收集與清理
- sources/scope-weight-map.md｜L22201 數據收集與清理

</details>

### 題 4｜`L22201`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

營收報表出現異常放大，且 ETL 日誌顯示同一批資料可能重跑兩次。若先做一項清理檢查，最合理的是什麼？

- `A` 只重畫圖表不看原始資料
- `B` 先把所有欄位轉成字串
- `C` 檢查重複資料與主鍵/唯一鍵一致性
- `D` 直接把所有數值乘以 0.5

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：若資料重複匯入，先從 duplicates 與唯一鍵檢查著手最直接。

其餘選項為何錯：
- `A`：只重畫圖無法修復原始資料品質。
- `B`：全轉字串不會解決重複匯入。
- `D`：直接縮小數值是掩蓋問題，不是修正根因。

補強知識點：
- 資料品質問題先找根因，不要直接修數字。
- 主鍵、時間戳、交易編號常是 dedup 的線索。

回看來源：
- sources/official-corpus.md｜L22201 數據收集與清理
- sources/scope-weight-map.md｜L22201 數據收集與清理

</details>

### 題 5｜`L22203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若欄位看起來像日期，但目前仍是字串，最合理的前處理方向為何？

- `A` 保留字串即可，之後再說
- `B` 全部改成整數索引
- `C` 只把欄位名稱改成 date
- `D` 轉成日期時間型態（datetime）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：日期分析常需排序、萃取月份、重取樣等操作，因此應先轉成 datetime。

其餘選項為何錯：
- `A`：保留字串容易造成排序與切片錯誤。
- `B`：整數索引不會自動保留日期語意。
- `C`：改欄位名稱不改內容型態。

補強知識點：
- 日期欄位若要做趨勢分析，先處理 datetime。
- 型態正確才能做 resample / month extraction。

回看來源：
- sources/official-corpus.md｜L22203 數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具

</details>

### 題 6｜`L22203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

你想做按月銷售趨勢分析，但發現日期欄位是純文字。若要先讓時間運算正確，該怎麼做？

- `A` 保留字串即可，之後再說
- `B` 全部改成整數索引
- `C` 只把欄位名稱改成 date
- `D` 轉成日期時間型態（datetime）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：日期分析常需排序、萃取月份、重取樣等操作，因此應先轉成 datetime。

其餘選項為何錯：
- `A`：保留字串容易造成排序與切片錯誤。
- `B`：整數索引不會自動保留日期語意。
- `C`：改欄位名稱不改內容型態。

補強知識點：
- 日期欄位若要做趨勢分析，先處理 datetime。
- 型態正確才能做 resample / month extraction。

回看來源：
- sources/official-corpus.md｜L22203 數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具

</details>

### 題 7｜`L22201`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若欄位同時有數字、空值與少量格式錯誤字串，資料清理的較佳順序通常為何？

- `A` 先強制 `astype(int)` 再看哪裡報錯
- `B` 先畫圖，不處理清理
- `C` 先把所有欄位都當作類別型資料
- `D` 先標準化缺失表達，再做型態轉換與例外檢查

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：先把 `N/A`、空字串等統一為缺失值，再轉型會更穩定。

其餘選項為何錯：
- `A`：直接強轉容易在最前面就失敗。
- `B`：圖表無法取代資料清理。
- `C`：全部當類別會失去數值分析能力。

補強知識點：
- 清理順序通常是標準化缺失表示，再做 cast。
- 型態轉換前先處理 dirty tokens。

回看來源：
- sources/official-corpus.md｜L22201 數據收集與清理
- sources/scope-weight-map.md｜L22201 數據收集與清理

</details>

### 題 8｜`L22201`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

數值欄位中混入 `N/A`、空字串與少量錯字。若你想降低後續轉型錯誤，較好的流程是什麼？

- `A` 先強制 `astype(int)` 再看哪裡報錯
- `B` 先畫圖，不處理清理
- `C` 先把所有欄位都當作類別型資料
- `D` 先標準化缺失表達，再做型態轉換與例外檢查

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：先把 `N/A`、空字串等統一為缺失值，再轉型會更穩定。

其餘選項為何錯：
- `A`：直接強轉容易在最前面就失敗。
- `B`：圖表無法取代資料清理。
- `C`：全部當類別會失去數值分析能力。

補強知識點：
- 清理順序通常是標準化缺失表示，再做 cast。
- 型態轉換前先處理 dirty tokens。

回看來源：
- sources/official-corpus.md｜L22201 數據收集與清理
- sources/scope-weight-map.md｜L22201 數據收集與清理

</details>

### 題 9｜`L22203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

對無序類別欄位做機器學習前，若不想引入假性的大小關係，常見的編碼方式為何？

- `A` One-hot encoding
- `B` 直接 label encoding 並假設數字大小有意義
- `C` 把欄位刪掉
- `D` 把所有值合併成同一類

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：無序類別若直接編成 1、2、3，部分模型會誤讀出大小關係；one-hot 較安全。

其餘選項為何錯：
- `B`：label encoding 可能讓模型誤讀排序。
- `C`：直接刪欄位會損失可能有用的訊息。
- `D`：全部合併成同類會消除區辨資訊。

補強知識點：
- 類別是否有序，決定編碼策略。
- one-hot 與 label encoding 的適用場景要分清。

回看來源：
- sources/official-corpus.md｜L22203 數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具

</details>

### 題 10｜`L22203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

欄位 `Color` 只有 `Red/Blue/Green` 三種值，且三者沒有自然大小順序。若要避免模型誤以為有大小關係，較合理的處理方式是什麼？

- `A` 把所有值合併成同一類
- `B` One-hot encoding
- `C` 直接 label encoding 並假設數字大小有意義
- `D` 把欄位刪掉

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：無序類別若直接編成 1、2、3，部分模型會誤讀出大小關係；one-hot 較安全。

其餘選項為何錯：
- `A`：全部合併成同類會消除區辨資訊。
- `C`：label encoding 可能讓模型誤讀排序。
- `D`：直接刪欄位會損失可能有用的訊息。

補強知識點：
- 類別是否有序，決定編碼策略。
- one-hot 與 label encoding 的適用場景要分清。

回看來源：
- sources/official-corpus.md｜L22203 數據處理技術與工具
- sources/scope-weight-map.md｜L22203 數據處理技術與工具

</details>

## 今日必補知識點

- 缺值處理要結合欄位語意與缺失機制，回看 [sources](../sources/) 內對應文件。
- 清理策略不應只追求方便，回看 [sources](../sources/) 內對應文件。
- 資料品質問題先找根因，不要直接修數字，回看 [sources](../sources/) 內對應文件。
- 主鍵、時間戳、交易編號常是 dedup 的線索，回看 [sources](../sources/) 內對應文件。
- 日期欄位若要做趨勢分析，先處理 datetime，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s2d5_datetime_cast, s2d5_label_vs_onehot
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
