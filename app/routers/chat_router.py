from fastapi import APIRouter, HTTPException
from app.schema.chat_schema import TranslationRequest
from app.services.ollama_service import OllamaService

router = APIRouter(prefix="/chat", tags=["translation"])

@router.post("/translate")
async def translate(request: TranslationRequest):
    if not request.text: # 텍스트가 없는 경우 400 에러 반환
                        # 400 에러 : 클라이언트의 요청이 부적절한 경우
        raise HTTPException(status_code=400, detail="텍스트를 입력해주세요.")
    
    try: # 번역 서비스 호출
        ollama_service = OllamaService() # service 객체 생성
        translated_text = ollama_service.translate_text(request.text, request.target_lang) 
        # 번역 내용, 언어 선택
        return {"translated_text": translated_text} 
    except Exception as e: # 오류 발생 시 500 에러 반환
                        # 500 에러 : 서버 문제 발생
        raise HTTPException(status_code=500, detail=f"오류 발생: {str(e)}")
