import requests

class OllamaService:
    def __init__(self, model="gemma2"): 
        self.base_url = "http://localhost:11434/api/generate" # Ollama 서버 엔드포인트
        self.model = model  # gemma2 모델 사용

    def translate_text(self, text: str, dest_lang: str): # 번역 내용, 언어 선택
        prompt = f"Translate this text to {dest_lang}: {text}" 
        payload = {
            "model": self.model, 
            "prompt": prompt,
            "stream": False
        }
        try:
            response = requests.post(self.base_url, json=payload) # POST 요청
            response.raise_for_status() # 오류 발생 시 예외 처리
            return response.json().get('response', '번역 결과가 없습니다.')
        except requests.exceptions.RequestException as e: # 요청 예외 처리
            raise Exception(f"Ollama API 호출 중 오류: {e}")
