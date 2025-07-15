# MyPortfolio - 個人網站

這是一個使用 Python Flask 框架建立的個人作品集網站，用於展示個人技能和興趣。

## 專案簡介

本專案是一個簡單的個人網站，包含：
- 首頁自我介紹
- 興趣/技能列表展示
- 技能詳細資訊頁面
- 使用 SQLite 資料庫儲存資料
- 響應式設計界面

## 功能特色

- **首頁**: 個人簡介和網站說明
- **興趣列表**: 以卡片形式展示各項興趣和技能
- **詳細頁面**: 點擊興趣卡片可查看詳細說明
- **資料庫驅動**: 使用 SQLAlchemy ORM 管理資料
- **響應式設計**: 適配不同螢幕尺寸

## 技術棧

- **後端**: Python Flask
- **資料庫**: SQLite + SQLAlchemy
- **前端**: HTML5, CSS3, Jinja2 模板
- **開發工具**: PyCharm IDE

## 專案結構

```
MyPortfolio/
├── .idea/                  # PyCharm IDE 設定檔
├── static/
│   └── style.css          # 樣式表
├── templates/
│   ├── base.html          # 基本模板
│   ├── index.html         # 首頁模板
│   ├── skills.html        # 技能列表模板
│   └── skill_detail.html  # 技能詳細頁模板
├── app.py                 # Flask 主應用程式
├── init_db.py             # 資料庫初始化腳本
└── data.sqlite            # SQLite 資料庫檔案
```

## 安裝與執行

### 環境需求

- Python 3.13 或更新版本
- Flask
- Flask-SQLAlchemy

### 安裝步驟

1. **克隆專案**
```bash
git clone <repository-url>
cd MyPortfolio
```

2. **建立虛擬環境**
```bash
python -m venv .venv
```

3. **啟動虛擬環境**
- Windows:
```bash
.venv\Scripts\activate
```
- macOS/Linux:
```bash
source .venv/bin/activate
```

4. **安裝依賴套件**
```bash
pip install flask flask-sqlalchemy
```

5. **初始化資料庫**
```bash
python init_db.py
```

6. **執行應用程式**
```bash
python app.py
```

7. **開啟瀏覽器**
前往 `http://localhost:5000` 查看網站

## 資料庫結構

### Skills 資料表
- `id`: 主鍵 (自動遞增)
- `url_id`: URL 識別碼 (唯一)
- `name`: 技能名稱
- `summary`: 簡短描述
- `details`: 詳細說明

## 路由說明

- `/`: 首頁 - 個人介紹
- `/skills`: 興趣/技能列表頁面
- `/skill/<skill_url_id>`: 特定技能的詳細資訊頁面

## 自訂內容

如需修改網站內容，請編輯 `init_db.py` 中的 `OLD_SKILLS_DATA` 字典，然後：

1. 刪除現有的 `data.sqlite` 檔案
2. 重新執行 `python init_db.py` 初始化資料庫

## 部署注意事項

在生產環境中部署時，請確保：
- 將 `app.run(debug=True)` 改為 `app.run(debug=False)`
- 使用 WSGI 伺服器（如 Gunicorn）
- 設定適當的環境變數
- 定期備份資料庫

## 未來改進方向

- [ ] 新增管理後台
- [ ] 支援圖片上傳
- [ ] 新增聯絡表單
- [ ] 實作使用者認證
- [ ] 支援多語言
- [ ] 新增專案展示功能

## 授權

本專案僅供學習和個人使用。

## 聯絡資訊

如有任何問題或建議，歡迎聯繫：
- 姓名：賴泉宏
- 身份：資工系大一新生

---

*最後更新：2025年7月*
