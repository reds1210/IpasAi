# Day 09｜科目 1 反向題單

- 今日焦點：`系統整合、部署、Kubernetes、監控`
- 題量：`8` 題
- 建議方式：先以 60–75 分鐘完成第一輪，再展開解析。｜優先級 A｜先刷這份，對過線最有幫助。
- 來源對照：
  - [official-corpus.md](../sources/official-corpus.md)
  - [scope-weight-map.md](../sources/scope-weight-map.md)
  - [question-source-map.md](../sources/question-source-map.md)
  - [question-patterns.md](../sources/question-patterns.md)
  - [book-bridge.md](../sources/book-bridge.md)

## 今日題目

### 題 1｜`L21302`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

Kubernetes 在 AI 模型部署與運行中的核心角色最接近下列何者？

- `A` 直接負責所有 GPU 推論計算本身
- `B` 管理與協調模型服務的部署、擴展與運行環境
- `C` 自動幫模型做超參數調整
- `D` 提供資料倉儲與版本控管的全部功能

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：Kubernetes 主要處理容器化服務的部署、調度、擴縮與穩定運行。

其餘選項為何錯：
- `A`：Kubernetes 會調度資源，但不等於 GPU 推論演算法本身。
- `C`：超參數調整屬訓練與實驗管理，不是 Kubernetes 的核心職責。
- `D`：資料倉儲與版本控管需要其他工具配合。

補強知識點：
- Kubernetes 是 orchestration，不是 model training tool。
- 分清部署平台、實驗平台、資料平台的責任。

回看來源：
- sources/official-corpus.md｜正式題出現 Kubernetes
- sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署

</details>

### 題 2｜`L21302`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若團隊想讓模型服務能自動部署、擴縮與管理執行環境，最符合 Kubernetes 價值的描述為何？

- `A` 管理與協調模型服務的部署、擴展與運行環境
- `B` 自動幫模型做超參數調整
- `C` 提供資料倉儲與版本控管的全部功能
- `D` 直接負責所有 GPU 推論計算本身

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：Kubernetes 主要處理容器化服務的部署、調度、擴縮與穩定運行。

其餘選項為何錯：
- `B`：超參數調整屬訓練與實驗管理，不是 Kubernetes 的核心職責。
- `C`：資料倉儲與版本控管需要其他工具配合。
- `D`：Kubernetes 會調度資源，但不等於 GPU 推論演算法本身。

補強知識點：
- Kubernetes 是 orchestration，不是 model training tool。
- 分清部署平台、實驗平台、資料平台的責任。

回看來源：
- sources/official-corpus.md｜正式題出現 Kubernetes
- sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署

</details>

### 題 3｜`L21302`｜難度：`中`
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

### 題 4｜`L21302`｜難度：`中`
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

### 題 5｜`L21302`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

模型上線後，若想監控輸入特徵分布是否偏離訓練資料，哪一類指標最有代表性？

- `A` 只看 commit 次數是否增加
- `B` 資料分布漂移指標，例如 PSI（Population Stability Index）
- `C` 只看 CPU 使用率
- `D` 只看 API 回應字數長短

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：當標籤尚未回收時，先看輸入分布是否偏移，是線上監控常見做法。

其餘選項為何錯：
- `A`：commit 次數與線上資料分布無直接關係。
- `C`：CPU 使用率是系統資源指標，不是資料漂移指標。
- `D`：回應字數無法直接代表資料分布是否偏移。

補強知識點：
- 把 model drift 與 system metrics 區分開。
- PSI、KL divergence、feature distribution monitoring 是常見 drift 訊號。

回看來源：
- sources/official-corpus.md｜正式題出現 PSI 類 drift 概念
- sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署

</details>

### 題 6｜`L21302`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

若你懷疑業務資料分布已改變，導致模型精度下降，但標籤回收還很慢，最先可用哪類監控訊號判斷 drift？

- `A` 只看 commit 次數是否增加
- `B` 資料分布漂移指標，例如 PSI（Population Stability Index）
- `C` 只看 CPU 使用率
- `D` 只看 API 回應字數長短

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：當標籤尚未回收時，先看輸入分布是否偏移，是線上監控常見做法。

其餘選項為何錯：
- `A`：commit 次數與線上資料分布無直接關係。
- `C`：CPU 使用率是系統資源指標，不是資料漂移指標。
- `D`：回應字數無法直接代表資料分布是否偏移。

補強知識點：
- 把 model drift 與 system metrics 區分開。
- PSI、KL divergence、feature distribution monitoring 是常見 drift 訊號。

回看來源：
- sources/official-corpus.md｜正式題出現 PSI 類 drift 概念
- sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署

</details>

### 題 7｜`L21302`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若企業想降低新模型上線事故對全部使用者的衝擊，最適合的部署策略為何？

- `A` 只在簡報中宣告模型已準備好
- `B` 採小流量試放的 canary 或分階段部署策略
- `C` 直接 100% 切到新版本
- `D` 先停掉舊服務再部署新版本

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：canary deployment 能在有限流量下觀察風險，便於回退。

其餘選項為何錯：
- `A`：文件宣告無法取代真實流量驗證。
- `C`：直接全量切換會把風險一次擴散到所有使用者。
- `D`：先停舊服務會增加停機與失敗風險。

補強知識點：
- 部署策略要跟風險控制綁在一起理解。
- 看到『小流量、先驗證、可回退』時，優先選 canary / phased rollout。

回看來源：
- sources/official-corpus.md｜L21302 系統部署與更新管理
- sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署

</details>

### 題 8｜`L21302`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

團隊準備替換線上模型，但擔心新版本會在真實流量下出現未預期錯誤。若要先在小流量驗證，應採哪種思路？

- `A` 直接 100% 切到新版本
- `B` 先停掉舊服務再部署新版本
- `C` 只在簡報中宣告模型已準備好
- `D` 採小流量試放的 canary 或分階段部署策略

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：canary deployment 能在有限流量下觀察風險，便於回退。

其餘選項為何錯：
- `A`：直接全量切換會把風險一次擴散到所有使用者。
- `B`：先停舊服務會增加停機與失敗風險。
- `C`：文件宣告無法取代真實流量驗證。

補強知識點：
- 部署策略要跟風險控制綁在一起理解。
- 看到『小流量、先驗證、可回退』時，優先選 canary / phased rollout。

回看來源：
- sources/official-corpus.md｜L21302 系統部署與更新管理
- sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署

</details>

## 今日必補知識點

- Kubernetes 是 orchestration，不是 model training tool，回看 [sources](../sources/) 內對應文件。
- 分清部署平台、實驗平台、資料平台的責任，回看 [sources](../sources/) 內對應文件。
- integration testing 看的是流程與介面，不是單一模型分數，回看 [sources](../sources/) 內對應文件。
- 題目提到資料平台、前後端時，先找 interface / schema / workflow consistency，回看 [sources](../sources/) 內對應文件。
- 把 model drift 與 system metrics 區分開，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s1d9_kubernetes, s1d9_integration_testing, s1d9_drift_monitoring, s1d9_canary
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
