from pydantic import BaseModel

class TranslationRequest(BaseModel): # 번역 모델
    text: str # 번역 내용
    target_lang: str # 언어 선택 : en, ko, ja