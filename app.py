import os
from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy

# 取得目前檔案所在的資料夾路徑
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# --- 資料庫設定 ---
# 設定資料庫檔案的路徑
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# 關閉不必要的追蹤，以節省系統資源
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化 SQLAlchemy，與 Flask app 建立關聯
db = SQLAlchemy(app)


# --- 資料庫模型 (Model) ---
# 我們用一個 Class 來對應到資料庫中的一個 Table
class Skill(db.Model):
    __tablename__ = 'skills'  # 自訂資料表名稱
    id = db.Column(db.Integer, primary_key=True)  # 主鍵，會自動增長
    # url_id 用來取代原本字典中的 key，例如 'python', 'flask'
    url_id = db.Column(db.String(64), unique=True, nullable=False)
    name = db.Column(db.String(64), nullable=False)
    summary = db.Column(db.String(200), nullable=False)
    details = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Skill {self.name}>'


# --- 路由 (Routes) ---
@app.route('/')
def home():
    """首頁路由"""
    return render_template('index.html')


@app.route('/skills')
def skills():
    """技能列表頁路由"""
    # 從資料庫查詢所有的技能資料，並依照 id 排序
    all_skills = Skill.query.order_by(Skill.id).all()
    return render_template('skills.html', skills=all_skills)


@app.route('/skill/<string:skill_url_id>')
def skill_detail(skill_url_id):
    print(skill_url_id)
    """
    動態路由，用於顯示單一技能的詳細資訊。
    現在我們用 url_id (例如 'python') 來查詢
    """
    # 使用 url_id 來查詢第一筆符合的資料，如果找不到就回傳 404
    skill = Skill.query.filter_by(url_id=skill_url_id).first_or_404()
    print(skill)
    return render_template('skill_detail.html', skill=skill)


@app.errorhandler(404)
def page_not_found(e):
    """自訂 404 錯誤頁面"""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)