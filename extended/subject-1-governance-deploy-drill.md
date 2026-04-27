# 科目 1 加練｜治理與部署補強

- 科目：`1`
- 優先級：`A`
- 優先級摘要：`A=4 / B=0 / C=0`
- 來源層級：`official-derived`
- 焦點：`PII、red teaming、人工覆核、可觀測性`
- 題數：`8` 題
- 建議加做時機：`建議在 Day 07、Day 09、Day 18 後加做`
- 作答單：[開啟](../attempts/subject-1-governance-deploy-drill-attempt.md)
- 批改報告：[開啟](../reports/subject-1-governance-deploy-drill-report.md)
- 批改指令：`python .\score_attempt.py --drill subject-1-governance-deploy-drill`
- 使用方式：先做題，再展開 `<details>` 看答案與排錯理由。

## 題源對照

- sources/official-corpus.md｜AI 風險管理與合規
- sources/scope-weight-map.md｜L21203 AI 風險管理
- sources/official-corpus.md｜生成式 AI 風險與治理
- sources/official-corpus.md｜AI 風險治理與責任

## 題目

### 題 1｜`L21203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若要把客服紀錄送到外部 LLM 服務分析，但內容含姓名、電話、身分證等資訊，最先該補哪個控管？

- `A` 直接全量送出，事後再刪紀錄
- `B` 只調整提示詞，不處理原資料
- `C` 只在輸出端檢查髒話與敏感字
- `D` 先做去識別化或 PII masking 再送入模型

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：個資風險主要來自原始輸入外流，因此前處理去識別化是第一道關卡。

其餘選項為何錯：
- `A`：事後刪紀錄無法回收已外送的敏感資料。
- `B`：提示詞無法替代資料遮罩。
- `C`：只檢查輸出忽略了輸入外送風險。

補強知識點：
- PII masking 是外部模型接入前的高頻治理題。
- 輸入風險與輸出風險要分開看。

回看來源：
- sources/official-corpus.md｜AI 風險管理與合規
- sources/scope-weight-map.md｜L21203 AI 風險管理

</details>

### 題 2｜`L21203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

企業想把內部案例交給第三方生成式 AI 做摘要。若你要先降個資風險，最優先的作法是什麼？

- `A` 只在輸出端檢查髒話與敏感字
- `B` 先做去識別化或 PII masking 再送入模型
- `C` 直接全量送出，事後再刪紀錄
- `D` 只調整提示詞，不處理原資料

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：個資風險主要來自原始輸入外流，因此前處理去識別化是第一道關卡。

其餘選項為何錯：
- `A`：只檢查輸出忽略了輸入外送風險。
- `C`：事後刪紀錄無法回收已外送的敏感資料。
- `D`：提示詞無法替代資料遮罩。

補強知識點：
- PII masking 是外部模型接入前的高頻治理題。
- 輸入風險與輸出風險要分開看。

回看來源：
- sources/official-corpus.md｜AI 風險管理與合規
- sources/scope-weight-map.md｜L21203 AI 風險管理

</details>

### 題 3｜`L21203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若企業擔心內部助理上線後遭提示注入、越獄或惡意繞規，正式發布前最值得先做什麼？

- `A` 只看平均回應速度
- `B` 只檢查 UI 顏色是否一致
- `C` 只在上線後等使用者回報
- `D` 進行 red teaming 與對抗式提示測試

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：對抗式測試能提早暴露越獄、洩漏與不當回應風險。

其餘選項為何錯：
- `A`：速度不是安全健壯性的主指標。
- `B`：UI 一致性與模型安全是不同層面。
- `C`：完全等上線後再發現，風險成本更高。

補強知識點：
- red teaming 常用於高風險 LLM 上線前檢查。
- 安全評估不只看 accuracy。

回看來源：
- sources/official-corpus.md｜生成式 AI 風險與治理
- sources/scope-weight-map.md｜L21203 AI 風險管理

</details>

### 題 4｜`L21203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

你準備把生成式 AI 服務開給大量員工使用。若要在上線前先找出安全弱點，最合理的測試方式為何？

- `A` 只在上線後等使用者回報
- `B` 進行 red teaming 與對抗式提示測試
- `C` 只看平均回應速度
- `D` 只檢查 UI 顏色是否一致

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：對抗式測試能提早暴露越獄、洩漏與不當回應風險。

其餘選項為何錯：
- `A`：完全等上線後再發現，風險成本更高。
- `C`：速度不是安全健壯性的主指標。
- `D`：UI 一致性與模型安全是不同層面。

補強知識點：
- red teaming 常用於高風險 LLM 上線前檢查。
- 安全評估不只看 accuracy。

回看來源：
- sources/official-corpus.md｜生成式 AI 風險與治理
- sources/scope-weight-map.md｜L21203 AI 風險管理

</details>

### 題 5｜`L21203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若 AI 輸出會影響授信、醫療建議或法務判斷，最合理的決策流程安排為何？

- `A` 把所有風險寫進免責聲明即可
- `B` 保留人工覆核與最終裁量權
- `C` 只要模型分數夠高就完全自動決策
- `D` 只做一次 demo 後就直接去人工

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：高風險場景通常需要 human-in-the-loop 來降低誤判與責任風險。

其餘選項為何錯：
- `A`：免責聲明不能替代實質控管。
- `C`：高分模型也可能在特殊案例失準。
- `D`：demo 不能取代持續治理與覆核。

補強知識點：
- high-impact use case 常優先想到人工覆核。
- human-in-the-loop 是治理題高頻關鍵字。

回看來源：
- sources/official-corpus.md｜AI 風險治理與責任
- sources/scope-weight-map.md｜L21203 AI 風險管理

</details>

### 題 6｜`L21203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

在高影響決策場景中，企業若要使用 AI 輔助而非放大風險，最應保留哪個機制？

- `A` 把所有風險寫進免責聲明即可
- `B` 保留人工覆核與最終裁量權
- `C` 只要模型分數夠高就完全自動決策
- `D` 只做一次 demo 後就直接去人工

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：高風險場景通常需要 human-in-the-loop 來降低誤判與責任風險。

其餘選項為何錯：
- `A`：免責聲明不能替代實質控管。
- `C`：高分模型也可能在特殊案例失準。
- `D`：demo 不能取代持續治理與覆核。

補強知識點：
- high-impact use case 常優先想到人工覆核。
- human-in-the-loop 是治理題高頻關鍵字。

回看來源：
- sources/official-corpus.md｜AI 風險治理與責任
- sources/scope-weight-map.md｜L21203 AI 風險管理

</details>

### 題 7｜`L21302`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若生成式 AI 服務已上線，為了盡早發現品質退化與系統異常，監控指標最不應只看哪一個單一維度？

- `A` 上線後要同時看品質、延遲、錯誤率與 fallback rate
- `B` 只看平均延遲即可
- `C` 只看 GPU 使用率即可
- `D` 只看登入人數即可

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：可觀測性要同時涵蓋服務穩定、輸出品質與降級行為，而不是只盯單一系統指標。

其餘選項為何錯：
- `B`：平均延遲無法代表輸出品質與降級情況。
- `C`：GPU 使用率是資源資訊，不足以涵蓋體驗與品質。
- `D`：登入人數更不是模型品質指標。

補強知識點：
- LLM/MLOps 監控要同時看系統與內容品質。
- fallback rate 是實務上很有用的風險訊號。

回看來源：
- sources/official-corpus.md｜系統集成與部署監控
- sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署

</details>

### 題 8｜`L21302`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

團隊說只要看平均延遲就好，不必再看錯誤率、fallback 比例或品質抽查。這個觀念最主要錯在哪裡？

- `A` 只看 GPU 使用率即可
- `B` 只看登入人數即可
- `C` 上線後要同時看品質、延遲、錯誤率與 fallback rate
- `D` 只看平均延遲即可

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：可觀測性要同時涵蓋服務穩定、輸出品質與降級行為，而不是只盯單一系統指標。

其餘選項為何錯：
- `A`：GPU 使用率是資源資訊，不足以涵蓋體驗與品質。
- `B`：登入人數更不是模型品質指標。
- `D`：平均延遲無法代表輸出品質與降級情況。

補強知識點：
- LLM/MLOps 監控要同時看系統與內容品質。
- fallback rate 是實務上很有用的風險訊號。

回看來源：
- sources/official-corpus.md｜系統集成與部署監控
- sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署

</details>

## 本組必補

- PII masking 是外部模型接入前的高頻治理題
- 輸入風險與輸出風險要分開看
- red teaming 常用於高風險 LLM 上線前檢查
- 安全評估不只看 accuracy
- high-impact use case 常優先想到人工覆核
- human-in-the-loop 是治理題高頻關鍵字

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
