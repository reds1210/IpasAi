# Scope Weight Map

這份文件把官方 L-code 主題轉成題包權重。權重不是官方配分，而是依你的 20 天反向刷題需求重新排序。

## 高權重原則

- 科目 1：`L211`、`L21203`、`L21302` 權重最高。
- 科目 2：`L22103`、`L22201`、`L22301`、`L22303`、`L22401` 權重最高。
- 若題目明確涉及 Python、統計檢定、回歸或視覺化，優先回補科目 2。

## L21101 自然語言處理技術與應用

- 規劃題量權重：`22` 題
- 題型來源：官方範圍 + 學習指引 + 樣題結構仿真
代表題：
- `s1d1_tokenization`：出現在 Day 01, 11, 17；補點焦點：區分 tokenization、lemmatization、stopword removal、TF-IDF 的先後次序。
- `s1d1_sentiment`：出現在 Day 01；補點焦點：建立文字任務與 NLP、影像任務與 CV 的快速對應。
- `s1d1_language_model_fit`：出現在 Day 01；補點焦點：從問題的輸入資料型態判斷技術路線。
- `s1d10_seq2seq`：出現在 Day 10, 16, 17；補點焦點：分清 classification、sequence labeling、sequence generation。

## L21102 電腦視覺技術與應用

- 規劃題量權重：`10` 題
- 題型來源：官方範圍 + 學習指引 + 樣題結構仿真
代表題：
- `s1d2_cv_tasks`：出現在 Day 02, 12；補點焦點：分類、偵測、語義分割、實例分割的輸出粒度要分清。
- `s1d2_cnn_fit`：出現在 Day 02；補點焦點：影像任務先聯想到 CNN；序列任務再考慮 RNN/Transformer。
- `s1d2_ocr`：出現在 Day 02；補點焦點：分清 OCR、ASR、NLP 的輸入資料型態差異。
- `s1d2_quality_inspection`：出現在 Day 02；補點焦點：根據輸入資料型態與業務目的選技術。

## L21103 生成式 AI 技術與應用

- 規劃題量權重：`22` 題
- 題型來源：官方範圍 + 學習指引 + 樣題結構仿真
代表題：
- `s1d1_rule_based_boundary`：出現在 Day 01, 19；補點焦點：區分 rule-based automation 與 ML system 的邊界。
- `s1d3_rag_core`：出現在 Day 03, 11, 17, 20；補點焦點：理解 RAG 的核心價值：檢索可信內容再生成。
- `s1d3_retrieval_stage`：出現在 Day 03, 15；補點焦點：把『檢索品質』與『生成品質』拆開看。
- `s1d3_augmentation_semantics`：出現在 Day 03, 19；補點焦點：資料增強不是越多越好，關鍵是語意一致與分布合理。

## L21104 多模態人工智慧應用

- 規劃題量權重：`12` 題
- 題型來源：官方範圍 + 學習指引 + 樣題結構仿真
代表題：
- `s1d4_early_fusion`：出現在 Day 04, 12；補點焦點：Early fusion 與 late fusion 的分界要靠『整合發生在何時』來記。
- `s1d4_transformer_multimodal`：出現在 Day 04；補點焦點：跨模態整合常見關鍵字：attention、alignment、Transformer。
- `s1d4_missing_modality`：出現在 Day 04, 16；補點焦點：多模態系統除了準確率，也要看可用性與魯棒性。
- `s1d4_shared_representation`：出現在 Day 04；補點焦點：理解多模態檢索的關鍵不是資料量，而是 representation alignment。

## L21201 AI 導入評估

- 規劃題量權重：`14` 題
- 題型來源：官方範圍 + 學習指引 + 樣題結構仿真
代表題：
- `s1d5_data_readiness`：出現在 Day 05, 12, 20；補點焦點：導入評估的第一關通常是資料、目標、指標，而不是先追模型。
- `s1d5_cost_benefit`：出現在 Day 05；補點焦點：評估階段要把效能、成本、風險、回收期一起看。
- `s1d5_poc`：出現在 Day 05, 16；補點焦點：評估階段的關鍵詞：PoC、pilot、low-risk validation。
- `s1d5_kpi`：出現在 Day 05；補點焦點：把『導入目的』轉成可量化指標是評估核心。

## L21202 AI 導入規劃

- 規劃題量權重：`14` 題
- 題型來源：官方範圍 + 學習指引 + 樣題結構仿真
代表題：
- `s1d6_requirement_first`：出現在 Day 06, 18, 20；補點焦點：規劃先於建置，需求先於選型。
- `s1d6_resource_allocation`：出現在 Day 06, 18；補點焦點：資源分配要包含人、資料、流程、算力與治理責任。
- `s1d6_rollout`：出現在 Day 06；補點焦點：rollout 規劃要有人工覆核、rollback 與監控。
- `s1d6_acceptance`：出現在 Day 06；補點焦點：KPI 與 acceptance criteria 要分開看：前者偏目標，後者偏交付門檻。

## L21203 AI 風險管理

- 規劃題量權重：`40` 題
- 題型來源：官方範圍 + 學習指引 + 樣題結構仿真
代表題：
- `s1d7_copyright_prevention`：出現在 Day 07, 11, 17；補點焦點：生成式 AI 法務風險通常要從流程治理，而非只從模型參數處理。
- `s1d7_supply_chain`：出現在 Day 07, 16；補點焦點：把『供應鏈』理解為所有外部依賴，不只是設備採購。
- `s1d7_adversarial_training`：出現在 Day 07, 19；補點焦點：把技術補強與流程治理分開看。
- `s1d7_transparency`：出現在 Day 07, 15, 20；補點焦點：記住 transparency、explainability、traceability 是一組常連動的治理概念。

## L21301 數據準備與模型選擇

- 規劃題量權重：`14` 題
- 題型來源：官方範圍 + 學習指引 + 樣題結構仿真
代表題：
- `s1d8_regression_fit`：出現在 Day 08, 12；補點焦點：先辨識目標變數型態：連續值選 regression，離散標籤選 classification。
- `s1d8_scaling`：出現在 Day 08, 15, 17；補點焦點：標準化、正規化與模型敏感度要建立連結。
- `s1d8_unsupervised_grouping`：出現在 Day 08；補點焦點：標籤有無，是分 supervised / unsupervised 的第一判斷點。
- `s1d8_feature_learning`：出現在 Day 08；補點焦點：結構化資料常做人工特徵；非結構化資料常做 representation learning。

## L21302 AI 技術系統集成與部署

- 規劃題量權重：`36` 題
- 題型來源：官方範圍 + 學習指引 + 樣題結構仿真
代表題：
- `s1d3_pruning`：出現在 Day 03；補點焦點：區分模型壓縮、訓練策略調整、資料工程三種不同問題。
- `s1d9_kubernetes`：出現在 Day 09, 11, 17；補點焦點：Kubernetes 是 orchestration，不是 model training tool。
- `s1d9_integration_testing`：出現在 Day 09, 16, 20；補點焦點：integration testing 看的是流程與介面，不是單一模型分數。
- `s1d9_drift_monitoring`：出現在 Day 09, 19；補點焦點：把 model drift 與 system metrics 區分開。

## L22101 敘述性統計與資料摘要技術

- 規劃題量權重：`14` 題
- 題型來源：官方範圍 + 學習指引 + 樣題結構仿真
代表題：
- `s2d1_descriptive_stats`：出現在 Day 01；補點焦點：中心趨勢與離散程度要分清。
- `s2d2_zscore`：出現在 Day 02, 16；補點焦點：熟記 Z-score 公式與意義。
- `s2d2_iqr`：出現在 Day 02, 15, 19；補點焦點：箱型圖、IQR、四分位數的關係要熟。
- `s2d2_outlier_choice`：出現在 Day 02；補點焦點：偏態資料先看 median 與 quartiles。

## L22102 機率分佈與資料分佈模型

- 規劃題量權重：`6` 題
- 題型來源：官方範圍 + 學習指引 + 樣題結構仿真
代表題：
- `s2d2_normal_distribution`：出現在 Day 02；補點焦點：常態分布的外型與位置關係要記熟。
- `s2d14_poisson`：出現在 Day 14, 16；補點焦點：Poisson 關鍵字：count、independent events、fixed rate。

## L22103 假設檢定與統計推論

- 規劃題量權重：`22` 題
- 題型來源：官方範圍 + 學習指引 + 樣題結構仿真
代表題：
- `s2d3_ttest`：出現在 Day 03, 11, 18；補點焦點：先判斷要比『平均數』還是『比例 / 類別』。
- `s2d3_anova`：出現在 Day 03, 12；補點焦點：題目出現三組以上平均數比較時，優先選 ANOVA。
- `s2d3_chisquare`：出現在 Day 03, 15；補點焦點：類別對類別的關係先想卡方。
- `s2d3_prop_test`：出現在 Day 03, 12, 18；補點焦點：先看目標是平均數還是比例。

## L22201 數據收集與清理

- 規劃題量權重：`24` 題
- 題型來源：官方範圍 + 學習指引 + 樣題結構仿真
代表題：
- `s2d1_year_float`：出現在 Day 01, 11, 19；補點焦點：理解 dtype 由內容而非欄位名稱決定。
- `s2d1_nullable_int`：出現在 Day 01, 11, 17；補點焦點：區分 Python / numpy 的整數型態與 pandas nullable integer。
- `s2d1_isna`：出現在 Day 01, 20；補點焦點：記住 pandas 缺值檢查常用 API：`isna` / `isnull`。
- `s2d1_dtype_cleanup`：出現在 Day 01；補點焦點：把 dtype cleanup 視為分析正確性的前置條件。

## L22202 數據儲存與管理

- 規劃題量權重：`14` 題
- 題型來源：官方範圍 + 學習指引 + 樣題結構仿真
代表題：
- `s2d13_graph_edge_property`：出現在 Day 13, 15, 18；補點焦點：圖資料庫的核心是節點、邊與屬性。
- `s2d13_rdf`：出現在 Day 13, 19；補點焦點：RDF、triple、ontology 是知識圖譜高頻詞。
- `s2d13_graph_vs_relational`：出現在 Day 13；補點焦點：多跳關係題先想 graph model。
- `s2d13_graph_query`：出現在 Day 13；補點焦點：圖資料庫的亮點是 traversal。

## L22203 數據處理技術與工具

- 規劃題量權重：`10` 題
- 題型來源：官方範圍 + 學習指引 + 樣題結構仿真
代表題：
- `s2d2_standardize_vs_normalize`：出現在 Day 02, 19；補點焦點：分清 standardization 與 normalization。
- `s2d5_datetime_cast`：出現在 Day 05；補點焦點：日期欄位若要做趨勢分析，先處理 datetime。
- `s2d5_label_vs_onehot`：出現在 Day 05；補點焦點：類別是否有序，決定編碼策略。
- `s2d8_scaler_pipeline`：出現在 Day 08；補點焦點：工程一致性也是資料分析能力的一部分。

## L22301 統計學在大數據中的應用

- 規劃題量權重：`70` 題
- 題型來源：官方範圍 + 學習指引 + 樣題結構仿真
代表題：
- `s2d4_roc`：出現在 Day 04, 11；補點焦點：ROC 與 PR curve 不要混。
- `s2d4_auc_interpret`：出現在 Day 04；補點焦點：AUC 與 accuracy 的意義要分清。
- `s2d7_fit_xy`：出現在 Day 07, 11, 17；補點焦點：記住 sklearn 介面慣例：X 在前、y 在後。
- `s2d7_coef_intercept`：出現在 Day 07, 12, 17；補點焦點：區分 `coef_` 與 `intercept_`。

## L22302 常見的大數據分析方法

- 規劃題量權重：`30` 題
- 題型來源：官方範圍 + 學習指引 + 樣題結構仿真
代表題：
- `s2d4_pca`：出現在 Day 04, 20；補點焦點：把 PCA 與 regression / classification 分清。
- `s2d4_dbscan`：出現在 Day 04；補點焦點：沒有標籤又有噪聲時，先想到 DBSCAN。
- `s2d4_kmeans_logic`：出現在 Day 04, 15；補點焦點：K-means 的關鍵字：centroid、最近中心、反覆更新。
- `s2d13_centrality`：出現在 Day 13；補點焦點：圖分析常考中心性、社群偵測、最短路徑。

## L22303 數據可視化工具

- 規劃題量權重：`20` 題
- 題型來源：官方範圍 + 學習指引 + 樣題結構仿真
代表題：
- `s2d6_groupby_sum`：出現在 Day 06, 16, 18；補點焦點：看到『總額』先找 sum，不要被 count 誤導。
- `s2d6_melt_barplot`：出現在 Day 06, 12, 17；補點焦點：寬表轉長表是資料視覺化常考轉換。
- `s2d6_nlargest`：出現在 Day 06, 18；補點焦點：top-N 題先看排序依據是什麼欄位。
- `s2d6_valuecounts`：出現在 Day 06；補點焦點：先分清題目要 count 還是要 measure aggregation。

## L22401 大數據與機器學習

- 規劃題量權重：`12` 題
- 題型來源：官方範圍 + 學習指引 + 樣題結構仿真
代表題：
- `s2d10_smote`：出現在 Day 10, 12, 17, 20；補點焦點：SMOTE、class weight、threshold tuning 是不平衡分類三個高頻補救方向。
- `s2d10_class_weight`：出現在 Day 10, 20；補點焦點：SMOTE 是資料層，class weight 是模型層。

## L22402 大數據在鑑別式 AI 中的應用

- 規劃題量權重：`2` 題
- 題型來源：官方範圍 + 學習指引 + 樣題結構仿真
代表題：
- `s2d13_knowledge_graph_use`：出現在 Day 13；補點焦點：把知識圖譜當成『關係結構化 + 可推理』的工具。
