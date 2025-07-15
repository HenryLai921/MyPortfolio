from app import app, db, Skill

# 這是原本在 app.py 中的舊資料
OLD_SKILLS_DATA = {
    '興趣一:寫程式(python)': {
        'name': '興趣一:寫程式(python)',
        'summary': '一種通用、高階的程式語言，以其簡潔的語法和強大的生態系而聞名。',
        'details': '我擅長使用 Python 進行後端開發 (Flask/Django)、數據分析 (Pandas, NumPy) 和自動化腳本撰寫。擁有豐富的專案經驗，能快速解決問題。'
    },
    '興趣二:組電腦': {
        'name': '興趣二:組電腦',
        'summary': '一個輕量級的 Python Web 框架，具有高度的靈活性和擴充性。',
        'details': '我使用 Flask 建立了多個 Web 應用程式，包括 RESTful API 和如此網站。熟悉其路由、模板、藍圖 (Blueprints) 等核心概念。'
    },
    '興趣三:彈鋼琴': {
        'name': '興趣三:彈鋼琴',
        'summary': '網頁前端開發的核心語言，賦予網頁互動性。',
        'details': '我能使用原生 JavaScript (ES6+) 進行 DOM 操作和事件處理。同時也熟悉 React 和 Vue.js 等現代前端框架，能建構複雜的單頁應用 (SPA)。'
    },
    '興趣四:觀察電腦二手市場': {
        'name': '興趣四:觀察電腦二手市場',
        'summary': '一個開源的容器化平台，用於打包、發布和執行應用程式。',
        'details': '我習慣使用 Docker 來容器化我的應用程式，確保開發、測試和生產環境的一致性。能夠撰寫 Dockerfile 並使用 Docker Compose 管理多容器應用。'
    }
}

# 使用 app.app_context() 確保在 Flask 的應用程式情境下執行
with app.app_context():
    # 根據定義好的模型建立所有資料表
    # 如果資料庫檔案或資料表已存在，它不會重複建立
    print("正在建立資料庫資料表...")
    db.create_all()
    print("資料表建立完成。")

    # 檢查資料庫是否已有資料，避免重複寫入
    if Skill.query.first() is None:
        print("資料庫是空的，正在寫入初始資料...")
        # 遍歷舊資料字典
        for url_id, data in OLD_SKILLS_DATA.items():
            # 為每一筆資料建立一個 Skill 物件
            new_skill = Skill(
                url_id=url_id,
                name=data['name'],
                summary=data['summary'],
                details=data['details']
            )
            # 將新物件加入到資料庫的 session 中
            db.session.add(new_skill)

        # 一次性提交所有變更到資料庫
        db.session.commit()
        print("初始資料寫入成功！")
    else:
        print("資料庫中已有資料，略過寫入步驟。")