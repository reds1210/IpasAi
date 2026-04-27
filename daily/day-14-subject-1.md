# Day 14｜科目 1 反向題單

- 今日焦點：`部署事故與對抗攻擊`
- 題量：`10` 題
- 建議方式：先以 60–75 分鐘完成第一輪，再展開解析。｜優先級 A｜先刷這份，對過線最有幫助。
- 來源對照：
  - [official-corpus.md](../sources/official-corpus.md)
  - [scope-weight-map.md](../sources/scope-weight-map.md)
  - [question-source-map.md](../sources/question-source-map.md)
  - [question-patterns.md](../sources/question-patterns.md)
  - [book-bridge.md](../sources/book-bridge.md)

## 今日題目

### 題 1｜`L21203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若企業擔心模型受到惡意格式輸入或極端異常值衝擊，上線前最實務的第一層保護通常是什麼？

- `A` 加強輸入驗證與資料前處理檢查
- `B` 把所有異常輸入都直接當成正常樣本餵進模型
- `C` 只提高 GPU 數量
- `D` 只增加輸出長度上限

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：入口檢查能在模型看到資料前先過濾明顯錯誤或惡意輸入，是低成本有效的第一層防線。

其餘選項為何錯：
- `B`：把異常資料當正常資料只會放大風險。
- `C`：GPU 數量與輸入安全性無直接關聯。
- `D`：輸出長度不會改善入口資料品質。

補強知識點：
- 風險管理要分成入口、模型、流程三層看。
- 看到『格式不符、極端值』先想 input validation。

回看來源：
- sources/official-corpus.md｜正式題出現對抗攻擊與資料前處理
- sources/scope-weight-map.md｜L21203 AI 風險管理

</details>

### 題 2｜`L21203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

除了從模型本身補強外，若要先在系統入口擋掉格式異常與極端輸入，最合理的做法為何？

- `A` 只提高 GPU 數量
- `B` 只增加輸出長度上限
- `C` 加強輸入驗證與資料前處理檢查
- `D` 把所有異常輸入都直接當成正常樣本餵進模型

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：入口檢查能在模型看到資料前先過濾明顯錯誤或惡意輸入，是低成本有效的第一層防線。

其餘選項為何錯：
- `A`：GPU 數量與輸入安全性無直接關聯。
- `B`：輸出長度不會改善入口資料品質。
- `D`：把異常資料當正常資料只會放大風險。

補強知識點：
- 風險管理要分成入口、模型、流程三層看。
- 看到『格式不符、極端值』先想 input validation。

回看來源：
- sources/official-corpus.md｜正式題出現對抗攻擊與資料前處理
- sources/scope-weight-map.md｜L21203 AI 風險管理

</details>

### 題 3｜`L21203`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

若想從根本提升模型面對微小惡意擾動的抵抗力，哪一種技術手段最直接？

- `A` 只增加簡報中對模型的信心描述
- `B` 在訓練階段加入對抗樣本訓練
- `C` 只把介面字體變大
- `D` 只把檔案名稱改成英文

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：把對抗樣本納入訓練能讓模型學到更穩健的決策邊界。

其餘選項為何錯：
- `A`：文字宣示不是技術補強。
- `C`：介面字體不會影響模型的魯棒性。
- `D`：檔名格式與模型抗擾動能力無關。

補強知識點：
- 看到『微小擾動、欺騙模型』就回到 adversarial training。
- 題目若問『從根本』，通常在找模型層或訓練層答案。

回看來源：
- sources/official-corpus.md｜正式題對抗樣本情境
- sources/scope-weight-map.md｜L21203 AI 風險管理

</details>

### 題 4｜`L21203`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

上線模型常被帶有微小噪音的輸入騙過。若你要在訓練流程中補一個最對題的做法，應選什麼？

- `A` 只增加簡報中對模型的信心描述
- `B` 在訓練階段加入對抗樣本訓練
- `C` 只把介面字體變大
- `D` 只把檔案名稱改成英文

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：把對抗樣本納入訓練能讓模型學到更穩健的決策邊界。

其餘選項為何錯：
- `A`：文字宣示不是技術補強。
- `C`：介面字體不會影響模型的魯棒性。
- `D`：檔名格式與模型抗擾動能力無關。

補強知識點：
- 看到『微小擾動、欺騙模型』就回到 adversarial training。
- 題目若問『從根本』，通常在找模型層或訓練層答案。

回看來源：
- sources/official-corpus.md｜正式題對抗樣本情境
- sources/scope-weight-map.md｜L21203 AI 風險管理

</details>

### 題 5｜`L21302`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

新模型上線後若指標異常惡化，哪種事前規劃最能縮短事故處理時間？

- `A` 預先定義 rollback 與版本切換流程
- `B` 等出事後再臨時決定如何回退
- `C` 只保留最新版本，不保留舊版映像
- `D` 只在內部聊天訊息中口頭說明應變方式

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：有清楚的 rollback 流程與版本管理，才能在異常發生時迅速恢復服務。

其餘選項為何錯：
- `B`：臨時決策會拉長停機與誤判時間。
- `C`：沒有舊版映像就無法快速回切。
- `D`：口頭說明缺乏一致性與可執行性。

補強知識點：
- 部署題除了 canary，也常考 rollback preparedness。
- 『出事怎麼回來』是部署規劃不可省略的一段。

回看來源：
- sources/official-corpus.md｜L21302 系統部署與更新管理
- sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署

</details>

### 題 6｜`L21302`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

團隊擔心部署後若精度突然下降會影響交易流程。若要讓事故處理更快，規劃階段最值得先準備的是什麼？

- `A` 只保留最新版本，不保留舊版映像
- `B` 只在內部聊天訊息中口頭說明應變方式
- `C` 預先定義 rollback 與版本切換流程
- `D` 等出事後再臨時決定如何回退

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：有清楚的 rollback 流程與版本管理，才能在異常發生時迅速恢復服務。

其餘選項為何錯：
- `A`：沒有舊版映像就無法快速回切。
- `B`：口頭說明缺乏一致性與可執行性。
- `D`：臨時決策會拉長停機與誤判時間。

補強知識點：
- 部署題除了 canary，也常考 rollback preparedness。
- 『出事怎麼回來』是部署規劃不可省略的一段。

回看來源：
- sources/official-corpus.md｜L21302 系統部署與更新管理
- sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署

</details>

### 題 7｜`L21302`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若系統要在部署後主動發現模型品質異常，哪一種做法最完整？

- `A` 只監控 GPU 溫度即可
- `B` 只觀察單次 demo 表現，不設線上門檻
- `C` 只在月報時人工回顧，不做即時告警
- `D` 同時監控資料分布、服務指標與業務 KPI，並設定告警門檻

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：線上模型品質異常可能來自資料、服務或業務結果，監控要多維且有告警門檻。

其餘選項為何錯：
- `A`：GPU 溫度只反映硬體狀態，不等於模型品質。
- `B`：demo 無法代表真實線上變化。
- `C`：月報回顧太慢，不利於快速處置。

補強知識點：
- 把 service monitoring、data monitoring、business KPI 三層一起記。
- 沒有 threshold 的監控通常不算可操作。

回看來源：
- sources/official-corpus.md｜L21302 系統部署與效能監控
- sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署

</details>

### 題 8｜`L21302`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

團隊不想等客訴才知道模型失準。若要先補齊一套較完整的監控思路，最合理的答案為何？

- `A` 只監控 GPU 溫度即可
- `B` 只觀察單次 demo 表現，不設線上門檻
- `C` 只在月報時人工回顧，不做即時告警
- `D` 同時監控資料分布、服務指標與業務 KPI，並設定告警門檻

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：線上模型品質異常可能來自資料、服務或業務結果，監控要多維且有告警門檻。

其餘選項為何錯：
- `A`：GPU 溫度只反映硬體狀態，不等於模型品質。
- `B`：demo 無法代表真實線上變化。
- `C`：月報回顧太慢，不利於快速處置。

補強知識點：
- 把 service monitoring、data monitoring、business KPI 三層一起記。
- 沒有 threshold 的監控通常不算可操作。

回看來源：
- sources/official-corpus.md｜L21302 系統部署與效能監控
- sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署

</details>

### 題 9｜`L21302`｜難度：`中`
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

### 題 10｜`L21302`｜難度：`中`
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

- 風險管理要分成入口、模型、流程三層看，回看 [sources](../sources/) 內對應文件。
- 看到『格式不符、極端值』先想 input validation，回看 [sources](../sources/) 內對應文件。
- 看到『微小擾動、欺騙模型』就回到 adversarial training，回看 [sources](../sources/) 內對應文件。
- 題目若問『從根本』，通常在找模型層或訓練層答案，回看 [sources](../sources/) 內對應文件。
- 部署題除了 canary，也常考 rollback preparedness，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s1d14_input_validation, s1d14_adversarial_training_again, s1d14_canary_rollback, s1d14_monitoring_threshold, s1d14_fail_safe
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
