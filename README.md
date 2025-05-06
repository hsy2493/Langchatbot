# `Lagnchatbot` - <대규모언어모델 개인 프로젝트(3차)>✍️ <br>
1. 작업 기간 : 2025. 04. 01 ~ 2025. 04. 02
2. 주제 : 번역기 AI 사이트
3. 목적 : 고객이 한국어를 입력하면 지정된 외국어로 번역해주는 번역기 AI 사이트 프로젝트 입니다. 대규모언어모델(LLM)을 활용하여 자연스럽고 정확한 번역을 제공하고, 언어 장벽을 해소하여 원활한 소통을 돕는 것을 주목적으로 합니다.
4. 주요 기능 : 입력한 내용을 외국어로 번역
5. 사용 툴 :
- 사용 언어 : python
- LLM 모델 정의 : ollama 기반 gemma2 모델
- UI : FastAPI로 대체

<br>
6. 결과물 : <br>

## <화면 구현(FastAPI로 대체)> <br>
(1) 입력한 내용 외국어로 번역 <br>
<img width="1242" alt="image" src="https://github.com/user-attachments/assets/2d4c2fd6-ff3e-4b07-834d-33a32d9387e6" />
 <br>
<설명> <br>
-번역할 내용과 언어 입력 후, Execute 버튼 클릭 시, 선택한 언어로 내용이 번역된다. <br>
- FastAPI main - 화면구현 상세 코드 <br>
https://github.com/hsy2493/Langchatbot/blob/main/main.py <br>


## <기능 구현> <br>
(1) LLM 모델 정의 :  ollama 기반 gemma2 모델 사용 <br>
<img width="908" alt="image" src="https://github.com/user-attachments/assets/44d43eeb-dc0c-43d8-b4aa-b4eacf95ca57" /> <br>
<img width="1195" alt="image" src="https://github.com/user-attachments/assets/d5fc0e6e-d507-43c6-bb8c-e742fa6bf3bb" /> <br>
<img width="519" alt="image" src="https://github.com/user-attachments/assets/b6c10c61-c1e8-4de0-a11c-8d0d56edcadc" /> <br>
<img width="621" alt="image" src="https://github.com/user-attachments/assets/1d4688d4-f523-47b0-adbd-9d61a4e852aa" /> <br>
<설명> <br>
-base_url로 현재 실행 중인 ollama 모델과 POST 요청으로 통신을 진행한다. <br>
-text와 dest_lang을 사용하여, 각각 번역할 내용과 번역할 언어를 선택한다(json 형태). <br>
- gemma2 service - 기능구현 상세 코드 <br>
https://github.com/hsy2493/Langchatbot/blob/main/app/services/ollama_service.py <br> 

(2) 예외 처리 
<img width="1192" alt="image" src="https://github.com/user-attachments/assets/4b204457-6bf2-4015-9fa2-9a336c863d3d" /> <br>
<img width="669" alt="image" src="https://github.com/user-attachments/assets/8da8a38b-8c06-4088-855e-806576d52c9f" />
<br>
<설명> <br>
-번역 내용이 null(공백)인 경우, "텍스트를 입력해주세요." 라는 메세지와 함께 400에러 코드로 예외 처리를 한다. <br>
- gemma2 router - 기능구현 상세 코드 <br>
https://github.com/hsy2493/Langchatbot/blob/main/app/routers/chat_router.py <br> 

<b>
7. 성과 : <br>
- ollama 설치 및 사용법을 학습하고, 이를 통하여 LLM 기반 개인 프로젝트 진행을 경험함.
- ollama 기반 gemma2 모델을 활용하여, LLM 기반 번역기 AI 기능구현이 가능함.
- UI 대신 FastAPI를 활용하여, 대규모 언어 모델 프로젝트 테스트 진행을 경험함.
- FastAPT로 gemma2 서버 엔드포인트로 통신하는 것을 학습함.
- 프로젝트 진행 목적에 대한 중요성을 다시끔 깨달음. 앞으로 간단한 프로젝트를 진행하더라도, 구체적인 진행 목적을 지정해야겠음 (창의성 향상).
</b>
