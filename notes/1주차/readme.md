# FastAPI 기본 사용법

Welcome 디렉토리로 이동하자.

```shell
cd Welcome
```

uvicorn - asgi 서버를 구현해주는 프로그램. cli 명령어.

```shell
uvicorn main:app --port=8081 --reload
#main.py 에 있는 app이라는 FastApi 객체를 uvicorn 명령어로 실행
#--port: 포트 번호를 지정
#--reload: 서버 파일 수정된 부분을 바로 반영해주는 옵션. uvicorn 명령어로 다시 서버를 띄우지 않아도 돼서 편함
```

접속

- localhost:8081의 /(루트 라우터에 get 요청을 보내서 반환받은 값)

```
http://localhost:8081/
```

docs:
swagger UI가 자동으로 구현되어 있다.

```
http://localhost:8081/docs
```

```
http://localhost:8081/redoc
```

브라우저에 주소를 치면 get 방식으로 요청이 들어감.
response 는 상태코드 콘텐트타입 등이 헤더에 추가 된다.

> swaggerUI 사용법
> summary: 라우터에 대한 설명을 작성
> tags: 라우터를 태그로 분류 할 수 있음
> 함수 아래 multiline 주석: md 형식으로 라우터에 대한 docs를 정리할 수 있음.

```python
@app.get("/", summary="간단한 API",
		 tags=["Simple"]
)
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
```

## 실습 - Swagger UI 꾸미기

<명세>

- 루트 라우터
- DA 라우터
- DS 라우터
- DE 라우터
- 를 만들고 태그로 분류하고 마크다운 형식으로 문서를 정리하기
- 모든 라우터는 ALL 이라는 태그를 가집니다.
- Try it now -> execute 에 나와있는 Curl 예제코드로 쉘에서 request를 날려보기

# FastAPI Request
