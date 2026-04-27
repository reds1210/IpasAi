from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parent
SOURCES_DIR = ROOT / "sources"
DAILY_DIR = ROOT / "daily"
PROGRESS_DIR = ROOT / "progress"


OFFICIAL_LINKS = {
    "exam_info": "https://ipd.nat.gov.tw/ipas/certification/AIAP/exam-info",
    "learning_resources": "https://ipd.nat.gov.tw/ipas/certification/AIAP/learning-resources",
    "brochure_115": "https://www.ipas.org.tw/api/proxy/uploads/certification/AIAP/115%E5%B9%B4%E5%BA%A6AI%E6%87%89%E7%94%A8%E8%A6%8F%E5%8A%83%E5%B8%AB%E8%83%BD%E5%8A%9B%E9%91%91%E5%AE%9A%E7%B0%A1%E7%AB%A0%28%E5%88%9D%E3%80%81%E4%B8%AD%E7%B4%9A%29_0410_20260410115646.pdf",
    "scope_11404": "https://ipd.nat.gov.tw/ipas/DownloadFile.ashx?filename=14ae134c-fb2f-4741-9f6d-062c02bdbc94_AI%E6%87%89%E7%94%A8%E8%A6%8F%E5%8A%83%E5%B8%AB%E8%83%BD%E5%8A%9B%E9%91%91%E5%AE%9A_%E8%A9%95%E9%91%91%E5%85%A7%E5%AE%B9%E7%AF%84%E5%9C%8D%E5%8F%83%E8%80%83_11404.pdf&type=10",
    "sample_11409": "https://www.ipas.org.tw/DownloadFile.ashx?filename=4002eaa2-bfea-400e-abd1-2f4c1a1f8de8_iPAS+AI%E6%87%89%E7%94%A8%E8%A6%8F%E5%8A%83%E5%B8%AB%E4%B8%AD%E7%B4%9A%E8%83%BD%E5%8A%9B%E9%91%91%E5%AE%9A-%E8%80%83%E8%A9%A6%E6%A8%A3%E9%A1%8C%28114%E5%B9%B49%E6%9C%88%E7%89%88%29+_v2.pdf&type=10",
    "guide_subject_1": "https://www.ipas.org.tw/api/proxy/uploads/certification_resource/bf93f438f7be48d295c1b40a34d79f3d/AI%E6%87%89%E7%94%A8%E8%A6%8F%E5%8A%83%E5%B8%AB%28%E4%B8%AD%E7%B4%9A%29-%E5%AD%B8%E7%BF%92%E6%8C%87%E5%BC%95-%E7%A7%91%E7%9B%AE1%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%8A%80%E8%A1%93%E6%87%89%E7%94%A8%E8%A6%8F%E5%8A%83_20251222101833.pdf",
    "guide_subject_2": "https://www.ipas.org.tw/api/proxy/uploads/certification_resource/bf93f438f7be48d295c1b40a34d79f3d/AI%E6%87%89%E7%94%A8%E8%A6%8F%E5%8A%83%E5%B8%AB%28%E4%B8%AD%E7%B4%9A%29-%E5%AD%B8%E7%BF%92%E6%8C%87%E5%BC%95-%E7%A7%91%E7%9B%AE2%E5%A4%A7%E6%95%B8%E6%93%9A%E8%99%95%E7%90%86%E5%88%86%E6%9E%90%E8%88%87%E6%87%89%E7%94%A8_20251222101850.pdf",
    "book_list": "https://ipd.nat.gov.tw/ipas/AIAP/AbilityPageContent.aspx?ablno=d91b8785-d890-4865-abdc-36cd576cc744&mnuno=d7804e4b-29a5-4aa3-a88d-c05bcd9998d7&pgeno=4de5cc7f-a878-43bd-bd6f-ee11ea40be1c",
}


DAY_META = {
    1: {"s1_count": 8, "s2_count": 10, "s1_focus": "NLP 基礎與 AI/ML 邊界", "s2_focus": "資料型態、NaN、dtype、敘述統計"},
    2: {"s1_count": 8, "s2_count": 10, "s1_focus": "電腦視覺基本任務", "s2_focus": "常態分布、Z-score、IQR、異常值"},
    3: {"s1_count": 8, "s2_count": 10, "s1_focus": "生成式 AI 與 RAG", "s2_focus": "t 檢定、ANOVA、卡方、比例檢定"},
    4: {"s1_count": 8, "s2_count": 10, "s1_focus": "多模態與融合方式", "s2_focus": "ROC、AUC、PCA、分群基礎"},
    5: {"s1_count": 8, "s2_count": 10, "s1_focus": "AI 導入評估", "s2_focus": "資料清理、缺值處理、型別轉換"},
    6: {"s1_count": 8, "s2_count": 10, "s1_focus": "AI 導入規劃", "s2_focus": "groupby、value_counts、melt、視覺化選型"},
    7: {"s1_count": 8, "s2_count": 10, "s1_focus": "AI 風險治理與責任", "s2_focus": "線性迴歸、係數解讀、截距、顯著性"},
    8: {"s1_count": 8, "s2_count": 10, "s1_focus": "數據準備與模型選擇", "s2_focus": "LinearRegression.fit、OLS、coef_、p-value"},
    9: {"s1_count": 8, "s2_count": 10, "s1_focus": "系統整合、部署、Kubernetes、監控", "s2_focus": "交叉驗證、Bootstrap、模型驗證方法"},
    10: {"s1_count": 8, "s2_count": 10, "s1_focus": "Seq2Seq、Word2Vec、資料增強", "s2_focus": "不平衡資料、SMOTE、召回率與閾值"},
    11: {"s1_count": 8, "s2_count": 10, "s1_focus": "第一次高頻回鍋", "s2_focus": "第一次統計與程式回鍋"},
    12: {"s1_count": 8, "s2_count": 10, "s1_focus": "半模擬跨章整合", "s2_focus": "半模擬跨章整合"},
    13: {"s1_count": 10, "s2_count": 12, "s1_focus": "生成式 AI 法規與著作權", "s2_focus": "圖資料庫、知識圖譜、RDF"},
    14: {"s1_count": 10, "s2_count": 12, "s1_focus": "部署事故與對抗攻擊", "s2_focus": "時間序列、ARIMA、ACF、殘差診斷"},
    15: {"s1_count": 10, "s2_count": 12, "s1_focus": "易混概念對抗題", "s2_focus": "Python/統計錯題變體"},
    16: {"s1_count": 10, "s2_count": 12, "s1_focus": "第二輪半模擬", "s2_focus": "第二輪半模擬"},
    17: {"s1_count": 12, "s2_count": 14, "s1_focus": "高頻壓力題單", "s2_focus": "高密度程式判讀與回歸解讀"},
    18: {"s1_count": 12, "s2_count": 14, "s1_focus": "導入規劃與治理混題", "s2_focus": "檢定、視覺化、資料處理混題"},
    19: {"s1_count": 12, "s2_count": 14, "s1_focus": "曾錯主題反向變體", "s2_focus": "曾錯主題反向變體"},
    20: {"s1_count": 12, "s2_count": 14, "s1_focus": "最終過線題單", "s2_focus": "最終過線題單"},
}


def mc(
    item_id: str,
    lcode: str,
    difficulty: str,
    stems: list[str],
    correct: str,
    distractors: list[str],
    why_correct: str,
    distractor_notes: list[str],
    gaps: list[str],
    refs: list[str],
    code: str | None = None,
    priority: str | None = None,
    priority_reason: str | None = None,
    source_tier: str | None = None,
    source_refs: list[str] | None = None,
    evidence_tags: list[str] | None = None,
) -> dict:
    return {
        "id": item_id,
        "lcode": lcode,
        "difficulty": difficulty,
        "stems": stems,
        "correct": correct,
        "distractors": distractors,
        "why_correct": why_correct,
        "distractor_notes": distractor_notes,
        "gaps": gaps,
        "refs": refs,
        "code": code,
        "priority": priority,
        "priority_reason": priority_reason,
        "source_tier": source_tier,
        "source_refs": source_refs or [],
        "evidence_tags": evidence_tags or [],
    }


PRIORITY_A_LCODES_S1 = {"L21101", "L21103", "L21201", "L21203", "L21301", "L21302"}
PRIORITY_A_LCODES_S2 = {"L22103", "L22203", "L22301", "L22303", "L22401", "L22202"}
PRIORITY_B_LCODES_S2 = {"L22101", "L22102", "L22201", "L22302", "L22402"}


def item_subject(item: dict) -> int:
    item_id = item.get("id", "")
    if item_id.startswith("s1") or item.get("lcode", "").startswith("L21"):
        return 1
    return 2


def infer_item_priority(item: dict) -> str:
    if item.get("priority") in {"A", "B", "C"}:
        return item["priority"]

    subject = item_subject(item)
    lcode = item.get("lcode", "")
    item_id = item.get("id", "")

    if subject == 1:
        if lcode in PRIORITY_A_LCODES_S1:
            return "A"
        if any(token in item_id for token in ["rag", "nlp", "risk", "govern", "deploy"]):
            return "A"
        return "B"

    if lcode in PRIORITY_A_LCODES_S2:
        return "A"
    if lcode in PRIORITY_B_LCODES_S2:
        return "B"
    return "C"


def infer_item_priority_reason(item: dict) -> str:
    if item.get("priority_reason"):
        return item["priority_reason"]

    subject = item_subject(item)
    lcode = item.get("lcode", "")
    priority = infer_item_priority(item)

    if priority == "A" and subject == 2:
        return f"{lcode} 屬於科目 2 通過影響最大的高頻區，優先刷。"
    if priority == "A" and subject == 1:
        return f"{lcode} 屬於科目 1 高頻主軸，值得放在前排。"
    if priority == "B":
        return f"{lcode} 屬於官方範圍內的重要補強區，但不是最前排。"
    return f"{lcode} 偏補洞或延伸題，放在最後補。"


def infer_item_source_tier(item: dict) -> str:
    if item.get("source_tier"):
        return item["source_tier"]
    return "official-derived"


def infer_session_priority(subject: int, items: list[dict]) -> str:
    priorities = [infer_item_priority(item) for item in items]
    if not priorities:
        return "C"
    if priorities.count("A") >= max(1, len(priorities) // 2):
        return "A"
    if "A" in priorities or priorities.count("B") >= max(1, len(priorities) // 2):
        return "B"
    return "C"


def infer_session_priority_summary(subject: int, items: list[dict]) -> str:
    priority = infer_session_priority(subject, items)
    if priority == "A":
        return "先刷這份，對過線最有幫助。"
    if priority == "B":
        return "主線刷完後優先補這份。"
    return "放在最後補洞或額外加練。"


def rotate_options(correct: str, distractors: list[str], seed: int) -> tuple[list[tuple[str, str]], str]:
    options = [correct] + distractors
    shift = seed % len(options)
    rotated = options[shift:] + options[:shift]
    labels = ["A", "B", "C", "D"]
    answer_label = labels[rotated.index(correct)]
    return list(zip(labels, rotated)), answer_label


def stable_seed(text: str) -> int:
    return sum(ord(ch) for ch in text)


def option_note_map(options: list[tuple[str, str]], correct: str, distractors: list[str], distractor_notes: list[str]) -> dict[str, str]:
    notes = {correct: "正解"}
    for text, note in zip(distractors, distractor_notes):
        notes[text] = note
    return {label: notes[text] for label, text in options}


def render_question(item: dict, q_no: int, stem_variant: int, concise: bool = False) -> str:
    stem = item["stems"][stem_variant]
    options, answer_label = rotate_options(item["correct"], item["distractors"], stable_seed(item["id"] + stem))
    note_map = option_note_map(options, item["correct"], item["distractors"], item["distractor_notes"])
    priority = infer_item_priority(item)
    source_tier = infer_item_source_tier(item)
    stem = f"優先級：`{priority}`｜來源層級：`{source_tier}`\n\n{stem}"

    wrong_lines = []
    for label, text in options:
        if label == answer_label:
            continue
        wrong_lines.append(f"- `{label}`：{note_map[label]}")

    lines = [
        f"### 題 {q_no}｜`{item['lcode']}`｜難度：`{item['difficulty']}`",
        stem,
    ]
    if item.get("code"):
        lines.append("")
        lines.append("```python")
        lines.extend(item["code"].strip().splitlines())
        lines.append("```")
    lines.append("")
    lines.extend(f"- `{label}` {text}" for label, text in options)
    lines.append("")
    lines.append("<details>")
    lines.append("<summary>顯示答案與說明</summary>")
    lines.append("")
    lines.append(f"正解：`{answer_label}`")
    lines.append(f"來源層級：`{source_tier}`")
    lines.append("")

    if concise:
        lines.append(f"秒判理由：{item['why_correct']}")
        lines.append("")
        lines.append("必補點：")
        lines.extend(f"- {gap}" for gap in item["gaps"][:2])
    else:
        lines.append(f"說明：{item['why_correct']}")
        lines.append("")
        lines.append("其餘選項為何錯：")
        lines.extend(wrong_lines)
        lines.append("")
        lines.append("補強知識點：")
        lines.extend(f"- {gap}" for gap in item["gaps"])
        lines.append("")
        lines.append("回看來源：")
        lines.extend(f"- {ref}" for ref in item["refs"])

    lines.append("")
    lines.append("</details>")
    return "\n".join(lines)


def render_daily_file(day: int, subject: int, items: list[dict], concise: bool = False) -> str:
    meta = DAY_META[day]
    focus = meta["s1_focus"] if subject == 1 else meta["s2_focus"]
    count = meta["s1_count"] if subject == 1 else meta["s2_count"]
    session_priority = infer_session_priority(subject, items)
    session_priority_summary = infer_session_priority_summary(subject, items)
    stem_rows = []
    q_no = 1
    for item in items:
        stem_rows.append(render_question(item, q_no, 0, concise=concise))
        q_no += 1
        stem_rows.append(render_question(item, q_no, 1, concise=concise))
        q_no += 1

    all_gaps = []
    seen = set()
    for item in items:
        for gap in item["gaps"]:
            if gap not in seen:
                seen.add(gap)
                all_gaps.append(gap)
    must_fill = all_gaps[:5]
    a_items = [item["id"] for item in items if infer_item_priority(item) == "A"][:5]

    backfill = dedent(
        """
        - 若本日錯在術語辨識，明天先回看 `sources/scope-weight-map.md` 的對應 L-code。
        - 若本日答對但講不出原因，把該題登錄到 `progress/knowledge-gaps.md`。
        - 若同概念連錯兩次，於 `progress/wrong-answer-map.md` 找下一次回鍋日。
        """
    ).strip()
    if a_items:
        backfill = f"- A 級優先題：{', '.join(a_items)}\n" + backfill

    title = f"Day {day:02d}｜科目 {subject} 反向題單"
    suggestion = "3–5 小時內完成，先做題、再補點。" if subject == 2 else "先以 60–75 分鐘完成第一輪，再展開解析。"
    suggestion = f"{suggestion}｜優先級 {session_priority}｜{session_priority_summary}"

    lines = [
        f"# {title}",
        "",
        f"- 今日焦點：`{focus}`",
        f"- 題量：`{count}` 題",
        f"- 建議方式：{suggestion}",
        "- 來源對照：",
        "  - [official-corpus.md](../sources/official-corpus.md)",
        "  - [scope-weight-map.md](../sources/scope-weight-map.md)",
        "  - [question-source-map.md](../sources/question-source-map.md)",
        "  - [question-patterns.md](../sources/question-patterns.md)",
        "  - [book-bridge.md](../sources/book-bridge.md)",
        "",
        "## 今日題目",
        "",
        "\n\n".join(stem_rows),
        "",
        "## 今日必補知識點",
        "",
    ]
    lines.extend(f"- {gap.rstrip('。') }，回看 [sources](../sources/) 內對應文件。" for gap in must_fill)
    lines.extend(["", "## 明日回補標記", "", backfill])
    return "\n".join(lines).strip() + "\n"


S1_BASE: dict[int, list[dict]] = {
    1: [
        mc(
            "s1d1_tokenization",
            "L21101",
            "中",
            [
                "在文本前處理中，將連續文字切成可供模型處理的詞彙單位，這個步驟稱為何者？",
                "客服團隊想先把抱怨訊息拆成模型可處理的 token，再做後續分析，最先應執行哪個技術？",
            ],
            "斷詞（Tokenization）",
            ["詞形還原（Lemmatization）", "停用詞移除（Stopword Removal）", "詞頻逆文件頻率（TF-IDF）"],
            "斷詞的目的就是把連續文本切成 token，通常是 NLP 前處理的起點。",
            ["詞形還原是把單字轉回原型，不負責切分字串。", "停用詞移除是在切詞之後刪掉低資訊量詞語。", "TF-IDF 是權重計算方法，不是切詞步驟。"],
            ["區分 tokenization、lemmatization、stopword removal、TF-IDF 的先後次序。", "記住 NLP 前處理常見管線：切詞、清理、向量化。"],
            ["sources/official-corpus.md｜114.09 樣題曾出現 tokenization 類題", "sources/scope-weight-map.md｜L21101 自然語言處理技術與應用"],
        ),
        mc(
            "s1d1_sentiment",
            "L21101",
            "易",
            [
                "下列何者最符合自然語言處理在機器學習中的典型用途？",
                "銀行想分析客服留言的正負向傾向，若資料主要是文字，最適合先導入哪一類 AI 任務？",
            ],
            "情緒分析（Sentiment Analysis）",
            ["圖像分類（Image Classification）", "預測性維護（Predictive Maintenance）", "供應鏈優化（Supply Chain Optimization）"],
            "情緒分析直接處理文字的語意與情緒極性，是 NLP 的典型應用。",
            ["圖像分類屬於電腦視覺，不處理文字語意。", "預測性維護通常依賴感測器或設備紀錄，不是文字情緒任務。", "供應鏈優化偏向營運分析，並非文字理解任務。"],
            ["建立文字任務與 NLP、影像任務與 CV 的快速對應。", "看到『留言、評論、客服紀錄』時，優先想到文本分析。"],
            ["sources/official-corpus.md｜官方樣題有 NLP 情緒分析類型", "sources/scope-weight-map.md｜L21101 自然語言處理技術與應用"],
        ),
        mc(
            "s1d1_rule_based_boundary",
            "L21103",
            "中",
            [
                "下列哪一種情境最不屬於使用 AI 或機器學習能力的系統？",
                "若一個象棋程式只依預先寫死的規則枚舉下一步，沒有依資料學習，最合理的判斷為何？",
            ],
            "使用固定規則決定行為的傳統程式",
            ["透過深度神經網路進行語音辨識的系統", "使用 NLP 理解用戶查詢的聊天機器人", "透過資料訓練改善準確率的影像辨識模型"],
            "只有固定規則、沒有從資料中學習或泛化能力的系統，不應被誤判成機器學習系統。",
            ["語音辨識常使用深度學習模型，屬於 AI/ML。", "聊天機器人若理解文本與生成回覆，屬於 NLP 應用。", "影像辨識若依資料訓練改善效能，屬於機器學習。"],
            ["區分 rule-based automation 與 ML system 的邊界。", "看到『固定規則、無訓練資料』時，先排除 ML。"],
            ["sources/official-corpus.md｜114.09 樣題出現 AI/ML 邊界判斷", "sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用"],
        ),
        mc(
            "s1d1_language_model_fit",
            "L21101",
            "中",
            [
                "若企業要從大量 FAQ 與客服逐字稿中自動找出常見問題與關鍵主題，最先應考慮哪一類技術？",
                "製造商累積大量維修文字紀錄，想讓系統先理解文本內容再做分類與摘要，最適合的起點為何？",
            ],
            "自然語言處理技術（NLP）",
            ["電腦視覺技術（CV）", "單純關聯式資料庫正規化", "只做規則式關鍵字比對且不建立語意表示"],
            "任務核心是理解文字內容、主題與語意，因此應先選 NLP 技術。",
            ["CV 主要處理影像與影片，不處理文本語意。", "資料庫正規化是資料儲存設計，無法直接理解文本語意。", "純關鍵字規則缺乏語意泛化能力，面對同義表達容易失效。"],
            ["從問題的輸入資料型態判斷技術路線。", "文字理解任務優先想 NLP，而不是存儲或純規則方案。"],
            ["sources/official-corpus.md｜官方範圍將 NLP 列在 L21101", "sources/scope-weight-map.md｜L21101 自然語言處理技術與應用"],
        ),
    ],
    2: [
        mc(
            "s1d2_cv_tasks",
            "L21102",
            "中",
            [
                "若模型只需判定一張照片中主要物件屬於哪個類別，最符合哪一種電腦視覺任務？",
                "零售商只想知道商品照片屬於鞋子、包包或外套，不需框出位置，應選哪種 CV 任務？",
            ],
            "圖像分類（Image Classification）",
            ["物件偵測（Object Detection）", "語義分割（Semantic Segmentation）", "實例分割（Instance Segmentation）"],
            "圖像分類只回答整張圖的類別，不要求定位或像素級分割。",
            ["物件偵測還要輸出邊界框與位置。", "語義分割需要對每個像素標上類別。", "實例分割除了像素標註，還要區分同類別不同個體。"],
            ["分類、偵測、語義分割、實例分割的輸出粒度要分清。", "看到『只要知道是什麼』先想 classification。"],
            ["sources/official-corpus.md｜官方樣題曾比較多種 CV 任務", "sources/scope-weight-map.md｜L21102 電腦視覺技術與應用"],
        ),
        mc(
            "s1d2_cnn_fit",
            "L21102",
            "易",
            [
                "哪一種深度學習架構通常最適合處理影像辨識任務？",
                "工廠想用影像自動檢測零件表面瑕疵，若以深度學習為主體，最常見的核心架構是哪一類？",
            ],
            "卷積神經網路（CNN）",
            ["朴素貝氏分類器（Naive Bayes）", "單純遞迴神經網路（RNN）", "Apriori 關聯規則演算法"],
            "CNN 能有效抽取局部空間特徵，是影像辨識的標準基礎架構。",
            ["Naive Bayes 可做分類，但不擅長高維影像特徵表示。", "RNN 較適合序列資料，不是影像辨識主流骨幹。", "Apriori 用於關聯規則分析，與影像辨識無關。"],
            ["影像任務先聯想到 CNN；序列任務再考慮 RNN/Transformer。", "辨識演算法名稱與資料型態的典型搭配。"],
            ["sources/official-corpus.md｜科目一評鑑範圍含 CV 技術", "sources/scope-weight-map.md｜L21102 電腦視覺技術與應用"],
        ),
        mc(
            "s1d2_ocr",
            "L21102",
            "中",
            [
                "若企業要把紙本發票中的文字轉成可搜尋的文字資料，最符合哪一種技術應用？",
                "倉儲人員拍攝送貨單影像，想自動擷取影像中的品名與數量，最先應想到哪種 CV/NLP 橋接技術？",
            ],
            "光學字元辨識（OCR）",
            ["語音轉文字（ASR）", "情緒分析（Sentiment Analysis）", "推薦系統（Recommendation System）"],
            "OCR 的核心是從影像中辨識文字內容，再轉成結構化或可搜尋文本。",
            ["ASR 處理的是語音，不是影像中的文字。", "情緒分析是文本理解任務，不負責從影像擷取文字。", "推薦系統不處理影像文字抽取。"],
            ["分清 OCR、ASR、NLP 的輸入資料型態差異。", "看到『影像裡的文字』時，優先想到 OCR。"],
            ["sources/official-corpus.md｜L21102 涵蓋 CV 技術應用", "sources/scope-weight-map.md｜L21102 電腦視覺技術與應用"],
        ),
        mc(
            "s1d2_quality_inspection",
            "L21102",
            "中",
            [
                "下列哪一種場景最適合優先導入電腦視覺技術？",
                "電子廠想在產線上即時檢查焊點是否缺件或偏移，最合理的 AI 技術起點為何？",
            ],
            "以影像做瑕疵檢測與物件定位的電腦視覺方案",
            ["只用文字規則判斷客服情緒的 NLP 系統", "只靠時間序列做下季營收預測的迴歸模型", "只用手動表單蒐集設備巡檢紀錄的流程系統"],
            "產線瑕疵檢測的輸入是影像，且常需定位缺陷，電腦視覺是最直接的路線。",
            ["客服情緒是文字任務，不屬於影像檢測。", "營收預測是數值預測問題，與影像辨識不同。", "手動表單流程本身不提供自動影像判讀能力。"],
            ["根據輸入資料型態與業務目的選技術。", "品質檢測、定位、辨識通常優先落在 CV 範圍。"],
            ["sources/official-corpus.md｜L21102 電腦視覺技術與應用", "sources/scope-weight-map.md｜L21102 電腦視覺技術與應用"],
        ),
    ],
    3: [
        mc(
            "s1d3_rag_core",
            "L21103",
            "中",
            [
                "檢索增強生成（RAG）最主要想解決大型語言模型的哪一類問題？",
                "法務團隊抱怨內部生成式 AI 會引用過時資料並偶爾胡亂編造答案，若先不重訓模型，最合理的補強方向為何？",
            ],
            "降低知識過時與幻覺風險",
            ["讓模型完全不需要任何外部資料", "讓模型只依隨機生成內容作答", "把所有回應限制為固定規則模板"],
            "RAG 透過外部檢索補入最新或可信文件，能降低知識過時與幻覺。",
            ["RAG 的目的正是引入外部知識，而不是移除外部資料。", "隨機生成不會提升正確性，反而增加不穩定性。", "固定模板會降低表達能力，也無法解決知識更新問題。"],
            ["理解 RAG 的核心價值：檢索可信內容再生成。", "區分『更新知識』與『重訓模型』兩條不同路線。"],
            ["sources/official-corpus.md｜評鑑範圍含生成式 AI 技術與應用", "sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用"],
        ),
        mc(
            "s1d3_retrieval_stage",
            "L21103",
            "難",
            [
                "建立高效能 RAG 系統時，在檢索階段最關鍵的挑戰通常是什麼？",
                "若生成式 AI 明明可讀很多 token，但檢索回來的文件與問題常常不夠相關，系統品質仍差，最先該檢查哪一段？",
            ],
            "能否找回語意相關且可信的文件",
            ["把所有文件一次塞進 context window", "一律提高溫度（temperature）讓回答更有創意", "只增加輸出字數上限而不調整檢索品質"],
            "RAG 成敗首先取決於找回的文件是否相關且可信，生成器再強也難以修正錯誤檢索。",
            ["把不相關文件全塞進上下文會增加噪音。", "提高 temperature 影響生成風格，不會改善檢索精準度。", "只增加輸出長度無法彌補檢索來源不對的問題。"],
            ["把『檢索品質』與『生成品質』拆開看。", "看到 RAG 錯誤時，先查 embedding、索引與召回文件品質。"],
            ["sources/official-corpus.md｜官方正式題與樣題都偏好 RAG 情境判斷", "sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用"],
        ),
        mc(
            "s1d3_augmentation_semantics",
            "L21103",
            "難",
            [
                "訓練生成式 AI 時導入資料增強後，模型效能反而下降，下列哪個原因最合理？",
                "團隊把原始影像或文本做大量 augmentation 後，發現模型泛化能力變差。若要先抓最可能的根因，應優先懷疑什麼？",
            ],
            "增強後資料分布偏離原任務語意，破壞了泛化基礎",
            ["只要資料量變多，模型一定會變好", "提高增強比例必然能修正所有過擬合問題", "把增強資料混入後，不需要再確認語意一致性"],
            "資料增強若破壞原始語意或讓分布偏離真實資料，可能直接傷害模型學習。",
            ["資料量增加不等於訊號品質提升。", "過高比例的低品質增強資料可能讓模型學到偏差模式。", "augmentation 仍需維持語意一致性，否則標註訊號會失真。"],
            ["資料增強不是越多越好，關鍵是語意一致與分布合理。", "先檢查 augmentation strategy，再調 learning rate 或模型大小。"],
            ["sources/official-corpus.md｜正式題曾出現 Data Augmentation 情境", "sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用"],
        ),
        mc(
            "s1d3_pruning",
            "L21302",
            "中",
            [
                "企業導入生成式 AI 時，若希望在不大幅犧牲效果下減少模型記憶體占用，最常見的壓縮方法是哪一種？",
                "若邊緣設備無法承載完整模型權重，團隊希望先從模型壓縮著手，最合理的第一步為何？",
            ],
            "參數剪枝（Pruning）",
            ["增加模型層數", "把訓練資料維度做得更高", "只提高 batch size 不改模型結構"],
            "參數剪枝會移除低重要性的權重，是常見的模型壓縮技術。",
            ["增加模型層數通常會提高記憶體需求。", "提高資料維度反而增加計算與儲存負擔。", "batch size 影響訓練批次，不是主要的模型壓縮手段。"],
            ["區分模型壓縮、訓練策略調整、資料工程三種不同問題。", "記住 pruning、quantization、distillation 都是常見壓縮家族。"],
            ["sources/official-corpus.md｜114.09 樣題出現模型壓縮", "sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署"],
        ),
    ],
    4: [
        mc(
            "s1d4_early_fusion",
            "L21104",
            "中",
            [
                "在多模態學習中，Early Fusion 的主要特徵為何？",
                "若系統在模型輸入或特徵提取階段就把影像、文本與表格資料整合，這種做法最接近哪種融合方式？",
            ],
            "在輸入階段或特徵階段整合不同模態資料",
            ["只在最終決策階段投票合併輸出", "完全分開訓練且永不對齊不同模態", "只允許模型處理單一來源資料"],
            "Early Fusion 是先整合不同模態的表示，再交給後續模型學習。",
            ["只在最後投票是 late fusion 的特徵。", "永不對齊模態無法形成有效多模態表示。", "單模態處理不符合多模態學習定義。"],
            ["Early fusion 與 late fusion 的分界要靠『整合發生在何時』來記。", "看到輸入階段整合就先選 early fusion。"],
            ["sources/official-corpus.md｜114.09 樣題出現 Early Fusion", "sources/scope-weight-map.md｜L21104 多模態人工智慧應用"],
        ),
        mc(
            "s1d4_transformer_multimodal",
            "L21104",
            "中",
            [
                "若要強化醫療多模態 AI 同時處理影像與臨床文本的整合能力，下列哪項技術最有幫助？",
                "醫院希望把 CT 影像與病歷文字一起輸入模型做輔助判讀，若追求跨模態對齊與語意整合，最合理的架構方向為何？",
            ],
            "採用 Transformer 架構做跨模態整合",
            ["只用預先定義規則直接產生診斷", "只用單一 CNN 同時處理影像與文字", "只依單一模態資料建立通用模型"],
            "Transformer 與注意力機制較適合做跨模態對齊與長距關聯建模。",
            ["規則系統缺乏跨模態表徵學習能力。", "單一 CNN 不適合直接處理文字與影像的跨模態語意對齊。", "單模態模型無法發揮多模態互補資訊。"],
            ["跨模態整合常見關鍵字：attention、alignment、Transformer。", "不要把單模態最佳模型直接套成多模態答案。"],
            ["sources/official-corpus.md｜114.09 樣題出現醫療多模態整合", "sources/scope-weight-map.md｜L21104 多模態人工智慧應用"],
        ),
        mc(
            "s1d4_missing_modality",
            "L21104",
            "難",
            [
                "多模態模型在推論時若某一模態缺失，最合理的穩定策略為何？",
                "若線上系統偶爾只有影像、沒有文字描述，你仍希望模型保持可用，應優先採取哪類設計思路？",
            ],
            "建立可容忍模態缺失的備援或缺失感知機制",
            ["要求所有輸入一律齊全，缺一就直接停機", "把缺失模態隨便補成固定噪聲而不標記", "完全忽略缺失模態問題，只依訓練集假設上線"],
            "實務系統需考慮模態缺失，因此要設計 fallback、mask 或缺失感知流程。",
            ["實務環境不保證資料永遠齊全，直接停機可用性很差。", "隨機補噪聲但不讓模型知道缺失狀態，容易引入偏差。", "上線後忽略缺失模態風險，系統穩定性不足。"],
            ["多模態系統除了準確率，也要看可用性與魯棒性。", "題目提到某模態缺失時，先找 fallback 或 masking 類答案。"],
            ["sources/official-corpus.md｜正式題曾出現模態缺失情境", "sources/scope-weight-map.md｜L21104 多模態人工智慧應用"],
        ),
        mc(
            "s1d4_shared_representation",
            "L21104",
            "中",
            [
                "多模態模型若希望讓文字與影像能在同一語意空間互相比對，最核心的設計目標是什麼？",
                "商品搜尋系統想做到『輸入一句描述就找到相符圖片』，若從模型設計角度看，最重要的能力是什麼？",
            ],
            "建立共享表徵空間（shared representation space）",
            ["把不同模態永遠分開儲存，不做對齊", "只增加單一模態資料量，不做跨模態學習", "只依關鍵字規則做固定映射，不學習向量表示"],
            "跨模態檢索與對齊依賴共享語意空間，讓不同模態可被共同比較。",
            ["完全分開儲存無法支撐跨模態相似度計算。", "只增加單一模態資料量不會自動形成跨模態對齊。", "固定規則映射缺乏彈性與泛化能力。"],
            ["理解多模態檢索的關鍵不是資料量，而是 representation alignment。", "『一句話找圖片』通常對應 shared embedding space。"],
            ["sources/official-corpus.md｜L21104 多模態應用", "sources/scope-weight-map.md｜L21104 多模態人工智慧應用"],
        ),
    ],
    5: [
        mc(
            "s1d5_data_readiness",
            "L21201",
            "中",
            [
                "企業評估是否導入 AI 前，若想先判斷專案可行性，最先要確認哪一項基礎條件？",
                "主管急著上生成式 AI，但團隊連乾淨資料、標註規則與更新流程都沒有。若你只能先做一項評估，最優先的是什麼？",
            ],
            "資料可用性與資料品質是否支撐目標任務",
            ["先挑最流行的模型名稱", "先購買最多 GPU，再回頭想資料", "先承諾上線日期，再補需求訪談"],
            "資料是 AI 專案能否落地的基礎，沒有足夠且可信的資料，再好的模型也難以成功。",
            ["模型流行不代表適合當前資料條件與業務問題。", "硬體採購不能替代資料治理。", "先承諾時程但未完成需求與資料評估，風險最高。"],
            ["導入評估的第一關通常是資料、目標、指標，而不是先追模型。", "看到『可行性』就先問資料與需求是否成立。"],
            ["sources/official-corpus.md｜L21201 AI 導入評估", "sources/scope-weight-map.md｜L21201 AI 導入評估"],
        ),
        mc(
            "s1d5_cost_benefit",
            "L21201",
            "中",
            [
                "在 AI 導入評估中，成本效益分析的主要目的為何？",
                "若兩種解決方案都做得到，但一種建置成本高且維運複雜，另一種效能稍低但回收期短，評估階段最該比較的是什麼？",
            ],
            "確認預期效益是否足以支持建置與維運成本",
            ["只比較模型參數量大小", "只看供應商簡報中的準確率最高值", "只以技術新穎程度做決策"],
            "導入評估不能只看技術能力，還要看 ROI、維運成本、風險與可持續性。",
            ["參數量不是商業價值的直接替代指標。", "單次準確率展示常忽略資料條件與維運成本。", "技術新穎不等於商業上最值得導入。"],
            ["評估階段要把效能、成本、風險、回收期一起看。", "ROI 與 TCO 是常見管理層判斷語言。"],
            ["sources/official-corpus.md｜AI 導入評估範圍含成本效益分析", "sources/scope-weight-map.md｜L21201 AI 導入評估"],
        ),
        mc(
            "s1d5_poc",
            "L21201",
            "中",
            [
                "在全面上線前，哪一種做法最適合作為 AI 導入評估的中間步驟？",
                "企業對生成式 AI 專案仍不確定內部流程能否承接，若不想直接大規模上線，最合適的下一步是什麼？",
            ],
            "先做 PoC 或小規模試點驗證",
            ["直接全公司同步切換到新系統", "先簽五年長約再決定需求", "跳過驗證直接把模型接到核心交易流程"],
            "PoC 能以較低風險驗證資料、流程、指標與使用者接受度。",
            ["直接全量切換缺乏風險緩衝。", "先綁長約會鎖死後續調整空間。", "跳過驗證導致上線風險與責任暴增。"],
            ["評估階段的關鍵詞：PoC、pilot、low-risk validation。", "先小範圍驗證，再決定是否擴大部署。"],
            ["sources/official-corpus.md｜L21201 AI 導入評估", "sources/scope-weight-map.md｜L21201 AI 導入評估"],
        ),
        mc(
            "s1d5_kpi",
            "L21201",
            "中",
            [
                "AI 導入評估若沒有明確 KPI，最常見的問題是什麼？",
                "若主管只說『要導入 AI 提升效率』，卻沒有定義要縮短多少時間、降低多少錯誤率，這在評估階段最主要的缺口是什麼？",
            ],
            "無法客觀判斷專案是否成功",
            ["模型一定會訓練失敗", "所有資料都會自動變得不可用", "雲端成本一定會高於地端成本"],
            "沒有明確 KPI，就難以衡量效益、比較方案與決定是否擴張部署。",
            ["KPI 不明不代表模型一定訓練失敗，但會讓驗收標準模糊。", "資料可用性是另一個問題，不會因 KPI 不明自動失效。", "部署成本取決於設計與規模，不能直接由 KPI 問題推出。"],
            ["把『導入目的』轉成可量化指標是評估核心。", "常見 KPI：工時、召回率、錯誤率、處理時效、人工覆核比例。"],
            ["sources/official-corpus.md｜AI 導入評估與規劃均強調目標與指標", "sources/scope-weight-map.md｜L21201 AI 導入評估"],
        ),
    ],
    6: [
        mc(
            "s1d6_requirement_first",
            "L21202",
            "中",
            [
                "AI 導入規劃時，若企業需求仍不清楚，最合理的第一步為何？",
                "行銷、客服、法務各自想要不同 AI 功能，但都還沒定義輸入、輸出與責任邊界。你若先做一件事，應優先做什麼？",
            ],
            "先做需求分析與利害關係人對齊",
            ["直接選定最熱門模型並開始訓練", "先採購硬體與軟體，再回頭補需求", "先把所有流程完全自動化，不留人工審核"],
            "需求不清時，先對齊目標、使用者、輸入輸出與責任邊界，才能做後續架構規劃。",
            ["先選模型容易造成技術與問題錯配。", "先採購資源可能造成閒置或規格錯誤。", "未完成需求與風險分析前，不應貿然全面自動化。"],
            ["規劃先於建置，需求先於選型。", "題目提到多部門分歧時，優先想到需求澄清與 stakeholder alignment。"],
            ["sources/official-corpus.md｜L21202 AI 導入規劃", "sources/scope-weight-map.md｜L21202 AI 導入規劃"],
        ),
        mc(
            "s1d6_resource_allocation",
            "L21202",
            "中",
            [
                "AI 導入規劃中的資源分配，最不應忽略哪一類非模型資源？",
                "團隊只排了 GPU 與 API 預算，卻沒有安排資料治理、標註維護與業務驗證人力。這在規劃上最主要的問題是什麼？",
            ],
            "資料治理與業務驗證人力也是核心資源",
            ["只要模型準確率高，其他角色都可省略", "資源分配只需要看硬體，不必看流程維運", "AI 專案只要工程師，不需要業務與法務參與"],
            "AI 專案不是只有模型與硬體，資料治理、業務驗證與風險控管都是必要資源。",
            ["高準確率不能替代流程與治理人力。", "只看硬體會忽略資料更新與使用者導入成本。", "業務與法務角色關係到需求正確性與合規性。"],
            ["資源分配要包含人、資料、流程、算力與治理責任。", "看到『只買設備』的答案通常不完整。"],
            ["sources/official-corpus.md｜L21202 AI 導入規劃", "sources/scope-weight-map.md｜L21202 AI 導入規劃"],
        ),
        mc(
            "s1d6_rollout",
            "L21202",
            "中",
            [
                "若企業希望降低 AI 導入失敗的營運衝擊，最合理的上線策略為何？",
                "客服單位擔心新 AI 摘要系統一上線就全面替代舊流程會出現錯誤，從導入規劃角度最好的安排是什麼？",
            ],
            "採分階段上線並保留人工覆核與回退機制",
            ["在沒有備援下直接全面切換", "只做一次內部 demo 就宣告專案完成", "先停掉舊流程再看新系統是否穩定"],
            "分階段 rollout 能保留修正空間，也能逐步觀察使用者與品質指標。",
            ["全面切換在錯誤發生時缺乏緩衝。", "demo 只能展示功能，不足以證明穩定度。", "先停掉舊流程會讓風險在第一天就擴散。"],
            ["rollout 規劃要有人工覆核、rollback 與監控。", "『分階段』通常比『一次到位』更安全。"],
            ["sources/official-corpus.md｜L21202 AI 導入規劃", "sources/scope-weight-map.md｜L21202 AI 導入規劃"],
        ),
        mc(
            "s1d6_acceptance",
            "L21202",
            "中",
            [
                "在 AI 導入規劃中，驗收條件（acceptance criteria）最主要的作用為何？",
                "若專案團隊與業務部門對『模型做得不錯』的理解不同，為避免上線爭議，規劃階段最該先補什麼？",
            ],
            "把可接受的品質門檻與責任邊界寫清楚",
            ["讓模型不需要再做任何監控", "保證模型永遠不會產生錯誤", "取代所有需求訪談與使用者測試"],
            "驗收條件是用來定義什麼叫『可以上線』，不是消滅所有風險。",
            ["監控仍是上線後必要機制。", "任何模型都無法保證永遠零錯誤。", "驗收條件不能取代前期訪談與測試，只能補強共識。"],
            ["KPI 與 acceptance criteria 要分開看：前者偏目標，後者偏交付門檻。", "有驗收標準，才有明確的 go / no-go 決策點。"],
            ["sources/official-corpus.md｜L21202 AI 導入規劃", "sources/scope-weight-map.md｜L21202 AI 導入規劃"],
        ),
    ],
    7: [
        mc(
            "s1d7_copyright_prevention",
            "L21203",
            "中",
            [
                "企業部署生成式 AI 協助行銷內容產出，若要降低著作權侵權風險，最有效的預防策略為何？",
                "內容團隊常把 AI 生成文案直接外發。若你要從流程面先降風險，最優先的安排應是什麼？",
            ],
            "建立資料來源審查、輸出覆核與授權檢查流程",
            ["只要模型夠大，就不會有著作權風險", "把所有輸出都自動發布，避免人工拖慢速度", "只看點擊率，不必檢查引用來源與授權"],
            "著作權風險主要來自訓練來源、輸出近似與使用流程，因此要建立審查與覆核機制。",
            ["模型大小與侵權風險沒有必然反比關係。", "自動發布會放大錯誤輸出與侵權責任。", "只看商業指標會忽略法律風險。"],
            ["生成式 AI 法務風險通常要從流程治理，而非只從模型參數處理。", "看到『侵權』優先想到授權、來源、覆核、紀錄。"],
            ["sources/official-corpus.md｜正式題出現生成式 AI 著作權風險", "sources/scope-weight-map.md｜L21203 AI 風險管理"],
        ),
        mc(
            "s1d7_supply_chain",
            "L21203",
            "中",
            [
                "供應鏈攻擊（Supply Chain Attack）對企業內部 AI 系統的主要風險來源為何？",
                "企業大量依賴第三方開源模型、套件與資料集。若要描述其最核心的供應鏈風險，下列哪項最合理？",
            ],
            "第三方模型或資料可能被植入惡意內容",
            ["供應鏈攻擊只會發生在硬體層", "只要在內網使用 AI，就沒有供應鏈問題", "供應鏈攻擊與開源套件、模型權重無關"],
            "AI 系統常依賴外部模型、資料與套件，因此第三方來源被污染會直接影響內部系統安全。",
            ["供應鏈問題不只在硬體，也可能在軟體、模型與資料。", "內網部署仍可能引入受污染的外部元件。", "開源套件與模型權重正是常見供應鏈入口。"],
            ["把『供應鏈』理解為所有外部依賴，不只是設備採購。", "對第三方模型與資料做 provenance 檢查是基本功。"],
            ["sources/official-corpus.md｜114.09 樣題出現供應鏈攻擊", "sources/scope-weight-map.md｜L21203 AI 風險管理"],
        ),
        mc(
            "s1d7_adversarial_training",
            "L21203",
            "難",
            [
                "若模型容易被對抗樣本騙過，從模型層面最直接的補強做法通常是什麼？",
                "金融風控模型被駭客透過微小特徵擾動成功誤導。若你想優先提升模型對這類攻擊的辨識韌性，較合理的技術方向為何？",
            ],
            "導入對抗訓練（adversarial training）",
            ["只增加輸出字數上限", "只把訓練資料做欄位重新命名", "只在簡報中加入風險聲明而不調整模型"],
            "對抗訓練是直接把擾動樣本納入訓練，提升模型對惡意擾動的穩健性。",
            ["輸出字數與對抗韌性無直接關聯。", "重新命名欄位不會改變模型面對對抗擾動的能力。", "風險聲明屬治理措施，不是模型層補強。"],
            ["把技術補強與流程治理分開看。", "只要題目強調『惡意擾動輸入』，優先想到 adversarial training 或 robust training。"],
            ["sources/official-corpus.md｜正式題出現對抗攻擊情境", "sources/scope-weight-map.md｜L21203 AI 風險管理"],
        ),
        mc(
            "s1d7_transparency",
            "L21203",
            "中",
            [
                "在 AI 治理脈絡下，透明性（Transparency）通常指什麼？",
                "若企業要讓審查單位能追蹤 AI 如何得出決策、使用何種資料與規則，最符合哪項治理原則？",
            ],
            "決策流程與依據具可理解性與可追溯性",
            ["所有模型都必須完全開源", "系統只要速度夠快就算透明", "只要模型有商業價值，就不需要說明原理"],
            "透明性重點在可解釋與可追溯，不等於所有細節都要公開原始碼。",
            ["開源與否是治理手段選項，不是透明性的唯一條件。", "速度快與是否透明是不同維度。", "有商業價值不代表可以忽略說明責任。"],
            ["記住 transparency、explainability、traceability 是一組常連動的治理概念。", "不要把『透明』誤解成『全部開源』。"],
            ["sources/official-corpus.md｜L21203 AI 風險管理與治理", "sources/scope-weight-map.md｜L21203 AI 風險管理"],
        ),
    ],
    8: [
        mc(
            "s1d8_regression_fit",
            "L21301",
            "中",
            [
                "若目標是根據歷史銷售資料預測下一季銷售額，下列哪種模型類型最適合？",
                "電商老闆想依過去產品銷量預估下季數量，以便調整庫存，最合理的第一個模型方向為何？",
            ],
            "迴歸模型（Regression）",
            ["分群模型（Clustering）", "分類模型（Classification）", "關聯規則分析（Association Rules）"],
            "預測連續數值目標時，首選應是迴歸模型。",
            ["分群用於找群組，不直接輸出連續預測值。", "分類輸出類別標籤，不是連續數值。", "關聯規則用來找共現模式，不是數值預測。"],
            ["先辨識目標變數型態：連續值選 regression，離散標籤選 classification。", "看到『預測金額、銷量、工時』時，優先想回歸。"],
            ["sources/official-corpus.md｜114.09 樣題出現回歸任務選型", "sources/scope-weight-map.md｜L21301 數據準備與模型選擇"],
        ),
        mc(
            "s1d8_scaling",
            "L21301",
            "中",
            [
                "資料中若特徵尺度差異極大，最常見的前處理解法是什麼？",
                "當年齡範圍是 0–100、收入範圍是 0–1,000,000，模型容易偏向高尺度欄位。若要先穩定模型，最合理的做法為何？",
            ],
            "對特徵做標準化或正規化",
            ["直接刪除尺度較小的欄位", "把所有欄位都加上一個常數", "完全不處理尺度差異"],
            "對尺度敏感的模型常需先做標準化或正規化，避免某些欄位因量級大而主導學習。",
            ["刪欄位可能損失有效訊息，且不是解決尺度問題的標準做法。", "加常數不會改變相對尺度關係。", "忽略尺度差異會讓模型學習不穩定。"],
            ["標準化、正規化與模型敏感度要建立連結。", "尺度問題通常先補 preprocessing，而不是先換演算法。"],
            ["sources/official-corpus.md｜114.09 樣題出現標準化情境", "sources/scope-weight-map.md｜L21301 數據準備與模型選擇"],
        ),
        mc(
            "s1d8_unsupervised_grouping",
            "L21301",
            "中",
            [
                "若事前沒有定義用戶類型，想先把相似用戶自動分群，最合理的模型方向為何？",
                "音樂平台只有使用者聽歌與搜尋行為，沒有既定標籤，卻想先找出使用者類型輪廓，應先選哪一種學習範式？",
            ],
            "非監督式學習（Unsupervised Learning）",
            ["監督式學習（Supervised Learning）", "強化學習（Reinforcement Learning）", "規則式專家系統"],
            "沒有標籤時，先用非監督式方法探索群組或資料結構最合理。",
            ["監督式學習需要既有標籤作為訓練目標。", "強化學習需要回饋訊號與互動環境。", "規則式系統無法自動從資料中學出群組結構。"],
            ["標籤有無，是分 supervised / unsupervised 的第一判斷點。", "看到『事前沒有定義類型』，優先找 clustering 或密度方法。"],
            ["sources/official-corpus.md｜114.09 樣題出現 DBSCAN 分群情境", "sources/scope-weight-map.md｜L21301 數據準備與模型選擇"],
        ),
        mc(
            "s1d8_feature_learning",
            "L21301",
            "中",
            [
                "對於低結構化的文本或圖像資料，下列哪種特徵工程方向通常最適用？",
                "若資料多為原始圖像與長文本，不想手工設計大量欄位，較合理的方向為何？",
            ],
            "特徵學習（Feature Learning）",
            ["只做手工特徵挑選", "只做人工資料輸入格式化", "只依人工規則固定欄位值"],
            "非結構化資料常由模型自行學習表徵，比純手工欄位設計更有效。",
            ["手工特徵挑選對非結構化資料通常不夠彈性。", "格式化只是清理資料，不等於學到有用表徵。", "固定規則欄位難以覆蓋複雜語意或視覺特徵。"],
            ["結構化資料常做人工特徵；非結構化資料常做 representation learning。", "看到文本/圖像原始輸入時，先想 embedding 或 deep feature learning。"],
            ["sources/official-corpus.md｜114.09 樣題出現特徵學習", "sources/scope-weight-map.md｜L21301 數據準備與模型選擇"],
        ),
    ],
    9: [
        mc(
            "s1d9_kubernetes",
            "L21302",
            "中",
            [
                "Kubernetes 在 AI 模型部署與運行中的核心角色最接近下列何者？",
                "若團隊想讓模型服務能自動部署、擴縮與管理執行環境，最符合 Kubernetes 價值的描述為何？",
            ],
            "管理與協調模型服務的部署、擴展與運行環境",
            ["自動幫模型做超參數調整", "提供資料倉儲與版本控管的全部功能", "直接負責所有 GPU 推論計算本身"],
            "Kubernetes 主要處理容器化服務的部署、調度、擴縮與穩定運行。",
            ["超參數調整屬訓練與實驗管理，不是 Kubernetes 的核心職責。", "資料倉儲與版本控管需要其他工具配合。", "Kubernetes 會調度資源，但不等於 GPU 推論演算法本身。"],
            ["Kubernetes 是 orchestration，不是 model training tool。", "分清部署平台、實驗平台、資料平台的責任。"],
            ["sources/official-corpus.md｜正式題出現 Kubernetes", "sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署"],
        ),
        mc(
            "s1d9_integration_testing",
            "L21302",
            "中",
            [
                "AI 模型即將進入系統整合測試階段，下列哪項驗證最應優先執行？",
                "模型在驗證集表現不差，但即將接到前後端與資料平台。若只能先做一項整合檢查，最應先確認什麼？",
            ],
            "模型服務與資料平台、前後端介面的資料格式與流程是否協同正常",
            ["只再看一次訓練集準確率", "只檢查 commit message 是否符合規範", "只審閱文件版面是否美觀"],
            "整合測試要先確認模組在真實流程中能正常交換資料與協同運作。",
            ["訓練集表現不代表系統整合無誤。", "程式碼規範重要，但不是整合測試第一優先。", "文件格式不會驗證流程是否可用。"],
            ["integration testing 看的是流程與介面，不是單一模型分數。", "題目提到資料平台、前後端時，先找 interface / schema / workflow consistency。"],
            ["sources/official-corpus.md｜114.09 樣題出現整合測試", "sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署"],
        ),
        mc(
            "s1d9_drift_monitoring",
            "L21302",
            "難",
            [
                "模型上線後，若想監控輸入特徵分布是否偏離訓練資料，哪一類指標最有代表性？",
                "若你懷疑業務資料分布已改變，導致模型精度下降，但標籤回收還很慢，最先可用哪類監控訊號判斷 drift？",
            ],
            "資料分布漂移指標，例如 PSI（Population Stability Index）",
            ["只看 CPU 使用率", "只看 API 回應字數長短", "只看 commit 次數是否增加"],
            "當標籤尚未回收時，先看輸入分布是否偏移，是線上監控常見做法。",
            ["CPU 使用率是系統資源指標，不是資料漂移指標。", "回應字數無法直接代表資料分布是否偏移。", "commit 次數與線上資料分布無直接關係。"],
            ["把 model drift 與 system metrics 區分開。", "PSI、KL divergence、feature distribution monitoring 是常見 drift 訊號。"],
            ["sources/official-corpus.md｜正式題出現 PSI 類 drift 概念", "sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署"],
        ),
        mc(
            "s1d9_canary",
            "L21302",
            "中",
            [
                "若企業想降低新模型上線事故對全部使用者的衝擊，最適合的部署策略為何？",
                "團隊準備替換線上模型，但擔心新版本會在真實流量下出現未預期錯誤。若要先在小流量驗證，應採哪種思路？",
            ],
            "採小流量試放的 canary 或分階段部署策略",
            ["直接 100% 切到新版本", "先停掉舊服務再部署新版本", "只在簡報中宣告模型已準備好"],
            "canary deployment 能在有限流量下觀察風險，便於回退。",
            ["直接全量切換會把風險一次擴散到所有使用者。", "先停舊服務會增加停機與失敗風險。", "文件宣告無法取代真實流量驗證。"],
            ["部署策略要跟風險控制綁在一起理解。", "看到『小流量、先驗證、可回退』時，優先選 canary / phased rollout。"],
            ["sources/official-corpus.md｜L21302 系統部署與更新管理", "sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署"],
        ),
    ],
    10: [
        mc(
            "s1d10_seq2seq",
            "L21101",
            "中",
            [
                "若任務是把輸入序列轉成另一段輸出序列，例如翻譯或摘要，最合理的模型方向為何？",
                "若系統要把輸入文字轉成語意等價的另一段文字，例如自動翻譯或摘要，最合理的模型方向為何？",
            ],
            "序列到序列（Seq2Seq）模型",
            ["只做關鍵字頻率統計", "只做圖像分類", "只做實體名稱標註（NER）"],
            "Seq2Seq 適合處理輸入序列到輸出序列的映射，例如翻譯與摘要。",
            ["關鍵字頻率統計不會生成新的序列。", "圖像分類處理的是整張圖的類別。", "NER 是序列標註，不等於生成另一段序列。"],
            ["分清 classification、sequence labeling、sequence generation。", "看到『翻譯、摘要、改寫』時，優先想 Seq2Seq。"],
            ["sources/official-corpus.md｜正式題出現 Seq2Seq", "sources/scope-weight-map.md｜L21101 自然語言處理技術與應用"],
        ),
        mc(
            "s1d10_word2vec",
            "L21101",
            "難",
            [
                "資料量大且希望更有效捕捉罕見詞語意關聯時，Word2Vec 較適合採哪種訓練策略？",
                "客服語料中有大量低頻專有名詞，若想讓詞向量更能學到罕見詞的上下文關係，較合理的選擇為何？",
            ],
            "採用 Skip-gram 架構",
            ["採用只靠詞頻排序的 TF-IDF", "採用 CBOW 並假設它對罕見詞一定更有利", "完全不做詞向量，只保留原始字串"],
            "Skip-gram 以中心詞預測周邊詞，對低頻詞的表示通常更有優勢。",
            ["TF-IDF 是加權方法，不是分散式詞向量模型。", "CBOW 訓練較快，但對低頻詞的語意關聯通常不如 Skip-gram 穩定。", "不做向量化無法讓模型有效利用詞的語意鄰近關係。"],
            ["把 TF-IDF 與 Word2Vec 分清：前者是稀疏權重，後者是嵌入向量。", "低頻詞、上下文語意、Skip-gram 這三個關鍵字要連在一起。"],
            ["sources/official-corpus.md｜正式題出現 Word2Vec / Skip-gram", "sources/scope-weight-map.md｜L21101 自然語言處理技術與應用"],
        ),
        mc(
            "s1d10_automl_trend",
            "L21302",
            "中",
            [
                "下列何者較符合機器學習模型在業界部署的主要趨勢？",
                "若題目問近年企業在部署機器學習時最明顯的共通方向，下列哪個選項最合理？",
            ],
            "越來越多地採用 AutoML 與自動化流程",
            ["全面放棄雲端平台", "全面改回手動超參數調整", "盡量改用更少資料與更少監控"],
            "業界趨勢是把訓練、部署與監控流程自動化，提高效率與可重複性。",
            ["雲端與平台化能力仍是主流基礎設施之一。", "手動調參仍存在，但不是主要趨勢方向。", "資料與監控不足通常會提高風險，不是成熟部署方向。"],
            ["AutoML、MLOps、自動化 pipeline 常一起出現。", "趨勢題通常考『流程自動化』而非『全面手動』。"],
            ["sources/official-corpus.md｜114.09 樣題出現 AutoML 趨勢", "sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署"],
        ),
        mc(
            "s1d10_augmentation_control",
            "L21103",
            "中",
            [
                "在資料增強（data augmentation）策略中，哪個做法最能避免模型學到錯誤訊號？",
                "若團隊希望利用 augmentation 增加資料量，但又不想讓模型學到與真實任務不一致的樣本，最該守住哪個原則？",
            ],
            "維持增強後資料與原任務語意一致",
            ["只要數量夠大，語意是否一致不重要", "增強比例越高越安全", "完全不檢查標註與分布是否改變"],
            "增強的價值在於增加合理變化，不是破壞原任務定義與標註訊號。",
            ["大量低品質資料只會放大噪音。", "增強比例沒有固定越高越好的結論。", "不檢查標註與分布會直接導致模型偏差。"],
            ["augmentation 的第一原則是 semantic consistency。", "先看資料訊號是否仍對準原任務，再談數量與模型。"],
            ["sources/official-corpus.md｜正式題出現 augmentation 分布偏移", "sources/scope-weight-map.md｜L21103 生成式 AI 技術與應用"],
        ),
    ],
    13: [
        mc(
            "s1d13_license_provenance",
            "L21203",
            "難",
            [
                "生成式 AI 導入到正式內容流程前，若要降低法規與授權爭議，對訓練或檢索資料最應先做哪項管理？",
                "法務要求團隊能回答『這份模型或知識庫內容從哪裡來、能不能用』，最核心的治理補強是什麼？",
            ],
            "建立資料來源與授權狀態的 provenance 管理",
            ["只保留模型名稱，不記來源", "只要是網路上找得到的資料就可直接使用", "只看生成速度，不必保留資料使用紀錄"],
            "能追溯來源與授權，是處理著作權與合規爭議的基礎能力。",
            ["只記模型名稱無法回答來源是否合法。", "公開可見不等於可合法重製或再利用。", "沒有紀錄就很難做事後審核與責任釐清。"],
            ["provenance、licensing、usage log 是一組要一起記的概念。", "看到法規或授權題，優先找 traceability 類答案。"],
            ["sources/official-corpus.md｜book-bridge 亦對應治理與規管書目", "sources/scope-weight-map.md｜L21203 AI 風險管理"],
        ),
        mc(
            "s1d13_human_review",
            "L21203",
            "中",
            [
                "若生成內容要對外發布，哪一項流程最能降低錯誤引用與侵權輸出的責任風險？",
                "行銷團隊想直接把 AI 產出的文案推上官網。若你只能補一個控管點，最值得先加的是什麼？",
            ],
            "在人機流程中加入人工覆核與發布前審查",
            ["把人工全部拿掉以提升速度", "只在事後出問題時再補說明", "只根據點閱率決定是否發布"],
            "對外發布前的人工作業能攔截侵權、錯誤事實與不當語句，是高風險場景常見必要控管。",
            ["完全去除人工會放大錯誤外部化風險。", "事後補救通常成本更高且傷害已發生。", "點閱率是商業指標，不等於合規或正確性。"],
            ["高風險輸出場景常考 human-in-the-loop。", "把『內部輔助』與『對外發布』的治理強度分開。"],
            ["sources/official-corpus.md｜L21203 AI 風險管理", "sources/scope-weight-map.md｜L21203 AI 風險管理"],
        ),
        mc(
            "s1d13_pii_masking",
            "L21203",
            "中",
            [
                "若企業把客戶對話送進生成式 AI 服務前，最重要的隱私保護前處理之一是什麼？",
                "客服逐字稿內含姓名、電話與地址，團隊想拿來做摘要與知識庫整理。若要先補一個資料安全動作，最應做什麼？",
            ],
            "先做個資遮罩或去識別化處理",
            ["直接把原始資料完整上傳，之後再說", "只改檔名，不改內容", "只壓縮檔案大小，不處理隱私欄位"],
            "個資遮罩或去識別化可在送入模型前降低敏感資訊外洩風險。",
            ["原樣上傳會放大外洩與合規風險。", "只改檔名不會改變內容中的敏感資訊。", "壓縮大小與隱私保護沒有直接關係。"],
            ["隱私保護看資料內容，不看檔案外觀。", "看到姓名、電話、地址等欄位時，先想 masking / de-identification。"],
            ["sources/official-corpus.md｜L21203 風險管理含安全與合規", "sources/scope-weight-map.md｜L21203 AI 風險管理"],
        ),
        mc(
            "s1d13_audit_log",
            "L21203",
            "中",
            [
                "若日後要追查 AI 為何輸出某段內容，哪種治理設計最有助於事後稽核？",
                "法遵單位要求『出事後能回溯是誰用什麼資料、什麼提示、哪個版本的模型產生結果』，最合理的作法為何？",
            ],
            "保留提示、資料來源、模型版本與操作紀錄的 audit trail",
            ["只保留最終輸出文字即可", "只記誰登入，不記模型與資料版本", "只保留模型名稱，不記操作歷程"],
            "可稽核紀錄能支撐責任釐清、問題重現與法遵要求。",
            ["只有最終輸出不足以重建決策脈絡。", "只記登入資訊無法回推出內容生成依據。", "只有模型名稱也缺少資料與提示上下文。"],
            ["audit trail 通常要包含人、資料、提示、版本、時間。", "追溯題的核心不是再訓練，而是紀錄完整性。"],
            ["sources/official-corpus.md｜治理與風險管理", "sources/scope-weight-map.md｜L21203 AI 風險管理"],
        ),
        mc(
            "s1d13_model_card",
            "L21203",
            "中",
            [
                "若企業要向內部說明模型用途、限制、偏誤風險與適用情境，下列哪種文件化做法最有幫助？",
                "你需要讓非技術主管快速了解模型能做什麼、不能做什麼、在哪些條件下容易失準。最適合優先建立哪種文件？",
            ],
            "建立模型卡（model card）或同類型能力說明文件",
            ["只保留程式碼，不提供任何說明", "只給最高準確率數字，不寫限制", "只在口頭會議上描述，不留文件"],
            "模型卡能把用途、限制、偏誤、資料條件與監控建議說清楚，是治理常用文件。",
            ["只有程式碼對非技術利害關係人不夠透明。", "只給最高分數會掩蓋模型限制與風險。", "不留文件不利於知識傳承與稽核。"],
            ["治理題常把文件透明化視為風險控管的一部分。", "記住 model card 的用途是『說明能力與限制』。"],
            ["sources/official-corpus.md｜治理與透明性導向題型", "sources/scope-weight-map.md｜L21203 AI 風險管理"],
        ),
    ],
    14: [
        mc(
            "s1d14_input_validation",
            "L21203",
            "中",
            [
                "若企業擔心模型受到惡意格式輸入或極端異常值衝擊，上線前最實務的第一層保護通常是什麼？",
                "除了從模型本身補強外，若要先在系統入口擋掉格式異常與極端輸入，最合理的做法為何？",
            ],
            "加強輸入驗證與資料前處理檢查",
            ["把所有異常輸入都直接當成正常樣本餵進模型", "只提高 GPU 數量", "只增加輸出長度上限"],
            "入口檢查能在模型看到資料前先過濾明顯錯誤或惡意輸入，是低成本有效的第一層防線。",
            ["把異常資料當正常資料只會放大風險。", "GPU 數量與輸入安全性無直接關聯。", "輸出長度不會改善入口資料品質。"],
            ["風險管理要分成入口、模型、流程三層看。", "看到『格式不符、極端值』先想 input validation。"],
            ["sources/official-corpus.md｜正式題出現對抗攻擊與資料前處理", "sources/scope-weight-map.md｜L21203 AI 風險管理"],
        ),
        mc(
            "s1d14_adversarial_training_again",
            "L21203",
            "難",
            [
                "若想從根本提升模型面對微小惡意擾動的抵抗力，哪一種技術手段最直接？",
                "上線模型常被帶有微小噪音的輸入騙過。若你要在訓練流程中補一個最對題的做法，應選什麼？",
            ],
            "在訓練階段加入對抗樣本訓練",
            ["只把介面字體變大", "只把檔案名稱改成英文", "只增加簡報中對模型的信心描述"],
            "把對抗樣本納入訓練能讓模型學到更穩健的決策邊界。",
            ["介面字體不會影響模型的魯棒性。", "檔名格式與模型抗擾動能力無關。", "文字宣示不是技術補強。"],
            ["看到『微小擾動、欺騙模型』就回到 adversarial training。", "題目若問『從根本』，通常在找模型層或訓練層答案。"],
            ["sources/official-corpus.md｜正式題對抗樣本情境", "sources/scope-weight-map.md｜L21203 AI 風險管理"],
        ),
        mc(
            "s1d14_canary_rollback",
            "L21302",
            "中",
            [
                "新模型上線後若指標異常惡化，哪種事前規劃最能縮短事故處理時間？",
                "團隊擔心部署後若精度突然下降會影響交易流程。若要讓事故處理更快，規劃階段最值得先準備的是什麼？",
            ],
            "預先定義 rollback 與版本切換流程",
            ["等出事後再臨時決定如何回退", "只保留最新版本，不保留舊版映像", "只在內部聊天訊息中口頭說明應變方式"],
            "有清楚的 rollback 流程與版本管理，才能在異常發生時迅速恢復服務。",
            ["臨時決策會拉長停機與誤判時間。", "沒有舊版映像就無法快速回切。", "口頭說明缺乏一致性與可執行性。"],
            ["部署題除了 canary，也常考 rollback preparedness。", "『出事怎麼回來』是部署規劃不可省略的一段。"],
            ["sources/official-corpus.md｜L21302 系統部署與更新管理", "sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署"],
        ),
        mc(
            "s1d14_monitoring_threshold",
            "L21302",
            "中",
            [
                "若系統要在部署後主動發現模型品質異常，哪一種做法最完整？",
                "團隊不想等客訴才知道模型失準。若要先補齊一套較完整的監控思路，最合理的答案為何？",
            ],
            "同時監控資料分布、服務指標與業務 KPI，並設定告警門檻",
            ["只監控 GPU 溫度即可", "只觀察單次 demo 表現，不設線上門檻", "只在月報時人工回顧，不做即時告警"],
            "線上模型品質異常可能來自資料、服務或業務結果，監控要多維且有告警門檻。",
            ["GPU 溫度只反映硬體狀態，不等於模型品質。", "demo 無法代表真實線上變化。", "月報回顧太慢，不利於快速處置。"],
            ["把 service monitoring、data monitoring、business KPI 三層一起記。", "沒有 threshold 的監控通常不算可操作。"],
            ["sources/official-corpus.md｜L21302 系統部署與效能監控", "sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署"],
        ),
        mc(
            "s1d14_fail_safe",
            "L21302",
            "中",
            [
                "若生成式 AI 服務短暫失效，但業務流程不能中斷，最合理的架構規劃是什麼？",
                "客服摘要服務偶爾會 timeout，但客服工作不能停止。若要先從系統設計面降低衝擊，較好的方案為何？",
            ],
            "設計 fail-safe 或 fallback 流程，必要時切回規則或人工模式",
            ["服務失效時直接中斷整個業務流程", "把所有請求不加判斷地重試到無限次", "刪掉人工流程，避免回退複雜"],
            "高可用系統要能在模型不可用時降級運行，而不是把整個流程綁死在單一模型上。",
            ["直接中斷流程會放大營運損失。", "無限重試可能造成雪崩與資源耗盡。", "拿掉人工流程會失去最後保險。"],
            ["部署與可靠度題常考 fallback、degradation、manual override。", "模型不是唯一真理來源，流程設計要留後路。"],
            ["sources/official-corpus.md｜系統穩定性與可用性", "sources/scope-weight-map.md｜L21302 AI 技術系統集成與部署"],
        ),
    ],
}
S2_BASE: dict[int, list[dict]] = {
    1: [
        mc(
            "s2d1_year_float",
            "L22201",
            "中",
            [
                "讀入 CSV 後發現 `Year` 欄位是 `float64` 而不是整數，下列哪個原因最合理？",
                "資料分析師發現年份欄位變成 `float64`，若原始欄位理應是年份，最先應懷疑哪種狀況？",
            ],
            "欄位中含有 NaN 或帶小數格式的值",
            ["Pandas 會把所有數值欄位強制讀成 float64", "只要欄位名稱叫 Year 就一定會轉成字串", "資料只要超過 100 筆就會自動升成浮點數"],
            "含 NaN 的整數欄位在傳統 `numpy` 型態下常被升成浮點數，或原始資料本來就含 `2006.0` 類值。",
            ["Pandas 會依內容推斷型態，不會把所有數值欄位都強制轉成 float64。", "欄位名稱不會決定資料型態。", "筆數多寡與是否升成浮點數無直接關係。"],
            ["理解 dtype 由內容而非欄位名稱決定。", "看到 `float64` 年份欄位時，先檢查 NaN 與原始值格式。"],
            ["sources/official-corpus.md｜正式題公開題目出現 Year float64 情境", "sources/scope-weight-map.md｜L22201 數據收集與清理"],
        ),
        mc(
            "s2d1_nullable_int",
            "L22201",
            "中",
            [
                "若年份欄位包含 NaN，但你仍想保留整數語意，最合適的轉型方式為何？",
                "資料中 `Year` 有缺值，你又不想把缺值硬補成 0 或 1。若還要維持整數欄位，最合理的 pandas 型態為何？",
            ],
            "使用 pandas 的 `Int64` nullable integer 型態",
            ["直接 `astype(int)`", "先全部轉成 `str`", "把所有 NaN 都改成 1900 再轉 `int`"],
            "`Int64` 可在保留缺值的同時維持整數語意，是 pandas 常見解法。",
            ["`astype(int)` 遇到 NaN 會失敗。", "轉字串會失去數值操作便利性。", "用 1900 等假值硬補會污染分析結果。"],
            ["區分 Python / numpy 的整數型態與 pandas nullable integer。", "看到『保留 NaN 又想是整數』就先想 `Int64`。"],
            ["sources/official-corpus.md｜正式題公開題目出現 `astype('Int64')`", "sources/scope-weight-map.md｜L22201 數據收集與清理"],
        ),
        mc(
            "s2d1_isna",
            "L22201",
            "易",
            [
                "在 pandas 中，要統計每個欄位 NaN 個數，最標準的寫法是哪一類？",
                "若你想快速檢查資料各欄位缺失值數量，哪個 pandas 方法組合最可靠？",
            ],
            "使用 `isna().sum()` 或 `isnull().sum()`",
            ["使用 `isNaN().sum()`", "使用 `isnan().sum()` 在 DataFrame 直接呼叫", "使用 `missing().count()`"],
            "在 pandas 裡，`isna()` 與 `isnull()` 是等價的常用缺值檢查方法。",
            ["`isNaN()` 不是 pandas DataFrame 的標準方法名稱。", "`isnan()` 不是 DataFrame 物件的通用方法。", "`missing()` 不是 pandas 的標準 API。"],
            ["記住 pandas 缺值檢查常用 API：`isna` / `isnull`。", "不要把 numpy 或其他語言的命名直接套進 pandas。"],
            ["sources/official-corpus.md｜正式題公開題目出現 `isna()` / `isnull()`", "sources/scope-weight-map.md｜L22201 數據收集與清理"],
        ),
        mc(
            "s2d1_descriptive_stats",
            "L22101",
            "中",
            [
                "若資料分布可能有極端值，描述中心趨勢時哪個統計量通常比平均數更穩健？",
                "銷售資料右偏且有少數超高值，若主管只想知道『典型值』，你較優先報告哪個統計量？",
            ],
            "中位數（median）",
            ["平均數（mean）一定更穩健", "標準差（standard deviation）", "樣本數（count）"],
            "中位數較不受極端值影響，對偏態資料通常比平均數穩健。",
            ["平均數容易被極端值拉動。", "標準差描述離散程度，不是中心趨勢。", "樣本數只描述資料量，不描述典型位置。"],
            ["中心趨勢與離散程度要分清。", "偏態與極端值情境優先想 median。"],
            ["sources/official-corpus.md｜L22101 敘述性統計與資料摘要技術", "sources/scope-weight-map.md｜L22101 敘述性統計與資料摘要技術"],
        ),
        mc(
            "s2d1_dtype_cleanup",
            "L22201",
            "中",
            [
                "下列哪一項最符合資料型態清理（dtype cleanup）的主要目的？",
                "若分析流程常在合併、排序、計算時出錯，而原因是欄位型態混亂，最核心的修正方向為何？",
            ],
            "讓後續計算、過濾與視覺化建立在正確資料語意上",
            ["只為了讓檔案看起來整齊", "只是為了讓資料列數變少", "只是為了讓圖表顏色更好看"],
            "dtype 正確與否會直接影響排序、比較、聚合與繪圖結果。",
            ["型態清理不只是版面問題。", "型態修正不一定會改變列數。", "圖表顏色屬視覺設計，非 dtype cleanup 核心。"],
            ["把 dtype cleanup 視為分析正確性的前置條件。", "數值、類別、日期、文字欄位要各自用對型態。"],
            ["sources/official-corpus.md｜L22201 數據收集與清理", "sources/scope-weight-map.md｜L22201 數據收集與清理"],
        ),
    ],
    2: [
        mc(
            "s2d2_zscore",
            "L22101",
            "易",
            [
                "一組成績平均數為 70、標準差為 10。若某學生得 90 分，其 Z-score 約為多少？",
                "若觀測值高於平均數 20 分，而標準差是 10，該筆資料的標準化分數最接近何者？",
            ],
            "2",
            ["0", "1", "3"],
            "Z-score = (90 - 70) / 10 = 2，用來衡量該值離平均數幾個標準差。",
            ["0 代表剛好等於平均數。", "1 只離平均數 1 個標準差。", "3 代表離平均數 30 分。"],
            ["熟記 Z-score 公式與意義。", "標準化分數常用來比較不同量尺資料的位置。"],
            ["sources/official-corpus.md｜114.09 樣題出現 Z-score", "sources/scope-weight-map.md｜L22101 敘述性統計與資料摘要技術"],
        ),
        mc(
            "s2d2_iqr",
            "L22101",
            "中",
            [
                "使用 IQR 方法做異常值偵測時，哪一個區間外的值會被視為異常？",
                "若 Q1 與 Q3 已知，想用箱型圖慣用規則找 outlier，判斷門檻通常是哪一組？",
            ],
            "低於 `Q1 - 1.5×IQR` 或高於 `Q3 + 1.5×IQR`",
            ["低於 `Q2 - 2×IQR` 或高於 `Q2 + 2×IQR`", "低於 `Q1 - 1×IQR` 或高於 `Q3 + 1×IQR`", "只要超過平均數就算異常"],
            "IQR 法的標準 outlier 規則是以四分位數與 1.5 倍 IQR 建界。",
            ["Q2 不是 IQR 法的常用邊界中心。", "1×IQR 不是標準箱型圖常見異常值門檻。", "超過平均數不代表異常。"],
            ["箱型圖、IQR、四分位數的關係要熟。", "異常值規則常考 1.5×IQR，而不是 2×IQR。"],
            ["sources/official-corpus.md｜114.09 樣題出現 IQR", "sources/scope-weight-map.md｜L22101 敘述性統計與資料摘要技術"],
        ),
        mc(
            "s2d2_standardize_vs_normalize",
            "L22203",
            "中",
            [
                "若模型對特徵尺度敏感，且希望各欄位轉成平均數 0、標準差 1，應選哪種處理方式？",
                "年齡與收入量級差異很大，若你想讓它們落在共同的標準差尺度而非 0–1 區間，應採哪一種方法？",
            ],
            "標準化（Standardization / Z-score scaling）",
            ["最小最大正規化（Min-Max Normalization）", "刪除所有數值欄位", "只把欄位改英文名稱"],
            "標準化會把特徵轉成平均數 0、標準差 1，常用於尺度敏感模型。",
            ["Min-Max 是壓到指定區間，不是平均數 0、標準差 1。", "刪除數值欄位會損失主要訊息。", "改欄位名不影響尺度。"],
            ["分清 standardization 與 normalization。", "題目若明講平均數 0、標準差 1，就選 standardization。"],
            ["sources/official-corpus.md｜正式題與樣題多次出現尺度處理", "sources/scope-weight-map.md｜L22203 數據處理技術與工具"],
        ),
        mc(
            "s2d2_normal_distribution",
            "L22102",
            "中",
            [
                "下列哪個敘述最符合常態分布的基本特徵？",
                "若題目說資料『近似鐘形、左右對稱，平均數約等於中位數』，最可能在描述哪種分布？",
            ],
            "常態分布以平均數為中心，左右大致對稱",
            ["常態分布只會出現在類別資料", "常態分布一定沒有任何離群值", "常態分布的平均數一定小於中位數"],
            "常態分布常見特徵是對稱鐘形，平均數、中位數、眾數相近。",
            ["類別資料不適用常態分布。", "即使母體近似常態，樣本仍可能出現離群值。", "平均數不會系統性小於中位數。"],
            ["常態分布的外型與位置關係要記熟。", "別把分布形狀與樣本偶發值混在一起。"],
            ["sources/official-corpus.md｜L22102 機率分佈與資料分佈模型", "sources/scope-weight-map.md｜L22102 機率分佈與資料分佈模型"],
        ),
        mc(
            "s2d2_outlier_choice",
            "L22101",
            "中",
            [
                "若資料右偏且有少量極端高值，下列哪種 summary 最能先幫助你判斷是否有離群點？",
                "主管丟給你一欄銷售資料，懷疑有少數超高訂單拉高整體平均。若先看一組指標，哪組最能幫助判讀？",
            ],
            "中位數與四分位數（含 IQR）",
            ["只有平均數", "只有樣本筆數", "只有欄位名稱與單位"],
            "中位數與四分位數較穩健，也能直接支援 IQR 异常值判讀。",
            ["只有平均數容易被極端值誤導。", "筆數不會告訴你分布位置或離群狀況。", "欄位名稱與單位不提供統計分布資訊。"],
            ["偏態資料先看 median 與 quartiles。", "IQR 是 outlier 與 robust summary 的橋樑。"],
            ["sources/official-corpus.md｜L22101 敘述性統計與資料摘要技術", "sources/scope-weight-map.md｜L22101 敘述性統計與資料摘要技術"],
        ),
    ],
    3: [
        mc(
            "s2d3_ttest",
            "L22103",
            "中",
            [
                "要檢定兩個獨立群體的平均數是否有差異，最常見的統計方法是哪一種？",
                "若你想比較一年級與二年級平均身高是否不同，且資料近似常態，最先該選哪種檢定？",
            ],
            "雙樣本 t 檢定（two-sample t-test）",
            ["卡方檢定（Chi-square test）", "變異數分析（ANOVA）", "主成分分析（PCA）"],
            "兩組平均數比較且資料近似常態時，雙樣本 t 檢定是標準起點。",
            ["卡方檢定主要處理類別資料或次數分配。", "ANOVA 常用於三組以上平均數比較。", "PCA 是降維方法，不是顯著性檢定。"],
            ["先判斷要比『平均數』還是『比例 / 類別』。", "兩組平均數差異優先想 t-test。"],
            ["sources/official-corpus.md｜樣題出現一年級與二年級平均數比較", "sources/scope-weight-map.md｜L22103 假設檢定與統計推論"],
        ),
        mc(
            "s2d3_anova",
            "L22103",
            "中",
            [
                "若要同時比較三個以上群體的平均數是否存在差異，最適合的檢定是什麼？",
                "若題目改成比較一年級、二年級、三年級平均身高是否不同，哪個統計方法最合理？",
            ],
            "ANOVA（變異數分析）",
            ["雙樣本 t 檢定", "ROC 曲線", "IQR 異常值法"],
            "ANOVA 用於三組以上平均數差異檢定，避免多次兩兩比較造成問題。",
            ["t-test 主要是兩組平均數比較。", "ROC 是分類模型評估工具。", "IQR 用於描述分布與找離群值，不做平均數差異推論。"],
            ["題目出現三組以上平均數比較時，優先選 ANOVA。", "平均數比較與模型評估不要混。"],
            ["sources/official-corpus.md｜樣題出現三組平均數差異", "sources/scope-weight-map.md｜L22103 假設檢定與統計推論"],
        ),
        mc(
            "s2d3_chisquare",
            "L22103",
            "中",
            [
                "若要檢定兩個類別變數之間是否獨立，最常見的方法是哪一種？",
                "研究者想知道『是否購買會員』與『地區類別』是否相關，最先該選哪個檢定？",
            ],
            "卡方檢定（Chi-square test）",
            ["線性迴歸", "雙樣本 t 檢定", "K-means 分群"],
            "卡方檢定適用於類別資料的列聯表與獨立性分析。",
            ["線性迴歸處理的是連續數值關係。", "t 檢定處理的是平均數差異。", "K-means 是分群，不做顯著性檢定。"],
            ["類別對類別的關係先想卡方。", "列聯表、獨立性、比例分布常一起出現。"],
            ["sources/official-corpus.md｜L22103 假設檢定與統計推論", "sources/scope-weight-map.md｜L22103 假設檢定與統計推論"],
        ),
        mc(
            "s2d3_prop_test",
            "L22103",
            "難",
            [
                "若要比較兩條生產線良率 95% 與 97% 的差異是否有統計意義，最合理的方法是什麼？",
                "工程師各抽樣 100 件產品，比較新舊產線的良率差異是否顯著。這裡最接近哪種檢定？",
            ],
            "雙比例 Z 檢定（two-proportion Z-test）",
            ["雙樣本平均數 t 檢定", "ANOVA", "PCA"],
            "當目標是比較兩個比例或成功率時，雙比例 Z 檢定最對題。",
            ["t 檢定比較的是平均數，不是比例。", "ANOVA 也不是比例檢定。", "PCA 屬於降維方法。"],
            ["先看目標是平均數還是比例。", "良率、轉換率、點擊率差異常對應 two-proportion test。"],
            ["sources/official-corpus.md｜正式題公開題目出現產線良率比較", "sources/scope-weight-map.md｜L22103 假設檢定與統計推論"],
        ),
        mc(
            "s2d3_hypothesis_logic",
            "L22103",
            "中",
            [
                "假設檢定中的 p-value 最接近哪一種解讀？",
                "若在虛無假設成立前提下觀察到目前資料或更極端結果的機率很低，通常代表什麼？",
            ],
            "當 p-value 很小時，表示資料對虛無假設不利",
            ["p-value 就是虛無假設為真的機率", "p-value 很小代表模型一定正確", "p-value 與顯著水準無任何關係"],
            "p-value 是在虛無假設為真前提下，得到目前或更極端結果的機率，用來判斷是否拒絕虛無假設。",
            ["p-value 不是 H0 為真的機率。", "顯著不代表模型或因果敘事一定正確。", "p-value 會拿來和顯著水準 alpha 比較。"],
            ["p-value 的定義與常見誤解要能區分。", "拒絕 H0 不等於證明所有其他敘事都成立。"],
            ["sources/official-corpus.md｜L22103 假設檢定與統計推論", "sources/scope-weight-map.md｜L22103 假設檢定與統計推論"],
        ),
    ],
    4: [
        mc(
            "s2d4_roc",
            "L22301",
            "中",
            [
                "ROC 曲線主要描繪哪兩個量之間的關係？",
                "若你要解釋 AUC-ROC 的基礎圖形，最核心的兩個座標軸是什麼？",
            ],
            "真陽性率（TPR）與假陽性率（FPR）",
            ["精確率（Precision）與召回率（Recall）", "平均數與標準差", "截距與斜率"],
            "ROC 的橫軸通常是假陽性率，縱軸是真陽性率，用來評估分類器在不同閾值下的表現。",
            ["Precision-Recall 是另一種曲線，不是 ROC 的定義。", "平均數與標準差屬描述統計。", "截距與斜率是迴歸概念。"],
            ["ROC 與 PR curve 不要混。", "AUC-ROC 常配二元分類一起出現。"],
            ["sources/official-corpus.md｜114.09 樣題出現 ROC", "sources/scope-weight-map.md｜L22301 統計學在大數據中的應用"],
        ),
        mc(
            "s2d4_pca",
            "L22302",
            "中",
            [
                "主成分分析（PCA）最主要的用途為何？",
                "若高維資料太多欄位，你想在盡量保留變異資訊下壓縮維度，最合理的方法為何？",
            ],
            "降維並保留主要變異資訊",
            ["做監督式分類", "直接做時間序列預測", "生成更多標註資料"],
            "PCA 透過線性組合形成主成分，常用來降低維度與去除共線性。",
            ["PCA 本身不是分類器。", "時間序列預測有其他專門方法。", "PCA 不會憑空生成標註資料。"],
            ["把 PCA 與 regression / classification 分清。", "看到『高維、降維、主成分』就先選 PCA。"],
            ["sources/official-corpus.md｜114.09 樣題出現 PCA", "sources/scope-weight-map.md｜L22302 常見的大數據分析方法"],
        ),
        mc(
            "s2d4_dbscan",
            "L22302",
            "中",
            [
                "若事前沒有定義群體類型，且資料中可能有雜訊點，較適合哪一種分群方法？",
                "音樂平台想根據使用者行為自動分出類型，還希望把離群用戶當作噪聲處理。下列哪種方法較合理？",
            ],
            "DBSCAN",
            ["邏輯迴歸", "線性迴歸", "決策樹分類"],
            "DBSCAN 是密度式分群方法，可處理未知群數與雜訊點。",
            ["邏輯迴歸是監督式分類。", "線性迴歸處理連續值預測。", "決策樹分類需要標籤。"],
            ["沒有標籤又有噪聲時，先想到 DBSCAN。", "把 clustering 與 supervised models 的輸入前提分開。"],
            ["sources/official-corpus.md｜114.09 樣題出現 DBSCAN 情境", "sources/scope-weight-map.md｜L22302 常見的大數據分析方法"],
        ),
        mc(
            "s2d4_kmeans_logic",
            "L22302",
            "中",
            [
                "若一段虛擬程式碼描述『隨機初始化中心點、計算距離、重新更新中心點直到收斂』，最可能是哪種演算法？",
                "若題目描述重複執行『分配樣本到最近中心』與『更新群中心』的流程，最符合哪一種分群方法？",
            ],
            "K-means 分群",
            ["高斯混合模型", "階層式分群", "Apriori 關聯規則"],
            "K-means 的核心流程就是分配到最近中心，再更新中心點並重複迭代。",
            ["高斯混合模型多了機率分布假設。", "階層式分群不是以重算 centroid 為核心。", "Apriori 不屬於分群演算法。"],
            ["K-means 的關鍵字：centroid、最近中心、反覆更新。", "看到『收斂前重算中心點』時要快速聯想到 K-means。"],
            ["sources/official-corpus.md｜正式題公開題目出現 K-means pseudocode", "sources/scope-weight-map.md｜L22302 常見的大數據分析方法"],
        ),
        mc(
            "s2d4_auc_interpret",
            "L22301",
            "中",
            [
                "下列哪個敘述最符合 AUC-ROC 的一般解讀？",
                "若模型的 AUC-ROC 越高，最常代表什麼？",
            ],
            "模型在不同閾值下區分正負類的整體能力較強",
            ["模型的準確率一定等於 100%", "模型只適用於回歸問題", "AUC 一定只能是 1 或 0"],
            "AUC-ROC 衡量的是分類器跨閾值的整體區辨能力，不等於單一閾值下的準確率。",
            ["AUC 高不代表準確率一定滿分。", "ROC 主要用在分類，不是回歸。", "AUC 介於 0 到 1 之間，通常不是只有 0 或 1。"],
            ["AUC 與 accuracy 的意義要分清。", "評估指標題常考『跨閾值整體能力』這句話。"],
            ["sources/official-corpus.md｜ROC/AUC 類型題", "sources/scope-weight-map.md｜L22301 統計學在大數據中的應用"],
        ),
    ],
    5: [
        mc(
            "s2d5_fillna_strategy",
            "L22201",
            "中",
            [
                "若欄位包含缺失值，但不能隨便用 0 或 1 亂補，最合理的清理原則為何？",
                "資料欄位有 NaN，若硬補成 0 會扭曲商業意義。這種情況下，先做哪種判斷最重要？",
            ],
            "依欄位意義與分析目的決定補值或保留缺失",
            ["一律補 0，這樣最方便", "一律刪掉所有含缺值列", "完全忽略缺值直接建模"],
            "缺值處理沒有單一萬用答案，應依欄位意義、缺失機制與後續模型需求決定。",
            ["補 0 可能引入不存在的實際意義。", "全部刪除可能犧牲太多資料。", "忽略缺值常使模型或統計結果失真。"],
            ["缺值處理要結合欄位語意與缺失機制。", "清理策略不應只追求方便。"],
            ["sources/official-corpus.md｜L22201 數據收集與清理", "sources/scope-weight-map.md｜L22201 數據收集與清理"],
        ),
        mc(
            "s2d5_duplicates",
            "L22201",
            "中",
            [
                "資料清理時若懷疑同一筆交易被重複匯入，最應先檢查哪一類問題？",
                "營收報表出現異常放大，且 ETL 日誌顯示同一批資料可能重跑兩次。若先做一項清理檢查，最合理的是什麼？",
            ],
            "檢查重複資料與主鍵/唯一鍵一致性",
            ["直接把所有數值乘以 0.5", "只重畫圖表不看原始資料", "先把所有欄位轉成字串"],
            "若資料重複匯入，先從 duplicates 與唯一鍵檢查著手最直接。",
            ["直接縮小數值是掩蓋問題，不是修正根因。", "只重畫圖無法修復原始資料品質。", "全轉字串不會解決重複匯入。"],
            ["資料品質問題先找根因，不要直接修數字。", "主鍵、時間戳、交易編號常是 dedup 的線索。"],
            ["sources/official-corpus.md｜L22201 數據收集與清理", "sources/scope-weight-map.md｜L22201 數據收集與清理"],
        ),
        mc(
            "s2d5_datetime_cast",
            "L22203",
            "中",
            [
                "若欄位看起來像日期，但目前仍是字串，最合理的前處理方向為何？",
                "你想做按月銷售趨勢分析，但發現日期欄位是純文字。若要先讓時間運算正確，該怎麼做？",
            ],
            "轉成日期時間型態（datetime）",
            ["保留字串即可，之後再說", "全部改成整數索引", "只把欄位名稱改成 date"],
            "日期分析常需排序、萃取月份、重取樣等操作，因此應先轉成 datetime。",
            ["保留字串容易造成排序與切片錯誤。", "整數索引不會自動保留日期語意。", "改欄位名稱不改內容型態。"],
            ["日期欄位若要做趨勢分析，先處理 datetime。", "型態正確才能做 resample / month extraction。"],
            ["sources/official-corpus.md｜L22203 數據處理技術與工具", "sources/scope-weight-map.md｜L22203 數據處理技術與工具"],
        ),
        mc(
            "s2d5_type_safe_missing",
            "L22201",
            "中",
            [
                "若欄位同時有數字、空值與少量格式錯誤字串，資料清理的較佳順序通常為何？",
                "數值欄位中混入 `N/A`、空字串與少量錯字。若你想降低後續轉型錯誤，較好的流程是什麼？",
            ],
            "先標準化缺失表達，再做型態轉換與例外檢查",
            ["先強制 `astype(int)` 再看哪裡報錯", "先畫圖，不處理清理", "先把所有欄位都當作類別型資料"],
            "先把 `N/A`、空字串等統一為缺失值，再轉型會更穩定。",
            ["直接強轉容易在最前面就失敗。", "圖表無法取代資料清理。", "全部當類別會失去數值分析能力。"],
            ["清理順序通常是標準化缺失表示，再做 cast。", "型態轉換前先處理 dirty tokens。"],
            ["sources/official-corpus.md｜L22201 數據收集與清理", "sources/scope-weight-map.md｜L22201 數據收集與清理"],
        ),
        mc(
            "s2d5_label_vs_onehot",
            "L22203",
            "中",
            [
                "對無序類別欄位做機器學習前，若不想引入假性的大小關係，常見的編碼方式為何？",
                "欄位 `Color` 只有 `Red/Blue/Green` 三種值，且三者沒有自然大小順序。若要避免模型誤以為有大小關係，較合理的處理方式是什麼？",
            ],
            "One-hot encoding",
            ["直接 label encoding 並假設數字大小有意義", "把欄位刪掉", "把所有值合併成同一類"],
            "無序類別若直接編成 1、2、3，部分模型會誤讀出大小關係；one-hot 較安全。",
            ["label encoding 可能讓模型誤讀排序。", "直接刪欄位會損失可能有用的訊息。", "全部合併成同類會消除區辨資訊。"],
            ["類別是否有序，決定編碼策略。", "one-hot 與 label encoding 的適用場景要分清。"],
            ["sources/official-corpus.md｜L22203 數據處理技術與工具", "sources/scope-weight-map.md｜L22203 數據處理技術與工具"],
        ),
    ],
    13: [
        mc(
            "s2d13_graph_edge_property",
            "L22202",
            "中",
            [
                "在圖形資料庫中，若『按讚』行為本身還帶有時間戳與裝置類型等資訊，較合適的建模方式是什麼？",
                "社群資料中，使用者與貼文之間的 like 互動還要保留時間與裝置欄位。若用圖資料庫，最合理的設計方向為何？",
            ],
            "把按讚視為帶屬性的邊（edge/property）來連結節點",
            ["把所有按讚都寫回使用者節點文字欄位", "完全不用圖模型，改成隨意 Excel 記錄", "把裝置類型改成人工備註而不建模關聯"],
            "圖資料庫很適合用邊來表示互動關係，邊上再保留時間與裝置等屬性。",
            ["寫回單一節點會破壞關聯查詢能力。", "Excel 不是圖查詢與關聯推理的設計。", "不建模關係就失去圖資料庫價值。"],
            ["圖資料庫的核心是節點、邊與屬性。", "互動事件若天然是關係，先考慮 edge property。"],
            ["sources/official-corpus.md｜正式題公開題目出現 graph database edge property", "sources/scope-weight-map.md｜L22202 數據儲存與管理"],
        ),
        mc(
            "s2d13_rdf",
            "L22202",
            "中",
            [
                "若希望知識圖譜支援語意查詢與關聯推理，哪種資料模型最常見？",
                "企業想把研究報告、專利與專家知識整合成可推理的知識圖譜。若從資料模型來看，哪個方向最對題？",
            ],
            "RDF 三元組（subject-predicate-object）",
            ["只把所有內容塞進單一文字欄位", "只存成普通 CSV 而不保留關係語意", "只畫心智圖不建立機器可讀模型"],
            "RDF 三元組是知識圖譜的常見基礎模型，適合做語意關係與推理。",
            ["單一文字欄位無法表達可機器推理的關係。", "普通 CSV 缺乏語意連結結構。", "心智圖若不可機器讀取，無法直接支援推理。"],
            ["RDF、triple、ontology 是知識圖譜高頻詞。", "知識圖譜題常考『語意查詢與推理』。"],
            ["sources/official-corpus.md｜正式題公開題目出現 RDF", "sources/scope-weight-map.md｜L22202 數據儲存與管理"],
        ),
        mc(
            "s2d13_graph_vs_relational",
            "L22202",
            "中",
            [
                "若資料重點在多跳關聯查詢與關係探索，哪種資料庫模型通常更有優勢？",
                "若分析任務常問『A 透過哪些人間接連到 B』這類多層關係問題，較合適的儲存模型為何？",
            ],
            "圖資料庫（Graph Database）",
            ["只用純檔案系統", "只用樞紐分析表", "只用隨機文字摘要"],
            "圖資料庫對多跳關係查詢與圖演算法通常較自然。",
            ["檔案系統不負責關係查詢。", "樞紐分析表偏彙整展示，不是關係遍歷工具。", "文字摘要不是結構化關聯模型。"],
            ["多跳關係題先想 graph model。", "資料模型選擇要看查詢型態，而不只看資料量。"],
            ["sources/official-corpus.md｜L22202 數據儲存與管理", "sources/scope-weight-map.md｜L22202 數據儲存與管理"],
        ),
        mc(
            "s2d13_knowledge_graph_use",
            "L22402",
            "中",
            [
                "下列哪種 AI 應用情境最能受益於知識圖譜的語意關聯能力？",
                "若企業想整合產品、專利、客訴與技術文件，並支援語意查詢與關係推理，最適合優先考慮哪個方向？",
            ],
            "建立知識圖譜支援語意檢索與關聯推理",
            ["只做簡單平均數報表", "只把資料壓縮成 zip 檔", "只靠單一關鍵字字典做固定匹配"],
            "知識圖譜特別適合異質知識整合、關聯查詢與推理。",
            ["平均數報表不需要圖推理。", "壓縮檔只是儲存形式。", "固定字典匹配缺少關聯推理能力。"],
            ["把知識圖譜當成『關係結構化 + 可推理』的工具。", "異質知識整合題通常不是單純 BI 報表題。"],
            ["sources/official-corpus.md｜L22402 大數據在鑑別式 AI 中的應用", "sources/scope-weight-map.md｜L22402 大數據在鑑別式 AI 中的應用"],
        ),
        mc(
            "s2d13_centrality",
            "L22302",
            "中",
            [
                "若要找出社群網路中最有影響力或最居中的節點，哪一類分析概念最直接？",
                "若企業想找出知識網絡中的關鍵專家節點，最合理先看的圖分析方向為何？",
            ],
            "中心性（centrality）分析",
            ["只看所有節點名稱長度", "只做字串排序", "只比較檔案大小"],
            "中心性分析用來衡量節點在網路中的重要性或位置。",
            ["名稱長度與網路影響力無關。", "字串排序不反映關係結構。", "檔案大小也與節點位置無關。"],
            ["圖分析常考中心性、社群偵測、最短路徑。", "看到『關鍵節點』就先想 centrality。"],
            ["sources/official-corpus.md｜L22302 常見的大數據分析方法", "sources/scope-weight-map.md｜L22302 常見的大數據分析方法"],
        ),
        mc(
            "s2d13_graph_query",
            "L22202",
            "中",
            [
                "若任務重點是查詢複雜關係鏈與語意路徑，下列哪項能力最重要？",
                "知識圖譜若要回答『某專家透過哪些專利與主題間接關聯到某產品問題』，資料平台最需要具備哪類能力？",
            ],
            "支援關係路徑查詢與圖遍歷",
            ["只支援單欄位排序", "只支援把圖片縮圖", "只支援文字上色"],
            "圖模型的價值之一就是能高效處理路徑與關聯遍歷查詢。",
            ["單欄位排序不是路徑查詢。", "圖片縮圖與圖資料無關。", "文字上色不是查詢能力。"],
            ["圖資料庫的亮點是 traversal。", "看到『經由哪些關係連過去』時要聯想到 path query。"],
            ["sources/official-corpus.md｜L22202 數據儲存與管理", "sources/scope-weight-map.md｜L22202 數據儲存與管理"],
        ),
    ],
    14: [
        mc(
            "s2d14_arima_residual",
            "L22302",
            "難",
            [
                "ARIMA 模型建立後，若殘差 ACF 在多個 lag 上仍顯著不為 0，最合理的診斷是什麼？",
                "若時間序列模型的誤差仍呈現週期性、自相關顯著，表示模型最可能有什麼問題？",
            ],
            "模型仍未充分捕捉時間依賴，存在配適不足",
            ["代表殘差一定是白噪音", "代表模型完全不需要再調整", "代表只能改成分類模型"],
            "若殘差仍有結構，表示資訊還留在誤差中，模型尚未充分擬合。",
            ["白噪音應接近無系統自相關。", "有殘差結構時通常需要再調整模型。", "時間序列配適不足不會直接推出改做分類。"],
            ["時間序列診斷常看殘差是否近白噪音。", "ACF 顯著不為 0 常暗示 underfitting 或規格不完整。"],
            ["sources/official-corpus.md｜正式題公開題目出現 ARIMA 殘差診斷", "sources/scope-weight-map.md｜L22302 常見的大數據分析方法"],
        ),
        mc(
            "s2d14_poisson",
            "L22102",
            "中",
            [
                "卜瓦松分布（Poisson distribution）較適合描述哪一類事件？",
                "若題目說『每小時瑕疵品個數、平均發生率固定、事件彼此獨立』，最可能對應哪一種分布？",
            ],
            "固定時間或空間內稀有事件的發生次數",
            ["連續型測量值的精準高度", "只有類別標籤的比例值", "影像像素顏色的 RGB 三通道值"],
            "Poisson 常用於描述在固定區間內獨立事件的計數資料。",
            ["連續型高度常不直接以 Poisson 描述。", "比例值與 Poisson 的計數本質不同。", "RGB 三通道不是事件次數模型。"],
            ["Poisson 關鍵字：count、independent events、fixed rate。", "看到『每小時幾次』常先想 Poisson。"],
            ["sources/official-corpus.md｜正式題公開題目出現 Poisson", "sources/scope-weight-map.md｜L22102 機率分佈與資料分佈模型"],
        ),
        mc(
            "s2d14_differencing",
            "L22302",
            "中",
            [
                "若時間序列存在趨勢而不平穩，常見的基本處理方式之一是什麼？",
                "你懷疑序列平均數隨時間漂移，不符合平穩假設。若先做一個基本轉換，較合理的是什麼？",
            ],
            "做差分（differencing）",
            ["把所有值都取絕對值", "只把欄位名稱改成 t", "直接 one-hot encoding 時間索引"],
            "差分常用來移除趨勢，幫助序列更接近平穩。",
            ["取絕對值不會系統性處理趨勢。", "改欄位名不影響資料性質。", "one-hot 時間索引與平穩化是不同問題。"],
            ["非平穩序列與差分處理要成對記。", "ARIMA 的 I 就是 integrated / differencing。"],
            ["sources/official-corpus.md｜L22302 常見的大數據分析方法", "sources/scope-weight-map.md｜L22302 常見的大數據分析方法"],
        ),
        mc(
            "s2d14_white_noise",
            "L22302",
            "中",
            [
                "在時間序列模型診斷中，『殘差接近白噪音』通常代表什麼？",
                "若模型殘差不再顯示明顯自相關結構，最常見的正向解讀為何？",
            ],
            "模型已捕捉大部分可解釋的時間結構",
            ["模型一定 100% 正確", "資料集完全沒有外部干擾", "未來預測值保證不會出錯"],
            "殘差近白噪音表示剩餘誤差較接近隨機波動，是模型診斷的好訊號之一。",
            ["白噪音不等於模型完美無誤。", "外部干擾仍可能存在。", "任何預測都不可能保證零錯誤。"],
            ["白噪音是『較理想』，不是『完美』。", "診斷題要避免過度解讀。"],
            ["sources/official-corpus.md｜時間序列殘差診斷", "sources/scope-weight-map.md｜L22302 常見的大數據分析方法"],
        ),
        mc(
            "s2d14_seasonality",
            "L22302",
            "中",
            [
                "若每週或每月都出現固定重複波動，下列哪個概念最貼近這種現象？",
                "銷售資料在每個月初都會固定飆升，這種可重複的週期結構最常稱為什麼？",
            ],
            "季節性（seasonality）",
            ["缺失值（missingness）", "共線性（multicollinearity）", "正規化（normalization）"],
            "規律重複的週期波動通常稱為季節性，是時間序列的重要結構之一。",
            ["缺失值是資料缺漏。", "共線性是多變數之間的線性關聯問題。", "正規化是前處理方法。"],
            ["時間序列的趨勢、季節性、殘差要拆開記。", "固定週期波動不是隨機噪聲。"],
            ["sources/official-corpus.md｜時間序列分析主題", "sources/scope-weight-map.md｜L22302 常見的大數據分析方法"],
        ),
        mc(
            "s2d14_lag",
            "L22302",
            "中",
            [
                "在 ACF 圖中提到的 lag，最接近哪個意思？",
                "若說某序列在 lag 3 上仍有明顯自相關，這裡的 lag 3 通常指什麼？",
            ],
            "目前值與往前 3 個時間步之間的延遲關係",
            ["第三個特徵欄位的名稱", "第三個模型版本", "第三種資料型態"],
            "lag 描述的是時間序列向後回看的延遲步數。",
            ["lag 與特徵欄位編號無關。", "模型版本不是時間延遲。", "資料型態也與 lag 無關。"],
            ["時間序列的 lag 是延遲，不是欄位序號。", "ACF/PACF 題常用 lag 當關鍵詞。"],
            ["sources/official-corpus.md｜時間序列分析主題", "sources/scope-weight-map.md｜L22302 常見的大數據分析方法"],
        ),
    ],
}

S2_BASE.update({
    6: [
        mc(
            "s2d6_groupby_sum",
            "L22303",
            "中",
            [
                "若想統計每個平台的全球銷售總額並畫長條圖，下列哪種 pandas 思路最正確？",
                "分析師要比較各遊戲平台的總銷售量，而不是遊戲筆數。若先寫一行資料聚合，最合理的方向是什麼？",
            ],
            "以 `groupby(平台)[銷售額].sum()` 聚合後再畫 bar chart",
            ["直接 `value_counts()` 平台名稱就好", "只算平均數而非總和", "直接用 `countplot` 畫原始列數"],
            "題目要的是銷售總額，因此要先按平台分組，再對銷售額做加總。",
            ["`value_counts()` 只會算筆數，不是總銷售額。", "平均數回答的是平均單筆，不是總額。", "countplot 也是筆數導向，不是金額聚合。"],
            ["看到『總額』先找 sum，不要被 count 誤導。", "資料聚合與視覺化要先釐清度量是 count、sum 還是 mean。"],
            ["sources/official-corpus.md｜正式題公開題目出現 `groupby().sum()`", "sources/scope-weight-map.md｜L22303 數據可視化工具"],
        ),
        mc(
            "s2d6_melt_barplot",
            "L22303",
            "難",
            [
                "若要比較多個地區銷售欄位的總額比例，並用 seaborn 長條圖顯示，較合理的資料整理方式為何？",
                "資料表中 `NA_Sales/EU_Sales/JP_Sales/Other_Sales` 分散在不同欄位。若要先轉成適合 seaborn `barplot` 的長表格式，哪種作法最合理？",
            ],
            "先用 `pd.melt()` 轉長表，再以 `barplot(..., estimator=sum)` 繪圖",
            ["直接 `countplot` 原始欄位名稱", "直接 `lineplot` 把四個欄位名稱當 y", "只畫 `histplot` 就能比較總額比例"],
            "多欄位數值若要用 seaborn 一致地比較總額，常先轉長表再指定聚合函數。",
            ["countplot 主要算類別出現次數，不適合直接比較總銷售額。", "lineplot 不適合這種欄位到欄位的聚合比較。", "histplot 用來看分布，不是總額比較的首選。"],
            ["寬表轉長表是資料視覺化常考轉換。", "melt 與 estimator=sum 要一起記。"],
            ["sources/official-corpus.md｜正式題公開題目出現 `pd.melt` + seaborn", "sources/scope-weight-map.md｜L22303 數據可視化工具"],
        ),
        mc(
            "s2d6_nlargest",
            "L22303",
            "中",
            [
                "若想找出北美銷售最好的前五名遊戲並畫條狀圖，較合理的資料選取方法為何？",
                "你要用 `seaborn.barplot` 畫出 `NA_Sales` 最高的 5 款遊戲，最先應怎麼挑資料？",
            ],
            "先用 `nlargest(5, 'NA_Sales')` 取前五筆",
            ["直接 `head(5)` 原始資料", "先 `sort_values()` 由小到大再取前五筆", "直接 `countplot` 遊戲名稱"],
            "題目要的是銷售最高前五名，因此要依目標欄位排序並選最大值。",
            ["`head(5)` 只取前五列，不一定是銷售最高。", "由小到大排序後取前五會得到最小值。", "countplot 不會反映銷售額大小。"],
            ["top-N 題先看排序依據是什麼欄位。", "視覺化前先把資料子集選對。"],
            ["sources/official-corpus.md｜正式題公開題目出現 `nlargest`", "sources/scope-weight-map.md｜L22303 數據可視化工具"],
        ),
        mc(
            "s2d6_valuecounts",
            "L22303",
            "中",
            [
                "若你只想知道每個平台出現幾筆資料，而不是總銷售額，較適合的函式是哪一類？",
                "分析師現在不是要比較金額，而是只想看平台資料筆數分布。這時最貼切的 pandas 方法為何？",
            ],
            "使用 `value_counts()` 或分組後 `count()`",
            ["使用 `sum()` 計算銷售總額", "使用 `mean()` 計算平均售額", "直接做 `LinearRegression`"],
            "當度量是『出現次數』時，`value_counts()` 或 `count()` 比較直接。",
            ["sum 與 mean 都在處理數值聚合，不是筆數。", "迴歸模型不是用來統計類別筆數。", "這題重點是 count，不是 predictive modeling。"],
            ["先分清題目要 count 還是要 measure aggregation。", "筆數分布和銷售總額常是考試常見陷阱。"],
            ["sources/official-corpus.md｜L22303 數據可視化工具", "sources/scope-weight-map.md｜L22303 數據可視化工具"],
        ),
        mc(
            "s2d6_chart_selection",
            "L22303",
            "中",
            [
                "若想比較不同類別之間的總量高低，最直觀的圖表通常是哪一種？",
                "主管想快速比較不同遊戲平台的總銷售量高低，不強調時間連續性。此時最適合優先畫哪種圖？",
            ],
            "長條圖（bar chart）",
            ["折線圖（line chart）", "散佈圖（scatter plot）", "熱力圖（heatmap）"],
            "類別間高低比較最直觀的通常是長條圖。",
            ["折線圖較適合強調時間或有序序列變化。", "散佈圖強調兩數值變數關係。", "熱力圖較適合矩陣關係或密度概覽。"],
            ["先判斷資料型態：類別比較常用 bar。", "時間趨勢才優先考慮 line。"],
            ["sources/official-corpus.md｜L22303 數據可視化工具", "sources/scope-weight-map.md｜L22303 數據可視化工具"],
        ),
    ],
    7: [
        mc(
            "s2d7_fit_xy",
            "L22301",
            "中",
            [
                "在 `LinearRegression().fit()` 中，哪個參數順序才是正確的？",
                "若你要用 `sklearn` 建立線性迴歸模型，X 與 y 的輸入位置應如何安排？",
            ],
            "`fit(X, y)`",
            ["`fit(y, X)`", "`fit(X)` 就足夠", "`fit(y)` 後模型會自己找特徵"],
            "`sklearn` 的監督式模型介面通常是 `fit(features, target)`。",
            ["把 y 放前面會把目標與特徵顛倒。", "監督式迴歸需要特徵與目標。", "只給 y 不會讓模型自動知道特徵。"],
            ["記住 sklearn 介面慣例：X 在前、y 在後。", "程式題常考最基本的 API 使用順序。"],
            ["sources/official-corpus.md｜正式題公開題目出現 `fit(X, y)`", "sources/scope-weight-map.md｜L22301 統計學在大數據中的應用"],
        ),
        mc(
            "s2d7_coef_intercept",
            "L22301",
            "中",
            [
                "在 `sklearn` 線性迴歸中，`coef_` 主要代表什麼？",
                "若你在 `LinearRegression` 訓練後印出 `reg.coef_`，最合理的解讀是什麼？",
            ],
            "各特徵對目標變數的迴歸係數，不包含截距",
            ["包含截距在內的所有係數", "模型的 p-value 清單", "每個欄位的缺失值數量"],
            "`coef_` 反映各特徵的斜率係數；截距通常在 `intercept_`。",
            ["截距通常另存在 `intercept_`。", "p-value 不是 sklearn `LinearRegression` 直接提供的欄位。", "缺失值數量與迴歸係數無關。"],
            ["區分 `coef_` 與 `intercept_`。", "sklearn 與 statsmodels 提供的統計資訊層級不同。"],
            ["sources/official-corpus.md｜正式題公開題目出現 `coef_` 解讀", "sources/scope-weight-map.md｜L22301 統計學在大數據中的應用"],
        ),
        mc(
            "s2d7_pvalue",
            "L22301",
            "中",
            [
                "在統計建模中，若某係數的 p-value 小於 0.05，最常見的解讀是什麼？",
                "若 OLS 報表顯示某變數 p-value < 0.05，在常見顯著水準下最合理的判斷為何？",
            ],
            "在該顯著水準下，該係數對目標的解釋關係具有統計顯著性",
            ["代表這個變數一定具有強因果關係", "代表模型一定是最佳模型", "代表資料完全沒有噪聲"],
            "p-value 小通常只支持『不容易由隨機波動造成』，不等於因果、最佳或零噪聲。",
            ["顯著不等於因果成立。", "單一係數顯著不代表整個模型就是最佳。", "真實資料仍可能有噪聲與偏差。"],
            ["統計顯著與因果解釋要切開。", "顯著性只是一個證據，不是最終商業結論。"],
            ["sources/official-corpus.md｜L22301 統計學在大數據中的應用", "sources/scope-weight-map.md｜L22301 統計學在大數據中的應用"],
        ),
        mc(
            "s2d7_intercept_meaning",
            "L22301",
            "中",
            [
                "線性迴歸中的截距（intercept）通常代表什麼？",
                "若所有特徵都等於 0，模型預測值對應的那個常數項，一般稱為什麼？",
            ],
            "所有特徵為 0 時的預測基準值",
            ["資料筆數", "相關係數", "目標變數的標準差"],
            "截距是模型的常數項，代表當所有解釋變數為 0 時的預測值。",
            ["資料筆數不屬於模型參數。", "相關係數是變數關聯程度，不是迴歸常數項。", "標準差是離散程度，不是模型基準值。"],
            ["`intercept_` 與 `coef_` 的角色要分清。", "截距的業務意義要結合 0 是否有實際含義再解讀。"],
            ["sources/official-corpus.md｜正式題公開題目出現截距項解讀", "sources/scope-weight-map.md｜L22301 統計學在大數據中的應用"],
        ),
        mc(
            "s2d7_boxcox",
            "L22301",
            "難",
            [
                "若線性迴歸的目標變數明顯右偏，且變異隨 X 增大而增加，哪種前處理較合理？",
                "研究者發現 Y 分布右偏且異質變異明顯。若想更符合線性模型假設，較值得優先嘗試哪個轉換？",
            ],
            "對 Y 做 Box-Cox 轉換",
            ["對 X 做標準化就一定能解決", "對資料做一次差分", "直接刪掉所有高值樣本"],
            "Box-Cox 常用於處理正值且右偏的資料，能改善偏態與變異不穩定問題。",
            ["標準化 X 不一定能解決 Y 的偏態與異質變異。", "差分主要常見於時間序列處理。", "直接刪高值可能扭曲資料而非改善模型假設。"],
            ["偏態與異質變異時要想到變數轉換。", "Box-Cox 適合正值目標變數。"],
            ["sources/official-corpus.md｜正式題公開題目出現 Box-Cox", "sources/scope-weight-map.md｜L22301 統計學在大數據中的應用"],
        ),
    ],
    8: [
        mc(
            "s2d8_ols_order",
            "L22301",
            "難",
            [
                "使用 `statsmodels` 建立 OLS 模型時，較正確的呼叫方向為何？",
                "若你要用 `statsmodels.api.OLS` 建立線性模型，下列哪個概念順序最合理？",
            ],
            "`OLS(y, X_with_constant).fit()`",
            ["`OLS(X, y).fit()`", "`OLS(X).fit(y)`", "`OLS(y).fit(X)`"],
            "在 statsmodels 中，第一個位置通常是目標 y，第二個是設計矩陣 X。",
            ["把 X 與 y 顛倒會把資料語意反轉。", "fit 不接受這種拆開方式。", "只給單邊參數不構成完整 OLS 模型。"],
            ["sklearn 與 statsmodels 的介面習慣要分清。", "statsmodels 題常考 y、X 的順序與常數項。"],
            ["sources/official-corpus.md｜正式題公開題目出現 OLS 呼叫方向", "sources/scope-weight-map.md｜L22301 統計學在大數據中的應用"],
        ),
        mc(
            "s2d8_add_constant",
            "L22301",
            "中",
            [
                "在 `statsmodels` 做 OLS 時，若想顯式估計截距項，常需要先做哪個步驟？",
                "為了讓 OLS 報表中含有常數項，對設計矩陣 X 最常見的前處理是什麼？",
            ],
            "使用 `sm.add_constant(X)` 加入常數欄位",
            ["把 X 全部轉成字串", "先做 one-hot 才會有截距", "把 y 乘上一個常數即可"],
            "statsmodels 不一定自動補截距，常見做法是先對 X 加常數欄。",
            ["轉字串與截距無關。", "one-hot 用於類別編碼，不是專門為截距設計。", "改 y 不會自動產生設計矩陣中的常數項。"],
            ["`add_constant` 是 statsmodels 題的高頻 API。", "sklearn 與 statsmodels 對截距的預設行為不同。"],
            ["sources/official-corpus.md｜正式題公開題目出現常數項", "sources/scope-weight-map.md｜L22301 統計學在大數據中的應用"],
        ),
        mc(
            "s2d8_residuals",
            "L22301",
            "中",
            [
                "線性迴歸中的殘差（residual）最接近哪個定義？",
                "如果你想檢查模型是否系統性低估或高估，最直接會看的量是什麼？",
            ],
            "實際值減去預測值的差",
            ["各特徵之間的相關係數", "模型的截距項", "資料列數與欄位數的差"],
            "殘差反映單筆樣本的預測誤差，是模型診斷的重要基礎。",
            ["相關係數衡量變數關聯，不是單筆誤差。", "截距是模型參數，不是單筆預測誤差。", "資料形狀與殘差定義無關。"],
            ["殘差診斷與整體指標（R²、RMSE）要一起看。", "單筆誤差與整體模型品質不是同一層次。"],
            ["sources/official-corpus.md｜L22301 統計學在大數據中的應用", "sources/scope-weight-map.md｜L22301 統計學在大數據中的應用"],
        ),
        mc(
            "s2d8_corr_causation",
            "L22301",
            "中",
            [
                "當兩個變數高度相關時，下列哪個敘述最嚴謹？",
                "若你在回歸分析中看到某特徵與銷售高度正相關，最安全的結論應是什麼？",
            ],
            "相關性不自動代表因果關係",
            ["只要相關高就代表有直接因果", "相關高代表模型一定無偏", "相關高代表不用做驗證與實驗設計"],
            "相關只描述同時變動，是否因果仍需更多設計、控制與領域證據。",
            ["相關高可能來自混雜因素。", "相關高不保證模型無偏。", "驗證與設計仍然必要。"],
            ["考試常拿 correlation vs causation 當判斷陷阱。", "看到『高度相關』不要自動跳到『因果成立』。"],
            ["sources/official-corpus.md｜L22301 統計學在大數據中的應用", "sources/scope-weight-map.md｜L22301 統計學在大數據中的應用"],
        ),
        mc(
            "s2d8_scaler_pipeline",
            "L22203",
            "中",
            [
                "若要避免資料前處理與模型訓練步驟在實驗與部署間不一致，較佳的工程做法是什麼？",
                "團隊擔心訓練時做了標準化，但上線推論忘記套同樣規則。若想降低這類錯誤，較好的作法為何？",
            ],
            "把前處理與模型包進同一條 pipeline",
            ["每次手動重打一遍前處理", "只在簡報中描述前處理步驟", "把標準化留到使用者自行處理"],
            "把 scaler 與 model 放在同一 pipeline 能降低訓練/推論不一致。",
            ["手動重做容易出現人為偏差。", "簡報無法保證系統實作一致。", "把責任丟給使用者會提高線上錯誤率。"],
            ["工程一致性也是資料分析能力的一部分。", "preprocessing drift 不只在數值，也可能在流程。"],
            ["sources/official-corpus.md｜L22203 數據處理技術與工具", "sources/scope-weight-map.md｜L22203 數據處理技術與工具"],
        ),
    ],
    9: [
        mc(
            "s2d9_kfold",
            "L22301",
            "中",
            [
                "若想降低單次切分造成的評估波動，最常見的模型驗證方法是哪一種？",
                "當資料量不算太小，且你想更穩定評估模型泛化能力，哪種驗證方式通常最合適？",
            ],
            "K-fold 交叉驗證",
            ["只看訓練集分數", "完全不切驗證集", "只隨機挑一筆做測試"],
            "K-fold 會反覆切分資料並平均結果，比單次 hold-out 更穩定。",
            ["只看訓練集會過度樂觀。", "沒有驗證集無法評估泛化。", "單筆測試完全不穩定。"],
            ["交叉驗證的重點是反覆切分與平均。", "穩定評估通常優先想到 K-fold。"],
            ["sources/official-corpus.md｜L22301 統計學在大數據中的應用", "sources/scope-weight-map.md｜L22301 統計學在大數據中的應用"],
        ),
        mc(
            "s2d9_bootstrap",
            "L22301",
            "難",
            [
                "若資料有限，且想估計模型表現或統計量的不確定性，哪種方法常被採用？",
                "你想多次重抽樣資料來觀察指標波動範圍，而不是固定切 K 份。這時較合理的方法為何？",
            ],
            "Bootstrap 重抽樣",
            ["只做一次平均數計算", "只調高學習率", "只用 `value_counts()` 看筆數"],
            "Bootstrap 透過有放回重抽樣來估計指標或統計量的變異與不確定性。",
            ["一次平均數無法反映估計不確定性。", "學習率是模型訓練參數，不是重抽樣方法。", "筆數統計無法替代不確定性估計。"],
            ["Bootstrap 的核心是『有放回重抽樣』。", "當題目談不確定性或抽樣變異時，可優先想到 bootstrap。"],
            ["sources/official-corpus.md｜正式題公開題目出現 bootstrap", "sources/scope-weight-map.md｜L22301 統計學在大數據中的應用"],
        ),
        mc(
            "s2d9_holdout_limits",
            "L22301",
            "中",
            [
                "為何單次 hold-out 驗證常被認為不如交叉驗證穩定？",
                "若你只做一次 train/test split，模型評估最主要的風險是什麼？",
            ],
            "結果容易受到特定切分方式影響",
            ["它完全不能用於任何任務", "它會自動避免所有過擬合", "它不需要任何隨機種子或資料分層"],
            "單次切分若剛好抽到偏樣本，評估結果可能高估或低估模型能力。",
            ["hold-out 仍可用，只是穩定性較差。", "單次切分不會自動消除過擬合。", "切分策略與 random state 仍然重要。"],
            ["validation method 的重點在穩定性與偏差。", "單次切分不是錯，而是風險較高。"],
            ["sources/official-corpus.md｜L22301 統計學在大數據中的應用", "sources/scope-weight-map.md｜L22301 統計學在大數據中的應用"],
        ),
        mc(
            "s2d9_train_val_test",
            "L22301",
            "中",
            [
                "在一般訓練流程中，驗證集（validation set）的主要用途為何？",
                "若團隊要調超參數、挑模型版本，但不想偷看最終測試集，這時應主要依賴哪個資料切分？",
            ],
            "用來調整模型與超參數，而非作最終公正測試",
            ["用來取代所有訓練資料", "用來永久當正式上線資料", "用來當唯一的商業 KPI 報表來源"],
            "validation set 主要支援 model selection 與 tuning，final test 則負責較公正的最後評估。",
            ["validation 不是訓練資料的替代品。", "上線資料與驗證集角色不同。", "商業 KPI 報表來源不應只依賴 validation。"],
            ["train/validation/test 三者角色要分清。", "調參看 validation，最終報告看 test。"],
            ["sources/official-corpus.md｜L22301 統計學在大數據中的應用", "sources/scope-weight-map.md｜L22301 統計學在大數據中的應用"],
        ),
        mc(
            "s2d9_stratify",
            "L22301",
            "中",
            [
                "若分類資料類別極不平衡，在切分 train/test 時常見的安全作法是什麼？",
                "資料集中 95% 是正常類、5% 是異常類。若想避免測試集幾乎抽不到異常類，較合理的切分策略為何？",
            ],
            "採用分層切分（stratified split）",
            ["完全不打亂資料直接切", "只依索引奇偶切分", "先刪除少數類再切分"],
            "分層切分可讓各子集維持接近原始類別比例。",
            ["不打亂可能引入順序偏差。", "奇偶切分沒有保證類別比例。", "刪掉少數類會讓問題更嚴重。"],
            ["不平衡分類題除了 SMOTE，也常考 stratified split。", "先保住分布，再談建模。"],
            ["sources/official-corpus.md｜L22301 統計學在大數據中的應用", "sources/scope-weight-map.md｜L22301 統計學在大數據中的應用"],
        ),
    ],
    10: [
        mc(
            "s2d10_smote",
            "L22401",
            "難",
            [
                "在少數類樣本極少、又想提升少數類偵測能力時，下列哪一種策略最合理？",
                "罕見疾病分類中，確診樣本不到 1%，又短期內拿不到更多標註資料。若想先提升少數類學習效果，哪個方法較對題？",
            ],
            "使用 SMOTE 生成合成少數類樣本",
            ["只隨機刪掉大量多數類而不評估代價", "完全不處理不平衡問題", "只提高決策閾值卻不檢查整體泛化"],
            "SMOTE 能在特徵空間中合成少數類樣本，常用於不平衡分類前處理。",
            ["欠採樣有時可行，但粗暴刪資料可能損失太多資訊。", "完全不處理通常會讓模型偏向多數類。", "只調閾值不能替代資料層補強。"],
            ["SMOTE、class weight、threshold tuning 是不平衡分類三個高頻補救方向。", "先看題目要的是資料層、模型層還是決策層補強。"],
            ["sources/official-corpus.md｜正式題公開題目出現 SMOTE", "sources/scope-weight-map.md｜L22401 大數據與機器學習"],
        ),
        mc(
            "s2d10_recall_threshold",
            "L22301",
            "中",
            [
                "若任務重點是盡量抓到少數類，不希望漏判，較應優先關注哪一項指標？",
                "在疾病偵測或詐欺攔截場景中，若漏掉真正異常代價最高，調整模型時最優先看的通常是哪個方向？",
            ],
            "召回率（Recall）",
            ["只看整體準確率（Accuracy）", "只看資料筆數", "只看訓練時間長短"],
            "當漏判成本高時，召回率比單純準確率更重要。",
            ["在高度不平衡資料中，accuracy 可能誤導。", "資料筆數不是模型性能指標。", "訓練時間不是任務目標指標。"],
            ["任務成本決定你優先的 metric。", "偵測少數類場景常優先 recall 或 PR 指標。"],
            ["sources/official-corpus.md｜L22301 統計學在大數據中的應用", "sources/scope-weight-map.md｜L22301 統計學在大數據中的應用"],
        ),
        mc(
            "s2d10_threshold_tuning",
            "L22301",
            "中",
            [
                "若模型機率輸出已存在，但你想在不重訓模型的前提下提升召回率，哪個調整方向最直接？",
                "你想讓模型抓到更多異常案例，且允許多一些誤報。若先不重建資料或改演算法，較合理的做法為何？",
            ],
            "調整分類決策閾值（decision threshold）",
            ["只改欄位名稱", "只提高 batch size", "只增加訓練輪數而不重新驗證"],
            "閾值調整直接影響 precision / recall 取捨，是不重訓下最直接的方法之一。",
            ["欄位名稱與分類邏輯無關。", "batch size 主要影響訓練流程。", "增加訓練輪數不一定能朝你要的 error trade-off 前進。"],
            ["threshold tuning 是決策層調整，不是資料層。", "題目若說『不重訓』，常先想 threshold。"],
            ["sources/official-corpus.md｜不平衡資料與召回率題型", "sources/scope-weight-map.md｜L22301 統計學在大數據中的應用"],
        ),
        mc(
            "s2d10_precision_recall_tradeoff",
            "L22301",
            "中",
            [
                "下列哪個敘述最符合 precision 與 recall 的常見取捨？",
                "若你把分類閾值調低，通常更容易發生哪一類現象？",
            ],
            "召回率可能提升，但誤報也可能增加",
            ["準確率一定同步提高", "資料量會自動翻倍", "模型就不再需要驗證"],
            "降低閾值常讓模型抓到更多正類，同時也更可能把負類誤判成正類。",
            ["不同指標不會自動同向改善。", "調閾值不會改變資料量。", "任何閾值調整後都仍需要重新驗證。"],
            ["precision/recall 是 trade-off，不是一起無條件上升。", "閾值題常考『抓更多正類』的代價。"],
            ["sources/official-corpus.md｜L22301 統計學在大數據中的應用", "sources/scope-weight-map.md｜L22301 統計學在大數據中的應用"],
        ),
        mc(
            "s2d10_class_weight",
            "L22401",
            "中",
            [
                "若資料極不平衡，但你不想先改動樣本分布，還有哪些模型層常見作法？",
                "團隊不希望先做過採樣，而是想在訓練時讓模型更重視少數類。較合理的方向為何？",
            ],
            "調整 class weight 或成本敏感學習",
            ["把所有樣本權重都設成一樣", "只把欄位排序改掉", "完全不理會類別比例"],
            "class weight 會讓模型在訓練時對少數類錯誤給更高代價，是不平衡分類常見手段。",
            ["權重全相同無法處理不平衡。", "欄位排序與類別偏誤無關。", "不理會比例常讓模型只學會多數類。"],
            ["SMOTE 是資料層，class weight 是模型層。", "同一題要先判斷它在問哪一層補強。"],
            ["sources/official-corpus.md｜L22401 大數據與機器學習", "sources/scope-weight-map.md｜L22401 大數據與機器學習"],
        ),
    ],
})

S1_REVIEW: dict[int, list[str]] = {
    11: ["s1d1_tokenization", "s1d3_rag_core", "s1d7_copyright_prevention", "s1d9_kubernetes"],
    12: ["s1d2_cv_tasks", "s1d4_early_fusion", "s1d5_data_readiness", "s1d8_regression_fit"],
    15: ["s1d3_retrieval_stage", "s1d7_transparency", "s1d8_scaling", "s1d9_canary", "s1d10_word2vec"],
    16: ["s1d5_poc", "s1d7_supply_chain", "s1d9_integration_testing", "s1d10_seq2seq", "s1d4_missing_modality"],
    17: ["s1d1_tokenization", "s1d3_rag_core", "s1d7_copyright_prevention", "s1d9_kubernetes", "s1d8_scaling", "s1d10_seq2seq"],
    18: ["s1d6_requirement_first", "s1d6_resource_allocation", "s1d13_audit_log", "s1d13_model_card", "s1d14_canary_rollback", "s1d14_fail_safe"],
    19: ["s1d1_rule_based_boundary", "s1d3_augmentation_semantics", "s1d7_adversarial_training", "s1d9_drift_monitoring", "s1d10_word2vec", "s1d14_input_validation"],
    20: ["s1d3_rag_core", "s1d7_transparency", "s1d5_data_readiness", "s1d6_requirement_first", "s1d9_integration_testing", "s1d14_fail_safe"],
}

S2_REVIEW: dict[int, list[str]] = {
    11: ["s2d1_year_float", "s2d1_nullable_int", "s2d3_ttest", "s2d4_roc", "s2d7_fit_xy"],
    12: ["s2d3_anova", "s2d3_prop_test", "s2d6_melt_barplot", "s2d7_coef_intercept", "s2d10_smote"],
    15: ["s2d2_iqr", "s2d3_chisquare", "s2d4_kmeans_logic", "s2d8_add_constant", "s2d10_threshold_tuning", "s2d13_graph_edge_property"],
    16: ["s2d2_zscore", "s2d6_groupby_sum", "s2d7_pvalue", "s2d9_kfold", "s2d9_bootstrap", "s2d14_poisson"],
    17: ["s2d1_nullable_int", "s2d6_melt_barplot", "s2d7_fit_xy", "s2d7_coef_intercept", "s2d10_smote", "s2d10_recall_threshold", "s2d14_arima_residual"],
    18: ["s2d3_ttest", "s2d3_prop_test", "s2d6_groupby_sum", "s2d6_nlargest", "s2d8_add_constant", "s2d10_threshold_tuning", "s2d13_graph_edge_property"],
    19: ["s2d1_year_float", "s2d2_iqr", "s2d2_standardize_vs_normalize", "s2d7_boxcox", "s2d9_stratify", "s2d13_rdf", "s2d14_arima_residual"],
    20: ["s2d1_isna", "s2d4_pca", "s2d9_kfold", "s2d10_smote", "s2d10_class_weight", "s2d14_white_noise", "s2d14_lag"],
}

LCODE_LABELS = {
    "L21101": "自然語言處理技術與應用",
    "L21102": "電腦視覺技術與應用",
    "L21103": "生成式 AI 技術與應用",
    "L21104": "多模態人工智慧應用",
    "L21201": "AI 導入評估",
    "L21202": "AI 導入規劃",
    "L21203": "AI 風險管理",
    "L21301": "數據準備與模型選擇",
    "L21302": "AI 技術系統集成與部署",
    "L22101": "敘述性統計與資料摘要技術",
    "L22102": "機率分佈與資料分佈模型",
    "L22103": "假設檢定與統計推論",
    "L22201": "數據收集與清理",
    "L22202": "數據儲存與管理",
    "L22203": "數據處理技術與工具",
    "L22301": "統計學在大數據中的應用",
    "L22302": "常見的大數據分析方法",
    "L22303": "數據可視化工具",
    "L22401": "大數據與機器學習",
    "L22402": "大數據在鑑別式 AI 中的應用",
}


def flatten_items(base_map: dict[int, list[dict]]) -> dict[str, dict]:
    flattened = {}
    for items in base_map.values():
        for item in items:
            flattened[item["id"]] = item
    return flattened


S1_ALL = flatten_items(S1_BASE)
S2_ALL = flatten_items(S2_BASE)


def items_for_day(subject: int, day: int) -> list[dict]:
    if subject == 1:
        if day in S1_BASE:
            return S1_BASE[day]
        return [S1_ALL[item_id] for item_id in S1_REVIEW[day]]
    if day in S2_BASE:
        return S2_BASE[day]
    return [S2_ALL[item_id] for item_id in S2_REVIEW[day]]


def all_day_item_ids(subject: int) -> dict[int, list[str]]:
    mapping = {}
    for day in range(1, 21):
        mapping[day] = [item["id"] for item in items_for_day(subject, day)]
    return mapping


S1_DAY_IDS = all_day_item_ids(1)
S2_DAY_IDS = all_day_item_ids(2)


def question_appearance_map(subject: int) -> dict[str, list[int]]:
    result: dict[str, list[int]] = defaultdict(list)
    source = S1_DAY_IDS if subject == 1 else S2_DAY_IDS
    for day, item_ids in source.items():
        for item_id in item_ids:
            result[item_id].append(day)
    return dict(result)


S1_APPEARANCES = question_appearance_map(1)
S2_APPEARANCES = question_appearance_map(2)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def render_readme() -> str:
    return dedent(
        """
        # iPAS 中級 AI 規劃師 20 天反向刷題包

        - `sources/`：命題依據、權重地圖、題型模板、書目索引。
        - `daily/`：20 天、每天兩份題單，答案用可收折區塊包住。
        - `progress/`：弱點追蹤、回鍋規劃、每日索引。

        重新生成：

        ```powershell
        python .\\generate_ipas_reverse_pack.py
        ```
        """
    ).strip() + "\n"


def render_official_corpus() -> str:
    return dedent(
        f"""
        # Official Corpus

        這份文件只整理官方可回溯資料，作為整包題單的命題母本。

        ## 官方文件清單

        - [考試資訊]({OFFICIAL_LINKS["exam_info"]})
        - [學習資源]({OFFICIAL_LINKS["learning_resources"]})
        - [115 年簡章 PDF]({OFFICIAL_LINKS["brochure_115"]})
        - [114.04 評鑑內容範圍參考]({OFFICIAL_LINKS["scope_11404"]})
        - [114.09 中級樣題 PDF]({OFFICIAL_LINKS["sample_11409"]})
        - [中級科目 1 學習指引]({OFFICIAL_LINKS["guide_subject_1"]})
        - [中級科目 2 學習指引]({OFFICIAL_LINKS["guide_subject_2"]})
        - [考試樣題與參考書目頁]({OFFICIAL_LINKS["book_list"]})

        ## 題型與制度摘要

        - 中級為 `科目 1 +（科目 2 或科目 3 擇一）`。
        - 你本次只準備 `科目 1 + 科目 2`。
        - 每科 `50 題單選`，採 `電腦測驗`。
        - 科目 1 與科目 2 各 `90 分鐘`。
        - 科目 2 自官方公告後已納入 `程式相關題型`，因此本題包特別拉高 `pandas / sklearn / statsmodels / seaborn` 權重。

        ## 科目 1 命題主軸

        - `L211`：NLP、電腦視覺、生成式 AI、多模態。
        - `L212`：AI 導入評估、導入規劃、風險管理。
        - `L213`：數據準備、模型選擇、系統整合、部署、監控。

        ## 科目 2 命題主軸

        - `L221`：敘述統計、機率分布、假設檢定。
        - `L222`：資料收集與清理、儲存與管理、處理工具。
        - `L223`：統計分析方法、視覺化、模型驗證。
        - `L224`：大數據在機器學習與鑑別式 AI 的應用。

        ## 使用規則

        - 每天先做 `daily/` 題單，不先讀理論。
        - 題目不會直接抄官方原題，但會保留官方題型的判斷邏輯、干擾模式與術語範圍。
        - 題目做完後，再回看 `sources/scope-weight-map.md` 與 `sources/book-bridge.md` 補洞。
        """
    ).strip() + "\n"


def exposure_rows() -> list[tuple[str, str, int, list[int]]]:
    rows = []
    for item_id, item in {**S1_ALL, **S2_ALL}.items():
        appearances = (S1_APPEARANCES if item_id.startswith("s1") else S2_APPEARANCES)[item_id]
        rows.append((item["lcode"], item_id, len(appearances) * 2, appearances))
    rows.sort(key=lambda row: (-row[2], row[0], row[1]))
    return rows


def render_scope_weight_map() -> str:
    lcode_map: dict[str, dict[str, object]] = defaultdict(lambda: {"questions": 0, "items": []})
    for item_id, item in {**S1_ALL, **S2_ALL}.items():
        appearances = (S1_APPEARANCES if item_id.startswith("s1") else S2_APPEARANCES)[item_id]
        lcode_map[item["lcode"]]["questions"] += len(appearances) * 2
        lcode_map[item["lcode"]]["items"].append((item_id, appearances, item["gaps"][0]))

    sections = []
    for lcode in sorted(lcode_map):
        payload = lcode_map[lcode]
        items = payload["items"][:4]
        section_lines = [
            f"## {lcode} {LCODE_LABELS.get(lcode, '')}",
            "",
            f"- 規劃題量權重：`{payload['questions']}` 題",
            "- 題型來源：官方範圍 + 學習指引 + 樣題結構仿真",
            "代表題：",
        ]
        section_lines.extend(
            f"- `{item_id}`：出現在 Day {', '.join(f'{day:02d}' for day in appearances)}；補點焦點：{gap}"
            for item_id, appearances, gap in items
        )
        sections.append("\n".join(section_lines))

    return dedent(
        """
        # Scope Weight Map

        這份文件把官方 L-code 主題轉成題包權重。權重不是官方配分，而是依你的 20 天反向刷題需求重新排序。

        ## 高權重原則

        - 科目 1：`L211`、`L21203`、`L21302` 權重最高。
        - 科目 2：`L22103`、`L22201`、`L22301`、`L22303`、`L22401` 權重最高。
        - 若題目明確涉及 Python、統計檢定、回歸或視覺化，優先回補科目 2。
        """
    ).strip() + "\n\n" + "\n\n".join(sections) + "\n"


def render_question_patterns() -> str:
    return dedent(
        """
        # Question Patterns

        ## 題型模板

        - 定義辨識題：給概念定義，要求指出正確術語。
        - 任務選型題：給業務情境，要求選出最適合的模型、方法或平台。
        - 反向排除題：四個選項都看似合理，但只有一個最對題，重點在排除干擾。
        - 風險治理題：把技術、法務、流程治理混在一起，考你先抓真正風險來源。
        - 程式判讀題：看 `pandas / sklearn / statsmodels / seaborn` 程式片段，判斷 API、輸出或概念。
        - 統計檢定題：先辨識資料型態與檢定目標，再選 t-test、ANOVA、chi-square 或比例檢定。
        - 視覺化題：先辨識要比的是 `count / sum / mean / trend`，再選對圖與聚合方式。
        - 時序診斷題：看 `lag / ACF / residual / seasonality` 再判斷模型問題。

        ## 反向學習規則

        - 先作答，再打開 `<details>` 看答案。
        - 若答錯，先記錄「哪個選項吸引你」，不要只記正解。
        - 若答對但講不出排除理由，也要登錄到 `progress/knowledge-gaps.md`。

        ## 日常使用

        - Day 01–10：建立高頻術語與基本判斷。
        - Day 11–16：用回鍋題把錯誤類型固定住。
        - Day 17–20：只做高頻壓縮與反向變體，避免知識點越補越散。
        """
    ).strip() + "\n"


def render_book_bridge() -> str:
    return dedent(
        """
        # Book Bridge

        這份文件只做「主題對應哪本官方參考書目」的索引，不做通讀筆記。

        | 主題 | 優先書目 | 用法 |
        | --- | --- | --- |
        | NLP / 多模態 / 生成式 AI 基礎 | 圖解 AI、人工智慧導論 | 只補術語邊界與任務差異 |
        | AI 導入評估 / 規劃 / 治理 | 數位治理韌性、AI、規管；人工智慧導論 | 只補法規、風險、責任與流程治理 |
        | 統計檢定 / 分布 / 敘述統計 | 統計之美；大數據分析與資料挖礦 2/e | 只補檢定選型、分布概念與統計語意 |
        | pandas / 資料清理 / 視覺化 | 大數據分析與應用實戰 | 直接對照程式題與圖表題 |
        | 回歸 / 模型評估 / 特徵工程 | 大數據分析與資料挖礦 2/e；資料科學的建模基礎 | 只看你在題單中連錯的章節 |
        | 機器學習數學底子 | 機器學習的數學基礎 | 只在某個統計或尺度觀念一直卡住時翻 |

        ## 書目使用順序

        - 題目先做完。
        - 只針對 `progress/knowledge-gaps.md` 已登錄的知識點翻書。
        - 一次只補一個概念，不展開整章通讀。
        """
    ).strip() + "\n"


def render_daily_review_index() -> str:
    rows = []
    for day in range(1, 21):
        s1_priority = infer_session_priority(1, items_for_day(1, day))
        s2_priority = infer_session_priority(2, items_for_day(2, day))
        rows.append(
            f"| Day {day:02d} | [科目1](../daily/day-{day:02d}-subject-1.md) | {DAY_META[day]['s1_focus']} | {s1_priority} | [科目2](../daily/day-{day:02d}-subject-2.md) | {DAY_META[day]['s2_focus']} | {s2_priority} |"
        )
    return dedent(
        """
        # Daily Review Index

        | 天數 | 科目 1 題單 | 焦點 | 優先級 | 科目 2 題單 | 焦點 | 優先級 |
        | --- | --- | --- | --- | --- | --- | --- |
        """
    ).strip() + "\n" + "\n".join(rows) + "\n"


def render_wrong_answer_map() -> str:
    rows = []
    combined = {**S1_ALL, **S2_ALL}
    appearance_map = {**S1_APPEARANCES, **S2_APPEARANCES}
    for item_id, item in combined.items():
        days = appearance_map[item_id]
        if len(days) < 3:
            continue
        rows.append(
            f"| `{item_id}` | {'科目1' if item_id.startswith('s1') else '科目2'} | `{item['lcode']}` | Day {days[0]:02d} | {', '.join(f'Day {day:02d}' for day in days[1:])} | {item['gaps'][0]} |"
        )
    rows.sort()
    return dedent(
        """
        # Wrong Answer Map

        這不是實際錯題紀錄，而是預先排好的高風險概念回鍋表。若你在第一次出現時答錯，就沿著後續回鍋日繼續追。

        | Concept ID | 科目 | L-code | 首次出現 | 後續回鍋日 | 建議追蹤重點 |
        | --- | --- | --- | --- | --- | --- |
        """
    ).strip() + "\n" + "\n".join(rows) + "\n"


def render_knowledge_gaps() -> str:
    return dedent(
        """
        # Knowledge Gaps

        ## 使用規則

        - 這份文件是 `人工補充版`；若你要看系統自動整理的弱點，優先看 `progress/auto-knowledge-gaps.md`。
        - 只記錄 `連錯兩次以上` 或 `雖答對但無法解釋` 的概念。
        - 每一列只寫一個知識點，不要把整份題單塞進來。
        - 若某概念已補熟，請標記為 `closed`。

        ## 空白模板

        | 狀態 | Subject | Concept ID | L-code | 問題描述 | 第一次卡住日期 | 下次回鍋日 | 補救方式 |
        | --- | --- | --- | --- | --- | --- | --- | --- |
        |  |  |  |  |  |  |  |  |

        ## 填寫範例（使用前請刪掉）

        | 狀態 | Subject | Concept ID | L-code | 問題描述 | 第一次卡住日期 | 下次回鍋日 | 補救方式 |
        | --- | --- | --- | --- | --- | --- | --- | --- |
        | open | 科目2 | s2d3_ttest | L22103 | 分不清 t-test 和比例檢定 | Day 03 | Day 11 | 回看 scope-weight-map + 重做題單 |

        ## 建議優先監控

        - 科目 1：RAG、AI 風險治理、Kubernetes、rollback / fallback。
        - 科目 2：NaN / dtype、檢定選型、回歸係數解讀、SMOTE、ARIMA 殘差診斷。
        """
    ).strip() + "\n"


def validate_counts() -> None:
    for day in range(1, 21):
        assert len(items_for_day(1, day)) * 2 == DAY_META[day]["s1_count"], f"subject 1 day {day} count mismatch"
        assert len(items_for_day(2, day)) * 2 == DAY_META[day]["s2_count"], f"subject 2 day {day} count mismatch"


def generate() -> None:
    validate_counts()

    write_text(ROOT / "README.md", render_readme())
    write_text(SOURCES_DIR / "official-corpus.md", render_official_corpus())
    write_text(SOURCES_DIR / "scope-weight-map.md", render_scope_weight_map())
    write_text(SOURCES_DIR / "question-patterns.md", render_question_patterns())
    write_text(SOURCES_DIR / "book-bridge.md", render_book_bridge())

    write_text(PROGRESS_DIR / "daily-review-index.md", render_daily_review_index())
    write_text(PROGRESS_DIR / "wrong-answer-map.md", render_wrong_answer_map())
    write_text(PROGRESS_DIR / "knowledge-gaps.md", render_knowledge_gaps())

    for day in range(1, 21):
        write_text(DAILY_DIR / f"day-{day:02d}-subject-1.md", render_daily_file(day, 1, items_for_day(1, day), concise=False))
        write_text(DAILY_DIR / f"day-{day:02d}-subject-2.md", render_daily_file(day, 2, items_for_day(2, day), concise=False))


if __name__ == "__main__":
    generate()
