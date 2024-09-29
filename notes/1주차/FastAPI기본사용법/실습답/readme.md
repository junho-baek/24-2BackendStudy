### 라우터 예시:

```python
from fastapi import FastAPI

app = FastAPI()

# 루트 라우터
@app.get("/", summary="루트 라우터", tags=["ALL", "Root"])
async def root():
    '''
    # 루트 API

    이 API는 루트 경로에 대한 기본적인 응답을 반환합니다.
    '''
    return {"message": "Hello from Root"}

# DA 라우터
@app.get("/da", summary="DA 라우터", tags=["ALL", "DA"])
async def da():
    '''
    # DA API

    이 API는 DA 관련 요청을 처리합니다.
    '''
    return {"message": "Hello from DA"}

# DS 라우터
@app.get("/ds", summary="DS 라우터", tags=["ALL", "DS"])
async def ds():
    '''
    # DS API

    이 API는 DS 관련 요청을 처리합니다.
    '''
    return {"message": "Hello from DS"}

# DE 라우터
@app.get("/de", summary="DE 라우터", tags=["ALL", "DE"])
async def de():
    '''
    # DE API

    이 API는 DE 관련 요청을 처리합니다.
    '''
    return {"message": "Hello from DE"}
```

```shell
curl -X 'GET' \
  'http://localhost:8081/da' \
  -H 'accept: application/json'
```
