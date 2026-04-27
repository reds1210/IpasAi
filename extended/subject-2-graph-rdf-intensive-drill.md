# 科目 2 加練｜圖資料庫、知識圖譜與 RDF 強化

- 科目：`2`
- 優先級：`A`
- 優先級摘要：`A=4 / B=0 / C=0`
- 來源層級：`official-derived`
- 焦點：`property graph、RDF 三元組、知識圖譜、多跳關聯查詢`
- 題數：`8` 題
- 建議加做時機：`Day 13、Day 18、Day 19 後加做`
- 作答單：[開啟](../attempts/subject-2-graph-rdf-intensive-drill-attempt.md)
- 批改報告：[開啟](../reports/subject-2-graph-rdf-intensive-drill-report.md)
- 批改指令：`python .\score_attempt.py --drill subject-2-graph-rdf-intensive-drill`
- 使用方式：先做題，再展開 `<details>` 看答案與排錯理由。

## 題源對照

- sources/question-source-map.md｜114 第二梯次科目 2 公告試題
- sources/scope-weight-map.md｜L22202 數據儲存與管理
- sources/question-source-map.md｜官方樣題與公告題顯示圖資料庫為高頻
- sources/question-source-map.md｜圖資料庫、知識圖譜與 RDF

## 題目

### 題 1｜`L22202`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若要把「客戶 A 購買 商品 B」表達成 RDF 最核心的三元組，下列何者最符合 RDF 表示法？

- `A` 把資料拆成只有欄位名稱的二維表
- `B` 只記錄節點，不記錄節點間關係
- `C` 先把資料轉成影像向量再查詢
- `D` 以主詞、述詞、受詞三元組表達實體與關係

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：RDF 的基本單位就是主詞、述詞、受詞三元組，用來描述實體與其關係。

其餘選項為何錯：
- `A`：二維表能存資料，但不是 RDF 的核心表示法。
- `B`：只記節點沒有關係，無法形成知識圖譜可推理結構。
- `C`：影像向量與 RDF 結構是不同層次的表示方式。

補強知識點：
- 記住 RDF = subject / predicate / object。
- 分清 RDF、關聯式表格、向量資料表示的用途。

回看來源：
- sources/official-corpus.md｜114 第二梯次科目 2 公告試題含 RDF 題型
- sources/question-source-map.md｜A 級必擴官方題源

</details>

### 題 2｜`L22202`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

知識圖譜專案要把『王小明修讀資料科學』轉成 RDF 三元組，最合理的基本結構是什麼？

- `A` 以主詞、述詞、受詞三元組表達實體與關係
- `B` 把資料拆成只有欄位名稱的二維表
- `C` 只記錄節點，不記錄節點間關係
- `D` 先把資料轉成影像向量再查詢

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：RDF 的基本單位就是主詞、述詞、受詞三元組，用來描述實體與其關係。

其餘選項為何錯：
- `B`：二維表能存資料，但不是 RDF 的核心表示法。
- `C`：只記節點沒有關係，無法形成知識圖譜可推理結構。
- `D`：影像向量與 RDF 結構是不同層次的表示方式。

補強知識點：
- 記住 RDF = subject / predicate / object。
- 分清 RDF、關聯式表格、向量資料表示的用途。

回看來源：
- sources/official-corpus.md｜114 第二梯次科目 2 公告試題含 RDF 題型
- sources/question-source-map.md｜A 級必擴官方題源

</details>

### 題 3｜`L22202`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

物流公司要分析『倉庫 A 到門市 B』這條配送路徑的距離、運費與平均時延，最適合把這些資訊建在何處？

- `A` 把每個屬性拆成獨立模型權重
- `B` 建在邊（edge）屬性上
- `C` 建在所有節點的共同欄位中
- `D` 只建在圖的名稱描述裡

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：路徑距離、互動時間、停留秒數都是關係本身的資訊，最適合放在邊屬性。

其餘選項為何錯：
- `A`：模型權重不負責保存圖資料的業務屬性。
- `C`：共同欄位無法正確表示每一條關係自己的數值。
- `D`：圖的名稱描述不是可查詢的關係屬性結構。

補強知識點：
- 分清節點屬性與邊屬性。
- 看到『關係自己的數值』優先想到 edge property。

回看來源：
- sources/official-corpus.md｜圖資料庫題型整理
- sources/question-source-map.md｜圖資料庫、知識圖譜與 RDF 為 A 級必擴主題

</details>

### 題 4｜`L22202`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若推薦系統要記錄「使用者看過商品」這條關係的時間與停留秒數，property graph 最適合把這些值放在哪裡？

- `A` 建在邊（edge）屬性上
- `B` 建在所有節點的共同欄位中
- `C` 只建在圖的名稱描述裡
- `D` 把每個屬性拆成獨立模型權重

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：路徑距離、互動時間、停留秒數都是關係本身的資訊，最適合放在邊屬性。

其餘選項為何錯：
- `B`：共同欄位無法正確表示每一條關係自己的數值。
- `C`：圖的名稱描述不是可查詢的關係屬性結構。
- `D`：模型權重不負責保存圖資料的業務屬性。

補強知識點：
- 分清節點屬性與邊屬性。
- 看到『關係自己的數值』優先想到 edge property。

回看來源：
- sources/official-corpus.md｜圖資料庫題型整理
- sources/question-source-map.md｜圖資料庫、知識圖譜與 RDF 為 A 級必擴主題

</details>

### 題 5｜`L22303`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若要查出『買過相同商品、且都來自同一城市』的客戶群，再延伸找出他們共同關注的品牌，哪種資料模型通常更適合？

- `A` 只用影像分類模型即可處理
- `B` 把所有資料壓成單一平均值即可
- `C` 知識圖譜或圖資料庫較適合多跳關聯查詢
- `D` 純文字摘要最適合做關聯查詢

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：多跳關聯查詢是圖結構的強項，知識圖譜與圖資料庫能更自然描述路徑與關係。

其餘選項為何錯：
- `A`：影像分類模型不負責多跳關聯推理。
- `B`：平均值會破壞實體與關係網路。
- `D`：文字摘要不能取代關聯結構查詢。

補強知識點：
- 辨識多跳查詢情境。
- 知道知識圖譜適合做關聯探索與語意推理。

回看來源：
- sources/official-corpus.md｜圖資料庫、知識圖譜高頻主題
- sources/question-source-map.md｜官方題源與培訓資源都覆蓋圖資料

</details>

### 題 6｜`L22303`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

公司想做多跳關聯分析，從病患到症狀到藥物再到副作用一路追查，哪種結構通常比單純關聯式表更自然？

- `A` 把所有資料壓成單一平均值即可
- `B` 知識圖譜或圖資料庫較適合多跳關聯查詢
- `C` 純文字摘要最適合做關聯查詢
- `D` 只用影像分類模型即可處理

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：多跳關聯查詢是圖結構的強項，知識圖譜與圖資料庫能更自然描述路徑與關係。

其餘選項為何錯：
- `A`：平均值會破壞實體與關係網路。
- `C`：文字摘要不能取代關聯結構查詢。
- `D`：影像分類模型不負責多跳關聯推理。

補強知識點：
- 辨識多跳查詢情境。
- 知道知識圖譜適合做關聯探索與語意推理。

回看來源：
- sources/official-corpus.md｜圖資料庫、知識圖譜高頻主題
- sources/question-source-map.md｜官方題源與培訓資源都覆蓋圖資料

</details>

### 題 7｜`L22202`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

下列何者最能說明 ontology 與 graph database 的差異？

- `A` ontology 主要用來做影像增強
- `B` graph database 只適合存數值矩陣
- `C` ontology 著重概念與關係定義，graph database 著重資料儲存與查詢
- `D` 兩者完全同義，只是名稱不同

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：ontology 是語意層與概念模型，graph database 則是實際承載與查詢圖資料的系統或模型。

其餘選項為何錯：
- `A`：ontology 不處理影像增強。
- `B`：graph database 不只存數值矩陣，核心是節點與邊關係。
- `D`：兩者相關但不等同，一個偏語意規格，一個偏資料存取。

補強知識點：
- 分清 ontology、knowledge graph、graph database 的層次。
- 不要把語意模型與資料儲存系統混成同義詞。

回看來源：
- sources/question-source-map.md｜公開整理常提醒 ontology / knowledge graph / graph DB 易混淆
- sources/question-patterns.md｜易混概念對抗題

</details>

### 題 8｜`L22202`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

在知識圖譜專案中，團隊同時提到 ontology 與 graph database。下列哪個理解最正確？

- `A` ontology 主要用來做影像增強
- `B` graph database 只適合存數值矩陣
- `C` ontology 著重概念與關係定義，graph database 著重資料儲存與查詢
- `D` 兩者完全同義，只是名稱不同

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：ontology 是語意層與概念模型，graph database 則是實際承載與查詢圖資料的系統或模型。

其餘選項為何錯：
- `A`：ontology 不處理影像增強。
- `B`：graph database 不只存數值矩陣，核心是節點與邊關係。
- `D`：兩者相關但不等同，一個偏語意規格，一個偏資料存取。

補強知識點：
- 分清 ontology、knowledge graph、graph database 的層次。
- 不要把語意模型與資料儲存系統混成同義詞。

回看來源：
- sources/question-source-map.md｜公開整理常提醒 ontology / knowledge graph / graph DB 易混淆
- sources/question-patterns.md｜易混概念對抗題

</details>

## 本組必補

- 記住 RDF = subject / predicate / object
- 分清 RDF、關聯式表格、向量資料表示的用途
- 分清節點屬性與邊屬性
- 看到『關係自己的數值』優先想到 edge property
- 辨識多跳查詢情境
- 知道知識圖譜適合做關聯探索與語意推理

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
