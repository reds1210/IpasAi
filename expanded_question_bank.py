from __future__ import annotations

from pathlib import Path
from textwrap import dedent

import generate_ipas_reverse_pack as pack
import study_pack_lib as lib


ROOT = Path(__file__).resolve().parent
EXTENDED_DIR = ROOT / "extended"


def drill(
    key: str,
    title: str,
    subject: int,
    focus: str,
    recommended_after: str,
    items: list[dict],
) -> dict:
    return {
        "key": key,
        "title": title,
        "subject": subject,
        "focus": focus,
        "recommended_after": recommended_after,
        "items": items,
    }


DRILL_PRIORITY_OVERRIDES = {
    "subject-1-rag-nlp-drill": "A",
    "subject-1-governance-deploy-drill": "A",
    "subject-2-stats-core-drill": "A",
    "subject-2-python-cleaning-drill": "A",
    "subject-2-regression-eval-drill": "A",
    "subject-2-timeseries-graph-drill": "B",
    "subject-2-code-practice-drill": "A",
    "subject-2-pandas-sklearn-intensive-drill": "A",
    "subject-2-statsmodels-seaborn-timeseries-drill": "A",
}

DRILL_SOURCE_TIER_OVERRIDES = {
    "subject-2-public-patterns-mixed-drill": "public-pattern-derived",
}

DRILL_SOURCE_REF_OVERRIDES = {
    "subject-2-public-patterns-mixed-drill": [
        "sources/question-source-map.md｜AITerms、S 測驗、CCChen 題型整理",
        "sources/question-patterns.md｜公開題型轉寫規則",
    ],
}

DRILL_EVIDENCE_TAG_OVERRIDES = {
    "subject-2-public-patterns-mixed-drill": ["public-practice", "python-pattern", "stats-pattern"],
}


def drill_priority(drill_payload: dict) -> str:
    override = DRILL_PRIORITY_OVERRIDES.get(drill_payload["key"])
    if override:
        return override
    priorities = [pack.infer_item_priority(item) for item in drill_payload["items"]]
    if priorities.count("A") >= max(1, len(priorities) // 2):
        return "A"
    if "B" in priorities:
        return "B"
    return "C"


def drill_priority_summary(drill_payload: dict) -> str:
    counts = {"A": 0, "B": 0, "C": 0}
    for item in drill_payload["items"]:
        counts[pack.infer_item_priority(item)] = counts.get(pack.infer_item_priority(item), 0) + 1
    return f"A={counts['A']} / B={counts['B']} / C={counts['C']}"


def drill_source_tier(drill_payload: dict) -> str:
    return DRILL_SOURCE_TIER_OVERRIDES.get(drill_payload["key"], "official-derived")


def drill_source_refs(drill_payload: dict) -> list[str]:
    override = DRILL_SOURCE_REF_OVERRIDES.get(drill_payload["key"])
    if override:
        return override
    refs: list[str] = []
    for item in drill_payload["items"]:
        for ref in item.get("source_refs") or item.get("refs", []):
            if ref not in refs:
                refs.append(ref)
    if refs:
        return refs[:4]
    return [
        "sources/official-corpus.md｜官方樣題、公告試題與學習指引整理",
        "sources/scope-weight-map.md｜L-code 權重與高頻熱區",
    ]


def drill_evidence_tags(drill_payload: dict) -> list[str]:
    override = DRILL_EVIDENCE_TAG_OVERRIDES.get(drill_payload["key"])
    if override:
        return override
    tags: list[str] = []
    for item in drill_payload["items"]:
        for tag in item.get("evidence_tags", []):
            if tag not in tags:
                tags.append(tag)
    return tags or ["official-scope", "official-sample"]


DRILLS = [
    drill(
        "subject-1-rag-nlp-drill",
        "科目 1 加練｜RAG 與進階 NLP",
        1,
        "embedding 檢索、chunking、reranker、grounding",
        "建議在 Day 03、Day 11、Day 17 後加做",
        [
            pack.mc(
                "ex1_embedding_search",
                "L21103",
                "中",
                [
                    "若搜尋系統希望找出語意相近但未必共用相同關鍵字的文件，最合理的檢索方式為何？",
                    "使用者問題和知識庫文件常用不同字詞表達同一意思。若想改善召回，最值得優先加入哪種能力？",
                ],
                "將查詢與文件轉成 embedding 後做向量相似度檢索",
                ["只做完全相同字串比對", "按檔案大小排序文件", "隨機抽取前 10 份文件"],
                "embedding 檢索能抓語意鄰近關係，不必完全依賴關鍵字重疊。",
                ["完全字串比對容易漏掉同義改寫。", "檔案大小與語意相關性無關。", "隨機抽樣沒有檢索能力。"],
                ["RAG 的第一關通常是把語意相近文件找回來。", "keyword match 與 vector search 的差異要分清。"],
                ["sources/official-corpus.md｜生成式 AI 與檢索增強應用", "sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用"],
            ),
            pack.mc(
                "ex1_chunking_overlap",
                "L21103",
                "中",
                [
                    "在 RAG 建知識庫時，若 chunk 切得過大或過小都可能影響檢索品質。較合理的實務做法為何？",
                    "若你要切分長文件供檢索使用，哪種 chunking 策略通常比較穩健？",
                ],
                "依語意段落切 chunk，並保留適度 overlap",
                ["整份文件永遠不切", "每 3 個字固定切一段且不保留上下文", "只依頁碼平均切分，不看語意結構"],
                "以語意段落切分並保留少量 overlap，通常能兼顧檢索精準度與上下文完整性。",
                ["整份文件不切會讓檢索粒度太粗。", "過細切分會破壞上下文連貫。", "只看頁碼不看內容結構，常切斷完整語意。"],
                ["chunk size 與 overlap 都會影響 RAG 品質。", "切分粒度要跟語意單位對齊。"],
                ["sources/official-corpus.md｜生成式 AI 應用與資料處理", "sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用"],
            ),
            pack.mc(
                "ex1_reranker",
                "L21103",
                "中",
                [
                    "若第一階段檢索能找回大致相關文件，但排名常不夠準，下一步最合理的補強是什麼？",
                    "RAG 系統已能粗略召回候選文件，但最相關片段不一定排最前面。此時最常見的補強方向為何？",
                ],
                "先粗召回候選文件，再用 reranker 重新排序",
                ["把所有候選文件都直接塞進 prompt", "只提高 temperature", "只增加模型輸出字數"],
                "兩階段檢索常先做高召回，再用 reranker 改善前排結果的相關性。",
                ["全部塞進 prompt 會增加雜訊與成本。", "temperature 影響生成風格，不解決排序問題。", "輸出字數不會改善檢索排序品質。"],
                ["粗召回與精排序是常見的兩段式檢索思路。", "retrieval quality 與 generation settings 要分開看。"],
                ["sources/official-corpus.md｜生成式 AI 技術應用", "sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用"],
            ),
            pack.mc(
                "ex1_grounded_citation",
                "L21103",
                "中",
                [
                    "若你想降低 RAG 回答看似合理但無法核對來源的風險，最有效的輸出要求是什麼？",
                    "內部知識助理常回答得很像真的，但使用者無法知道依據從何而來。若先補一個控管，最值得做什麼？",
                ],
                "要求答案附上對應片段或引用來源",
                ["只要求回答更流暢", "只提高模型溫度", "只限制回答字數更短"],
                "附帶來源或片段能讓使用者快速核對回答是否 grounded。",
                ["流暢不等於可驗證。", "提高溫度常增加隨機性。", "縮短字數不會自動增加可追溯性。"],
                ["grounding 與 citation 是降低幻覺的重要手段。", "能查證來源，才更適合企業場景。"],
                ["sources/official-corpus.md｜生成式 AI 應用與風險", "sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用"],
            ),
        ],
    ),
    drill(
        "subject-1-governance-deploy-drill",
        "科目 1 加練｜治理與部署補強",
        1,
        "PII、red teaming、人工覆核、可觀測性",
        "建議在 Day 07、Day 09、Day 18 後加做",
        [
            pack.mc(
                "ex2_pii_masking",
                "L21203",
                "中",
                [
                    "若要把客服紀錄送到外部 LLM 服務分析，但內容含姓名、電話、身分證等資訊，最先該補哪個控管？",
                    "企業想把內部案例交給第三方生成式 AI 做摘要。若你要先降個資風險，最優先的作法是什麼？",
                ],
                "先做去識別化或 PII masking 再送入模型",
                ["直接全量送出，事後再刪紀錄", "只調整提示詞，不處理原資料", "只在輸出端檢查髒話與敏感字"],
                "個資風險主要來自原始輸入外流，因此前處理去識別化是第一道關卡。",
                ["事後刪紀錄無法回收已外送的敏感資料。", "提示詞無法替代資料遮罩。", "只檢查輸出忽略了輸入外送風險。"],
                ["PII masking 是外部模型接入前的高頻治理題。", "輸入風險與輸出風險要分開看。"],
                ["sources/official-corpus.md｜AI 風險管理與合規", "sources/scope-weight-map.md｜L21203 AI 風險管理"],
            ),
            pack.mc(
                "ex2_red_teaming",
                "L21203",
                "中",
                [
                    "若企業擔心內部助理上線後遭提示注入、越獄或惡意繞規，正式發布前最值得先做什麼？",
                    "你準備把生成式 AI 服務開給大量員工使用。若要在上線前先找出安全弱點，最合理的測試方式為何？",
                ],
                "進行 red teaming 與對抗式提示測試",
                ["只看平均回應速度", "只檢查 UI 顏色是否一致", "只在上線後等使用者回報"],
                "對抗式測試能提早暴露越獄、洩漏與不當回應風險。",
                ["速度不是安全健壯性的主指標。", "UI 一致性與模型安全是不同層面。", "完全等上線後再發現，風險成本更高。"],
                ["red teaming 常用於高風險 LLM 上線前檢查。", "安全評估不只看 accuracy。"],
                ["sources/official-corpus.md｜生成式 AI 風險與治理", "sources/scope-weight-map.md｜L21203 AI 風險管理"],
            ),
            pack.mc(
                "ex2_human_review",
                "L21203",
                "中",
                [
                    "若 AI 輸出會影響授信、醫療建議或法務判斷，最合理的決策流程安排為何？",
                    "在高影響決策場景中，企業若要使用 AI 輔助而非放大風險，最應保留哪個機制？",
                ],
                "保留人工覆核與最終裁量權",
                ["只要模型分數夠高就完全自動決策", "只做一次 demo 後就直接去人工", "把所有風險寫進免責聲明即可"],
                "高風險場景通常需要 human-in-the-loop 來降低誤判與責任風險。",
                ["高分模型也可能在特殊案例失準。", "demo 不能取代持續治理與覆核。", "免責聲明不能替代實質控管。"],
                ["high-impact use case 常優先想到人工覆核。", "human-in-the-loop 是治理題高頻關鍵字。"],
                ["sources/official-corpus.md｜AI 風險治理與責任", "sources/scope-weight-map.md｜L21203 AI 風險管理"],
            ),
            pack.mc(
                "ex2_observability",
                "L21302",
                "中",
                [
                    "若生成式 AI 服務已上線，為了盡早發現品質退化與系統異常，監控指標最不應只看哪一個單一維度？",
                    "團隊說只要看平均延遲就好，不必再看錯誤率、fallback 比例或品質抽查。這個觀念最主要錯在哪裡？",
                ],
                "上線後要同時看品質、延遲、錯誤率與 fallback rate",
                ["只看平均延遲即可", "只看 GPU 使用率即可", "只看登入人數即可"],
                "可觀測性要同時涵蓋服務穩定、輸出品質與降級行為，而不是只盯單一系統指標。",
                ["平均延遲無法代表輸出品質與降級情況。", "GPU 使用率是資源資訊，不足以涵蓋體驗與品質。", "登入人數更不是模型品質指標。"],
                ["LLM/MLOps 監控要同時看系統與內容品質。", "fallback rate 是實務上很有用的風險訊號。"],
                ["sources/official-corpus.md｜系統集成與部署監控", "sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署"],
            ),
        ],
    ),
    drill(
        "subject-2-stats-core-drill",
        "科目 2 加練｜統計推論核心",
        2,
        "第一二類錯誤、信賴區間、power",
        "建議在 Day 03、Day 11、Day 16 後加做",
        [
            pack.mc(
                "ex3_type1_error",
                "L22103",
                "中",
                [
                    "第一類錯誤（Type I error）最接近哪個意思？",
                    "若其實新策略沒有提升效果，但檢定結果卻說有顯著差異，這最接近哪種錯誤？",
                ],
                "把原本為真的虛無假設誤判為應被拒絕",
                ["把真實存在的效果誤判為不存在", "樣本數太大", "平均數一定算錯"],
                "Type I error 就是假陽性，實際無效果卻錯判為有顯著效果。",
                ["這是 Type II error 的方向。", "樣本數大小會影響錯誤率與 power，但不是 Type I 的定義。", "平均數算錯是資料或運算問題，不是統計定義。"],
                ["Type I = false positive；Type II = false negative。", "把『誤拒真 H0』這句話背熟。"],
                ["sources/official-corpus.md｜假設檢定與統計推論", "sources/scope-weight-map.md｜L22103 假設檢定與統計推論"],
            ),
            pack.mc(
                "ex3_type2_error",
                "L22103",
                "中",
                [
                    "第二類錯誤（Type II error）最接近哪個意思？",
                    "若新功能其實真的有效，但檢定卻沒檢出差異，這最接近哪種錯誤？",
                ],
                "原本應被拒絕的虛無假設卻沒有被拒絕",
                ["把原本為真的虛無假設誤拒絕", "顯著水準一定設錯", "所有樣本都必須獨立"],
                "Type II error 就是假陰性，有效果卻沒檢出來。",
                ["這是 Type I error 的方向。", "顯著水準設置會影響錯誤率，但不是 Type II 的定義。", "獨立性是檢定假設之一，不是 Type II 的直接定義。"],
                ["Type II = false negative。", "power 與 Type II error 彼此相關。"],
                ["sources/official-corpus.md｜假設檢定與統計推論", "sources/scope-weight-map.md｜L22103 假設檢定與統計推論"],
            ),
            pack.mc(
                "ex3_confidence_interval",
                "L22103",
                "中",
                [
                    "若某差異的 95% 信賴區間橫跨 0，最常見的保守解讀為何？",
                    "A/B 測試估計值的 95% CI 為 `[-0.02, 0.05]`。在常見顯著水準下，最合理的判斷是什麼？",
                ],
                "在該信心水準下，效果尚未明確與 0 區分開",
                ["代表效果一定為 0", "代表新方案一定比較差", "代表樣本資料不能用"],
                "若信賴區間跨 0，通常表示在該水準下無法明確排除零效果。",
                ["CI 跨 0 不等於效果絕對為 0。", "區間跨 0 不足以直接判定方向一定較差。", "資料仍可用，只是證據不夠強。"],
                ["CI 與顯著性解讀要連在一起。", "跨 0 常代表證據不足，不是絕對沒有效果。"],
                ["sources/official-corpus.md｜統計推論與效果解讀", "sources/scope-weight-map.md｜L22103 假設檢定與統計推論"],
            ),
            pack.mc(
                "ex3_power_sample",
                "L22103",
                "中",
                [
                    "若你希望在真實效果存在時更容易檢出差異，哪個方向通常最直接？",
                    "研究團隊抱怨『明明可能有差異，但一直檢不出來』。若先做一個常見補強，最合理的是什麼？",
                ],
                "在其他條件近似不變時，增加樣本數以提升檢定 power",
                ["一律把顯著水準改成 0.5", "完全不做實驗設計，只多看一次 p-value", "把所有異常值都直接刪光"],
                "增加樣本數常能降低估計不穩定性，讓真實效果較容易被檢出。",
                ["顯著水準 0.5 會讓假陽性嚴重失控。", "只反覆看 p-value 不會系統性提升設計品質。", "粗暴刪異常值可能扭曲結果。"],
                ["power 與樣本數常一起考。", "不要用放寬門檻取代改善設計。"],
                ["sources/official-corpus.md｜統計推論與檢定", "sources/scope-weight-map.md｜L22103 假設檢定與統計推論"],
            ),
        ],
    ),
    drill(
        "subject-2-python-cleaning-drill",
        "科目 2 加練｜Python 資料清理",
        2,
        "merge、重複值、日期轉型、transform",
        "建議在 Day 05、Day 06、Day 17 後加做",
        [
            pack.mc(
                "ex4_left_join",
                "L22203",
                "中",
                [
                    "若你要把會員主表接上交易摘要，但不希望因沒有交易紀錄而把會員列弄丟，較合理的 join 是哪一種？",
                    "分析師希望合併兩張表時保留左表全部資料列，即使右表有些 key 對不到也沒關係。最適合用哪種 join？",
                ],
                "left join，保留左表全部列",
                ["inner join，因為最乾淨", "cross join，因為資料最多", "只用 concat 不看 key"],
                "left join 的核心就是保留左表所有列，右表對不到時以缺值補上。",
                ["inner join 會丟掉對不到 key 的左表列。", "cross join 會產生笛卡兒積，不符合主鍵合併需求。", "concat 只是拼接，不等於按 key 關聯。"],
                ["join 題先判斷『哪些列一定要留下』。", "left / inner / outer 的差異要熟。"],
                ["sources/official-corpus.md｜數據處理技術與工具", "sources/scope-weight-map.md｜L22203 數據處理技術與工具"],
            ),
            pack.mc(
                "ex4_drop_duplicates",
                "L22201",
                "中",
                [
                    "若同一客戶可能有多筆重複資料，但你想依 `customer_id` 去重並保留第一筆，最常見的 pandas 作法為何？",
                    "資料表裡同一個主鍵出現重複列。若你只想留下第一筆紀錄，哪種操作方向最合理？",
                ],
                "使用 `drop_duplicates(subset=['customer_id'], keep='first')`",
                ["直接 `sort_values()` 就會自動去重", "只要 `reset_index()` 就會消失重複列", "把整個 DataFrame 轉成字串再比對"],
                "`drop_duplicates` 可依指定欄位判定重複，並控制保留第一筆或最後一筆。",
                ["排序不會自動刪除重複。", "重設索引不會改變資料重複性。", "轉字串比對不是 pandas 的標準清理流程。"],
                ["subset 與 keep 是去重題常考參數。", "先想重複判定依據是哪個 key。"],
                ["sources/official-corpus.md｜數據收集與清理", "sources/scope-weight-map.md｜L22201 數據收集與清理"],
            ),
            pack.mc(
                "ex4_to_datetime",
                "L22203",
                "中",
                [
                    "若欄位目前是字串日期，例如 `2026-04-27`，而你接下來要萃取年月或計算時間差，最合理的第一步是什麼？",
                    "資料欄位看起來像日期，但 dtype 仍是 `object`。若後續要做時間分析，最值得先做哪個轉換？",
                ],
                "先用 `pd.to_datetime()` 轉成 datetime 型態",
                ["直接對字串做平均數", "只把欄位名稱改成 date", "先轉成 category 以加速時間差運算"],
                "日期分析前通常先把字串轉成 datetime，後續才能穩定做時間屬性與差值運算。",
                ["字串無法直接做合理的日期平均。", "改欄位名不會改變資料型態。", "category 不適合作為日期運算主型態。"],
                ["date parsing 是資料清理常考基本功。", "看到 object 日期欄，先想到 `to_datetime`。"],
                ["sources/official-corpus.md｜數據處理技術與工具", "sources/scope-weight-map.md｜L22203 數據處理技術與工具"],
            ),
            pack.mc(
                "ex4_groupby_transform",
                "L22203",
                "中",
                [
                    "若你想把『每個部門的平均薪資』回填到原始每一列，之後再計算個人薪資與部門平均的差距，較合理的方法方向為何？",
                    "分析師需要把群組統計量保留在原表同樣列數上，而不是變成彙總表。這時最常想到哪個 pandas 方法？",
                ],
                "使用 `groupby(...).transform(...)` 把群組統計回填原列",
                ["只用 `groupby().agg()` 然後假設列數不會改變", "只用 `value_counts()`", "直接把整張表 `dropna()`"],
                "`transform` 會回傳與原表等長的結果，適合把群組統計量貼回每列。",
                ["`agg()` 通常會產生彙總表，不一定保持原列數。", "`value_counts()` 是計數，不是通用群組回填工具。", "`dropna()` 與群組統計回填無關。"],
                ["transform 與 agg 的輸出形狀差異要熟。", "需要保留原列數時先想 transform。"],
                ["sources/official-corpus.md｜數據處理技術與工具", "sources/scope-weight-map.md｜L22203 數據處理技術與工具"],
            ),
        ],
    ),
    drill(
        "subject-2-regression-eval-drill",
        "科目 2 加練｜回歸與評估補強",
        2,
        "資料洩漏、VIF、RMSE/MAE、Adjusted R²",
        "建議在 Day 07、Day 08、Day 17 後加做",
        [
            pack.mc(
                "ex5_scaler_leakage",
                "L22301",
                "中",
                [
                    "若你在做監督式學習時需要標準化特徵，為避免資料洩漏，最合理的流程是什麼？",
                    "團隊先對整份資料 `fit_transform` 再切 train/test。這個做法的主要問題是什麼？",
                ],
                "先切分 train/test，再只用 train fit scaler，最後套到 test",
                ["先對全資料 fit scaler 才最公平", "先看 test 再決定 train 的縮放方式", "完全不切資料，直接在全資料上報分數"],
                "若先看過全資料分布再縮放，測試集資訊就提前滲入訓練流程。",
                ["全資料先 fit 會造成 leakage。", "先看 test 決定轉換更是直接洩漏。", "不切資料無法評估泛化。"],
                ["preprocessing 也可能 leakage，不只模型本身。", "fit 在 train，transform 套到 test 是標準流程。"],
                ["sources/official-corpus.md｜模型驗證與統計應用", "sources/scope-weight-map.md｜L22301 統計學在大數據中的應用"],
            ),
            pack.mc(
                "ex5_vif_multicollinearity",
                "L22301",
                "中",
                [
                    "若線性迴歸中多個特徵高度相關，想量化多重共線性的程度，最常見的指標是哪一個？",
                    "你懷疑特徵之間彼此太像，導致係數不穩。若想先看一個經典診斷量，最合理的是什麼？",
                ],
                "VIF（Variance Inflation Factor）",
                ["AUC", "Silhouette score", "Lift chart"],
                "VIF 是多重共線性的常見診斷指標，值高代表該特徵可被其他特徵高度解釋。",
                ["AUC 是分類辨識能力指標。", "Silhouette score 用於分群評估。", "Lift chart 多見於分類/行銷排序評估。"],
                ["共線性題優先想到 VIF。", "高 VIF 不一定要刪欄，但代表係數解讀要小心。"],
                ["sources/official-corpus.md｜回歸與統計分析應用", "sources/scope-weight-map.md｜L22301 統計學在大數據中的應用"],
            ),
            pack.mc(
                "ex5_rmse_vs_mae",
                "L22301",
                "中",
                [
                    "若你特別不希望模型出現少數非常大的預測誤差，評估時通常會偏向哪一種指標？",
                    "兩個模型平均表現差不多，但其中一個偶爾會犯很大的錯。若你想更重懲大誤差，應優先看哪種指標？",
                ],
                "RMSE，因為它對大誤差懲罰更重",
                ["MAE，因為它永遠比 RMSE 更嚴格", "Accuracy，因為任何任務都可用", "只看平均數，不需要誤差指標"],
                "RMSE 會平方誤差，因此對少數大錯誤更敏感。",
                ["MAE 較線性，對極端大誤差懲罰沒 RMSE 那麼重。", "Accuracy 不是回歸主指標。", "只看平均數無法評估預測誤差。"],
                ["MAE 線性、RMSE 重罰大誤差，這是高頻比較題。", "先看業務在意的是穩定還是避免大錯。"],
                ["sources/official-corpus.md｜模型評估方法", "sources/scope-weight-map.md｜L22301 統計學在大數據中的應用"],
            ),
            pack.mc(
                "ex5_adjusted_r2",
                "L22301",
                "中",
                [
                    "若你想比較不同特徵數量的線性迴歸模型，並避免因亂加欄位而誤以為表現變好，較適合看的指標是哪個？",
                    "一般 R² 加特徵後常不下降。若你要在比較模型時對多餘特徵做一些懲罰，應優先參考哪個量？",
                ],
                "Adjusted R²",
                ["單看訓練集 Accuracy", "只看資料列數", "只看欄位名稱長度"],
                "Adjusted R² 會考慮特徵數量，避免單純因增加欄位而讓指標看起來變好。",
                ["Accuracy 不是回歸主指標。", "資料列數不是模型擬合品質指標。", "欄位名稱長度與模型評估無關。"],
                ["R² 與 Adjusted R² 的用途差異要分清。", "比較不同欄位數模型時，Adjusted R² 更有參考價值。"],
                ["sources/official-corpus.md｜回歸與模型評估", "sources/scope-weight-map.md｜L22301 統計學在大數據中的應用"],
            ),
        ],
    ),
    drill(
        "subject-2-timeseries-graph-drill",
        "科目 2 加練｜時間序列與圖分析",
        2,
        "time split、seasonal naive、centrality、shortest path",
        "建議在 Day 13、Day 14、Day 18 後加做",
        [
            pack.mc(
                "ex6_time_split_order",
                "L22302",
                "中",
                [
                    "若資料是時間序列，做訓練/測試切分時最重要的原則通常是什麼？",
                    "你要評估銷售預測模型。若把 2026 年資料隨機打亂分到 train 與 test，主要風險是什麼？",
                ],
                "保留時間順序，避免把未來資訊洩漏到過去",
                ["一律隨機切分最公平", "先看測試表現再決定資料切法", "只留最後一筆做測試即可"],
                "時間序列的核心是時序依賴，隨機打亂常會讓未來資訊洩漏到訓練資料。",
                ["隨機切分常破壞時序結構。", "先看測試再決定切法會造成驗證偏誤。", "只留最後一筆樣本太不穩定。"],
                ["time split 與 leakage 常一起考。", "時間序列驗證與一般 IID 資料不同。"],
                ["sources/official-corpus.md｜常見的大數據分析方法", "sources/scope-weight-map.md｜L22302 常見的大數據分析方法"],
            ),
            pack.mc(
                "ex6_seasonal_naive",
                "L22302",
                "中",
                [
                    "若序列有明顯每週或每月重複型態，建立第一個 baseline 時常見且合理的做法是什麼？",
                    "面對強季節性資料，若你想先有一個簡單但有意義的基準模型，哪種方向最自然？",
                ],
                "使用 seasonal naive，拿上一個相同季節位置的值當預測",
                ["直接永遠預測整體平均數", "只看第一筆資料後固定不變", "把時間戳欄位刪掉再說"],
                "若季節性很強，seasonal naive 往往是合理 baseline，能提供最低比較基準。",
                ["整體平均數通常忽略季節波動。", "只看第一筆資料沒有反映近期與週期資訊。", "刪掉時間欄會失去序列核心結構。"],
                ["time series baseline 題常考 naive / seasonal naive。", "先有 baseline，才能判斷複雜模型是否真的有幫助。"],
                ["sources/official-corpus.md｜時間序列分析主題", "sources/scope-weight-map.md｜L22302 常見的大數據分析方法"],
            ),
            pack.mc(
                "ex6_graph_centrality",
                "L22302",
                "中",
                [
                    "若你想找出社群網路中最有影響力、最值得優先關注的節點，通常會先看哪一類圖分析指標？",
                    "企業知識網絡裡，想先定位關鍵專家或關鍵中繼節點，最合理先做哪種分析？",
                ],
                "中心性（centrality）分析",
                ["只比較節點名稱長短", "只統計資料列數", "只看節點顏色是否一致"],
                "centrality 用來衡量節點在圖中的重要性或位置，是找關鍵節點的常見起點。",
                ["名稱長短不代表網路影響力。", "資料列數不反映圖結構位置。", "顏色只是視覺屬性，不是分析方法。"],
                ["關鍵節點題先想 centrality。", "不同 centrality 代表不同重要性定義。"],
                ["sources/official-corpus.md｜常見的大數據分析方法", "sources/scope-weight-map.md｜L22302 常見的大數據分析方法"],
            ),
            pack.mc(
                "ex6_shortest_path",
                "L22202",
                "中",
                [
                    "若你想回答『A 透過哪些關係最短連到 B』，圖資料平台最重要的能力是什麼？",
                    "知識圖譜要查某專家如何經由主題、專利與產品問題間接連結到另一節點，哪種查詢能力最對題？",
                ],
                "支援 shortest path / path traversal 類查詢",
                ["只支援單欄位排序", "只支援圖表配色設定", "只支援匯出成圖片"],
                "圖模型的一大價值就是高效做路徑遍歷與關係鏈查詢。",
                ["單欄位排序不是關係鏈查詢。", "配色是視覺層，不是資料查詢能力。", "匯出圖片不等於能回答關係路徑問題。"],
                ["path traversal 是圖資料庫高頻考點。", "看到『經由哪些關係』時就要想到路徑查詢。"],
                ["sources/official-corpus.md｜圖資料庫與知識圖譜主題", "sources/scope-weight-map.md｜L22202 數據儲存與管理"],
            ),
        ],
    ),
    drill(
        "subject-2-code-practice-drill",
        "科目 2 加練｜程式碼題型",
        2,
        "pandas、seaborn、sklearn、statsmodels code block 判讀",
        "建議在 Day 06、Day 08、Day 17 後加做",
        [
            pack.mc(
                "ex7_groupby_sort",
                "L22203",
                "中",
                [
                    "閱讀下列程式碼後，哪個敘述最正確？",
                    "若你要根據這段輸出快速判斷哪個 team 的總 sales 最高，哪個選項正確？",
                ],
                "程式先依 `team` 分組加總 `sales`，再依總銷售額由大到小排序，因此 `B` 會排在 `A` 前面，且總 sales 為 35。",
                [
                    "`A` 的總 sales 為 35，因此輸出會先看到 `A`。",
                    "這段程式是在計算每個 `region` 的平均 sales，而不是依 `team` 加總。",
                    "因為用了 `as_index=False`，所以結果不會真的做分組，只會保留原始列順序。",
                ],
                "`groupby(...)[col].sum()` 先做分組彙總，`sort_values(..., ascending=False)` 再把總量大的群組排在前面。這是 Subject 2 很常見的資料處理與輸出判讀題型。",
                [
                    "`A` 的 sales 是 10 + 15 = 25，不是 35；35 是 `B` 的總和。",
                    "程式明確是 `groupby(\"team\")[\"sales\"].sum()`，不是對 `region` 做平均。",
                    "`as_index=False` 的作用是讓 `team` 保留為一般欄位，不是取消分組。",
                ],
                [
                    "補強 `groupby`、`sum`、`sort_values` 的基本輸出判讀。",
                    "補強 `as_index=False` 與彙總表結構的差異。",
                ],
                [
                    "sources/official-corpus.md｜數據處理技術與工具",
                    "sources/scope-weight-map.md｜L22203 數據處理技術與工具",
                ],
                code=dedent(
                    """
                    import pandas as pd

                    df = pd.DataFrame({
                        "team": ["A", "A", "B", "B", "B"],
                        "sales": [10, 15, 7, 8, 20],
                        "region": ["N", "S", "N", "S", "N"],
                    })

                    out = (
                        df.groupby("team", as_index=False)["sales"]
                        .sum()
                        .sort_values("sales", ascending=False)
                    )
                    print(out)
                    """
                ),
            ),
            pack.mc(
                "ex7_left_merge_nan",
                "L22203",
                "中",
                [
                    "閱讀下列程式碼後，哪個敘述最正確？",
                    "如果這題出成 merge 後缺值判讀題，哪個選項是正解？",
                ],
                "因為使用 `how=\"left\"`，所以 `orders` 的列都會保留；`customer_id=103` 在 `vip_map` 找不到對應值，因此 `vip` 會出現 1 個 `NaN`。",
                [
                    "因為 `merge` 預設會丟掉對不到 key 的列，所以結果中不會看到 `customer_id=103`。",
                    "`vip` 欄位不會出現缺值，因為 pandas 會自動把找不到的值補成 `False`。",
                    "這段程式等同於 `inner join`，所以只會留下兩筆有對到 `customer_id` 的資料。",
                ],
                "`left join` 是最常考的資料整併觀念之一。左表所有列都保留，右表只提供能對上的欄位值；對不到的部分會變成缺值，必須後續再判斷是否 `fillna` 或另做處理。",
                [
                    "會丟掉對不到 key 的列的是 `inner join`，不是 `left join`。",
                    "pandas 不會自行把找不到的類別補成 `False`；找不到就是 `NaN`。",
                    "題目明確寫了 `how=\"left\"`，所以不會退化成 `inner join`。",
                ],
                [
                    "補強 `left / inner / outer join` 的保留列差異。",
                    "補強 merge 後缺值來源與 `NaN` 判讀。",
                ],
                [
                    "sources/official-corpus.md｜數據處理技術與工具",
                    "sources/scope-weight-map.md｜L22203 數據處理技術與工具",
                ],
                code=dedent(
                    """
                    import pandas as pd

                    orders = pd.DataFrame({
                        "customer_id": [101, 102, 103],
                        "amount": [200, 150, 300],
                    })
                    vip_map = pd.DataFrame({
                        "customer_id": [101, 102],
                        "vip": ["Y", "N"],
                    })

                    merged = orders.merge(vip_map, on="customer_id", how="left")
                    print(merged)
                    print(merged["vip"].isna().sum())
                    """
                ),
            ),
            pack.mc(
                "ex7_linear_regression_coef",
                "L22301",
                "中",
                [
                    "閱讀下列 `sklearn` 程式碼後，哪個敘述最正確？",
                    "若考題要你判讀 `coef_` 與 `intercept_`，哪個選項正確？",
                ],
                "`y = 5 + 2x`，因此模型訓練後的 `coef_` 會接近 2，`intercept_` 會接近 5。這代表 `x` 每增加 1，預測值平均增加約 2。",
                [
                    "`coef_` 會接近 5，`intercept_` 會接近 2，因為截距與斜率在 sklearn 會顛倒儲存。",
                    "`coef_` 會是 0，因為資料筆數太少，線性回歸無法估計參數。",
                    "`intercept_` 一定是 0，因為 `LinearRegression()` 預設不估計截距。",
                ],
                "`coef_` 對應斜率，`intercept_` 對應截距，這是 Subject 2 高頻程式題。考法通常不是要你手算，而是要你理解參數對模型的意義與方向。",
                [
                    "sklearn 不會顛倒儲存斜率與截距；`coef_` 就是斜率，`intercept_` 就是截距。",
                    "線性回歸不會因為只有 4 筆資料就無法估計；只要資料形狀正確就能擬合。",
                    "`LinearRegression()` 預設 `fit_intercept=True`，會估計截距。",
                ],
                [
                    "補強 `coef_`、`intercept_` 與線性關係的對應。",
                    "補強 `fit(X, y)` 後常見輸出欄位的判讀。",
                ],
                [
                    "sources/official-corpus.md｜模型訓練與評估",
                    "sources/scope-weight-map.md｜L22301 模型訓練與效能評估",
                ],
                code=dedent(
                    """
                    import numpy as np
                    from sklearn.linear_model import LinearRegression

                    X = np.array([[1], [2], [3], [4]])
                    y = np.array([7, 9, 11, 13])  # y = 5 + 2x

                    model = LinearRegression()
                    model.fit(X, y)

                    print(model.coef_)
                    print(model.intercept_)
                    """
                ),
            ),
            pack.mc(
                "ex7_statsmodels_pvalue",
                "L22103",
                "中",
                [
                    "閱讀下列 `statsmodels` 輸出片段後，哪個敘述最正確？",
                    "若題目要你判讀 OLS 的 `p-value`，哪個選項是合理結論？",
                ],
                "在顯著水準 0.05 下，`ad_spend` 的 `p-value = 0.010`，可視為對 `y` 有顯著關聯；`discount` 的 `p-value = 0.410`，則不能說有顯著效果。",
                [
                    "`discount` 比 `ad_spend` 更顯著，因為它的係數比較小。",
                    "只要 `p-value` 大於 0.05，就代表變數一定對 `y` 有正向效果。",
                    "`const` 的 `p-value` 顯著，就代表所有自變數都一定顯著。",
                ],
                "`p-value` 的核心是顯著性判讀，不是看係數大小。這題常搭配 `OLS`、`add_constant` 與表格輸出一起考，重點是知道哪些變數能支持「存在統計上顯著關聯」的說法。",
                [
                    "顯著性不是看係數絕對值大小，而是看對應的 `p-value` 是否低於顯著水準。",
                    "`p-value` 大於 0.05 通常表示沒有足夠證據拒絕虛無假設，不是證明正向效果。",
                    "截距顯著不代表所有自變數都顯著，變數要各自判讀。",
                ],
                [
                    "補強 OLS 輸出中 `p-value` 的判讀。",
                    "補強「顯著」與「效果大小」是不同概念。",
                ],
                [
                    "sources/official-corpus.md｜假設檢定與統計推論",
                    "sources/scope-weight-map.md｜L22103 假設檢定與統計推論",
                ],
                code=dedent(
                    """
                    import pandas as pd
                    import statsmodels.api as sm

                    X = pd.DataFrame({
                        "ad_spend": [1, 2, 3, 4, 5, 6],
                        "discount": [0, 0, 1, 1, 0, 1],
                    })
                    y = pd.Series([11, 13, 16, 18, 19, 22])

                    X = sm.add_constant(X)
                    model = sm.OLS(y, X).fit()

                    print(model.pvalues)
                    # const       0.002
                    # ad_spend    0.010
                    # discount    0.410
                    """
                ),
            ),
            pack.mc(
                "ex7_seaborn_barplot_sum",
                "L22303",
                "中",
                [
                    "閱讀下列 `seaborn` 程式碼後，哪個敘述最正確？",
                    "如果這題考的是圖表函式選型與輸出意義，哪個選項正確？",
                ],
                "這段程式會畫出各 `channel` 的 `orders` 總量比較圖；因為使用 `barplot(..., estimator=sum)`，重點是加總值，不是每個通路出現了幾筆資料。",
                [
                    "這會等同於 `countplot`，所以柱高只代表每個 `channel` 的筆數。",
                    "因為 `estimator=sum`，圖上會直接顯示每筆資料的原始折線，不會做彙總。",
                    "這段程式無法執行，因為 `barplot` 不接受 `y` 欄位。",
                ],
                "`countplot` 與 `barplot` 的差別是 Subject 2 很常見的干擾點。只要看到 `estimator=sum` 或 `mean`，就要想到這是聚合後的數值比較，而不是單純筆數統計。",
                [
                    "`countplot` 看的是筆數；這題明確用 `barplot` 加總 `orders`。",
                    "`barplot` 會先按類別聚合 `y`，不是把每筆資料直接畫成折線。",
                    "`barplot` 當然可以接受 `x` 與 `y` 欄位，這正是其常見用法。",
                ],
                [
                    "補強 `countplot`、`barplot`、`estimator` 的差異。",
                    "補強圖表選型時要先確認是在比較筆數還是聚合值。",
                ],
                [
                    "sources/official-corpus.md｜數據可視化工具",
                    "sources/scope-weight-map.md｜L22303 數據可視化工具",
                ],
                code=dedent(
                    """
                    import pandas as pd
                    import seaborn as sns

                    df = pd.DataFrame({
                        "channel": ["web", "web", "store", "store", "app"],
                        "orders": [120, 80, 90, 70, 60],
                    })

                    sns.barplot(data=df, x="channel", y="orders", estimator=sum)
                    """
                ),
            ),
            pack.mc(
                "ex7_threshold_recall",
                "L22401",
                "中",
                [
                    "閱讀下列程式碼後，若團隊最在意少漏抓正類，哪個敘述最正確？",
                    "如果這題考的是 threshold 調整效果判讀，哪個選項正確？",
                ],
                "把門檻從 `0.5` 降到 `0.3`，通常會讓更多樣本被判成正類，因此 recall 常會上升或至少不下降，但 false positive 也可能增加。",
                [
                    "把門檻從 `0.5` 降到 `0.3`，recall 一定下降，因為模型會更保守。",
                    "只要降低 threshold，precision 與 recall 一定會同時上升。",
                    "threshold 只影響顯示格式，不會改變任何預測類別。",
                ],
                "不平衡資料題常考 threshold tuning。考點不是背公式，而是理解門檻下修會放寬正類判定條件，於是較容易抓到真正例，同時也更容易引入假陽性。",
                [
                    "降低 threshold 不是更保守，而是更容易判成正類，所以 recall 通常不會下降。",
                    "precision 與 recall 經常存在 trade-off，不會保證同時上升。",
                    "threshold 直接影響最終 `pred` 類別，是分類決策的一部分。",
                ],
                [
                    "補強 threshold tuning 對 recall / precision 的影響。",
                    "補強不平衡資料時以商業目標決定評估指標。",
                ],
                [
                    "sources/official-corpus.md｜不平衡資料與模型調整",
                    "sources/scope-weight-map.md｜L22401 模型優化與調校",
                ],
                code=dedent(
                    """
                    y_true = [1, 1, 1, 0, 0]
                    prob = [0.92, 0.81, 0.63, 0.44, 0.31]

                    pred_05 = [1 if p >= 0.5 else 0 for p in prob]
                    pred_03 = [1 if p >= 0.3 else 0 for p in prob]

                    print(pred_05)
                    print(pred_03)
                    """
                ),
            ),
        ],
    ),
    drill(
        "subject-2-pandas-sklearn-intensive-drill",
        "科目 2 加練｜pandas + sklearn 程式強化",
        2,
        "缺值補值、one-hot、stratify、Pipeline、cross validation、PCA、feature importance、group transform",
        "建議在 Day 06、Day 08、Day 17、Day 18 後加做",
        [
            pack.mc(
                "ex8_fillna_median",
                "L22203",
                "中",
                [
                    "閱讀下列程式碼後，哪個敘述最正確？",
                    "如果這題考的是缺值補值策略與輸出判讀，哪個選項正確？",
                ],
                "`income` 欄位中的缺值會被中位數補上；在這組資料中中位數是 60000，因此 `filled.loc[1, \"income\"]` 會是 60000。",
                [
                    "程式會用平均數補值，所以缺值會被補成 65000。",
                    "`fillna` 只能處理字串欄位，這段程式會報錯。",
                    "補值後 `filled` 與原始 `df` 完全相同，缺值不會改變。",
                ],
                "`median()` 與 `mean()` 常被混淆。這題的核心是看懂 `fillna(df[col].median())` 的意義，以及為什麼偏態或離群值明顯時，中位數常比平均數穩定。",
                [
                    "程式明確使用 `median()`，不是 `mean()`。",
                    "數值欄位是 `fillna` 的典型使用場景，不會因為是數值就報錯。",
                    "補值完成後該欄位的 `NaN` 會被替換，不會和原始缺值狀態完全相同。",
                ],
                [
                    "補強 `mean` 與 `median` 的補值差異。",
                    "補強 `fillna` 與缺值處理的高頻寫法。",
                ],
                [
                    "sources/official-corpus.md｜數據處理技術與工具",
                    "sources/scope-weight-map.md｜L22203 數據處理技術與工具",
                ],
                code=dedent(
                    """
                    import pandas as pd

                    df = pd.DataFrame({
                        "income": [50000, None, 60000, 90000]
                    })

                    filled = df["income"].fillna(df["income"].median())
                    print(filled.tolist())
                    print(filled.loc[1])
                    """
                ),
            ),
            pack.mc(
                "ex8_get_dummies_drop_first",
                "L22203",
                "中",
                [
                    "閱讀下列程式碼後，哪個敘述最正確？",
                    "如果這題在考 one-hot encoding 的輸出欄位，哪個選項正確？",
                ],
                "因為用了 `drop_first=True`，`city` 只會展開成 2 個虛擬變數欄位，而不是 3 個全部保留。",
                [
                    "`get_dummies` 會把 `city` 直接改成單一整數欄位，效果等同 label encoding。",
                    "只要做 one-hot encoding，就一定要保留所有類別欄位，不能 drop first。",
                    "`drop_first=True` 只會刪除資料表的第一列，不會影響 dummy 欄位數量。",
                ],
                "`drop_first=True` 常用在避免完全共線性或簡化線性模型輸入。題目重點是辨識 one-hot encoding 與 label encoding 的差別，以及 `drop_first` 真正影響的是欄位，不是列。",
                [
                    "`get_dummies` 產生的是多個 0/1 欄位，不是單一整數標籤欄。",
                    "保留全部欄位不是唯一做法；`drop_first=True` 是常見選項。",
                    "`drop_first=True` 處理的是類別展開後的欄位，不是刪資料列。",
                ],
                [
                    "補強 one-hot encoding 與 label encoding 的差異。",
                    "補強 `drop_first=True` 對虛擬變數欄位數量的影響。",
                ],
                [
                    "sources/official-corpus.md｜數據處理技術與工具",
                    "sources/scope-weight-map.md｜L22203 數據處理技術與工具",
                ],
                code=dedent(
                    """
                    import pandas as pd

                    df = pd.DataFrame({
                        "city": ["Taipei", "Taichung", "Kaohsiung", "Taipei"]
                    })

                    out = pd.get_dummies(df, columns=["city"], drop_first=True)
                    print(out.columns.tolist())
                    """
                ),
            ),
            pack.mc(
                "ex8_train_test_split_stratify",
                "L22401",
                "中",
                [
                    "閱讀下列程式碼後，哪個敘述最正確？",
                    "如果這題在考不平衡資料切分策略，哪個選項正確？",
                ],
                "使用 `stratify=y` 的目的是讓訓練集與測試集盡量維持與原始資料相近的類別比例，這在不平衡分類問題特別重要。",
                [
                    "`stratify=y` 會自動完成 SMOTE，因此少數類會被複製到和多數類一樣多。",
                    "只要用了 `random_state=42`，就不需要 `stratify`，兩者作用完全相同。",
                    "`stratify=y` 只適用於回歸，分類資料不能用。",
                ],
                "`stratify` 是切分時維持比例，不是重抽樣。這題常見干擾就是把 `stratify`、`random_state`、`SMOTE` 混在一起考。",
                [
                    "`stratify` 不會生成新樣本；SMOTE 才是重抽樣方法。",
                    "`random_state` 只負責可重現，不能保證類別比例。",
                    "`stratify=y` 典型用於分類資料，不是回歸限定功能。",
                ],
                [
                    "補強 `stratify`、`random_state`、`SMOTE` 的功能差異。",
                    "補強不平衡分類切分時的基本原則。",
                ],
                [
                    "sources/official-corpus.md｜模型優化與調校",
                    "sources/scope-weight-map.md｜L22401 模型優化與調校",
                ],
                code=dedent(
                    """
                    from sklearn.model_selection import train_test_split

                    X = [[i] for i in range(20)]
                    y = [1, 1, 1, 1] + [0] * 16

                    X_train, X_test, y_train, y_test = train_test_split(
                        X, y, test_size=0.25, random_state=42, stratify=y
                    )

                    print(sum(y_train), len(y_train))
                    print(sum(y_test), len(y_test))
                    """
                ),
            ),
            pack.mc(
                "ex8_pipeline_scaler",
                "L22301",
                "中",
                [
                    "閱讀下列程式碼後，哪個敘述最正確？",
                    "若考題在問為什麼要把 `StandardScaler` 放進 `Pipeline`，哪個選項正確？",
                ],
                "把縮放與模型一起放進 `Pipeline`，可以讓每個交叉驗證切分只用訓練折來估計縮放參數，降低資料洩漏風險。",
                [
                    "`Pipeline` 的主要作用是讓模型一定變成非線性，和資料洩漏無關。",
                    "只要先在全資料做 `fit_transform`，再交叉驗證會更穩定，這是推薦做法。",
                    "`StandardScaler` 只改變欄位名稱，不會影響任何模型輸入分布。",
                ],
                "`Pipeline` 是 Subject 2 很常見的工程化題。核心不是語法本身，而是理解 preprocessing 也必須被包含在驗證流程裡，否則容易把測試資訊偷帶進訓練。",
                [
                    "`Pipeline` 不會自動讓模型變非線性；它的重點是串接前處理與模型流程。",
                    "先在全資料上 `fit_transform` 再做交叉驗證，反而容易造成資料洩漏。",
                    "`StandardScaler` 會改變數值尺度與分布中心，不只是改欄位名稱。",
                ],
                [
                    "補強 `Pipeline` 與資料洩漏的關係。",
                    "補強 `StandardScaler` 在模型流程中的正確位置。",
                ],
                [
                    "sources/official-corpus.md｜模型訓練與評估",
                    "sources/scope-weight-map.md｜L22301 模型訓練與效能評估",
                ],
                code=dedent(
                    """
                    from sklearn.pipeline import Pipeline
                    from sklearn.preprocessing import StandardScaler
                    from sklearn.linear_model import LogisticRegression
                    from sklearn.model_selection import cross_val_score
                    import numpy as np

                    X = np.array([[1, 100], [2, 120], [3, 80], [4, 200], [5, 220], [6, 210]])
                    y = np.array([0, 0, 0, 1, 1, 1])

                    pipe = Pipeline([
                        ("scaler", StandardScaler()),
                        ("model", LogisticRegression())
                    ])

                    scores = cross_val_score(pipe, X, y, cv=3)
                    print(scores)
                    """
                ),
            ),
            pack.mc(
                "ex8_cross_val_neg_mae",
                "L22301",
                "中",
                [
                    "閱讀下列程式碼後，哪個敘述最正確？",
                    "如果這題在考 `cross_val_score` 的 regression scoring，哪個選項正確？",
                ],
                "`scoring=\"neg_mean_absolute_error\"` 會回傳負值；比較模型時，數值越接近 0 通常代表 MAE 越小、表現越好。",
                [
                    "因為是 `mean_absolute_error`，分數一定是正值，所以越大越好。",
                    "`cross_val_score` 看到 `neg_` 會自動把結果取絕對值，因此不用管正負號。",
                    "只要是回歸任務，`cross_val_score` 都只能用 accuracy 做比較。",
                ],
                "`neg_*` 分數是 sklearn 的常見陷阱。這題不是要你背 API，而是要知道 regression loss 轉成 score 時常會帶負號，解讀時不能直接當成越大越差。",
                [
                    "這個 scoring 名稱就明確表示會回傳負的 MAE。",
                    "sklearn 不會自動幫你轉絕對值；你必須自己理解其意義。",
                    "accuracy 不是回歸任務常用指標，MAE、MSE、R² 才是高頻。",
                ],
                [
                    "補強 `neg_mean_absolute_error` 的解讀。",
                    "補強回歸指標與分類指標的區分。",
                ],
                [
                    "sources/official-corpus.md｜模型訓練與評估",
                    "sources/scope-weight-map.md｜L22301 模型訓練與效能評估",
                ],
                code=dedent(
                    """
                    from sklearn.model_selection import cross_val_score
                    from sklearn.linear_model import LinearRegression
                    import numpy as np

                    X = np.array([[1], [2], [3], [4], [5], [6]])
                    y = np.array([3, 5, 7, 9, 11, 13])

                    model = LinearRegression()
                    scores = cross_val_score(model, X, y, cv=3, scoring="neg_mean_absolute_error")
                    print(scores)
                    print(scores.mean())
                    """
                ),
            ),
            pack.mc(
                "ex8_group_transform_share",
                "L22203",
                "中",
                [
                    "閱讀下列程式碼後，哪個敘述最正確？",
                    "如果這題在考 `groupby().transform()` 的用途，哪個選項正確？",
                ],
                "`transform(\"sum\")` 會把每個部門的總 sales 對齊回原始列，因此 `share` 是每一列在自己部門總量中的占比。",
                [
                    "`transform(\"sum\")` 會把資料縮成每部門一列，因此 `share` 只會有 2 筆。",
                    "這段程式是在算全公司總 sales 的占比，和部門分組無關。",
                    "`transform` 只能搭配字串欄位，不能用在數值欄位。",
                ],
                "`agg` 與 `transform` 很容易混。`agg` 會彙總成較少列，`transform` 則把分組結果對齊回原始列，這是程式題很常出的差異點。",
                [
                    "`transform` 的特性就是維持原始列數，不會縮成每群一列。",
                    "這題明確以 `dept` 分組，因此占比是部門內占比，不是全體占比。",
                    "`transform` 可以常見地搭配數值欄位計算 sum、mean、max 等。",
                ],
                [
                    "補強 `agg` 與 `transform` 的差異。",
                    "補強分組後回填原始列的輸出判讀。",
                ],
                [
                    "sources/official-corpus.md｜數據處理技術與工具",
                    "sources/scope-weight-map.md｜L22203 數據處理技術與工具",
                ],
                code=dedent(
                    """
                    import pandas as pd

                    df = pd.DataFrame({
                        "dept": ["A", "A", "B", "B"],
                        "sales": [30, 70, 20, 80]
                    })

                    df["dept_total"] = df.groupby("dept")["sales"].transform("sum")
                    df["share"] = df["sales"] / df["dept_total"]
                    print(df)
                    """
                ),
            ),
            pack.mc(
                "ex8_pca_components_ratio",
                "L22302",
                "中",
                [
                    "閱讀下列程式碼後，哪個敘述最正確？",
                    "如果這題在考 PCA 輸出判讀，哪個選項正確？",
                ],
                "`explained_variance_ratio_` 用來看各主成分解釋了多少變異；設定 `n_components=2` 代表把原始 3 個特徵壓縮成 2 個主成分。",
                [
                    "`PCA(n_components=2)` 代表模型只會保留前 2 筆資料列，和特徵維度無關。",
                    "`explained_variance_ratio_` 是每個原始欄位的 p-value，所以可以拿來做顯著性檢定。",
                    "PCA 的主要目的就是直接提高分類 accuracy，不需要考慮降維或資訊保留。",
                ],
                "PCA 常見考點是降維意義與輸出欄位解讀，不是把它誤當成顯著性工具。這題要能分清楚『主成分數量』和『資料筆數』是不同概念。",
                [
                    "`n_components` 控制的是保留的主成分維度，不是保留幾筆資料。",
                    "`explained_variance_ratio_` 反映變異解釋比例，不是 p-value。",
                    "PCA 可能幫助模型，但主要目的仍是降維、去冗餘與壓縮資訊。",
                ],
                [
                    "補強 PCA 的降維意義與 `explained_variance_ratio_` 解讀。",
                    "補強主成分數量與資料筆數的區別。",
                ],
                [
                    "sources/official-corpus.md｜常見的大數據分析方法",
                    "sources/scope-weight-map.md｜L22302 常見的大數據分析方法",
                ],
                code=dedent(
                    """
                    from sklearn.decomposition import PCA
                    import numpy as np

                    X = np.array([
                        [1, 2, 3],
                        [2, 3, 4],
                        [3, 4, 5],
                        [4, 5, 6]
                    ])

                    pca = PCA(n_components=2)
                    X_reduced = pca.fit_transform(X)
                    print(X_reduced.shape)
                    print(pca.explained_variance_ratio_)
                    """
                ),
            ),
            pack.mc(
                "ex8_random_forest_importance",
                "L22301",
                "中",
                [
                    "閱讀下列程式碼後，哪個敘述最正確？",
                    "如果這題在考樹模型的 `feature_importances_`，哪個選項正確？",
                ],
                "`feature_importances_` 反映各特徵對樹模型分裂決策的重要程度；它不是線性模型的斜率，也不能直接解讀成『增加 1 單位會增加多少預測值』。",
                [
                    "`feature_importances_` 就等同線性回歸的 `coef_`，可以直接看正負方向與增加量。",
                    "只要看到 importance 比較高，就代表該特徵一定和目標變數有因果關係。",
                    "`RandomForestClassifier` 訓練後不會有任何特徵重要性資訊，必須另外手算。",
                ],
                "樹模型的重要性與線性係數是兩種不同概念。這題常用來測試你會不會把 `coef_` 的解讀硬套到 ensemble tree 模型上。",
                [
                    "`feature_importances_` 不提供線性方向與單位變化解讀，不能等同 `coef_`。",
                    "重要性高不等於因果關係成立，只代表模型決策時較常依賴該特徵。",
                    "隨機森林本身就能提供 `feature_importances_`。",
                ],
                [
                    "補強樹模型重要性與線性係數的差異。",
                    "補強特徵重要性不等於因果推論。",
                ],
                [
                    "sources/official-corpus.md｜模型訓練與評估",
                    "sources/scope-weight-map.md｜L22301 模型訓練與效能評估",
                ],
                code=dedent(
                    """
                    from sklearn.ensemble import RandomForestClassifier
                    import numpy as np

                    X = np.array([
                        [20, 1, 0],
                        [22, 1, 1],
                        [35, 0, 1],
                        [40, 0, 1],
                        [28, 1, 0],
                        [50, 0, 1],
                    ])
                    y = np.array([0, 0, 1, 1, 0, 1])

                    model = RandomForestClassifier(random_state=42, n_estimators=50)
                    model.fit(X, y)
                    print(model.feature_importances_)
                    """
                ),
            ),
        ],
    ),
    drill(
        "subject-2-statsmodels-seaborn-timeseries-drill",
        "科目 2 加練｜statsmodels + seaborn + 時間序列",
        2,
        "Adj. R²、confidence interval、lineplot、resample、rolling mean、TimeSeriesSplit、lag feature",
        "建議在 Day 07、Day 12、Day 14、Day 18 後加做",
        [
            pack.mc(
                "ex9_adjusted_r2",
                "L22301",
                "中",
                [
                    "閱讀下列 `statsmodels` 程式碼後，哪個敘述最正確？",
                    "如果這題在考 `R-squared` 與 `Adjusted R-squared` 的差異，哪個選項正確？",
                ],
                "`Adjusted R-squared` 會把變數數量納入考量，因此比單純 `R-squared` 更適合比較含不同特徵數量的回歸模型。",
                [
                    "`Adjusted R-squared` 只用於分類模型，線性回歸不會用到。",
                    "`R-squared` 與 `Adjusted R-squared` 一定完全相同，所以保留兩個欄位沒有意義。",
                    "只要 `R-squared` 高，就代表新增任何特徵都一定有實質幫助。",
                ],
                "這題常考你會不會把 `R-squared` 當成唯一指標。`Adjusted R-squared` 會對不必要特徵做懲罰，因此在多變數回歸中更有比較價值。",
                [
                    "`Adjusted R-squared` 就是回歸模型常見評估指標，不是分類限定。",
                    "兩者只有在少數情況接近，不會保證完全相同。",
                    "`R-squared` 可能因為加入無效特徵而上升，但不代表模型真的更好。",
                ],
                [
                    "補強 `R-squared` 與 `Adjusted R-squared` 的差異。",
                    "補強回歸模型評估時不能只看單一指標。",
                ],
                [
                    "sources/official-corpus.md｜模型訓練與評估",
                    "sources/scope-weight-map.md｜L22301 模型訓練與效能評估",
                ],
                code=dedent(
                    """
                    import pandas as pd
                    import statsmodels.api as sm

                    X = pd.DataFrame({
                        "tv": [1, 2, 3, 4, 5, 6],
                        "radio": [2, 1, 0, 1, 2, 3],
                        "noise": [9, 2, 7, 1, 8, 3],
                    })
                    y = pd.Series([5, 7, 9, 11, 13, 15])

                    X = sm.add_constant(X)
                    model = sm.OLS(y, X).fit()

                    print(model.rsquared)
                    print(model.rsquared_adj)
                    """
                ),
            ),
            pack.mc(
                "ex9_confint_zero",
                "L22103",
                "中",
                [
                    "閱讀下列 `statsmodels` 輸出片段後，哪個敘述最正確？",
                    "若這題考的是信賴區間是否跨過 0，哪個選項正確？",
                ],
                "`search_ads` 的 95% 信賴區間若完全不含 0，可視為其係數在該信賴水準下較可能不是 0；`coupon` 若區間跨過 0，則不宜主張其效果顯著。",
                [
                    "只要信賴區間比較窄，就一定代表變數顯著，不需要看是否跨過 0。",
                    "信賴區間跨過 0 代表這個變數一定有強烈負向效果。",
                    "回歸係數的信賴區間只能用來看平均數，不能用來判讀變數效果。",
                ],
                "這類題本質上仍是顯著性判讀，只是換成 `conf_int()` 的形式來考。重點不是背表，而是知道『是否包含 0』代表什麼。",
                [
                    "區間寬窄和是否顯著不是同一件事，關鍵仍是有沒有跨過 0。",
                    "跨過 0 代表方向不穩定或不足以拒絕係數為 0 的可能，不是證明負向效果。",
                    "回歸係數的信賴區間本來就常用來判讀效果估計的不確定性。",
                ],
                [
                    "補強用信賴區間判讀係數顯著性。",
                    "補強『跨 0』與『不跨 0』的實務意義。",
                ],
                [
                    "sources/official-corpus.md｜假設檢定與統計推論",
                    "sources/scope-weight-map.md｜L22103 假設檢定與統計推論",
                ],
                code=dedent(
                    """
                    import pandas as pd
                    import statsmodels.api as sm

                    X = pd.DataFrame({
                        "search_ads": [1, 2, 3, 4, 5, 6],
                        "coupon": [0, 1, 0, 1, 0, 1],
                    })
                    y = pd.Series([10, 13, 15, 18, 19, 23])

                    X = sm.add_constant(X)
                    model = sm.OLS(y, X).fit()

                    print(model.conf_int())
                    # search_ads  [0.80, 1.45]
                    # coupon      [-0.90, 1.10]
                    """
                ),
            ),
            pack.mc(
                "ex9_lineplot_time_trend",
                "L22303",
                "中",
                [
                    "閱讀下列 `seaborn` 程式碼後，哪個敘述最正確？",
                    "如果題目在考時間趨勢圖表選型，哪個選項正確？",
                ],
                "`lineplot` 適合呈現日期序列隨時間變動的趨勢，因為重點是連續時間上的升降與波動，而不是單純比較幾個不相關類別。",
                [
                    "只要資料筆數超過 10 筆，就一定要改用 `barplot`，`lineplot` 不適合時間資料。",
                    "`lineplot` 的主要用途是顯示每個類別出現次數，和時間趨勢無關。",
                    "只要 x 軸是日期，圖表一定會自動轉成季節性分解圖，不需要額外分析。",
                ],
                "這題的重點是圖表語意。時間序列資料最常見的第一步就是先看趨勢圖，`lineplot` 比 `barplot` 更能表達連續變化。",
                [
                    "時間資料並沒有『超過 10 筆就不能用 lineplot』這種規則。",
                    "顯示類別筆數通常更接近 `countplot` 的用途，不是 `lineplot`。",
                    "日期軸不會自動變成季節性分解，仍需要額外方法分析季節性。",
                ],
                [
                    "補強 `lineplot` 與 `barplot` 在時間資料的選型差異。",
                    "補強趨勢觀察與類別比較是不同圖表語意。",
                ],
                [
                    "sources/official-corpus.md｜數據可視化工具",
                    "sources/scope-weight-map.md｜L22303 數據可視化工具",
                ],
                code=dedent(
                    """
                    import pandas as pd
                    import seaborn as sns

                    df = pd.DataFrame({
                        "date": pd.date_range("2026-01-01", periods=5, freq="D"),
                        "traffic": [120, 135, 128, 150, 165],
                    })

                    sns.lineplot(data=df, x="date", y="traffic")
                    """
                ),
            ),
            pack.mc(
                "ex9_resample_monthly",
                "L22203",
                "中",
                [
                    "閱讀下列程式碼後，哪個敘述最正確？",
                    "若這題在考 `resample('M')` 的意義，哪個選項正確？",
                ],
                "`resample('M').sum()` 會把日資料依月份重新聚合成每月總 sales；前提是索引已經是日期型態。",
                [
                    "`resample('M')` 只會重新排序資料，不會做任何聚合。",
                    "只要寫 `resample('M')`，就會自動計算月平均，和後面接什麼方法無關。",
                    "`resample('M')` 可以直接套在任何字串索引上，不需要日期型態也能正確做月份聚合。",
                ],
                "時間序列題常用 `resample` 考頻率轉換。重點是知道它不是單獨完成所有事，而是先按時間頻率分組，再接 `sum()`、`mean()` 等聚合。",
                [
                    "`resample` 本身不是單純排序，它是依時間頻率重分組。",
                    "月總和、月平均要看後面接的聚合函式，不是固定月平均。",
                    "若索引不是日期型態，`resample` 通常無法按時間頻率正確運作。",
                ],
                [
                    "補強 `resample` 與聚合函式的搭配關係。",
                    "補強時間索引與日期型態的基本前提。",
                ],
                [
                    "sources/official-corpus.md｜數據處理技術與工具",
                    "sources/scope-weight-map.md｜L22203 數據處理技術與工具",
                ],
                code=dedent(
                    """
                    import pandas as pd

                    df = pd.DataFrame({
                        "date": pd.date_range("2026-01-28", periods=6, freq="D"),
                        "sales": [10, 12, 11, 30, 28, 35],
                    }).set_index("date")

                    monthly = df.resample("M").sum()
                    print(monthly)
                    """
                ),
            ),
            pack.mc(
                "ex9_rolling_mean",
                "L22302",
                "中",
                [
                    "閱讀下列程式碼後，哪個敘述最正確？",
                    "如果這題在考 rolling mean 的用途，哪個選項正確？",
                ],
                "`rolling(window=3).mean()` 會用最近 3 期資料計算移動平均，常用來平滑短期波動、協助觀察趨勢。",
                [
                    "`rolling(window=3).mean()` 會直接預測未來第 3 期的值，因此屬於預測模型。",
                    "移動平均只會保留原始尖峰，不會改變任何波動程度。",
                    "`window=3` 代表每 3 個欄位做平均，不是每 3 筆時間點。",
                ],
                "移動平均是時間序列前處理與視覺化高頻概念。這題要會分清楚『平滑觀察』和『正式預測模型』不是同一件事。",
                [
                    "rolling mean 主要是描述與平滑，不是直接做未來預測。",
                    "平滑的目的就是降低局部波動，尖峰影響通常會被稀釋。",
                    "在這種一維序列場景中，`window=3` 指的是 3 期觀測值。",
                ],
                [
                    "補強 rolling mean 的用途。",
                    "補強平滑處理與預測模型的差異。",
                ],
                [
                    "sources/official-corpus.md｜常見的大數據分析方法",
                    "sources/scope-weight-map.md｜L22302 常見的大數據分析方法",
                ],
                code=dedent(
                    """
                    import pandas as pd

                    s = pd.Series([100, 160, 120, 180, 140, 200])
                    ma3 = s.rolling(window=3).mean()
                    print(ma3.tolist())
                    """
                ),
            ),
            pack.mc(
                "ex9_timeseries_split",
                "L22302",
                "中",
                [
                    "閱讀下列程式碼後，哪個敘述最正確？",
                    "若這題在考時間序列驗證方法，哪個選項正確？",
                ],
                "`TimeSeriesSplit` 會保留時間順序，讓訓練集先於驗證集，這比隨機打散更適合時間序列資料。",
                [
                    "`TimeSeriesSplit` 的目的和 `shuffle=True` 完全一樣，都是把資料順序打亂後平均分配。",
                    "時間序列資料最推薦直接用一般 KFold 隨機切分，因為比較平均。",
                    "`TimeSeriesSplit` 只適用於分類資料，回歸型時間序列不能用。",
                ],
                "時間序列最怕未來資訊滲入過去。這題的重點是知道驗證方式也要符合時間先後，不然評估分數可能過度樂觀。",
                [
                    "`TimeSeriesSplit` 恰恰是不打亂順序，和 `shuffle=True` 方向相反。",
                    "一般隨機 KFold 容易把未來資料混入訓練，對時間序列不理想。",
                    "`TimeSeriesSplit` 跟任務是分類或回歸無直接限制，核心在資料順序。",
                ],
                [
                    "補強時間序列驗證方法與一般 KFold 的差異。",
                    "補強資料洩漏在時間序列情境下的風險。",
                ],
                [
                    "sources/official-corpus.md｜常見的大數據分析方法",
                    "sources/scope-weight-map.md｜L22302 常見的大數據分析方法",
                ],
                code=dedent(
                    """
                    from sklearn.model_selection import TimeSeriesSplit
                    import numpy as np

                    X = np.arange(12).reshape(-1, 1)
                    tscv = TimeSeriesSplit(n_splits=3)

                    for train_idx, test_idx in tscv.split(X):
                        print(train_idx, test_idx)
                    """
                ),
            ),
            pack.mc(
                "ex9_shift_lag1",
                "L22203",
                "中",
                [
                    "閱讀下列程式碼後，哪個敘述最正確？",
                    "如果這題在考 lag feature 的建立，哪個選項正確？",
                ],
                "`shift(1)` 會把前一期的 `sales` 往下對齊到當前列，因此 `lag1` 表示上一期數值，而第一列通常會變成 `NaN`。",
                [
                    "`shift(1)` 會把下一期數值對齊到當前列，所以第一列一定有值。",
                    "`lag1` 代表過去 1 個欄位名稱，不是時間序列特徵。",
                    "只要建立 `lag1`，模型就一定能正確預測未來，不需要其他處理。",
                ],
                "lag feature 是時間序列建模最常見的基礎題。核心在於你要知道它反映的是過去資訊，並且前幾列常會因為缺少歷史值而出現缺值。",
                [
                    "`shift(1)` 對齊的是上一期，不是下一期，因此第一列通常沒有可對應的歷史值。",
                    "lag feature 是把過去觀測值轉成特徵，不是欄位名稱操作而已。",
                    "建立 lag 只是特徵工程的一部分，不會保證模型一定準確。",
                ],
                [
                    "補強 lag feature 的意義與缺值位置。",
                    "補強時間序列特徵工程的基本觀念。",
                ],
                [
                    "sources/official-corpus.md｜數據處理技術與工具",
                    "sources/scope-weight-map.md｜L22203 數據處理技術與工具",
                ],
                code=dedent(
                    """
                    import pandas as pd

                    df = pd.DataFrame({
                        "sales": [100, 120, 130, 160]
                    })

                    df["lag1"] = df["sales"].shift(1)
                    print(df)
                    """
                ),
            ),
        ],
    ),
]


def render_drill_file(drill_payload: dict) -> str:
    stem_rows = []
    q_no = 1
    for item in drill_payload["items"]:
        stem_rows.append(pack.render_question(item, q_no, 0, concise=False))
        q_no += 1
        stem_rows.append(pack.render_question(item, q_no, 1, concise=False))
        q_no += 1

    gaps = []
    seen = set()
    for item in drill_payload["items"]:
        for gap in item["gaps"]:
            if gap not in seen:
                seen.add(gap)
                gaps.append(gap)

    lines = [
        f"# {drill_payload['title']}",
        "",
        f"- 科目：`{drill_payload['subject']}`",
        f"- 焦點：`{drill_payload['focus']}`",
        f"- 題量：`{len(drill_payload['items']) * 2}` 題",
        f"- 建議時機：{drill_payload['recommended_after']}",
        "- 使用方式：先做題，再展開 `<details>` 看答案與排錯理由。",
        "",
        "## 題目",
        "",
        "\n\n".join(stem_rows),
        "",
        "## 本組必補",
        "",
    ]
    lines.extend(f"- {gap.rstrip('。')}。" for gap in gaps[:6])
    lines.extend(
        [
            "",
            "## 自評",
            "",
            "| 題號 | 你的答案 | 是否已回看來源 | 備註 |",
            "| --- | --- | --- | --- |",
        ]
    )
    for q_no in range(1, len(drill_payload["items"]) * 2 + 1):
        lines.append(f"| {q_no} |  |  |  |")
    lines.append("")
    return "\n".join(lines)


def render_extended_index() -> str:
    rows = []
    for drill_payload in DRILLS:
        rows.append(
            f"| {drill_payload['title']} | 科目{drill_payload['subject']} | {drill_payload['focus']} | "
            f"{len(drill_payload['items']) * 2} | {drill_payload['recommended_after']} | "
            f"[開啟](./{drill_payload['key']}.md) |"
        )
    return "\n".join(
        [
            "# 擴充題庫索引",
            "",
            "這裡是主線 20 天之外的加練題組。設計原則是補高頻弱點，不直接打亂你原本每天的主線節奏。",
            "",
            "| 題組 | 科目 | 焦點 | 題量 | 建議時機 | 連結 |",
            "| --- | --- | --- | --- | --- | --- |",
            *rows,
            "",
            "## 使用建議",
            "",
            "- 先做主線 `daily/` 題單，再做對應加練。",
            "- 若某主題在 `progress/auto-knowledge-gaps.md` 重複出現，優先挑同主題加練題組。",
            "- 這批加練題目前以手動作答為主；若你要，我可以下一輪把它們也接進自動批改流程。",
            "",
        ]
    )


def render_drill_file_v2(drill_payload: dict) -> str:
    stem_rows = []
    q_no = 1
    for item in drill_payload["items"]:
        stem_rows.append(pack.render_question(item, q_no, 0, concise=False))
        q_no += 1
        stem_rows.append(pack.render_question(item, q_no, 1, concise=False))
        q_no += 1

    gaps = []
    seen = set()
    for item in drill_payload["items"]:
        for gap in item["gaps"]:
            if gap not in seen:
                seen.add(gap)
                gaps.append(gap)

    attempt_file = f"../attempts/{drill_payload['key']}-attempt.md"
    report_file = f"../reports/{drill_payload['key']}-report.md"
    score_command = f"python .\\score_attempt.py --drill {drill_payload['key']}"
    priority = drill_priority(drill_payload)
    source_tier = drill_source_tier(drill_payload)
    source_refs = drill_source_refs(drill_payload)

    lines = [
        f"# {drill_payload['title']}",
        "",
        f"- 科目：`{drill_payload['subject']}`",
        f"- 優先級：`{priority}`",
        f"- 優先級摘要：`{drill_priority_summary(drill_payload)}`",
        f"- 來源層級：`{source_tier}`",
        f"- 焦點：`{drill_payload['focus']}`",
        f"- 題數：`{len(drill_payload['items']) * 2}` 題",
        f"- 建議加做時機：`{drill_payload['recommended_after']}`",
        f"- 作答單：[開啟]({attempt_file})",
        f"- 批改報告：[開啟]({report_file})",
        f"- 批改指令：`{score_command}`",
        "- 使用方式：先做題，再展開 `<details>` 看答案與排錯理由。",
        "",
        "## 題源對照",
        "",
    ]
    lines.extend(f"- {ref}" for ref in source_refs)
    lines.extend(
        [
            "",
        "## 題目",
        "",
        "\n\n".join(stem_rows),
        "",
        "## 本組必補",
        "",
        ]
    )
    lines.extend(f"- {gap.rstrip('。')}" for gap in gaps[:6])
    lines.extend(
        [
            "",
            "## 自評",
            "",
            "| 題號 | 你的答案 | 能否自己解釋 | 備註 |",
            "| --- | --- | --- | --- |",
        ]
    )
    for q_no in range(1, len(drill_payload["items"]) * 2 + 1):
        lines.append(f"| {q_no} |  |  |  |")
    lines.append("")
    return "\n".join(lines)


def render_extended_index_v2() -> str:
    rows = []
    for drill_payload in DRILLS:
        rows.append(
            f"| {drill_payload['title']} | 科目 {drill_payload['subject']} | `{drill_priority(drill_payload)}` | `{drill_source_tier(drill_payload)}` | {drill_payload['focus']} | "
            f"{len(drill_payload['items']) * 2} | {drill_payload['recommended_after']} | "
            f"[題目](./{drill_payload['key']}.md) | "
            f"[作答](../attempts/{drill_payload['key']}-attempt.md) | "
            f"[報告](../reports/{drill_payload['key']}-report.md) |"
        )

    return "\n".join(
        [
            "# Extended 加練題庫",
            "",
            "這裡收的是 20 天主線之外的補強題庫，適合拿來集中刷弱點或加重程式題型。",
            "",
            "| 題庫 | 科目 | 優先級 | 來源層級 | 焦點 | 題數 | 建議加做時機 | 題目 | 作答 | 報告 |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
            *rows,
            "",
            "## 使用方式",
            "",
            "- 先從 `daily/` 主線題單做起，再用這些加練集中補弱點。",
            "- 如果你要留下分數與弱點追蹤，請填 `attempts/` 對應作答單後再批改。",
            "- 批改完成後，成績與弱點會一起出現在 `progress/` 下的追蹤文件中。",
            "",
        ]
    )


def generate_extended_drills() -> None:
    lib.write_text(EXTENDED_DIR / "README.md", render_extended_index_v2())
    for drill_payload in DRILLS:
        lib.write_text(EXTENDED_DIR / f"{drill_payload['key']}.md", render_drill_file_v2(drill_payload))


DRILL_PRIORITY_OVERRIDES.update(
    {
        "subject-2-graph-rdf-intensive-drill": "A",
        "subject-2-hypothesis-test-selector-drill": "A",
        "subject-2-public-patterns-mixed-drill": "B",
        "subject-1-genai-multimodal-planning-drill": "A",
        "subject-1-cross-scenario-integration-drill": "B",
    }
)


DRILLS.extend(
    [
        drill(
            "subject-2-graph-rdf-intensive-drill",
            "科目 2 加練｜圖資料庫、知識圖譜與 RDF 強化",
            2,
            "property graph、RDF 三元組、知識圖譜、多跳關聯查詢",
            "Day 13、Day 18、Day 19 後加做",
            [
                pack.mc(
                    "ex_graph_rdf_triple",
                    "L22202",
                    "中",
                    [
                        "若要把「客戶 A 購買 商品 B」表達成 RDF 最核心的三元組，下列何者最符合 RDF 表示法？",
                        "知識圖譜專案要把『王小明修讀資料科學』轉成 RDF 三元組，最合理的基本結構是什麼？",
                    ],
                    "以主詞、述詞、受詞三元組表達實體與關係",
                    ["把資料拆成只有欄位名稱的二維表", "只記錄節點，不記錄節點間關係", "先把資料轉成影像向量再查詢"],
                    "RDF 的基本單位就是主詞、述詞、受詞三元組，用來描述實體與其關係。",
                    [
                        "二維表能存資料，但不是 RDF 的核心表示法。",
                        "只記節點沒有關係，無法形成知識圖譜可推理結構。",
                        "影像向量與 RDF 結構是不同層次的表示方式。",
                    ],
                    ["記住 RDF = subject / predicate / object。", "分清 RDF、關聯式表格、向量資料表示的用途。"],
                    ["sources/official-corpus.md｜114 第二梯次科目 2 公告試題含 RDF 題型", "sources/question-source-map.md｜A 級必擴官方題源"],
                    priority="A",
                    source_tier="official-derived",
                    source_refs=["sources/question-source-map.md｜114 第二梯次科目 2 公告試題", "sources/scope-weight-map.md｜L22202 數據儲存與管理"],
                    evidence_tags=["official-formal", "graph-db", "rdf"],
                ),
                pack.mc(
                    "ex_graph_property_edge",
                    "L22202",
                    "中",
                    [
                        "物流公司要分析『倉庫 A 到門市 B』這條配送路徑的距離、運費與平均時延，最適合把這些資訊建在何處？",
                        "若推薦系統要記錄「使用者看過商品」這條關係的時間與停留秒數，property graph 最適合把這些值放在哪裡？",
                    ],
                    "建在邊（edge）屬性上",
                    ["建在所有節點的共同欄位中", "只建在圖的名稱描述裡", "把每個屬性拆成獨立模型權重"],
                    "路徑距離、互動時間、停留秒數都是關係本身的資訊，最適合放在邊屬性。",
                    [
                        "共同欄位無法正確表示每一條關係自己的數值。",
                        "圖的名稱描述不是可查詢的關係屬性結構。",
                        "模型權重不負責保存圖資料的業務屬性。",
                    ],
                    ["分清節點屬性與邊屬性。", "看到『關係自己的數值』優先想到 edge property。"],
                    ["sources/official-corpus.md｜圖資料庫題型整理", "sources/question-source-map.md｜圖資料庫、知識圖譜與 RDF 為 A 級必擴主題"],
                    priority="A",
                    source_tier="official-derived",
                    source_refs=["sources/question-source-map.md｜官方樣題與公告題顯示圖資料庫為高頻", "sources/scope-weight-map.md｜L22202 數據儲存與管理"],
                    evidence_tags=["official-scope", "graph-db"],
                ),
                pack.mc(
                    "ex_graph_multihop_query",
                    "L22303",
                    "中",
                    [
                        "若要查出『買過相同商品、且都來自同一城市』的客戶群，再延伸找出他們共同關注的品牌，哪種資料模型通常更適合？",
                        "公司想做多跳關聯分析，從病患到症狀到藥物再到副作用一路追查，哪種結構通常比單純關聯式表更自然？",
                    ],
                    "知識圖譜或圖資料庫較適合多跳關聯查詢",
                    ["純文字摘要最適合做關聯查詢", "只用影像分類模型即可處理", "把所有資料壓成單一平均值即可"],
                    "多跳關聯查詢是圖結構的強項，知識圖譜與圖資料庫能更自然描述路徑與關係。",
                    [
                        "文字摘要不能取代關聯結構查詢。",
                        "影像分類模型不負責多跳關聯推理。",
                        "平均值會破壞實體與關係網路。",
                    ],
                    ["辨識多跳查詢情境。", "知道知識圖譜適合做關聯探索與語意推理。"],
                    ["sources/official-corpus.md｜圖資料庫、知識圖譜高頻主題", "sources/question-source-map.md｜官方題源與培訓資源都覆蓋圖資料"],
                    priority="A",
                    source_tier="official-derived",
                    source_refs=["sources/question-source-map.md｜圖資料庫、知識圖譜與 RDF", "sources/scope-weight-map.md｜L22303 數據可視化與分析工具"],
                    evidence_tags=["official-scope", "knowledge-graph"],
                ),
                pack.mc(
                    "ex_graph_ontology_boundary",
                    "L22202",
                    "中",
                    [
                        "下列何者最能說明 ontology 與 graph database 的差異？",
                        "在知識圖譜專案中，團隊同時提到 ontology 與 graph database。下列哪個理解最正確？",
                    ],
                    "ontology 著重概念與關係定義，graph database 著重資料儲存與查詢",
                    ["兩者完全同義，只是名稱不同", "ontology 主要用來做影像增強", "graph database 只適合存數值矩陣"],
                    "ontology 是語意層與概念模型，graph database 則是實際承載與查詢圖資料的系統或模型。",
                    [
                        "兩者相關但不等同，一個偏語意規格，一個偏資料存取。",
                        "ontology 不處理影像增強。",
                        "graph database 不只存數值矩陣，核心是節點與邊關係。",
                    ],
                    ["分清 ontology、knowledge graph、graph database 的層次。", "不要把語意模型與資料儲存系統混成同義詞。"],
                    ["sources/question-source-map.md｜公開整理常提醒 ontology / knowledge graph / graph DB 易混淆", "sources/question-patterns.md｜易混概念對抗題"],
                    priority="A",
                    source_tier="official-derived",
                    source_refs=["sources/question-source-map.md｜圖資料主題轉寫規則", "sources/question-patterns.md｜易混概念題模板"],
                    evidence_tags=["graph-db", "ontology", "official-derived"],
                ),
            ],
        ),
        drill(
            "subject-2-hypothesis-test-selector-drill",
            "科目 2 加練｜統計檢定與分布秒判",
            2,
            "t-test、ANOVA、卡方、比例檢定、p-value、信賴區間",
            "Day 03、Day 11、Day 18 後加做",
            [
                pack.mc(
                    "ex_test_two_means",
                    "L22103",
                    "中",
                    [
                        "要比較 A/B 兩版登入頁的平均停留秒數是否不同，且兩組樣本彼此獨立，最常見的檢定方法是什麼？",
                        "行銷團隊抽兩組不同會員，比較平均客單價是否有顯著差異。若資料近似常態，應優先選哪種檢定？",
                    ],
                    "兩獨立樣本 t 檢定",
                    ["卡方檢定", "單因子 ANOVA", "主成分分析（PCA）"],
                    "比較兩組平均數差異，且樣本彼此獨立、資料近似常態時，典型做法是兩獨立樣本 t 檢定。",
                    [
                        "卡方檢定用於類別變數關聯，不是比較平均數。",
                        "ANOVA 常用於三組以上平均數比較；兩組也能用，但不是最直接首選。",
                        "PCA 是降維方法，不是顯著性檢定。",
                    ],
                    ["先辨識是『平均數』還是『比例/類別』問題。", "兩組平均數差異通常先想 t 檢定。"],
                    ["sources/official-corpus.md｜統計檢定為科目 2 核心", "sources/question-source-map.md｜官方與公開練習都高頻出現 t-test 題"],
                    priority="A",
                    source_tier="official-derived",
                    source_refs=["sources/question-source-map.md｜統計判斷必擴", "sources/scope-weight-map.md｜L22103 統計推論"],
                    evidence_tags=["official-scope", "t-test"],
                ),
                pack.mc(
                    "ex_test_anova",
                    "L22103",
                    "中",
                    [
                        "若要比較三種推薦策略對平均轉換率是否有顯著差異，最適合先用哪種檢定？",
                        "你有三個廣告版本，想知道平均點擊停留時間是否存在組間差異，第一步最常見的檢定是什麼？",
                    ],
                    "單因子 ANOVA",
                    ["兩獨立樣本 t 檢定", "卡方檢定", "皮爾森相關係數"],
                    "三組以上平均數比較時，最常先用單因子 ANOVA 檢查整體是否存在顯著差異。",
                    [
                        "t 檢定主要對兩組平均數，比三組以上不合適。",
                        "卡方檢定處理類別變數關聯，不是平均數差異。",
                        "相關係數描述線性關聯，不是多組平均數檢定。",
                    ],
                    ["看到『三組以上平均數』先想 ANOVA。", "分清平均數差異與類別關聯。"],
                    ["sources/official-corpus.md｜ANOVA 為高頻檢定題型", "sources/question-patterns.md｜統計檢定選型題模板"],
                    priority="A",
                    source_tier="official-derived",
                    source_refs=["sources/question-source-map.md｜官方與模擬題常見 ANOVA", "sources/question-patterns.md｜統計檢定題"],
                    evidence_tags=["official-scope", "anova"],
                ),
                pack.mc(
                    "ex_test_chisquare",
                    "L22103",
                    "中",
                    [
                        "若要判斷『是否為會員』與『是否購買年費方案』之間是否存在關聯，最常見的檢定是什麼？",
                        "醫療資料把病患分成吸菸/不吸菸與有症狀/無症狀兩類，若想檢驗兩個類別變數是否相關，應優先選哪種檢定？",
                    ],
                    "卡方獨立性檢定",
                    ["兩獨立樣本 t 檢定", "單因子 ANOVA", "線性迴歸係數檢定"],
                    "兩個類別變數之間是否存在關聯，經典方法是卡方獨立性檢定。",
                    [
                        "t 檢定是比較平均數，不是類別關聯。",
                        "ANOVA 比較多組平均數，不是類別交叉表關聯。",
                        "迴歸可以建模，但不是這類基礎關聯檢定的首選。",
                    ],
                    ["看到『類別對類別』先想卡方。", "交叉表與平均數比較是不同問題。"],
                    ["sources/official-corpus.md｜卡方與類別關聯為固定熱區", "sources/question-source-map.md｜S 測驗與官方都常見卡方題"],
                    priority="A",
                    source_tier="official-derived",
                    source_refs=["sources/question-source-map.md｜卡方題型高頻", "sources/scope-weight-map.md｜L22103 統計推論"],
                    evidence_tags=["official-scope", "chi-square"],
                ),
                pack.mc(
                    "ex_test_proportion",
                    "L22103",
                    "中",
                    [
                        "客服機器人的一次解決率目標是 80%。本月抽樣後想檢驗實際比例是否低於目標，最貼近的檢定是什麼？",
                        "產品團隊懷疑新版註冊流程的完成率未達 65% 目標。若要檢驗單一比例是否低於既定門檻，優先想到哪種方法？",
                    ],
                    "單一比例檢定",
                    ["卡方獨立性檢定", "兩獨立樣本 t 檢定", "主成分分析（PCA）"],
                    "當問題是『單一比例是否達標』時，應選單一比例檢定，而不是平均數或降維方法。",
                    [
                        "卡方獨立性檢定重點是兩個類別變數是否相關。",
                        "t 檢定比較平均數，不是比例是否達標。",
                        "PCA 與比例顯著性檢定無關。",
                    ],
                    ["分清比例問題與平均數問題。", "看到『達標/未達標』時先想比例檢定。"],
                    ["sources/question-source-map.md｜公開模擬題常出比例檢定選型", "sources/question-patterns.md｜統計檢定題模板"],
                    priority="A",
                    source_tier="official-derived",
                    source_refs=["sources/question-source-map.md｜比例檢定題型整理", "sources/question-patterns.md｜統計檢定題"],
                    evidence_tags=["public-pattern", "proportion-test", "official-derived"],
                ),
            ],
        ),
        drill(
            "subject-2-public-patterns-mixed-drill",
            "科目 2 加練｜公開題型轉寫混合題",
            2,
            "pandas 輸出判讀、Q-Q plot、箱型圖、門檻與指標選型",
            "Day 06、Day 12、Day 17 後加做",
            [
                pack.mc(
                    "ex_public_groupby_sort",
                    "L22203",
                    "中",
                    [
                        "觀察下列程式後，哪個敘述最可能正確？",
                        "若資料表中同一個部門有多筆資料，下列程式最終想達成什麼效果？",
                    ],
                    "先按部門聚合平均值，再依平均薪資由高到低排序",
                    ["先把缺值全部刪除，再展開欄位", "把每一列都轉成字串", "只計算每個部門的筆數，不會算平均"],
                    "程式中先做 groupby 與 mean，再接 sort_values，典型目的是算部門平均後排序。",
                    [
                        "題幹沒有 dropna 或欄位展開操作。",
                        "astype(str) 才會做字串轉換，這裡沒有。",
                        "若指定的是平均聚合，就不是只算筆數。",
                    ],
                    ["熟悉 groupby、agg/mean、sort_values 的常見組合。", "不要把聚合函式與計數函式混淆。"],
                    ["sources/question-source-map.md｜AITerms Python 題攻略", "sources/question-patterns.md｜程式判讀題模板"],
                    code="summary = (\n    df.groupby('dept', as_index=False)['salary']\n      .mean()\n      .sort_values('salary', ascending=False)\n)",
                    priority="B",
                    source_tier="public-pattern-derived",
                    source_refs=["sources/question-source-map.md｜AITerms Python 題攻略", "sources/question-patterns.md｜程式判讀題模板"],
                    evidence_tags=["public-practice", "python-pattern", "pandas"],
                ),
                pack.mc(
                    "ex_public_merge_nan",
                    "L22203",
                    "中",
                    [
                        "若 `left merge` 後發現右表沒有對上的資料，結果表最常出現哪種現象？",
                        "A 表保留所有列去接 B 表，某些 key 在 B 表不存在。這時合併結果最常如何呈現？",
                    ],
                    "右表對不上 key 的欄位會出現 NaN",
                    ["整列一定會被刪除", "所有欄位都會自動補成 0", "Pandas 會自動改成 inner join"],
                    "left join 會保留左表列，右表對不上的欄位以 NaN 表示。",
                    [
                        "left join 不會因為右表缺值而直接刪掉左表整列。",
                        "Pandas 不會自動把所有缺值補成 0。",
                        "join 類型不會自動改成 inner join。",
                    ],
                    ["熟悉 left merge 的保留規則。", "知道 NaN 常出現在合併後的未對應欄位。"],
                    ["sources/question-source-map.md｜AITerms Python 題攻略", "sources/question-source-map.md｜S 測驗科目 2 模擬題"],
                    priority="B",
                    source_tier="public-pattern-derived",
                    source_refs=["sources/question-source-map.md｜AITerms Python 題攻略", "sources/question-source-map.md｜S 測驗科目 2 模擬題"],
                    evidence_tags=["public-practice", "python-pattern", "merge"],
                ),
                pack.mc(
                    "ex_public_boxplot_choice",
                    "L22303",
                    "中",
                    [
                        "若你想快速檢查各門市交易金額的中位數、四分位距與離群值，最貼近目的的圖表是什麼？",
                        "資料分析會議上，主管要你一張圖同時看出分布位置、IQR 與離群值。你應先選哪種圖？",
                    ],
                    "箱型圖（box plot）",
                    ["長條圖（bar chart）", "圓餅圖（pie chart）", "雷達圖（radar chart）"],
                    "箱型圖能直接顯示中位數、四分位距與離群值，是這類分布檢查的標準選型。",
                    [
                        "長條圖適合比較彙總值，不擅長展示分布與離群值。",
                        "圓餅圖用來看比例結構，不適合分布檢查。",
                        "雷達圖不適合呈現 IQR 與離群值。",
                    ],
                    ["把圖表選型綁回分析目的。", "IQR、median、outlier 通常先想到 box plot。"],
                    ["sources/question-source-map.md｜S 測驗科目 2 模擬題", "sources/question-patterns.md｜視覺化題模板"],
                    priority="B",
                    source_tier="public-pattern-derived",
                    source_refs=["sources/question-source-map.md｜S 測驗科目 2 模擬題", "sources/question-patterns.md｜視覺化題模板"],
                    evidence_tags=["public-practice", "visualization", "boxplot"],
                ),
                pack.mc(
                    "ex_public_threshold_metric",
                    "L22401",
                    "中",
                    [
                        "詐欺偵測模型若目標是盡量少漏掉真詐欺案例，調整分類閾值時最應優先觀察哪類指標？",
                        "在高風險風控情境下，團隊寧可多抓一些可疑交易，也不想漏掉真正詐欺。這時評估應優先看哪個方向？",
                    ],
                    "優先提高召回率（recall），再權衡 precision",
                    ["只看 accuracy 即可", "只看訓練集損失最小即可", "只看 R² 是否提高"],
                    "詐欺偵測偏重少漏判，通常先看 recall；之後再評估 precision 與業務成本。",
                    [
                        "accuracy 在類別不平衡時常失真。",
                        "訓練集損失不能直接代表部署風險。",
                        "R² 是迴歸指標，不是分類閾值調整指標。",
                    ],
                    ["辨識不平衡分類情境。", "知道 recall、precision、threshold 三者的取捨。"],
                    ["sources/question-source-map.md｜CCChen 科目 2 模擬題", "sources/question-patterns.md｜指標選型與情境題"],
                    priority="B",
                    source_tier="public-pattern-derived",
                    source_refs=["sources/question-source-map.md｜CCChen 科目 2 模擬題", "sources/question-patterns.md｜指標選型題模板"],
                    evidence_tags=["public-practice", "threshold", "classification-metric"],
                ),
            ],
        ),
        drill(
            "subject-1-genai-multimodal-planning-drill",
            "科目 1 加練｜生成式 AI、RAG 與多模態規劃",
            1,
            "RAG、共享嵌入空間、缺模態、著作權與幻覺風險",
            "Day 03、Day 04、Day 13 後加做",
            [
                pack.mc(
                    "ex_s1_rag_vs_finetune",
                    "L21103",
                    "中",
                    [
                        "企業知識文件每週都會更新，希望客服生成答案時能引用最新內容且不想頻繁重訓模型，哪種做法通常更合適？",
                        "如果法規與產品文件變動很快，團隊想讓 LLM 回答可追溯到最新文件來源，應優先採哪種方案？",
                    ],
                    "採用 RAG，把最新文件檢索後再交給模型生成",
                    ["直接把所有文件寫死在 prompt 中", "每次文件更新都重新完整微調模型", "先把文件轉成資料庫索引後不用檢索"],
                    "RAG 能把知識更新與生成模型分開處理，適合高頻更新且需要引用來源的場景。",
                    [
                        "把所有文件硬塞進 prompt 不可擴展，也缺乏可維護性。",
                        "每次都完整微調成本高、更新慢。",
                        "只有索引而沒有檢索流程，模型拿不到相關上下文。",
                    ],
                    ["分清 RAG 與 fine-tuning 的適用情境。", "看到『知識常更新』優先想到檢索增強。"],
                    ["sources/question-source-map.md｜114 年第二梯次科目 1 公告試題", "sources/official-corpus.md｜RAG 與生成式 AI 高頻題型"],
                    priority="A",
                    source_tier="official-derived",
                    source_refs=["sources/question-source-map.md｜114 年第二梯次科目 1 公告試題", "sources/scope-weight-map.md｜L21103 AI 技術應用規劃"],
                    evidence_tags=["official-formal", "rag", "genai"],
                ),
                pack.mc(
                    "ex_s1_clip_embedding",
                    "L21201",
                    "中",
                    [
                        "若要讓系統用文字搜尋圖片，且文字與圖片都映射到可比較的向量空間，這種設計最接近哪個概念？",
                        "產品想做『輸入一句文字就找到最相關商品圖』，下列哪種多模態思路最合理？",
                    ],
                    "把文字與圖片投影到共享嵌入空間",
                    ["對每張圖都訓練一個獨立分類器", "先把圖片全轉成表格欄位再做卡方檢定", "只保留文字欄位，不處理圖片特徵"],
                    "文字搜圖的核心是讓不同模態可在同一表示空間比較相似度，典型思路就是共享嵌入空間。",
                    [
                        "每圖一個分類器不具擴展性，也不是跨模態比對方法。",
                        "卡方檢定不是跨模態檢索方案。",
                        "只保留文字會失去圖片模態資訊。",
                    ],
                    ["理解共享嵌入空間的用途。", "分清多模態檢索與單模態分類。"],
                    ["sources/question-source-map.md｜114 年第二梯次科目 1 公告試題", "sources/question-patterns.md｜多模態題模板"],
                    priority="A",
                    source_tier="official-derived",
                    source_refs=["sources/question-source-map.md｜科目 1 公告試題含 CLIP / 多模態題型", "sources/question-patterns.md｜任務選型題"],
                    evidence_tags=["official-formal", "multimodal", "clip"],
                ),
                pack.mc(
                    "ex_s1_missing_modality",
                    "L21201",
                    "中",
                    [
                        "多模態系統在實務上常遇到某些資料只有文字沒有圖片。若要提升穩定性，規劃時應優先考慮哪個方向？",
                        "如果部分客訴單只有文字、沒有上傳照片，設計多模態流程時最重要的規劃考量是什麼？",
                    ],
                    "設計缺模態（missing modality）時的退化處理與替代流程",
                    ["要求所有資料缺一不可，缺任何模態就全部丟棄", "先提高 GPU 規格即可解決", "只要模型參數夠大就不必處理缺模態"],
                    "多模態落地重點之一是缺模態處理，否則資料一不完整就會讓流程中斷或品質急降。",
                    [
                        "把不完整資料全丟掉常造成覆蓋率不足。",
                        "硬體升級不能解決流程設計缺失。",
                        "模型再大也不能替代缺模態的產品與資料策略。",
                    ],
                    ["多模態規劃要考慮資料現實。", "缺模態不是模型大小問題，而是流程設計問題。"],
                    ["sources/question-source-map.md｜114 年第二梯次科目 1 公告試題", "sources/official-corpus.md｜多模態規劃主題"],
                    priority="A",
                    source_tier="official-derived",
                    source_refs=["sources/question-source-map.md｜科目 1 公告試題", "sources/official-corpus.md｜多模態與導入規劃"],
                    evidence_tags=["official-formal", "multimodal", "planning"],
                ),
                pack.mc(
                    "ex_s1_copyright_guardrail",
                    "L21203",
                    "中",
                    [
                        "生成式 AI 影像專案要避免輸出高度近似受著作權保護作品，最應優先加入哪類治理措施？",
                        "設計企業內部文生圖服務時，若擔心侵權與不當輸出風險，第一層治理通常該放在哪裡？",
                    ],
                    "建立資料來源審查、提示與輸出審核、以及高風險內容管控",
                    ["只要把模型溫度調低就能解決侵權風險", "把所有輸入都轉成 CSV 就能避免著作權問題", "完全不記錄生成行為比較安全"],
                    "著作權與不當輸出風險需要治理流程，包括資料來源審查、審核機制與可追溯紀錄，不是單靠超參數調整。",
                    [
                        "溫度只影響隨機性，不能取代治理。",
                        "資料格式轉換不會自動消除法律風險。",
                        "完全不留紀錄反而降低稽核與追蹤能力。",
                    ],
                    ["技術控制與治理控制要分開想。", "著作權風險的第一層防線是流程與審查。"],
                    ["sources/question-source-map.md｜114 年第二梯次科目 1 公告試題", "sources/question-patterns.md｜風險治理題模板"],
                    priority="A",
                    source_tier="official-derived",
                    source_refs=["sources/question-source-map.md｜科目 1 公告試題", "sources/question-patterns.md｜風險治理題模板"],
                    evidence_tags=["official-formal", "copyright", "responsible-ai"],
                ),
            ],
        ),
        drill(
            "subject-1-cross-scenario-integration-drill",
            "科目 1 加練｜導入評估、部署與治理整合情境",
            1,
            "PoC 到上線、KPI、資料漂移、監控、PII 與回滾策略",
            "Day 09、Day 15、Day 20 後加做",
            [
                pack.mc(
                    "ex_s1_poc_kpi",
                    "L21301",
                    "中",
                    [
                        "企業做完 AI PoC 後，準備決定是否進入正式導入。下列哪個指標最適合作為 PoC 是否值得擴大的第一層依據？",
                        "如果主管只看模型準確率就想推全公司上線，作為 AI 導入規劃者，下一步最該補的是哪類判斷？",
                    ],
                    "同時檢查業務 KPI、資料可取得性、部署成本與風險",
                    ["只要準確率高於 90% 就應立刻全面上線", "只看 GPU 採購成本即可", "只看團隊是否會寫 Python 即可"],
                    "PoC 是否擴大要看業務價值、資料與部署可行性、治理風險，不是單一模型分數。",
                    [
                        "高準確率不代表商業與治理上可落地。",
                        "硬體成本只是其中一項，不足以單獨決策。",
                        "開發技能也不是唯一決策基準。",
                    ],
                    ["導入評估不是只看模型分數。", "PoC 到 production 要綜合 KPI、成本、風險與流程。"],
                    ["sources/question-source-map.md｜中級學習指引科目 1", "sources/question-patterns.md｜情境整合題模板"],
                    priority="B",
                    source_tier="official-derived",
                    source_refs=["sources/question-source-map.md｜中級學習指引科目 1", "sources/question-patterns.md｜情境整合題模板"],
                    evidence_tags=["official-guide", "deployment", "kpi"],
                ),
                pack.mc(
                    "ex_s1_drift_monitor",
                    "L21302",
                    "中",
                    [
                        "上線三個月後，模型整體準確率逐步下滑，但服務沒有中斷。這種情況最應先懷疑哪類問題？",
                        "若推薦模型最近分數慢慢變差，不是突然壞掉，而是隨時間退化，監控上第一個應追的是什麼？",
                    ],
                    "資料漂移或使用情境改變，需要檢查輸入分布與監控指標",
                    ["先把 CPU 升級即可", "這一定是前端按鈕配色問題", "只要把 learning rate 調低就會恢復"],
                    "分數逐步退化通常先想到資料漂移或情境改變，應檢查輸入分布、PSI 或其他監控指標。",
                    [
                        "硬體升級不會直接修復資料漂移。",
                        "前端配色與模型退化無關。",
                        "學習率屬於訓練設定，無法直接解釋上線後輸入分布改變。",
                    ],
                    ["資料漂移是上線監控高頻題。", "區分系統故障與模型效能退化。"],
                    ["sources/question-source-map.md｜114 年第二梯次科目 1 公告試題", "sources/official-corpus.md｜部署與監控主題"],
                    priority="B",
                    source_tier="official-derived",
                    source_refs=["sources/question-source-map.md｜科目 1 公告試題", "sources/official-corpus.md｜部署與監控"],
                    evidence_tags=["official-formal", "drift", "monitoring"],
                ),
                pack.mc(
                    "ex_s1_pii_guardrail",
                    "L21203",
                    "中",
                    [
                        "企業內部問答機器人可能在回答中帶出真實姓名、電話與訂單資訊。若只能先做一層緊急防護，最務實的第一步是什麼？",
                        "當生成式客服系統疑似會吐出個資時，哪個控制點最適合優先落地，作為正式上線前的最低防線？",
                    ],
                    "先做輸入/輸出端的個資偵測與遮罩，再補資料與權限治理",
                    ["完全關閉日誌，這樣就沒有個資風險", "把模型參數放大就能避免洩漏", "只改 UI 文案即可"],
                    "緊急防線通常先放在輸入與輸出端的偵測/遮罩，降低立即外洩風險，再往資料與權限治理補強。",
                    [
                        "不記錄日誌會讓稽核與追查更困難。",
                        "模型變大不等於不會洩漏個資。",
                        "UI 文案不能替代實際防護措施。",
                    ],
                    ["區分立即風險緩解與長期治理。", "PII 風險通常先做 I/O guardrail。"],
                    ["sources/question-source-map.md｜114 年第二梯次科目 1 公告試題", "sources/question-patterns.md｜風險治理題模板"],
                    priority="B",
                    source_tier="official-derived",
                    source_refs=["sources/question-source-map.md｜科目 1 公告試題", "sources/question-patterns.md｜風險治理題模板"],
                    evidence_tags=["official-formal", "pii", "guardrail"],
                ),
                pack.mc(
                    "ex_s1_rollback_strategy",
                    "L21302",
                    "中",
                    [
                        "新模型上線後，若關鍵 KPI 明顯下滑且客訴增加，哪個處置最符合穩健部署策略？",
                        "你在灰度發布後發現新模型造成轉換率下降。下列哪一步最務實，且能控制風險？",
                    ],
                    "啟動回滾或切回前版模型，同時保留監控與事故紀錄",
                    ["先刪除所有監控紀錄，避免留下負面證據", "繼續全量上線觀察一週再說", "只調整簡報數字讓 KPI 看起來正常"],
                    "穩健部署重點是可回滾與可追溯。當 KPI 明顯惡化，應先切回穩定版本，再分析根因。",
                    [
                        "刪除紀錄會破壞事故分析與治理。",
                        "已經出現明顯負面影響時，不應放任全量風險擴大。",
                        "美化數字不是工程處置。",
                    ],
                    ["上線策略要包含 rollback。", "監控、灰度發布、回滾要連成一套。"],
                    ["sources/question-source-map.md｜中級學習指引科目 1", "sources/question-patterns.md｜部署治理整合題"],
                    priority="B",
                    source_tier="official-derived",
                    source_refs=["sources/question-source-map.md｜中級學習指引科目 1", "sources/question-patterns.md｜部署治理整合題"],
                    evidence_tags=["official-guide", "rollback", "mlops"],
                ),
            ],
        ),
    ]
)
