# Day 06｜科目 1 反向題單

- 今日焦點：`AI 導入規劃`
- 題量：`8` 題
- 建議方式：先以 60–75 分鐘完成第一輪，再展開解析。｜優先級 B｜主線刷完後優先補這份。
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

### 題 5｜`L21202`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若企業希望降低 AI 導入失敗的營運衝擊，最合理的上線策略為何？

- `A` 採分階段上線並保留人工覆核與回退機制
- `B` 在沒有備援下直接全面切換
- `C` 只做一次內部 demo 就宣告專案完成
- `D` 先停掉舊流程再看新系統是否穩定

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：分階段 rollout 能保留修正空間，也能逐步觀察使用者與品質指標。

其餘選項為何錯：
- `B`：全面切換在錯誤發生時缺乏緩衝。
- `C`：demo 只能展示功能，不足以證明穩定度。
- `D`：先停掉舊流程會讓風險在第一天就擴散。

補強知識點：
- rollout 規劃要有人工覆核、rollback 與監控。
- 『分階段』通常比『一次到位』更安全。

回看來源：
- sources/official-corpus.md｜L21202 AI 導入規劃
- sources/scope-weight-map.md｜L21202 AI 導入規劃

</details>

### 題 6｜`L21202`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

客服單位擔心新 AI 摘要系統一上線就全面替代舊流程會出現錯誤，從導入規劃角度最好的安排是什麼？

- `A` 採分階段上線並保留人工覆核與回退機制
- `B` 在沒有備援下直接全面切換
- `C` 只做一次內部 demo 就宣告專案完成
- `D` 先停掉舊流程再看新系統是否穩定

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：分階段 rollout 能保留修正空間，也能逐步觀察使用者與品質指標。

其餘選項為何錯：
- `B`：全面切換在錯誤發生時缺乏緩衝。
- `C`：demo 只能展示功能，不足以證明穩定度。
- `D`：先停掉舊流程會讓風險在第一天就擴散。

補強知識點：
- rollout 規劃要有人工覆核、rollback 與監控。
- 『分階段』通常比『一次到位』更安全。

回看來源：
- sources/official-corpus.md｜L21202 AI 導入規劃
- sources/scope-weight-map.md｜L21202 AI 導入規劃

</details>

### 題 7｜`L21202`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

在 AI 導入規劃中，驗收條件（acceptance criteria）最主要的作用為何？

- `A` 讓模型不需要再做任何監控
- `B` 保證模型永遠不會產生錯誤
- `C` 取代所有需求訪談與使用者測試
- `D` 把可接受的品質門檻與責任邊界寫清楚

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：驗收條件是用來定義什麼叫『可以上線』，不是消滅所有風險。

其餘選項為何錯：
- `A`：監控仍是上線後必要機制。
- `B`：任何模型都無法保證永遠零錯誤。
- `C`：驗收條件不能取代前期訪談與測試，只能補強共識。

補強知識點：
- KPI 與 acceptance criteria 要分開看：前者偏目標，後者偏交付門檻。
- 有驗收標準，才有明確的 go / no-go 決策點。

回看來源：
- sources/official-corpus.md｜L21202 AI 導入規劃
- sources/scope-weight-map.md｜L21202 AI 導入規劃

</details>

### 題 8｜`L21202`｜難度：`中`
優先級：`B`｜來源層級：`official-derived`

若專案團隊與業務部門對『模型做得不錯』的理解不同，為避免上線爭議，規劃階段最該先補什麼？

- `A` 保證模型永遠不會產生錯誤
- `B` 取代所有需求訪談與使用者測試
- `C` 把可接受的品質門檻與責任邊界寫清楚
- `D` 讓模型不需要再做任何監控

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：驗收條件是用來定義什麼叫『可以上線』，不是消滅所有風險。

其餘選項為何錯：
- `A`：任何模型都無法保證永遠零錯誤。
- `B`：驗收條件不能取代前期訪談與測試，只能補強共識。
- `D`：監控仍是上線後必要機制。

補強知識點：
- KPI 與 acceptance criteria 要分開看：前者偏目標，後者偏交付門檻。
- 有驗收標準，才有明確的 go / no-go 決策點。

回看來源：
- sources/official-corpus.md｜L21202 AI 導入規劃
- sources/scope-weight-map.md｜L21202 AI 導入規劃

</details>

## 今日必補知識點

- 規劃先於建置，需求先於選型，回看 [sources](../sources/) 內對應文件。
- 題目提到多部門分歧時，優先想到需求澄清與 stakeholder alignment，回看 [sources](../sources/) 內對應文件。
- 資源分配要包含人、資料、流程、算力與治理責任，回看 [sources](../sources/) 內對應文件。
- 看到『只買設備』的答案通常不完整，回看 [sources](../sources/) 內對應文件。
- rollout 規劃要有人工覆核、rollback 與監控，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
