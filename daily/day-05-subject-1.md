# Day 05｜科目 1 反向題單

- 今日焦點：`AI 導入評估`
- 題量：`8` 題
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

### 題 2｜`L21201`｜難度：`中`
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

### 題 3｜`L21201`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

在 AI 導入評估中，成本效益分析的主要目的為何？

- `A` 確認預期效益是否足以支持建置與維運成本
- `B` 只比較模型參數量大小
- `C` 只看供應商簡報中的準確率最高值
- `D` 只以技術新穎程度做決策

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：導入評估不能只看技術能力，還要看 ROI、維運成本、風險與可持續性。

其餘選項為何錯：
- `B`：參數量不是商業價值的直接替代指標。
- `C`：單次準確率展示常忽略資料條件與維運成本。
- `D`：技術新穎不等於商業上最值得導入。

補強知識點：
- 評估階段要把效能、成本、風險、回收期一起看。
- ROI 與 TCO 是常見管理層判斷語言。

回看來源：
- sources/official-corpus.md｜AI 導入評估範圍含成本效益分析
- sources/scope-weight-map.md｜L21201 AI 導入評估

</details>

### 題 4｜`L21201`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若兩種解決方案都做得到，但一種建置成本高且維運複雜，另一種效能稍低但回收期短，評估階段最該比較的是什麼？

- `A` 只比較模型參數量大小
- `B` 只看供應商簡報中的準確率最高值
- `C` 只以技術新穎程度做決策
- `D` 確認預期效益是否足以支持建置與維運成本

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：導入評估不能只看技術能力，還要看 ROI、維運成本、風險與可持續性。

其餘選項為何錯：
- `A`：參數量不是商業價值的直接替代指標。
- `B`：單次準確率展示常忽略資料條件與維運成本。
- `C`：技術新穎不等於商業上最值得導入。

補強知識點：
- 評估階段要把效能、成本、風險、回收期一起看。
- ROI 與 TCO 是常見管理層判斷語言。

回看來源：
- sources/official-corpus.md｜AI 導入評估範圍含成本效益分析
- sources/scope-weight-map.md｜L21201 AI 導入評估

</details>

### 題 5｜`L21201`｜難度：`中`
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

### 題 6｜`L21201`｜難度：`中`
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

### 題 7｜`L21201`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

AI 導入評估若沒有明確 KPI，最常見的問題是什麼？

- `A` 所有資料都會自動變得不可用
- `B` 雲端成本一定會高於地端成本
- `C` 無法客觀判斷專案是否成功
- `D` 模型一定會訓練失敗

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：沒有明確 KPI，就難以衡量效益、比較方案與決定是否擴張部署。

其餘選項為何錯：
- `A`：資料可用性是另一個問題，不會因 KPI 不明自動失效。
- `B`：部署成本取決於設計與規模，不能直接由 KPI 問題推出。
- `D`：KPI 不明不代表模型一定訓練失敗，但會讓驗收標準模糊。

補強知識點：
- 把『導入目的』轉成可量化指標是評估核心。
- 常見 KPI：工時、召回率、錯誤率、處理時效、人工覆核比例。

回看來源：
- sources/official-corpus.md｜AI 導入評估與規劃均強調目標與指標
- sources/scope-weight-map.md｜L21201 AI 導入評估

</details>

### 題 8｜`L21201`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若主管只說『要導入 AI 提升效率』，卻沒有定義要縮短多少時間、降低多少錯誤率，這在評估階段最主要的缺口是什麼？

- `A` 無法客觀判斷專案是否成功
- `B` 模型一定會訓練失敗
- `C` 所有資料都會自動變得不可用
- `D` 雲端成本一定會高於地端成本

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：沒有明確 KPI，就難以衡量效益、比較方案與決定是否擴張部署。

其餘選項為何錯：
- `B`：KPI 不明不代表模型一定訓練失敗，但會讓驗收標準模糊。
- `C`：資料可用性是另一個問題，不會因 KPI 不明自動失效。
- `D`：部署成本取決於設計與規模，不能直接由 KPI 問題推出。

補強知識點：
- 把『導入目的』轉成可量化指標是評估核心。
- 常見 KPI：工時、召回率、錯誤率、處理時效、人工覆核比例。

回看來源：
- sources/official-corpus.md｜AI 導入評估與規劃均強調目標與指標
- sources/scope-weight-map.md｜L21201 AI 導入評估

</details>

## 今日必補知識點

- 導入評估的第一關通常是資料、目標、指標，而不是先追模型，回看 [sources](../sources/) 內對應文件。
- 看到『可行性』就先問資料與需求是否成立，回看 [sources](../sources/) 內對應文件。
- 評估階段要把效能、成本、風險、回收期一起看，回看 [sources](../sources/) 內對應文件。
- ROI 與 TCO 是常見管理層判斷語言，回看 [sources](../sources/) 內對應文件。
- 評估階段的關鍵詞：PoC、pilot、low-risk validation，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s1d5_data_readiness, s1d5_cost_benefit, s1d5_poc, s1d5_kpi
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
