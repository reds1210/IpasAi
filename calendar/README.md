# Google Calendar 匯入

這個資料夾提供可直接匯入 Google Calendar 的讀書計畫檔。

- 建議匯入檔：[google-calendar-study-plan-import.csv](./google-calendar-study-plan-import.csv)
- 舊版檔案：[google-calendar-study-plan.csv](./google-calendar-study-plan.csv)
- 主入口：[study-hub.md](https://github.com/reds1210/IpasAi/blob/main/study-hub.md)

建議優先使用 `google-calendar-study-plan-import.csv`。這份檔案採用 `UTF-8 BOM`，而且事件描述只用英文標籤搭配 GitHub 原始網址，能降低 Windows / Excel / Google Calendar 匯入時的亂碼風險。

## 匯入方式

1. 打開 Google Calendar。
2. 進入「設定」>「匯入與匯出」。
3. 匯入 `google-calendar-study-plan-import.csv`。
4. 每一天的事件描述都包含對應當天的 GitHub `daily/*.md` 連結，可直接點開。

## 日期範圍

- Day 01: 2026-04-28
- Day 20: 2026-05-17

## 事件內容

每個事件預設為「全天」事件，包含：

- 當日 `Subject 1 MD` 連結
- 當日 `Subject 2 MD` 連結
- `Study Hub` 入口連結
