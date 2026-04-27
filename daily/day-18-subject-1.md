# Day 18｜科目 1 反向題單

- 今日焦點：`導入規劃與治理混題`
- 題量：`12` 題
- 建議方式：先以 60–75 分鐘完成第一輪，再展開解析。｜優先級 A｜先刷這份，對過線最有幫助。
- 來源對照：
  - [official-corpus.md](../sources/official-corpus.md)
  - [scope-weight-map.md](../sources/scope-weight-map.md)
  - [question-source-map.md](../sources/question-source-map.md)
  - [question-patterns.md](../sources/question-patterns.md)
  - [book-bridge.md](../sources/book-bridge.md)

## 今日題目

### 題 1｜`L21202`｜難度：`中`
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

### 題 2｜`L21202`｜難度：`中`
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

### 題 3｜`L21202`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

AI 導入規劃中的資源分配，最不應忽略哪一類非模型資源？

- `A` 資料治理與業務驗證人力也是核心資源
- `B` 只要模型準確率高，其他角色都可省略
- `C` 資源分配只需要看硬體，不必看流程維運
- `D` AI 專案只要工程師，不需要業務與法務參與

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：AI 專案不是只有模型與硬體，資料治理、業務驗證與風險控管都是必要資源。

其餘選項為何錯：
- `B`：高準確率不能替代流程與治理人力。
- `C`：只看硬體會忽略資料更新與使用者導入成本。
- `D`：業務與法務角色關係到需求正確性與合規性。

補強知識點：
- 資源分配要包含人、資料、流程、算力與治理責任。
- 看到『只買設備』的答案通常不完整。

回看來源：
- sources/official-corpus.md｜L21202 AI 導入規劃
- sources/scope-weight-map.md｜L21202 AI 導入規劃

</details>

### 題 4｜`L21202`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

團隊只排了 GPU 與 API 預算，卻沒有安排資料治理、標註維護與業務驗證人力。這在規劃上最主要的問題是什麼？

- `A` AI 專案只要工程師，不需要業務與法務參與
- `B` 資料治理與業務驗證人力也是核心資源
- `C` 只要模型準確率高，其他角色都可省略
- `D` 資源分配只需要看硬體，不必看流程維運

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：AI 專案不是只有模型與硬體，資料治理、業務驗證與風險控管都是必要資源。

其餘選項為何錯：
- `A`：業務與法務角色關係到需求正確性與合規性。
- `C`：高準確率不能替代流程與治理人力。
- `D`：只看硬體會忽略資料更新與使用者導入成本。

補強知識點：
- 資源分配要包含人、資料、流程、算力與治理責任。
- 看到『只買設備』的答案通常不完整。

回看來源：
- sources/official-corpus.md｜L21202 AI 導入規劃
- sources/scope-weight-map.md｜L21202 AI 導入規劃

</details>

### 題 5｜`L21203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若日後要追查 AI 為何輸出某段內容，哪種治理設計最有助於事後稽核？

- `A` 只保留模型名稱，不記操作歷程
- `B` 保留提示、資料來源、模型版本與操作紀錄的 audit trail
- `C` 只保留最終輸出文字即可
- `D` 只記誰登入，不記模型與資料版本

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：可稽核紀錄能支撐責任釐清、問題重現與法遵要求。

其餘選項為何錯：
- `A`：只有模型名稱也缺少資料與提示上下文。
- `C`：只有最終輸出不足以重建決策脈絡。
- `D`：只記登入資訊無法回推出內容生成依據。

補強知識點：
- audit trail 通常要包含人、資料、提示、版本、時間。
- 追溯題的核心不是再訓練，而是紀錄完整性。

回看來源：
- sources/official-corpus.md｜治理與風險管理
- sources/scope-weight-map.md｜L21203 AI 風險管理

</details>

### 題 6｜`L21203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

法遵單位要求『出事後能回溯是誰用什麼資料、什麼提示、哪個版本的模型產生結果』，最合理的作法為何？

- `A` 只保留最終輸出文字即可
- `B` 只記誰登入，不記模型與資料版本
- `C` 只保留模型名稱，不記操作歷程
- `D` 保留提示、資料來源、模型版本與操作紀錄的 audit trail

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：可稽核紀錄能支撐責任釐清、問題重現與法遵要求。

其餘選項為何錯：
- `A`：只有最終輸出不足以重建決策脈絡。
- `B`：只記登入資訊無法回推出內容生成依據。
- `C`：只有模型名稱也缺少資料與提示上下文。

補強知識點：
- audit trail 通常要包含人、資料、提示、版本、時間。
- 追溯題的核心不是再訓練，而是紀錄完整性。

回看來源：
- sources/official-corpus.md｜治理與風險管理
- sources/scope-weight-map.md｜L21203 AI 風險管理

</details>

### 題 7｜`L21203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若企業要向內部說明模型用途、限制、偏誤風險與適用情境，下列哪種文件化做法最有幫助？

- `A` 只給最高準確率數字，不寫限制
- `B` 只在口頭會議上描述，不留文件
- `C` 建立模型卡（model card）或同類型能力說明文件
- `D` 只保留程式碼，不提供任何說明

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：模型卡能把用途、限制、偏誤、資料條件與監控建議說清楚，是治理常用文件。

其餘選項為何錯：
- `A`：只給最高分數會掩蓋模型限制與風險。
- `B`：不留文件不利於知識傳承與稽核。
- `D`：只有程式碼對非技術利害關係人不夠透明。

補強知識點：
- 治理題常把文件透明化視為風險控管的一部分。
- 記住 model card 的用途是『說明能力與限制』。

回看來源：
- sources/official-corpus.md｜治理與透明性導向題型
- sources/scope-weight-map.md｜L21203 AI 風險管理

</details>

### 題 8｜`L21203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

你需要讓非技術主管快速了解模型能做什麼、不能做什麼、在哪些條件下容易失準。最適合優先建立哪種文件？

- `A` 只給最高準確率數字，不寫限制
- `B` 只在口頭會議上描述，不留文件
- `C` 建立模型卡（model card）或同類型能力說明文件
- `D` 只保留程式碼，不提供任何說明

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：模型卡能把用途、限制、偏誤、資料條件與監控建議說清楚，是治理常用文件。

其餘選項為何錯：
- `A`：只給最高分數會掩蓋模型限制與風險。
- `B`：不留文件不利於知識傳承與稽核。
- `D`：只有程式碼對非技術利害關係人不夠透明。

補強知識點：
- 治理題常把文件透明化視為風險控管的一部分。
- 記住 model card 的用途是『說明能力與限制』。

回看來源：
- sources/official-corpus.md｜治理與透明性導向題型
- sources/scope-weight-map.md｜L21203 AI 風險管理

</details>

### 題 9｜`L21302`｜難度：`中`
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

### 題 10｜`L21302`｜難度：`中`
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

- 規劃先於建置，需求先於選型，回看 [sources](../sources/) 內對應文件。
- 題目提到多部門分歧時，優先想到需求澄清與 stakeholder alignment，回看 [sources](../sources/) 內對應文件。
- 資源分配要包含人、資料、流程、算力與治理責任，回看 [sources](../sources/) 內對應文件。
- 看到『只買設備』的答案通常不完整，回看 [sources](../sources/) 內對應文件。
- audit trail 通常要包含人、資料、提示、版本、時間，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s1d13_audit_log, s1d13_model_card, s1d14_canary_rollback, s1d14_fail_safe
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
