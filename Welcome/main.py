# FastAPI import
from fastapi import FastAPI

# FastAPI instance 생성. 
app = FastAPI()

# Path 오퍼레이션 생성. Path는 도메인명을 제외하고 / 로 시작하는 URL 부분
# 만약 url이 https://example.com/items/foo 라면 path는 /items/foo 
# Operation은 GET, POST, PUT/PATCH, DELETE등의 HTTP 메소드임. 
@app.get("/", summary="간단한 API"
         , tags=[ "root", "ALL"]
         )
# 비동기 방식으로 함수 선언.
async def root():
    # 주석과 동시에 swagger ui 에 md 형식으로 docs 추가 가능.
    '''
    # H1
    ## H2
    ### 이것은 간단한 API 입니다. 아래는 인자값입니다.
    - **인자값1**은 ~~ 입니다.
    - **인자값2**는 @@ 입니다.
    '''
    
    return {"message": "Hello World"}


@app.get("/da", summary="DA팀 라우터 입니다."
         , tags=["DA", "ALL"]
         )
async def da():
    # 주석과 동시에 swagger ui 에 md 형식으로 docs 추가 가능.
    '''
    # DA 팀 라우터입니다.
    ## 크롤링, 시각화 등을 처리하는 API
    
    '''
    
    return {"message": "Hello World"}

@app.get("/de", summary="DE팀 라우터 입니다."
         , tags=["DE", "ALL"]
         )
async def de():
    # 주석과 동시에 swagger ui 에 md 형식으로 docs 추가 가능.
    '''
    # DE 팀 라우터입니다.
    ## 데이터분산처리, 실시간 데이터 수집 등을 처리하는 API
    
    '''
    
    return {"message": "Hello World"}

@app.get("/ds", summary="DS팀 라우터 입니다."
         , tags=["DS", "ALL"]
         )
async def ds():
    # 주석과 동시에 swagger ui 에 md 형식으로 docs 추가 가능.
    '''
    # DS 팀 라우터입니다.
    ## 모델을 처리하는 API
    
    '''
    
    return {"message": "Hello World"}
