# Day 13｜科目 2 反向題單

- 今日焦點：`圖資料庫、知識圖譜、RDF`
- 題量：`12` 題
- 建議方式：3–5 小時內完成，先做題、再補點。｜優先級 A｜先刷這份，對過線最有幫助。
- 來源對照：
  - [official-corpus.md](../sources/official-corpus.md)
  - [scope-weight-map.md](../sources/scope-weight-map.md)
  - [question-source-map.md](../sources/question-source-map.md)
  - [question-patterns.md](../sources/question-patterns.md)
  - [book-bridge.md](../sources/book-bridge.md)

## 今日題目

### 題 1｜`L22202`｜難度：`中`
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

### 題 2｜`L22202`｜難度：`中`
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

### 題 3｜`L22202`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若希望知識圖譜支援語意查詢與關聯推理，哪種資料模型最常見？

- `A` RDF 三元組（subject-predicate-object）
- `B` 只把所有內容塞進單一文字欄位
- `C` 只存成普通 CSV 而不保留關係語意
- `D` 只畫心智圖不建立機器可讀模型

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：RDF 三元組是知識圖譜的常見基礎模型，適合做語意關係與推理。

其餘選項為何錯：
- `B`：單一文字欄位無法表達可機器推理的關係。
- `C`：普通 CSV 缺乏語意連結結構。
- `D`：心智圖若不可機器讀取，無法直接支援推理。

補強知識點：
- RDF、triple、ontology 是知識圖譜高頻詞。
- 知識圖譜題常考『語意查詢與推理』。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 RDF
- sources/scope-weight-map.md｜L22202 數據儲存與管理

</details>

### 題 4｜`L22202`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

企業想把研究報告、專利與專家知識整合成可推理的知識圖譜。若從資料模型來看，哪個方向最對題？

- `A` 只把所有內容塞進單一文字欄位
- `B` 只存成普通 CSV 而不保留關係語意
- `C` 只畫心智圖不建立機器可讀模型
- `D` RDF 三元組（subject-predicate-object）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：RDF 三元組是知識圖譜的常見基礎模型，適合做語意關係與推理。

其餘選項為何錯：
- `A`：單一文字欄位無法表達可機器推理的關係。
- `B`：普通 CSV 缺乏語意連結結構。
- `C`：心智圖若不可機器讀取，無法直接支援推理。

補強知識點：
- RDF、triple、ontology 是知識圖譜高頻詞。
- 知識圖譜題常考『語意查詢與推理』。

回看來源：
- sources/official-corpus.md｜正式題公開題目出現 RDF
- sources/scope-weight-map.md｜L22202 數據儲存與管理

</details>

### 題 5｜`L22202`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若資料重點在多跳關聯查詢與關係探索，哪種資料庫模型通常更有優勢？

- `A` 只用純檔案系統
- `B` 只用樞紐分析表
- `C` 只用隨機文字摘要
- `D` 圖資料庫（Graph Database）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：圖資料庫對多跳關係查詢與圖演算法通常較自然。

其餘選項為何錯：
- `A`：檔案系統不負責關係查詢。
- `B`：樞紐分析表偏彙整展示，不是關係遍歷工具。
- `C`：文字摘要不是結構化關聯模型。

補強知識點：
- 多跳關係題先想 graph model。
- 資料模型選擇要看查詢型態，而不只看資料量。

回看來源：
- sources/official-corpus.md｜L22202 數據儲存與管理
- sources/scope-weight-map.md｜L22202 數據儲存與管理

</details>

### 題 6｜`L22202`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若分析任務常問『A 透過哪些人間接連到 B』這類多層關係問題，較合適的儲存模型為何？

- `A` 只用隨機文字摘要
- `B` 圖資料庫（Graph Database）
- `C` 只用純檔案系統
- `D` 只用樞紐分析表

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：圖資料庫對多跳關係查詢與圖演算法通常較自然。

其餘選項為何錯：
- `A`：文字摘要不是結構化關聯模型。
- `C`：檔案系統不負責關係查詢。
- `D`：樞紐分析表偏彙整展示，不是關係遍歷工具。

補強知識點：
- 多跳關係題先想 graph model。
- 資料模型選擇要看查詢型態，而不只看資料量。

回看來源：
- sources/official-corpus.md｜L22202 數據儲存與管理
- sources/scope-weight-map.md｜L22202 數據儲存與管理

</details>

### 題 7｜`L22402`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

下列哪種 AI 應用情境最能受益於知識圖譜的語意關聯能力？

- `A` 只把資料壓縮成 zip 檔
- `B` 只靠單一關鍵字字典做固定匹配
- `C` 建立知識圖譜支援語意檢索與關聯推理
- `D` 只做簡單平均數報表

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：知識圖譜特別適合異質知識整合、關聯查詢與推理。

其餘選項為何錯：
- `A`：壓縮檔只是儲存形式。
- `B`：固定字典匹配缺少關聯推理能力。
- `D`：平均數報表不需要圖推理。

補強知識點：
- 把知識圖譜當成『關係結構化 + 可推理』的工具。
- 異質知識整合題通常不是單純 BI 報表題。

回看來源：
- sources/official-corpus.md｜L22402 大數據在鑑別式 AI 中的應用
- sources/scope-weight-map.md｜L22402 大數據在鑑別式 AI 中的應用

</details>

### 題 8｜`L22402`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若企業想整合產品、專利、客訴與技術文件，並支援語意查詢與關係推理，最適合優先考慮哪個方向？

- `A` 建立知識圖譜支援語意檢索與關聯推理
- `B` 只做簡單平均數報表
- `C` 只把資料壓縮成 zip 檔
- `D` 只靠單一關鍵字字典做固定匹配

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：知識圖譜特別適合異質知識整合、關聯查詢與推理。

其餘選項為何錯：
- `B`：平均數報表不需要圖推理。
- `C`：壓縮檔只是儲存形式。
- `D`：固定字典匹配缺少關聯推理能力。

補強知識點：
- 把知識圖譜當成『關係結構化 + 可推理』的工具。
- 異質知識整合題通常不是單純 BI 報表題。

回看來源：
- sources/official-corpus.md｜L22402 大數據在鑑別式 AI 中的應用
- sources/scope-weight-map.md｜L22402 大數據在鑑別式 AI 中的應用

</details>

### 題 9｜`L22302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若要找出社群網路中最有影響力或最居中的節點，哪一類分析概念最直接？

- `A` 中心性（centrality）分析
- `B` 只看所有節點名稱長度
- `C` 只做字串排序
- `D` 只比較檔案大小

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：中心性分析用來衡量節點在網路中的重要性或位置。

其餘選項為何錯：
- `B`：名稱長度與網路影響力無關。
- `C`：字串排序不反映關係結構。
- `D`：檔案大小也與節點位置無關。

補強知識點：
- 圖分析常考中心性、社群偵測、最短路徑。
- 看到『關鍵節點』就先想 centrality。

回看來源：
- sources/official-corpus.md｜L22302 常見的大數據分析方法
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

### 題 10｜`L22302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若企業想找出知識網絡中的關鍵專家節點，最合理先看的圖分析方向為何？

- `A` 中心性（centrality）分析
- `B` 只看所有節點名稱長度
- `C` 只做字串排序
- `D` 只比較檔案大小

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：中心性分析用來衡量節點在網路中的重要性或位置。

其餘選項為何錯：
- `B`：名稱長度與網路影響力無關。
- `C`：字串排序不反映關係結構。
- `D`：檔案大小也與節點位置無關。

補強知識點：
- 圖分析常考中心性、社群偵測、最短路徑。
- 看到『關鍵節點』就先想 centrality。

回看來源：
- sources/official-corpus.md｜L22302 常見的大數據分析方法
- sources/scope-weight-map.md｜L22302 常見的大數據分析方法

</details>

### 題 11｜`L22202`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若任務重點是查詢複雜關係鏈與語意路徑，下列哪項能力最重要？

- `A` 支援關係路徑查詢與圖遍歷
- `B` 只支援單欄位排序
- `C` 只支援把圖片縮圖
- `D` 只支援文字上色

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：圖模型的價值之一就是能高效處理路徑與關聯遍歷查詢。

其餘選項為何錯：
- `B`：單欄位排序不是路徑查詢。
- `C`：圖片縮圖與圖資料無關。
- `D`：文字上色不是查詢能力。

補強知識點：
- 圖資料庫的亮點是 traversal。
- 看到『經由哪些關係連過去』時要聯想到 path query。

回看來源：
- sources/official-corpus.md｜L22202 數據儲存與管理
- sources/scope-weight-map.md｜L22202 數據儲存與管理

</details>

### 題 12｜`L22202`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

知識圖譜若要回答『某專家透過哪些專利與主題間接關聯到某產品問題』，資料平台最需要具備哪類能力？

- `A` 只支援把圖片縮圖
- `B` 只支援文字上色
- `C` 支援關係路徑查詢與圖遍歷
- `D` 只支援單欄位排序

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：圖模型的價值之一就是能高效處理路徑與關聯遍歷查詢。

其餘選項為何錯：
- `A`：圖片縮圖與圖資料無關。
- `B`：文字上色不是查詢能力。
- `D`：單欄位排序不是路徑查詢。

補強知識點：
- 圖資料庫的亮點是 traversal。
- 看到『經由哪些關係連過去』時要聯想到 path query。

回看來源：
- sources/official-corpus.md｜L22202 數據儲存與管理
- sources/scope-weight-map.md｜L22202 數據儲存與管理

</details>

## 今日必補知識點

- 圖資料庫的核心是節點、邊與屬性，回看 [sources](../sources/) 內對應文件。
- 互動事件若天然是關係，先考慮 edge property，回看 [sources](../sources/) 內對應文件。
- RDF、triple、ontology 是知識圖譜高頻詞，回看 [sources](../sources/) 內對應文件。
- 知識圖譜題常考『語意查詢與推理』，回看 [sources](../sources/) 內對應文件。
- 多跳關係題先想 graph model，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s2d13_graph_edge_property, s2d13_rdf, s2d13_graph_vs_relational, s2d13_graph_query
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
