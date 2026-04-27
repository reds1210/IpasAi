# Day 16｜科目 1 反向題單

- 今日焦點：`第二輪半模擬`
- 題量：`10` 題
- 建議方式：先以 60–75 分鐘完成第一輪，再展開解析。｜優先級 A｜先刷這份，對過線最有幫助。
- 來源對照：
  - [official-corpus.md](../sources/official-corpus.md)
  - [scope-weight-map.md](../sources/scope-weight-map.md)
  - [question-source-map.md](../sources/question-source-map.md)
  - [question-patterns.md](../sources/question-patterns.md)
  - [book-bridge.md](../sources/book-bridge.md)

## 今日題目

### 題 1｜`L21201`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

在全面上線前，哪一種做法最適合作為 AI 導入評估的中間步驟？

- `A` 先做 PoC 或小規模試點驗證
- `B` 直接全公司同步切換到新系統
- `C` 先簽五年長約再決定需求
- `D` 跳過驗證直接把模型接到核心交易流程

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：PoC 能以較低風險驗證資料、流程、指標與使用者接受度。

其餘選項為何錯：
- `B`：直接全量切換缺乏風險緩衝。
- `C`：先綁長約會鎖死後續調整空間。
- `D`：跳過驗證導致上線風險與責任暴增。

補強知識點：
- 評估階段的關鍵詞：PoC、pilot、low-risk validation。
- 先小範圍驗證，再決定是否擴大部署。

回看來源：
- sources/official-corpus.md｜L21201 AI 導入評估
- sources/scope-weight-map.md｜L21201 AI 導入評估

</details>

### 題 2｜`L21201`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

企業對生成式 AI 專案仍不確定內部流程能否承接，若不想直接大規模上線，最合適的下一步是什麼？

- `A` 直接全公司同步切換到新系統
- `B` 先簽五年長約再決定需求
- `C` 跳過驗證直接把模型接到核心交易流程
- `D` 先做 PoC 或小規模試點驗證

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：PoC 能以較低風險驗證資料、流程、指標與使用者接受度。

其餘選項為何錯：
- `A`：直接全量切換缺乏風險緩衝。
- `B`：先綁長約會鎖死後續調整空間。
- `C`：跳過驗證導致上線風險與責任暴增。

補強知識點：
- 評估階段的關鍵詞：PoC、pilot、low-risk validation。
- 先小範圍驗證，再決定是否擴大部署。

回看來源：
- sources/official-corpus.md｜L21201 AI 導入評估
- sources/scope-weight-map.md｜L21201 AI 導入評估

</details>

### 題 3｜`L21203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

供應鏈攻擊（Supply Chain Attack）對企業內部 AI 系統的主要風險來源為何？

- `A` 供應鏈攻擊只會發生在硬體層
- `B` 只要在內網使用 AI，就沒有供應鏈問題
- `C` 供應鏈攻擊與開源套件、模型權重無關
- `D` 第三方模型或資料可能被植入惡意內容

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：AI 系統常依賴外部模型、資料與套件，因此第三方來源被污染會直接影響內部系統安全。

其餘選項為何錯：
- `A`：供應鏈問題不只在硬體，也可能在軟體、模型與資料。
- `B`：內網部署仍可能引入受污染的外部元件。
- `C`：開源套件與模型權重正是常見供應鏈入口。

補強知識點：
- 把『供應鏈』理解為所有外部依賴，不只是設備採購。
- 對第三方模型與資料做 provenance 檢查是基本功。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現供應鏈攻擊
- sources/scope-weight-map.md｜L21203 AI 風險管理

</details>

### 題 4｜`L21203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

企業大量依賴第三方開源模型、套件與資料集。若要描述其最核心的供應鏈風險，下列哪項最合理？

- `A` 只要在內網使用 AI，就沒有供應鏈問題
- `B` 供應鏈攻擊與開源套件、模型權重無關
- `C` 第三方模型或資料可能被植入惡意內容
- `D` 供應鏈攻擊只會發生在硬體層

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：AI 系統常依賴外部模型、資料與套件，因此第三方來源被污染會直接影響內部系統安全。

其餘選項為何錯：
- `A`：內網部署仍可能引入受污染的外部元件。
- `B`：開源套件與模型權重正是常見供應鏈入口。
- `D`：供應鏈問題不只在硬體，也可能在軟體、模型與資料。

補強知識點：
- 把『供應鏈』理解為所有外部依賴，不只是設備採購。
- 對第三方模型與資料做 provenance 檢查是基本功。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現供應鏈攻擊
- sources/scope-weight-map.md｜L21203 AI 風險管理

</details>

### 題 5｜`L21302`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

AI 模型即將進入系統整合測試階段，下列哪項驗證最應優先執行？

- `A` 只審閱文件版面是否美觀
- `B` 模型服務與資料平台、前後端介面的資料格式與流程是否協同正常
- `C` 只再看一次訓練集準確率
- `D` 只檢查 commit message 是否符合規範

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：整合測試要先確認模組在真實流程中能正常交換資料與協同運作。

其餘選項為何錯：
- `A`：文件格式不會驗證流程是否可用。
- `C`：訓練集表現不代表系統整合無誤。
- `D`：程式碼規範重要，但不是整合測試第一優先。

補強知識點：
- integration testing 看的是流程與介面，不是單一模型分數。
- 題目提到資料平台、前後端時，先找 interface / schema / workflow consistency。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現整合測試
- sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署

</details>

### 題 6｜`L21302`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

模型在驗證集表現不差，但即將接到前後端與資料平台。若只能先做一項整合檢查，最應先確認什麼？

- `A` 只檢查 commit message 是否符合規範
- `B` 只審閱文件版面是否美觀
- `C` 模型服務與資料平台、前後端介面的資料格式與流程是否協同正常
- `D` 只再看一次訓練集準確率

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：整合測試要先確認模組在真實流程中能正常交換資料與協同運作。

其餘選項為何錯：
- `A`：程式碼規範重要，但不是整合測試第一優先。
- `B`：文件格式不會驗證流程是否可用。
- `D`：訓練集表現不代表系統整合無誤。

補強知識點：
- integration testing 看的是流程與介面，不是單一模型分數。
- 題目提到資料平台、前後端時，先找 interface / schema / workflow consistency。

回看來源：
- sources/official-corpus.md｜114.09 樣題出現整合測試
- sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署

</details>

### 題 7｜`L21101`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若任務是把輸入序列轉成另一段輸出序列，例如翻譯或摘要，最合理的模型方向為何？

- `A` 只做關鍵字頻率統計
- `B` 只做圖像分類
- `C` 只做實體名稱標註（NER）
- `D` 序列到序列（Seq2Seq）模型

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：Seq2Seq 適合處理輸入序列到輸出序列的映射，例如翻譯與摘要。

其餘選項為何錯：
- `A`：關鍵字頻率統計不會生成新的序列。
- `B`：圖像分類處理的是整張圖的類別。
- `C`：NER 是序列標註，不等於生成另一段序列。

補強知識點：
- 分清 classification、sequence labeling、sequence generation。
- 看到『翻譯、摘要、改寫』時，優先想 Seq2Seq。

回看來源：
- sources/official-corpus.md｜正式題出現 Seq2Seq
- sources/scope-weight-map.md｜L21101 自然語言處理技術與應用

</details>

### 題 8｜`L21101`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若系統要把輸入文字轉成語意等價的另一段文字，例如自動翻譯或摘要，最合理的模型方向為何？

- `A` 只做實體名稱標註（NER）
- `B` 序列到序列（Seq2Seq）模型
- `C` 只做關鍵字頻率統計
- `D` 只做圖像分類

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：Seq2Seq 適合處理輸入序列到輸出序列的映射，例如翻譯與摘要。

其餘選項為何錯：
- `A`：NER 是序列標註，不等於生成另一段序列。
- `C`：關鍵字頻率統計不會生成新的序列。
- `D`：圖像分類處理的是整張圖的類別。

補強知識點：
- 分清 classification、sequence labeling、sequence generation。
- 看到『翻譯、摘要、改寫』時，優先想 Seq2Seq。

回看來源：
- sources/official-corpus.md｜正式題出現 Seq2Seq
- sources/scope-weight-map.md｜L21101 自然語言處理技術與應用

</details>

### 題 9｜`L21104`｜難度：`難`
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

### 題 10｜`L21104`｜難度：`難`
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

## 今日必補知識點

- 評估階段的關鍵詞：PoC、pilot、low-risk validation，回看 [sources](../sources/) 內對應文件。
- 先小範圍驗證，再決定是否擴大部署，回看 [sources](../sources/) 內對應文件。
- 把『供應鏈』理解為所有外部依賴，不只是設備採購，回看 [sources](../sources/) 內對應文件。
- 對第三方模型與資料做 provenance 檢查是基本功，回看 [sources](../sources/) 內對應文件。
- integration testing 看的是流程與介面，不是單一模型分數，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s1d5_poc, s1d7_supply_chain, s1d9_integration_testing, s1d10_seq2seq
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
