# Day 04｜科目 1 反向題單

- 今日焦點：`多模態與融合方式`
- 題量：`8` 題
- 建議方式：先以 60–75 分鐘完成第一輪，再展開解析。｜優先級 B｜主線刷完後優先補這份。
- 來源對照：
  - [official-corpus.md](../sources/official-corpus.md)
  - [scope-weight-map.md](../sources/scope-weight-map.md)
  - [question-source-map.md](../sources/question-source-map.md)
  - [question-patterns.md](../sources/question-patterns.md)
  - [book-bridge.md](../sources/book-bridge.md)

## 今日題目

### 題 1｜`L21104`｜難度：`中`
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

### 題 2｜`L21104`｜難度：`中`
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

### 題 3｜`L21104`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若要強化醫療多模態 AI 同時處理影像與臨床文本的整合能力，下列哪項技術最有幫助？

- `A` 只用單一 CNN 同時處理影像與文字
- `B` 只依單一模態資料建立通用模型
- `C` 採用 Transformer 架構做跨模態整合
- `D` 只用預先定義規則直接產生診斷

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：Transformer 與注意力機制較適合做跨模態對齊與長距關聯建模。

其餘選項為何錯：
- `A`：單一 CNN 不適合直接處理文字與影像的跨模態語意對齊。
- `B`：單模態模型無法發揮多模態互補資訊。
- `D`：規則系統缺乏跨模態表徵學習能力。

補強知識點：
- 跨模態整合常見關鍵字：attention、alignment、Transformer。
- 不要把單模態最佳模型直接套成多模態答案。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現醫療多模態整合
- sources/scope-weight-map.md｜L21104 多模態人工智慧應用

</details>

### 題 4｜`L21104`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

醫院希望把 CT 影像與病歷文字一起輸入模型做輔助判讀，若追求跨模態對齊與語意整合，最合理的架構方向為何？

- `A` 採用 Transformer 架構做跨模態整合
- `B` 只用預先定義規則直接產生診斷
- `C` 只用單一 CNN 同時處理影像與文字
- `D` 只依單一模態資料建立通用模型

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：Transformer 與注意力機制較適合做跨模態對齊與長距關聯建模。

其餘選項為何錯：
- `B`：規則系統缺乏跨模態表徵學習能力。
- `C`：單一 CNN 不適合直接處理文字與影像的跨模態語意對齊。
- `D`：單模態模型無法發揮多模態互補資訊。

補強知識點：
- 跨模態整合常見關鍵字：attention、alignment、Transformer。
- 不要把單模態最佳模型直接套成多模態答案。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現醫療多模態整合
- sources/scope-weight-map.md｜L21104 多模態人工智慧應用

</details>

### 題 5｜`L21104`｜難度：`難`
優先級：`B`｜來源層級：`official-derived`

多模態模型在推論時若某一模態缺失，最合理的穩定策略為何？

- `A` 完全忽略缺失模態問題，只依訓練集假設上線
- `B` 建立可容忍模態缺失的備援或缺失感知機制
- `C` 要求所有輸入一律齊全，缺一就直接停機
- `D` 把缺失模態隨便補成固定噪聲而不標記

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：實務系統需考慮模態缺失，因此要設計 fallback、mask 或缺失感知流程。

其餘選項為何錯：
- `A`：上線後忽略缺失模態風險，系統穩定性不足。
- `C`：實務環境不保證資料永遠齊全，直接停機可用性很差。
- `D`：隨機補噪聲但不讓模型知道缺失狀態，容易引入偏差。

補強知識點：
- 多模態系統除了準確率，也要看可用性與魯棒性。
- 題目提到某模態缺失時，先找 fallback 或 masking 類答案。

回看來源：
- sources/official-corpus.md｜正式題曾出現模態缺失情境
- sources/scope-weight-map.md｜L21104 多模態人工智慧應用

</details>

### 題 6｜`L21104`｜難度：`難`
優先級：`B`｜來源層級：`official-derived`

若線上系統偶爾只有影像、沒有文字描述，你仍希望模型保持可用，應優先採取哪類設計思路？

- `A` 完全忽略缺失模態問題，只依訓練集假設上線
- `B` 建立可容忍模態缺失的備援或缺失感知機制
- `C` 要求所有輸入一律齊全，缺一就直接停機
- `D` 把缺失模態隨便補成固定噪聲而不標記

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：實務系統需考慮模態缺失，因此要設計 fallback、mask 或缺失感知流程。

其餘選項為何錯：
- `A`：上線後忽略缺失模態風險，系統穩定性不足。
- `C`：實務環境不保證資料永遠齊全，直接停機可用性很差。
- `D`：隨機補噪聲但不讓模型知道缺失狀態，容易引入偏差。

補強知識點：
- 多模態系統除了準確率，也要看可用性與魯棒性。
- 題目提到某模態缺失時，先找 fallback 或 masking 類答案。

回看來源：
- sources/official-corpus.md｜正式題曾出現模態缺失情境
- sources/scope-weight-map.md｜L21104 多模態人工智慧應用

</details>

### 題 7｜`L21104`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

多模態模型若希望讓文字與影像能在同一語意空間互相比對，最核心的設計目標是什麼？

- `A` 把不同模態永遠分開儲存，不做對齊
- `B` 只增加單一模態資料量，不做跨模態學習
- `C` 只依關鍵字規則做固定映射，不學習向量表示
- `D` 建立共享表徵空間（shared representation space）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：跨模態檢索與對齊依賴共享語意空間，讓不同模態可被共同比較。

其餘選項為何錯：
- `A`：完全分開儲存無法支撐跨模態相似度計算。
- `B`：只增加單一模態資料量不會自動形成跨模態對齊。
- `C`：固定規則映射缺乏彈性與泛化能力。

補強知識點：
- 理解多模態檢索的關鍵不是資料量，而是 representation alignment。
- 『一句話找圖片』通常對應 shared embedding space。

回看來源：
- sources/official-corpus.md｜L21104 多模態應用
- sources/scope-weight-map.md｜L21104 多模態人工智慧應用

</details>

### 題 8｜`L21104`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

商品搜尋系統想做到『輸入一句描述就找到相符圖片』，若從模型設計角度看，最重要的能力是什麼？

- `A` 只增加單一模態資料量，不做跨模態學習
- `B` 只依關鍵字規則做固定映射，不學習向量表示
- `C` 建立共享表徵空間（shared representation space）
- `D` 把不同模態永遠分開儲存，不做對齊

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：跨模態檢索與對齊依賴共享語意空間，讓不同模態可被共同比較。

其餘選項為何錯：
- `A`：只增加單一模態資料量不會自動形成跨模態對齊。
- `B`：固定規則映射缺乏彈性與泛化能力。
- `D`：完全分開儲存無法支撐跨模態相似度計算。

補強知識點：
- 理解多模態檢索的關鍵不是資料量，而是 representation alignment。
- 『一句話找圖片』通常對應 shared embedding space。

回看來源：
- sources/official-corpus.md｜L21104 多模態應用
- sources/scope-weight-map.md｜L21104 多模態人工智慧應用

</details>

## 今日必補知識點

- Early fusion 與 late fusion 的分界要靠『整合發生在何時』來記，回看 [sources](../sources/) 內對應文件。
- 看到輸入階段整合就先選 early fusion，回看 [sources](../sources/) 內對應文件。
- 跨模態整合常見關鍵字：attention、alignment、Transformer，回看 [sources](../sources/) 內對應文件。
- 不要把單模態最佳模型直接套成多模態答案，回看 [sources](../sources/) 內對應文件。
- 多模態系統除了準確率，也要看可用性與魯棒性，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
