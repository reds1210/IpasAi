# Day 12｜科目 1 反向題單

- 今日焦點：`半模擬跨章整合`
- 題量：`8` 題
- 建議方式：先以 60–75 分鐘完成第一輪，再展開解析。｜優先級 A｜先刷這份，對過線最有幫助。
- 來源對照：
  - [official-corpus.md](../sources/official-corpus.md)
  - [scope-weight-map.md](../sources/scope-weight-map.md)
  - [question-source-map.md](../sources/question-source-map.md)
  - [question-patterns.md](../sources/question-patterns.md)
  - [book-bridge.md](../sources/book-bridge.md)

## 今日題目

### 題 1｜`L21102`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若模型只需判定一張照片中主要物件屬於哪個類別，最符合哪一種電腦視覺任務？

- `A` 物件偵測（Object Detection）
- `B` 語義分割（Semantic Segmentation）
- `C` 實例分割（Instance Segmentation）
- `D` 圖像分類（Image Classification）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：圖像分類只回答整張圖的類別，不要求定位或像素級分割。

其餘選項為何錯：
- `A`：物件偵測還要輸出邊界框與位置。
- `B`：語義分割需要對每個像素標上類別。
- `C`：實例分割除了像素標註，還要區分同類別不同個體。

補強知識點：
- 分類、偵測、語義分割、實例分割的輸出粒度要分清。
- 看到『只要知道是什麼』先想 classification。

回看來源：
- sources/official-corpus.md｜官方樣題曾比較多種 CV 任務
- sources/scope-weight-map.md｜L21102 電腦視覺技術與應用

</details>

### 題 2｜`L21102`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

零售商只想知道商品照片屬於鞋子、包包或外套，不需框出位置，應選哪種 CV 任務？

- `A` 物件偵測（Object Detection）
- `B` 語義分割（Semantic Segmentation）
- `C` 實例分割（Instance Segmentation）
- `D` 圖像分類（Image Classification）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：圖像分類只回答整張圖的類別，不要求定位或像素級分割。

其餘選項為何錯：
- `A`：物件偵測還要輸出邊界框與位置。
- `B`：語義分割需要對每個像素標上類別。
- `C`：實例分割除了像素標註，還要區分同類別不同個體。

補強知識點：
- 分類、偵測、語義分割、實例分割的輸出粒度要分清。
- 看到『只要知道是什麼』先想 classification。

回看來源：
- sources/official-corpus.md｜官方樣題曾比較多種 CV 任務
- sources/scope-weight-map.md｜L21102 電腦視覺技術與應用

</details>

### 題 3｜`L21104`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

在多模態學習中，Early Fusion 的主要特徵為何？

- `A` 只在最終決策階段投票合併輸出
- `B` 完全分開訓練且永不對齊不同模態
- `C` 只允許模型處理單一來源資料
- `D` 在輸入階段或特徵階段整合不同模態資料

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：Early Fusion 是先整合不同模態的表示，再交給後續模型學習。

其餘選項為何錯：
- `A`：只在最後投票是 late fusion 的特徵。
- `B`：永不對齊模態無法形成有效多模態表示。
- `C`：單模態處理不符合多模態學習定義。

補強知識點：
- Early fusion 與 late fusion 的分界要靠『整合發生在何時』來記。
- 看到輸入階段整合就先選 early fusion。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現 Early Fusion
- sources/scope-weight-map.md｜L21104 多模態人工智慧應用

</details>

### 題 4｜`L21104`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若系統在模型輸入或特徵提取階段就把影像、文本與表格資料整合，這種做法最接近哪種融合方式？

- `A` 在輸入階段或特徵階段整合不同模態資料
- `B` 只在最終決策階段投票合併輸出
- `C` 完全分開訓練且永不對齊不同模態
- `D` 只允許模型處理單一來源資料

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：Early Fusion 是先整合不同模態的表示，再交給後續模型學習。

其餘選項為何錯：
- `B`：只在最後投票是 late fusion 的特徵。
- `C`：永不對齊模態無法形成有效多模態表示。
- `D`：單模態處理不符合多模態學習定義。

補強知識點：
- Early fusion 與 late fusion 的分界要靠『整合發生在何時』來記。
- 看到輸入階段整合就先選 early fusion。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現 Early Fusion
- sources/scope-weight-map.md｜L21104 多模態人工智慧應用

</details>

### 題 5｜`L21201`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

企業評估是否導入 AI 前，若想先判斷專案可行性，最先要確認哪一項基礎條件？

- `A` 先承諾上線日期，再補需求訪談
- `B` 資料可用性與資料品質是否支撐目標任務
- `C` 先挑最流行的模型名稱
- `D` 先購買最多 GPU，再回頭想資料

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：資料是 AI 專案能否落地的基礎，沒有足夠且可信的資料，再好的模型也難以成功。

其餘選項為何錯：
- `A`：先承諾時程但未完成需求與資料評估，風險最高。
- `C`：模型流行不代表適合當前資料條件與業務問題。
- `D`：硬體採購不能替代資料治理。

補強知識點：
- 導入評估的第一關通常是資料、目標、指標，而不是先追模型。
- 看到『可行性』就先問資料與需求是否成立。

回看來源：
- sources/official-corpus.md｜L21201 AI 導入評估
- sources/scope-weight-map.md｜L21201 AI 導入評估

</details>

### 題 6｜`L21201`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

主管急著上生成式 AI，但團隊連乾淨資料、標註規則與更新流程都沒有。若你只能先做一項評估，最優先的是什麼？

- `A` 先購買最多 GPU，再回頭想資料
- `B` 先承諾上線日期，再補需求訪談
- `C` 資料可用性與資料品質是否支撐目標任務
- `D` 先挑最流行的模型名稱

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：資料是 AI 專案能否落地的基礎，沒有足夠且可信的資料，再好的模型也難以成功。

其餘選項為何錯：
- `A`：硬體採購不能替代資料治理。
- `B`：先承諾時程但未完成需求與資料評估，風險最高。
- `D`：模型流行不代表適合當前資料條件與業務問題。

補強知識點：
- 導入評估的第一關通常是資料、目標、指標，而不是先追模型。
- 看到『可行性』就先問資料與需求是否成立。

回看來源：
- sources/official-corpus.md｜L21201 AI 導入評估
- sources/scope-weight-map.md｜L21201 AI 導入評估

</details>

### 題 7｜`L21301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若目標是根據歷史銷售資料預測下一季銷售額，下列哪種模型類型最適合？

- `A` 分群模型（Clustering）
- `B` 分類模型（Classification）
- `C` 關聯規則分析（Association Rules）
- `D` 迴歸模型（Regression）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：預測連續數值目標時，首選應是迴歸模型。

其餘選項為何錯：
- `A`：分群用於找群組，不直接輸出連續預測值。
- `B`：分類輸出類別標籤，不是連續數值。
- `C`：關聯規則用來找共現模式，不是數值預測。

補強知識點：
- 先辨識目標變數型態：連續值選 regression，離散標籤選 classification。
- 看到『預測金額、銷量、工時』時，優先想回歸。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現回歸任務選型
- sources/scope-weight-map.md｜L21301 數據準備與模型選擇

</details>

### 題 8｜`L21301`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

電商老闆想依過去產品銷量預估下季數量，以便調整庫存，最合理的第一個模型方向為何？

- `A` 迴歸模型（Regression）
- `B` 分群模型（Clustering）
- `C` 分類模型（Classification）
- `D` 關聯規則分析（Association Rules）

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：預測連續數值目標時，首選應是迴歸模型。

其餘選項為何錯：
- `B`：分群用於找群組，不直接輸出連續預測值。
- `C`：分類輸出類別標籤，不是連續數值。
- `D`：關聯規則用來找共現模式，不是數值預測。

補強知識點：
- 先辨識目標變數型態：連續值選 regression，離散標籤選 classification。
- 看到『預測金額、銷量、工時』時，優先想回歸。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現回歸任務選型
- sources/scope-weight-map.md｜L21301 數據準備與模型選擇

</details>

## 今日必補知識點

- 分類、偵測、語義分割、實例分割的輸出粒度要分清，回看 [sources](../sources/) 內對應文件。
- 看到『只要知道是什麼』先想 classification，回看 [sources](../sources/) 內對應文件。
- Early fusion 與 late fusion 的分界要靠『整合發生在何時』來記，回看 [sources](../sources/) 內對應文件。
- 看到輸入階段整合就先選 early fusion，回看 [sources](../sources/) 內對應文件。
- 導入評估的第一關通常是資料、目標、指標，而不是先追模型，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s1d5_data_readiness, s1d8_regression_fit
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
