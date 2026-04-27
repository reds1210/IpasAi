# 科目 1 加練｜導入評估、部署與治理整合情境

- 科目：`1`
- 優先級：`B`
- 優先級摘要：`A=0 / B=4 / C=0`
- 來源層級：`official-derived`
- 焦點：`PoC 到上線、KPI、資料漂移、監控、PII 與回滾策略`
- 題數：`8` 題
- 建議加做時機：`Day 09、Day 15、Day 20 後加做`
- 作答單：[開啟](../attempts/subject-1-cross-scenario-integration-drill-attempt.md)
- 批改報告：[開啟](../reports/subject-1-cross-scenario-integration-drill-report.md)
- 批改指令：`python .\score_attempt.py --drill subject-1-cross-scenario-integration-drill`
- 使用方式：先做題，再展開 `<details>` 看答案與排錯理由。

## 題源對照

- sources/question-source-map.md｜中級學習指引科目 1
- sources/question-patterns.md｜情境整合題模板
- sources/question-source-map.md｜科目 1 公告試題
- sources/official-corpus.md｜部署與監控

## 題目

### 題 1｜`L21301`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

企業做完 AI PoC 後，準備決定是否進入正式導入。下列哪個指標最適合作為 PoC 是否值得擴大的第一層依據？

- `A` 只看團隊是否會寫 Python 即可
- `B` 同時檢查業務 KPI、資料可取得性、部署成本與風險
- `C` 只要準確率高於 90% 就應立刻全面上線
- `D` 只看 GPU 採購成本即可

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：PoC 是否擴大要看業務價值、資料與部署可行性、治理風險，不是單一模型分數。

其餘選項為何錯：
- `A`：開發技能也不是唯一決策基準。
- `C`：高準確率不代表商業與治理上可落地。
- `D`：硬體成本只是其中一項，不足以單獨決策。

補強知識點：
- 導入評估不是只看模型分數。
- PoC 到 production 要綜合 KPI、成本、風險與流程。

回看來源：
- sources/question-source-map.md｜中級學習指引科目 1
- sources/question-patterns.md｜情境整合題模板

</details>

### 題 2｜`L21301`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

如果主管只看模型準確率就想推全公司上線，作為 AI 導入規劃者，下一步最該補的是哪類判斷？

- `A` 只看團隊是否會寫 Python 即可
- `B` 同時檢查業務 KPI、資料可取得性、部署成本與風險
- `C` 只要準確率高於 90% 就應立刻全面上線
- `D` 只看 GPU 採購成本即可

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：PoC 是否擴大要看業務價值、資料與部署可行性、治理風險，不是單一模型分數。

其餘選項為何錯：
- `A`：開發技能也不是唯一決策基準。
- `C`：高準確率不代表商業與治理上可落地。
- `D`：硬體成本只是其中一項，不足以單獨決策。

補強知識點：
- 導入評估不是只看模型分數。
- PoC 到 production 要綜合 KPI、成本、風險與流程。

回看來源：
- sources/question-source-map.md｜中級學習指引科目 1
- sources/question-patterns.md｜情境整合題模板

</details>

### 題 3｜`L21302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

上線三個月後，模型整體準確率逐步下滑，但服務沒有中斷。這種情況最應先懷疑哪類問題？

- `A` 資料漂移或使用情境改變，需要檢查輸入分布與監控指標
- `B` 先把 CPU 升級即可
- `C` 這一定是前端按鈕配色問題
- `D` 只要把 learning rate 調低就會恢復

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：分數逐步退化通常先想到資料漂移或情境改變，應檢查輸入分布、PSI 或其他監控指標。

其餘選項為何錯：
- `B`：硬體升級不會直接修復資料漂移。
- `C`：前端配色與模型退化無關。
- `D`：學習率屬於訓練設定，無法直接解釋上線後輸入分布改變。

補強知識點：
- 資料漂移是上線監控高頻題。
- 區分系統故障與模型效能退化。

回看來源：
- sources/question-source-map.md｜114 年第二梯次科目 1 公告試題
- sources/official-corpus.md｜部署與監控主題

</details>

### 題 4｜`L21302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若推薦模型最近分數慢慢變差，不是突然壞掉，而是隨時間退化，監控上第一個應追的是什麼？

- `A` 資料漂移或使用情境改變，需要檢查輸入分布與監控指標
- `B` 先把 CPU 升級即可
- `C` 這一定是前端按鈕配色問題
- `D` 只要把 learning rate 調低就會恢復

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：分數逐步退化通常先想到資料漂移或情境改變，應檢查輸入分布、PSI 或其他監控指標。

其餘選項為何錯：
- `B`：硬體升級不會直接修復資料漂移。
- `C`：前端配色與模型退化無關。
- `D`：學習率屬於訓練設定，無法直接解釋上線後輸入分布改變。

補強知識點：
- 資料漂移是上線監控高頻題。
- 區分系統故障與模型效能退化。

回看來源：
- sources/question-source-map.md｜114 年第二梯次科目 1 公告試題
- sources/official-corpus.md｜部署與監控主題

</details>

### 題 5｜`L21203`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

企業內部問答機器人可能在回答中帶出真實姓名、電話與訂單資訊。若只能先做一層緊急防護，最務實的第一步是什麼？

- `A` 只改 UI 文案即可
- `B` 先做輸入/輸出端的個資偵測與遮罩，再補資料與權限治理
- `C` 完全關閉日誌，這樣就沒有個資風險
- `D` 把模型參數放大就能避免洩漏

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：緊急防線通常先放在輸入與輸出端的偵測/遮罩，降低立即外洩風險，再往資料與權限治理補強。

其餘選項為何錯：
- `A`：UI 文案不能替代實際防護措施。
- `C`：不記錄日誌會讓稽核與追查更困難。
- `D`：模型變大不等於不會洩漏個資。

補強知識點：
- 區分立即風險緩解與長期治理。
- PII 風險通常先做 I/O guardrail。

回看來源：
- sources/question-source-map.md｜114 年第二梯次科目 1 公告試題
- sources/question-patterns.md｜風險治理題模板

</details>

### 題 6｜`L21203`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

當生成式客服系統疑似會吐出個資時，哪個控制點最適合優先落地，作為正式上線前的最低防線？

- `A` 把模型參數放大就能避免洩漏
- `B` 只改 UI 文案即可
- `C` 先做輸入/輸出端的個資偵測與遮罩，再補資料與權限治理
- `D` 完全關閉日誌，這樣就沒有個資風險

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：緊急防線通常先放在輸入與輸出端的偵測/遮罩，降低立即外洩風險，再往資料與權限治理補強。

其餘選項為何錯：
- `A`：模型變大不等於不會洩漏個資。
- `B`：UI 文案不能替代實際防護措施。
- `D`：不記錄日誌會讓稽核與追查更困難。

補強知識點：
- 區分立即風險緩解與長期治理。
- PII 風險通常先做 I/O guardrail。

回看來源：
- sources/question-source-map.md｜114 年第二梯次科目 1 公告試題
- sources/question-patterns.md｜風險治理題模板

</details>

### 題 7｜`L21302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

新模型上線後，若關鍵 KPI 明顯下滑且客訴增加，哪個處置最符合穩健部署策略？

- `A` 繼續全量上線觀察一週再說
- `B` 只調整簡報數字讓 KPI 看起來正常
- `C` 啟動回滾或切回前版模型，同時保留監控與事故紀錄
- `D` 先刪除所有監控紀錄，避免留下負面證據

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：穩健部署重點是可回滾與可追溯。當 KPI 明顯惡化，應先切回穩定版本，再分析根因。

其餘選項為何錯：
- `A`：已經出現明顯負面影響時，不應放任全量風險擴大。
- `B`：美化數字不是工程處置。
- `D`：刪除紀錄會破壞事故分析與治理。

補強知識點：
- 上線策略要包含 rollback。
- 監控、灰度發布、回滾要連成一套。

回看來源：
- sources/question-source-map.md｜中級學習指引科目 1
- sources/question-patterns.md｜部署治理整合題

</details>

### 題 8｜`L21302`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

你在灰度發布後發現新模型造成轉換率下降。下列哪一步最務實，且能控制風險？

- `A` 繼續全量上線觀察一週再說
- `B` 只調整簡報數字讓 KPI 看起來正常
- `C` 啟動回滾或切回前版模型，同時保留監控與事故紀錄
- `D` 先刪除所有監控紀錄，避免留下負面證據

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：穩健部署重點是可回滾與可追溯。當 KPI 明顯惡化，應先切回穩定版本，再分析根因。

其餘選項為何錯：
- `A`：已經出現明顯負面影響時，不應放任全量風險擴大。
- `B`：美化數字不是工程處置。
- `D`：刪除紀錄會破壞事故分析與治理。

補強知識點：
- 上線策略要包含 rollback。
- 監控、灰度發布、回滾要連成一套。

回看來源：
- sources/question-source-map.md｜中級學習指引科目 1
- sources/question-patterns.md｜部署治理整合題

</details>

## 本組必補

- 導入評估不是只看模型分數
- PoC 到 production 要綜合 KPI、成本、風險與流程
- 資料漂移是上線監控高頻題
- 區分系統故障與模型效能退化
- 區分立即風險緩解與長期治理
- PII 風險通常先做 I/O guardrail

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
