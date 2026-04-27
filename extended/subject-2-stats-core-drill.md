# 科目 2 加練｜統計推論核心

- 科目：`2`
- 優先級：`A`
- 優先級摘要：`A=4 / B=0 / C=0`
- 來源層級：`official-derived`
- 焦點：`第一二類錯誤、信賴區間、power`
- 題數：`8` 題
- 建議加做時機：`建議在 Day 03、Day 11、Day 16 後加做`
- 作答單：[開啟](../attempts/subject-2-stats-core-drill-attempt.md)
- 批改報告：[開啟](../reports/subject-2-stats-core-drill-report.md)
- 批改指令：`python .\score_attempt.py --drill subject-2-stats-core-drill`
- 使用方式：先做題，再展開 `<details>` 看答案與排錯理由。

## 題源對照

- sources/official-corpus.md｜假設檢定與統計推論
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論
- sources/official-corpus.md｜統計推論與效果解讀
- sources/official-corpus.md｜統計推論與檢定

## 題目

### 題 1｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

第一類錯誤（Type I error）最接近哪個意思？

- `A` 把原本為真的虛無假設誤判為應被拒絕
- `B` 把真實存在的效果誤判為不存在
- `C` 樣本數太大
- `D` 平均數一定算錯

<details>
<summary>顯示答案與說明</summary>

正解：`A`
來源層級：`official-derived`

說明：Type I error 就是假陽性，實際無效果卻錯判為有顯著效果。

其餘選項為何錯：
- `B`：這是 Type II error 的方向。
- `C`：樣本數大小會影響錯誤率與 power，但不是 Type I 的定義。
- `D`：平均數算錯是資料或運算問題，不是統計定義。

補強知識點：
- Type I = false positive；Type II = false negative。
- 把『誤拒真 H0』這句話背熟。

回看來源：
- sources/official-corpus.md｜假設檢定與統計推論
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論

</details>

### 題 2｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若其實新策略沒有提升效果，但檢定結果卻說有顯著差異，這最接近哪種錯誤？

- `A` 樣本數太大
- `B` 平均數一定算錯
- `C` 把原本為真的虛無假設誤判為應被拒絕
- `D` 把真實存在的效果誤判為不存在

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：Type I error 就是假陽性，實際無效果卻錯判為有顯著效果。

其餘選項為何錯：
- `A`：樣本數大小會影響錯誤率與 power，但不是 Type I 的定義。
- `B`：平均數算錯是資料或運算問題，不是統計定義。
- `D`：這是 Type II error 的方向。

補強知識點：
- Type I = false positive；Type II = false negative。
- 把『誤拒真 H0』這句話背熟。

回看來源：
- sources/official-corpus.md｜假設檢定與統計推論
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論

</details>

### 題 3｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

第二類錯誤（Type II error）最接近哪個意思？

- `A` 顯著水準一定設錯
- `B` 所有樣本都必須獨立
- `C` 原本應被拒絕的虛無假設卻沒有被拒絕
- `D` 把原本為真的虛無假設誤拒絕

<details>
<summary>顯示答案與說明</summary>

正解：`C`
來源層級：`official-derived`

說明：Type II error 就是假陰性，有效果卻沒檢出來。

其餘選項為何錯：
- `A`：顯著水準設置會影響錯誤率，但不是 Type II 的定義。
- `B`：獨立性是檢定假設之一，不是 Type II 的直接定義。
- `D`：這是 Type I error 的方向。

補強知識點：
- Type II = false negative。
- power 與 Type II error 彼此相關。

回看來源：
- sources/official-corpus.md｜假設檢定與統計推論
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論

</details>

### 題 4｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若新功能其實真的有效，但檢定卻沒檢出差異，這最接近哪種錯誤？

- `A` 所有樣本都必須獨立
- `B` 原本應被拒絕的虛無假設卻沒有被拒絕
- `C` 把原本為真的虛無假設誤拒絕
- `D` 顯著水準一定設錯

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：Type II error 就是假陰性，有效果卻沒檢出來。

其餘選項為何錯：
- `A`：獨立性是檢定假設之一，不是 Type II 的直接定義。
- `C`：這是 Type I error 的方向。
- `D`：顯著水準設置會影響錯誤率，但不是 Type II 的定義。

補強知識點：
- Type II = false negative。
- power 與 Type II error 彼此相關。

回看來源：
- sources/official-corpus.md｜假設檢定與統計推論
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論

</details>

### 題 5｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若某差異的 95% 信賴區間橫跨 0，最常見的保守解讀為何？

- `A` 代表樣本資料不能用
- `B` 在該信心水準下，效果尚未明確與 0 區分開
- `C` 代表效果一定為 0
- `D` 代表新方案一定比較差

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：若信賴區間跨 0，通常表示在該水準下無法明確排除零效果。

其餘選項為何錯：
- `A`：資料仍可用，只是證據不夠強。
- `C`：CI 跨 0 不等於效果絕對為 0。
- `D`：區間跨 0 不足以直接判定方向一定較差。

補強知識點：
- CI 與顯著性解讀要連在一起。
- 跨 0 常代表證據不足，不是絕對沒有效果。

回看來源：
- sources/official-corpus.md｜統計推論與效果解讀
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論

</details>

### 題 6｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

A/B 測試估計值的 95% CI 為 `[-0.02, 0.05]`。在常見顯著水準下，最合理的判斷是什麼？

- `A` 代表效果一定為 0
- `B` 代表新方案一定比較差
- `C` 代表樣本資料不能用
- `D` 在該信心水準下，效果尚未明確與 0 區分開

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：若信賴區間跨 0，通常表示在該水準下無法明確排除零效果。

其餘選項為何錯：
- `A`：CI 跨 0 不等於效果絕對為 0。
- `B`：區間跨 0 不足以直接判定方向一定較差。
- `C`：資料仍可用，只是證據不夠強。

補強知識點：
- CI 與顯著性解讀要連在一起。
- 跨 0 常代表證據不足，不是絕對沒有效果。

回看來源：
- sources/official-corpus.md｜統計推論與效果解讀
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論

</details>

### 題 7｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

若你希望在真實效果存在時更容易檢出差異，哪個方向通常最直接？

- `A` 把所有異常值都直接刪光
- `B` 在其他條件近似不變時，增加樣本數以提升檢定 power
- `C` 一律把顯著水準改成 0.5
- `D` 完全不做實驗設計，只多看一次 p-value

<details>
<summary>顯示答案與說明</summary>

正解：`B`
來源層級：`official-derived`

說明：增加樣本數常能降低估計不穩定性，讓真實效果較容易被檢出。

其餘選項為何錯：
- `A`：粗暴刪異常值可能扭曲結果。
- `C`：顯著水準 0.5 會讓假陽性嚴重失控。
- `D`：只反覆看 p-value 不會系統性提升設計品質。

補強知識點：
- power 與樣本數常一起考。
- 不要用放寬門檻取代改善設計。

回看來源：
- sources/official-corpus.md｜統計推論與檢定
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論

</details>

### 題 8｜`L22103`｜難度：`中`
優先級：`A`｜來源層級：`official-derived`

研究團隊抱怨『明明可能有差異，但一直檢不出來』。若先做一個常見補強，最合理的是什麼？

- `A` 一律把顯著水準改成 0.5
- `B` 完全不做實驗設計，只多看一次 p-value
- `C` 把所有異常值都直接刪光
- `D` 在其他條件近似不變時，增加樣本數以提升檢定 power

<details>
<summary>顯示答案與說明</summary>

正解：`D`
來源層級：`official-derived`

說明：增加樣本數常能降低估計不穩定性，讓真實效果較容易被檢出。

其餘選項為何錯：
- `A`：顯著水準 0.5 會讓假陽性嚴重失控。
- `B`：只反覆看 p-value 不會系統性提升設計品質。
- `C`：粗暴刪異常值可能扭曲結果。

補強知識點：
- power 與樣本數常一起考。
- 不要用放寬門檻取代改善設計。

回看來源：
- sources/official-corpus.md｜統計推論與檢定
- sources/scope-weight-map.md｜L22103 假設檢定與統計推論

</details>

## 本組必補

- Type I = false positive；Type II = false negative
- 把『誤拒真 H0』這句話背熟
- Type II = false negative
- power 與 Type II error 彼此相關
- CI 與顯著性解讀要連在一起
- 跨 0 常代表證據不足，不是絕對沒有效果

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
