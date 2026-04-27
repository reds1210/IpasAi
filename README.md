# iPAS 中級 AI 規劃師 20 天反向刷題包

這個 workspace 已經整理成可直接作答、批改、追蹤弱點的格式。

- [study-hub.md](study-hub.md)：主入口，含 20 天每日題單與 extended 加練
- `daily/`：每日正式題單
- `extended/`：額外加練題庫
- `attempts/`：作答單
- `reports/`：批改報告
- `progress/`：成績、弱點、回看佇列
- `data/pack-manifest.json`：題單結構與正解索引

## 優先級說明

- `A`：先刷。高命中主戰場，優先來自官方範圍、官方樣題、官方公告題型。
- `B`：第二層。常見延伸題型，通常用來補回鍋與跨章情境。
- `C`：最後補。低報酬或偏補洞題，不影響 20 天過線主路徑。

## 來源層級

- `official-derived`：依官方範圍、官方樣題、官方公告題型轉寫。
- `public-pattern-derived`：依公開練習題、備考心得、非官方題型整理轉寫。
- 題目不直接照抄網路題面；公開來源只用來抽題型與干擾選項邏輯。

## 重建整包

```powershell
python .\build_full_pack.py
```

## 批改每日題單

```powershell
python .\score_attempt.py --day 1 --subject 1
```

也可以直接貼答案：

```powershell
python .\score_attempt.py --day 1 --subject 1 --answers D,A,C,B,D,A,C,B
```

## 批改 extended 加練

```powershell
python .\score_attempt.py --drill subject-2-code-practice-drill
```

## Extended 題庫入口

- [extended/README.md](extended/README.md)
