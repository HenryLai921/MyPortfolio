# 步驟 1: 選擇一個官方的 Python 執行環境作為基礎映像檔
# python:3.9-slim 是一個輕量化的版本，可以讓最終的映像檔小一點
FROM python:3.11-slim

# 步驟 2: 在容器內部建立一個工作目錄
WORKDIR /app

# 步驟 3: 複製相依性清單到容器中並安裝
# 我們先只複製這個檔案，因為它不常變動，可以利用 Docker 的快取機制
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 步驟 4: 將專案目錄中的所有檔案複製到容器的 /app 目錄中
COPY . .

# 步驟 5: 宣告容器對外開放的 port
# 這一步是給操作者看的提示，實際的 port 映射在 docker run 指令中進行
EXPOSE 8000

# 步驟 6: 定義容器啟動時要執行的指令
# 使用 gunicorn 來啟動我們的 app
# --bind 0.0.0.0:8000 表示監聽所有來自外部的流量，port 為 8000
# app:app 的意思是「執行 app.py 檔案中的 app 這個 Flask 實例」
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]