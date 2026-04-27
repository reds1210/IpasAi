# Wrong Answer Map

這不是實際錯題紀錄，而是預先排好的高風險概念回鍋表。若你在第一次出現時答錯，就沿著後續回鍋日繼續追。

| Concept ID | 科目 | L-code | 首次出現 | 後續回鍋日 | 建議追蹤重點 |
| --- | --- | --- | --- | --- | --- |
| `s1d10_seq2seq` | 科目1 | `L21101` | Day 10 | Day 16, Day 17 | 分清 classification、sequence labeling、sequence generation。 |
| `s1d10_word2vec` | 科目1 | `L21101` | Day 10 | Day 15, Day 19 | 把 TF-IDF 與 Word2Vec 分清：前者是稀疏權重，後者是嵌入向量。 |
| `s1d14_fail_safe` | 科目1 | `L21302` | Day 14 | Day 18, Day 20 | 部署與可靠度題常考 fallback、degradation、manual override。 |
| `s1d1_tokenization` | 科目1 | `L21101` | Day 01 | Day 11, Day 17 | 區分 tokenization、lemmatization、stopword removal、TF-IDF 的先後次序。 |
| `s1d3_rag_core` | 科目1 | `L21103` | Day 03 | Day 11, Day 17, Day 20 | 理解 RAG 的核心價值：檢索可信內容再生成。 |
| `s1d5_data_readiness` | 科目1 | `L21201` | Day 05 | Day 12, Day 20 | 導入評估的第一關通常是資料、目標、指標，而不是先追模型。 |
| `s1d6_requirement_first` | 科目1 | `L21202` | Day 06 | Day 18, Day 20 | 規劃先於建置，需求先於選型。 |
| `s1d7_copyright_prevention` | 科目1 | `L21203` | Day 07 | Day 11, Day 17 | 生成式 AI 法務風險通常要從流程治理，而非只從模型參數處理。 |
| `s1d7_transparency` | 科目1 | `L21203` | Day 07 | Day 15, Day 20 | 記住 transparency、explainability、traceability 是一組常連動的治理概念。 |
| `s1d8_scaling` | 科目1 | `L21301` | Day 08 | Day 15, Day 17 | 標準化、正規化與模型敏感度要建立連結。 |
| `s1d9_integration_testing` | 科目1 | `L21302` | Day 09 | Day 16, Day 20 | integration testing 看的是流程與介面，不是單一模型分數。 |
| `s1d9_kubernetes` | 科目1 | `L21302` | Day 09 | Day 11, Day 17 | Kubernetes 是 orchestration，不是 model training tool。 |
| `s2d10_smote` | 科目2 | `L22401` | Day 10 | Day 12, Day 17, Day 20 | SMOTE、class weight、threshold tuning 是不平衡分類三個高頻補救方向。 |
| `s2d10_threshold_tuning` | 科目2 | `L22301` | Day 10 | Day 15, Day 18 | threshold tuning 是決策層調整，不是資料層。 |
| `s2d13_graph_edge_property` | 科目2 | `L22202` | Day 13 | Day 15, Day 18 | 圖資料庫的核心是節點、邊與屬性。 |
| `s2d14_arima_residual` | 科目2 | `L22302` | Day 14 | Day 17, Day 19 | 時間序列診斷常看殘差是否近白噪音。 |
| `s2d1_nullable_int` | 科目2 | `L22201` | Day 01 | Day 11, Day 17 | 區分 Python / numpy 的整數型態與 pandas nullable integer。 |
| `s2d1_year_float` | 科目2 | `L22201` | Day 01 | Day 11, Day 19 | 理解 dtype 由內容而非欄位名稱決定。 |
| `s2d2_iqr` | 科目2 | `L22101` | Day 02 | Day 15, Day 19 | 箱型圖、IQR、四分位數的關係要熟。 |
| `s2d3_prop_test` | 科目2 | `L22103` | Day 03 | Day 12, Day 18 | 先看目標是平均數還是比例。 |
| `s2d3_ttest` | 科目2 | `L22103` | Day 03 | Day 11, Day 18 | 先判斷要比『平均數』還是『比例 / 類別』。 |
| `s2d6_groupby_sum` | 科目2 | `L22303` | Day 06 | Day 16, Day 18 | 看到『總額』先找 sum，不要被 count 誤導。 |
| `s2d6_melt_barplot` | 科目2 | `L22303` | Day 06 | Day 12, Day 17 | 寬表轉長表是資料視覺化常考轉換。 |
| `s2d7_coef_intercept` | 科目2 | `L22301` | Day 07 | Day 12, Day 17 | 區分 `coef_` 與 `intercept_`。 |
| `s2d7_fit_xy` | 科目2 | `L22301` | Day 07 | Day 11, Day 17 | 記住 sklearn 介面慣例：X 在前、y 在後。 |
| `s2d8_add_constant` | 科目2 | `L22301` | Day 08 | Day 15, Day 18 | `add_constant` 是 statsmodels 題的高頻 API。 |
| `s2d9_kfold` | 科目2 | `L22301` | Day 09 | Day 16, Day 20 | 交叉驗證的重點是反覆切分與平均。 |
