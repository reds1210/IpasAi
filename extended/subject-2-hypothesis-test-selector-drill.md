# 科目 2 加練｜統計檢定與分布秒判

- 科目：`2`
- 優先級：`A`
- 優先級摘要：`A=4 / B=0 / C=0`
- 來源層級：`official-derived`
- 焦點：`t-test、ANOVA、卡方、比例檢定、p-value、信賴區間`
- 題數：`8` 題
- 建議加做時機：`Day 03、Day 11、Day 18 後加做`
- 作答單：[開啟](../attempts/subject-2-hypothesis-test-selector-drill-attempt.md)
- 批改報告：[開啟](../reports/subject-2-hypothesis-test-selector-drill-report.md)
- 批改指令：`python .\score_attempt.py --drill subject-2-hypothesis-test-selector-drill`
- 使用方式：先做題，再展開 `<details>` 看答案與排錯理由。

## 題源對照

- sources/question-source-map.md｜統計判斷必擴
- sources/scope-weight-map.md｜L22103 統計推論
- sources/question-source-map.md｜官方與模擬題常見 ANOVA
- sources/question-patterns.md｜統計檢定題

## 題目

### 題 1｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

要比較 A/B 兩版登入頁的平均停留秒數是否不同，且兩組樣本彼此獨立，最常見的檢定方法是什麼？

- `A` 卡方檢定
- `B` 單因子 ANOVA
- `C` 主成分分析（PCA）
- `D` 兩獨立樣本 t 檢定

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：比較兩組平均數差異，且樣本彼此獨立、資料近似常態時，典型做法是兩獨立樣本 t 檢定。

其餘選項為何錯：
- `A`：卡方檢定用於類別變數關聯，不是比較平均數。
- `B`：ANOVA 常用於三組以上平均數比較；兩組也能用，但不是最直接首選。
- `C`：PCA 是降維方法，不是顯著性檢定。

補強知識點：
- 先辨識是『平均數』還是『比例/類別』問題。
- 兩組平均數差異通常先想 t 檢定。

回看來源：
- sources/official-corpus.md｜統計檢定為科目 2 核心
- sources/question-source-map.md｜官方與公開練習都高頻出現 t-test 題

</details>

### 題 2｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

行銷團隊抽兩組不同會員，比較平均客單價是否有顯著差異。若資料近似常態，應優先選哪種檢定？

- `A` 卡方檢定
- `B` 單因子 ANOVA
- `C` 主成分分析（PCA）
- `D` 兩獨立樣本 t 檢定

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：比較兩組平均數差異，且樣本彼此獨立、資料近似常態時，典型做法是兩獨立樣本 t 檢定。

其餘選項為何錯：
- `A`：卡方檢定用於類別變數關聯，不是比較平均數。
- `B`：ANOVA 常用於三組以上平均數比較；兩組也能用，但不是最直接首選。
- `C`：PCA 是降維方法，不是顯著性檢定。

補強知識點：
- 先辨識是『平均數』還是『比例/類別』問題。
- 兩組平均數差異通常先想 t 檢定。

回看來源：
- sources/official-corpus.md｜統計檢定為科目 2 核心
- sources/question-source-map.md｜官方與公開練習都高頻出現 t-test 題

</details>

### 題 3｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若要比較三種推薦策略對平均轉換率是否有顯著差異，最適合先用哪種檢定？

- `A` 兩獨立樣本 t 檢定
- `B` 卡方檢定
- `C` 皮爾森相關係數
- `D` 單因子 ANOVA

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：三組以上平均數比較時，最常先用單因子 ANOVA 檢查整體是否存在顯著差異。

其餘選項為何錯：
- `A`：t 檢定主要對兩組平均數，比三組以上不合適。
- `B`：卡方檢定處理類別變數關聯，不是平均數差異。
- `C`：相關係數描述線性關聯，不是多組平均數檢定。

補強知識點：
- 看到『三組以上平均數』先想 ANOVA。
- 分清平均數差異與類別關聯。

回看來源：
- sources/official-corpus.md｜ANOVA 為高頻檢定題型
- sources/question-patterns.md｜統計檢定選型題模板

</details>

### 題 4｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

你有三個廣告版本，想知道平均點擊停留時間是否存在組間差異，第一步最常見的檢定是什麼？

- `A` 兩獨立樣本 t 檢定
- `B` 卡方檢定
- `C` 皮爾森相關係數
- `D` 單因子 ANOVA

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：三組以上平均數比較時，最常先用單因子 ANOVA 檢查整體是否存在顯著差異。

其餘選項為何錯：
- `A`：t 檢定主要對兩組平均數，比三組以上不合適。
- `B`：卡方檢定處理類別變數關聯，不是平均數差異。
- `C`：相關係數描述線性關聯，不是多組平均數檢定。

補強知識點：
- 看到『三組以上平均數』先想 ANOVA。
- 分清平均數差異與類別關聯。

回看來源：
- sources/official-corpus.md｜ANOVA 為高頻檢定題型
- sources/question-patterns.md｜統計檢定選型題模板

</details>

### 題 5｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若要判斷『是否為會員』與『是否購買年費方案』之間是否存在關聯，最常見的檢定是什麼？

- `A` 卡方獨立性檢定
- `B` 兩獨立樣本 t 檢定
- `C` 單因子 ANOVA
- `D` 線性迴歸係數檢定

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：兩個類別變數之間是否存在關聯，經典方法是卡方獨立性檢定。

其餘選項為何錯：
- `B`：t 檢定是比較平均數，不是類別關聯。
- `C`：ANOVA 比較多組平均數，不是類別交叉表關聯。
- `D`：迴歸可以建模，但不是這類基礎關聯檢定的首選。

補強知識點：
- 看到『類別對類別』先想卡方。
- 交叉表與平均數比較是不同問題。

回看來源：
- sources/official-corpus.md｜卡方與類別關聯為固定熱區
- sources/question-source-map.md｜S 測驗與官方都常見卡方題

</details>

### 題 6｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

醫療資料把病患分成吸菸/不吸菸與有症狀/無症狀兩類，若想檢驗兩個類別變數是否相關，應優先選哪種檢定？

- `A` 線性迴歸係數檢定
- `B` 卡方獨立性檢定
- `C` 兩獨立樣本 t 檢定
- `D` 單因子 ANOVA

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：兩個類別變數之間是否存在關聯，經典方法是卡方獨立性檢定。

其餘選項為何錯：
- `A`：迴歸可以建模，但不是這類基礎關聯檢定的首選。
- `C`：t 檢定是比較平均數，不是類別關聯。
- `D`：ANOVA 比較多組平均數，不是類別交叉表關聯。

補強知識點：
- 看到『類別對類別』先想卡方。
- 交叉表與平均數比較是不同問題。

回看來源：
- sources/official-corpus.md｜卡方與類別關聯為固定熱區
- sources/question-source-map.md｜S 測驗與官方都常見卡方題

</details>

### 題 7｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

客服機器人的一次解決率目標是 80%。本月抽樣後想檢驗實際比例是否低於目標，最貼近的檢定是什麼？

- `A` 兩獨立樣本 t 檢定
- `B` 主成分分析（PCA）
- `C` 單一比例檢定
- `D` 卡方獨立性檢定

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：當問題是『單一比例是否達標』時，應選單一比例檢定，而不是平均數或降維方法。

其餘選項為何錯：
- `A`：t 檢定比較平均數，不是比例是否達標。
- `B`：PCA 與比例顯著性檢定無關。
- `D`：卡方獨立性檢定重點是兩個類別變數是否相關。

補強知識點：
- 分清比例問題與平均數問題。
- 看到『達標/未達標』時先想比例檢定。

回看來源：
- sources/question-source-map.md｜公開模擬題常出比例檢定選型
- sources/question-patterns.md｜統計檢定題模板

</details>

### 題 8｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

產品團隊懷疑新版註冊流程的完成率未達 65% 目標。若要檢驗單一比例是否低於既定門檻，優先想到哪種方法？

- `A` 主成分分析（PCA）
- `B` 單一比例檢定
- `C` 卡方獨立性檢定
- `D` 兩獨立樣本 t 檢定

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：當問題是『單一比例是否達標』時，應選單一比例檢定，而不是平均數或降維方法。

其餘選項為何錯：
- `A`：PCA 與比例顯著性檢定無關。
- `C`：卡方獨立性檢定重點是兩個類別變數是否相關。
- `D`：t 檢定比較平均數，不是比例是否達標。

補強知識點：
- 分清比例問題與平均數問題。
- 看到『達標/未達標』時先想比例檢定。

回看來源：
- sources/question-source-map.md｜公開模擬題常出比例檢定選型
- sources/question-patterns.md｜統計檢定題模板

</details>

## 本組必補

- 先辨識是『平均數』還是『比例/類別』問題
- 兩組平均數差異通常先想 t 檢定
- 看到『三組以上平均數』先想 ANOVA
- 分清平均數差異與類別關聯
- 看到『類別對類別』先想卡方
- 交叉表與平均數比較是不同問題

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
