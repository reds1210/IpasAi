# Day 07｜科目 1 反向題單

- 今日焦點：`AI 風險治理與責任`
- 題量：`8` 題
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

企業部署生成式 AI 協助行銷內容產出，若要降低著作權侵權風險，最有效的預防策略為何？

- `A` 只看點擊率，不必檢查引用來源與授權
- `B` 建立資料來源審查、輸出覆核與授權檢查流程
- `C` 只要模型夠大，就不會有著作權風險
- `D` 把所有輸出都自動發布，避免人工拖慢速度

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：著作權風險主要來自訓練來源、輸出近似與使用流程，因此要建立審查與覆核機制。

其餘選項為何錯：
- `A`：只看商業指標會忽略法律風險。
- `C`：模型大小與侵權風險沒有必然反比關係。
- `D`：自動發布會放大錯誤輸出與侵權責任。

補強知識點：
- 生成式 AI 法務風險通常要從流程治理，而非只從模型參數處理。
- 看到『侵權』優先想到授權、來源、覆核、紀錄。

回看來源：
- sources/official-corpus.md｜正式題出現生成式 AI 著作權風險
- sources/scope-weight-map.md｜L21203 AI 風險管理

</details>

### 題 2｜`L21203`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

內容團隊常把 AI 生成文案直接外發。若你要從流程面先降風險，最優先的安排應是什麼？

- `A` 把所有輸出都自動發布，避免人工拖慢速度
- `B` 只看點擊率，不必檢查引用來源與授權
- `C` 建立資料來源審查、輸出覆核與授權檢查流程
- `D` 只要模型夠大，就不會有著作權風險

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：著作權風險主要來自訓練來源、輸出近似與使用流程，因此要建立審查與覆核機制。

其餘選項為何錯：
- `A`：自動發布會放大錯誤輸出與侵權責任。
- `B`：只看商業指標會忽略法律風險。
- `D`：模型大小與侵權風險沒有必然反比關係。

補強知識點：
- 生成式 AI 法務風險通常要從流程治理，而非只從模型參數處理。
- 看到『侵權』優先想到授權、來源、覆核、紀錄。

回看來源：
- sources/official-corpus.md｜正式題出現生成式 AI 著作權風險
- sources/scope-weight-map.md｜L21203 AI 風險管理

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

### 題 5｜`L21203`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

若模型容易被對抗樣本騙過，從模型層面最直接的補強做法通常是什麼？

- `A` 導入對抗訓練（adversarial training）
- `B` 只增加輸出字數上限
- `C` 只把訓練資料做欄位重新命名
- `D` 只在簡報中加入風險聲明而不調整模型

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：對抗訓練是直接把擾動樣本納入訓練，提升模型對惡意擾動的穩健性。

其餘選項為何錯：
- `B`：輸出字數與對抗韌性無直接關聯。
- `C`：重新命名欄位不會改變模型面對對抗擾動的能力。
- `D`：風險聲明屬治理措施，不是模型層補強。

補強知識點：
- 把技術補強與流程治理分開看。
- 只要題目強調『惡意擾動輸入』，優先想到 adversarial training 或 robust training。

回看來源：
- sources/official-corpus.md｜正式題出現對抗攻擊情境
- sources/scope-weight-map.md｜L21203 AI 風險管理

</details>

### 題 6｜`L21203`｜難度：`難`
優先級：`A`｜來源層級：`official-derived`

金融風控模型被駭客透過微小特徵擾動成功誤導。若你想優先提升模型對這類攻擊的辨識韌性，較合理的技術方向為何？

- `A` 只增加輸出字數上限
- `B` 只把訓練資料做欄位重新命名
- `C` 只在簡報中加入風險聲明而不調整模型
- `D` 導入對抗訓練（adversarial training）

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：對抗訓練是直接把擾動樣本納入訓練，提升模型對惡意擾動的穩健性。

其餘選項為何錯：
- `A`：輸出字數與對抗韌性無直接關聯。
- `B`：重新命名欄位不會改變模型面對對抗擾動的能力。
- `C`：風險聲明屬治理措施，不是模型層補強。

補強知識點：
- 把技術補強與流程治理分開看。
- 只要題目強調『惡意擾動輸入』，優先想到 adversarial training 或 robust training。

回看來源：
- sources/official-corpus.md｜正式題出現對抗攻擊情境
- sources/scope-weight-map.md｜L21203 AI 風險管理

</details>

### 題 7｜`L21203`｜難度：`中`
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

### 題 8｜`L21203`｜難度：`中`
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

## 今日必補知識點

- 生成式 AI 法務風險通常要從流程治理，而非只從模型參數處理，回看 [sources](../sources/) 內對應文件。
- 看到『侵權』優先想到授權、來源、覆核、紀錄，回看 [sources](../sources/) 內對應文件。
- 把『供應鏈』理解為所有外部依賴，不只是設備採購，回看 [sources](../sources/) 內對應文件。
- 對第三方模型與資料做 provenance 檢查是基本功，回看 [sources](../sources/) 內對應文件。
- 把技術補強與流程治理分開看，回看 [sources](../sources/) 內對應文件。

## 明日回補標記

- A 級優先題：s1d7_copyright_prevention, s1d7_supply_chain, s1d7_adversarial_training, s1d7_transparency
- 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
- 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
- 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
