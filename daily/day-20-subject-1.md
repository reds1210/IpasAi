# Day 20｜科目 1 反向題單

- 今日焦點：`最終過線題單`
- 題量：`12` 題
- 建議方式：先以 60–75 分鐘完成第一輪，再展開解析。｜優先級 A｜先刷這份，對過線最有幫助。
- 來源對照：
  - [official-corpus.md](../sources/official-corpus.md)
  - [scope-weight-map.md](../sources/scope-weight-map.md)
  - [question-source-map.md](../sources/question-source-map.md)
  - [question-patterns.md](../sources/question-patterns.md)
  - [book-bridge.md](../sources/book-bridge.md)

## 今日題目

### 題 1｜`L21103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

檢索增強生成（RAG）最主要想解決大型語言模型的哪一類問題？

- `A` 讓模型完全不需要任何外部資料
- `B` 讓模型只依隨機生成內容作答
- `C` 把所有回應限制為固定規則模板
- `D` 降低知識過時與幻覺風險

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：RAG 透過外部檢索補入最新或可信文件，能降低知識過時與幻覺。

其餘選項為何錯：
- `A`：RAG 的目的正是引入外部知識，而不是移除外部資料。
- `B`：隨機生成不會提升正確性，反而增加不穩定性。
- `C`：固定模板會降低表達能力，也無法解決知識更新問題。

補強知識點：
- 理解 RAG 的核心價值：檢索可信內容再生成。
- 區分『更新知識』與『重訓模型』兩條不同路線。

回看來源：
- sources/official-corpus.md｜評鑑範圍含生成式 AI 技術與應用
- sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用

</details>

### 題 2｜`L21103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

法務團隊抱怨內部生成式 AI 會引用過時資料並偶爾胡亂編造答案，若先不重訓模型，最合理的補強方向為何？

- `A` 降低知識過時與幻覺風險
- `B` 讓模型完全不需要任何外部資料
- `C` 讓模型只依隨機生成內容作答
- `D` 把所有回應限制為固定規則模板

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：RAG 透過外部檢索補入最新或可信文件，能降低知識過時與幻覺。

其餘選項為何錯：
- `B`：RAG 的目的正是引入外部知識，而不是移除外部資料。
- `C`：隨機生成不會提升正確性，反而增加不穩定性。
- `D`：固定模板會降低表達能力，也無法解決知識更新問題。

補強知識點：
- 理解 RAG 的核心價值：檢索可信內容再生成。
- 區分『更新知識』與『重訓模型』兩條不同路線。

回看來源：
- sources/official-corpus.md｜評鑑範圍含生成式 AI 技術與應用
- sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用

</details>

### 題 3｜`L21203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

在 AI 治理脈絡下，透明性（Transparency）通常指什麼？

- `A` 系統只要速度夠快就算透明
- `B` 只要模型有商業價值，就不需要說明原理
- `C` 決策流程與依據具可理解性與可追溯性
- `D` 所有模型都必須完全開源

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：透明性重點在可解釋與可追溯，不等於所有細節都要公開原始碼。

其餘選項為何錯：
- `A`：速度快與是否透明是不同維度。
- `B`：有商業價值不代表可以忽略說明責任。
- `D`：開源與否是治理手段選項，不是透明性的唯一條件。

補強知識點：
- 記住 transparency、explainability、traceability 是一組常連動的治理概念。
- 不要把『透明』誤解成『全部開源』。

回看來源：
- sources/official-corpus.md｜L21203 AI 風險管理與治理
- sources/scope-weight-map.md｜L21203 AI 風險管理

</details>

### 題 4｜`L21203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若企業要讓審查單位能追蹤 AI 如何得出決策、使用何種資料與規則，最符合哪項治理原則？

- `A` 只要模型有商業價值，就不需要說明原理
- `B` 決策流程與依據具可理解性與可追溯性
- `C` 所有模型都必須完全開源
- `D` 系統只要速度夠快就算透明

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：透明性重點在可解釋與可追溯，不等於所有細節都要公開原始碼。

其餘選項為何錯：
- `A`：有商業價值不代表可以忽略說明責任。
- `C`：開源與否是治理手段選項，不是透明性的唯一條件。
- `D`：速度快與是否透明是不同維度。

補強知識點：
- 記住 transparency、explainability、traceability 是一組常連動的治理概念。
- 不要把『透明』誤解成『全部開源』。

回看來源：
- sources/official-corpus.md｜L21203 AI 風險管理與治理
- sources/scope-weight-map.md｜L21203 AI 風險管理

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

### 題 7｜`L21202`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

AI 導入規劃時，若企業需求仍不清楚，最合理的第一步為何？

- `A` 直接選定最熱門模型並開始訓練
- `B` 先採購硬體與軟體，再回頭補需求
- `C` 先把所有流程完全自動化，不留人工審核
- `D` 先做需求分析與利害關係人對齊

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：需求不清時，先對齊目標、使用者、輸入輸出與責任邊界，才能做後續架構規劃。

其餘選項為何錯：
- `A`：先選模型容易造成技術與問題錯配。
- `B`：先採購資源可能造成閒置或規格錯誤。
- `C`：未完成需求與風險分析前，不應貿然全面自動化。

補強知識點：
- 規劃先於建置，需求先於選型。
- 題目提到多部門分歧時，優先想到需求澄清與 stakeholder alignment。

回看來源：
- sources/official-corpus.md｜L21202 AI 導入規劃
- sources/scope-weight-map.md｜L21202 AI 導入規劃

</details>

### 題 8｜`L21202`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

行銷、客服、法務各自想要不同 AI 功能，但都還沒定義輸入、輸出與責任邊界。你若先做一件事，應優先做什麼？

- `A` 先採購硬體與軟體，再回頭補需求
- `B` 先把所有流程完全自動化，不留人工審核
- `C` 先做需求分析與利害關係人對齊
- `D` 直接選定最熱門模型並開始訓練

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：需求不清時，先對齊目標、使用者、輸入輸出與責任邊界，才能做後續架構規劃。

其餘選項為何錯：
- `A`：先採購資源可能造成閒置或規格錯誤。
- `B`：未完成需求與風險分析前，不應貿然全面自動化。
- `D`：先選模型容易造成技術與問題錯配。

補強知識點：
- 規劃先於建置，需求先於選型。
- 題目提到多部門分歧時，優先想到需求澄清與 stakeholder alignment。

回看來源：
- sources/official-corpus.md｜L21202 AI 導入規劃
- sources/scope-weight-map.md｜L21202 AI 導入規劃

</details>

### 題 9｜`L21302`｜難度：`中`
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

### 題 10｜`L21302`｜難度：`中`
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

### 題 11｜`L21302`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若生成式 AI 服務短暫失效，但業務流程不能中斷，最合理的架構規劃是什麼？

- `A` 刪掉人工流程，避免回退複雜
- `B` 設計 fail-safe 或 fallback 流程，必要時切回規則或人工模式
- `C` 服務失效時直接中斷整個業務流程
- `D` 把所有請求不加判斷地重試到無限次

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：高可用系統要能在模型不可用時降級運行，而不是把整個流程綁死在單一模型上。

其餘選項為何錯：
- `A`：拿掉人工流程會失去最後保險。
- `C`：直接中斷流程會放大營運損失。
- `D`：無限重試可能造成雪崩與資源耗盡。

補強知識點：
- 部署與可靠度題常考 fallback、degradation、manual override。
- 模型不是唯一真理來源，流程設計要留後路。

回看來源：
- sources/official-corpus.md｜系統穩定性與可用性
- sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署

</details>

### 題 12｜`L21302`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

客服摘要服務偶爾會 timeout，但客服工作不能停止。若要先從系統設計面降低衝擊，較好的方案為何？

- `A` 把所有請求不加判斷地重試到無限次
- `B` 刪掉人工流程，避免回退複雜
- `C` 設計 fail-safe 或 fallback 流程，必要時切回規則或人工模式
- `D` 服務失效時直接中斷整個業務流程

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：高可用系統要能在模型不可用時降級運行，而不是把整個流程綁死在單一模型上。

其餘選項為何錯：
- `A`：無限重試可能造成雪崩與資源耗盡。
- `B`：拿掉人工流程會失去最後保險。
- `D`：直接中斷流程會放大營運損失。

補強知識點：
- 部署與可靠度題常考 fallback、degradation、manual override。
- 模型不是唯一真理來源，流程設計要留後路。

回看來源：
- sources/official-corpus.md｜系統穩定性與可用性
- sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署

</details>

## 今日必補知識點

- 理解 RAG 的核心價值：檢索可信內容再生成，回看 [sources](../sources/) 內對應文件。
- 區分『更新知識』與『重訓模型』兩條不同路線，回看 [sources](../sources/) 內對應文件。
- 記住 transparency、explainability、traceability 是一組常連動的治理概念，回看 [sources](../sources/) 內對應文件。
- 不要把『透明』誤解成『全部開源』，回看 [sources](../sources/) 內對應文件。
- 導入評估的第一關通常是資料、目標、指標，而不是先追模型，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s1d3_rag_core, s1d7_transparency, s1d5_data_readiness, s1d9_integration_testing, s1d14_fail_safe
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
