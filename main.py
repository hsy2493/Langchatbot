# 사전설치 : pip install fastapi uvicorn pandas numpy scikit-learn tensorflow 
# 사전설치 : pip install sqlalchemy pymysql python-dotenv pydantic requests
import uvicorn
from fastapi import FastAPI
from app.routers import chat_router

app = FastAPI(title="Chatbot API", 
              description="""## 텍스트 번역 AI 챗봇 서비스
              \n### 테스트 방법 : \n #### 1. text: 번역 내용 입력 \n#### 2. target_lang: 언어 선택 (영어: en, 한국어: ko, 일본어: ja)
              """)

app.include_router(chat_router.router) # chat_router.py

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

# FastAPI : http://localhost:8000/docs 
