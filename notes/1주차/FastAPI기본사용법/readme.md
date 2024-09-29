# FastAPI 기본 사용법

## 1. 프로젝트 디렉토리로 이동

FastAPI 프로젝트가 있는 디렉토리로 이동합니다. 예를 들어 `Welcome` 디렉토리로 이동합니다.

```shell
cd Welcome
```

## 2. FastAPI 서버 실행하기

FastAPI는 `uvicorn`을 사용하여 ASGI 서버를 실행합니다. 아래의 명령어로 FastAPI 애플리케이션을 실행합니다.

```shell
uvicorn main:app --port=8081 --reload
```

### 명령어 설명:

- `main:app`: `main.py` 파일에 있는 `app` 객체를 실행하겠다는 의미입니다.
- `--port=8081`: 서버가 실행될 포트 번호를 지정합니다. 기본적으로 FastAPI는 8000번 포트를 사용하지만, 여기서는 8081번 포트를 지정했습니다.
- `--reload`: 파일이 수정되면 서버를 자동으로 재시작해주는 옵션입니다. 개발 중에는 매우 편리한 기능입니다.

## 3. FastAPI 서버 접속

FastAPI 서버가 실행되면 브라우저에서 접속할 수 있습니다.

- 기본 라우터 (`/`)에 접속:

```
http://localhost:8081/
```

이 라우터는 FastAPI의 기본 `GET` 요청을 처리합니다.

## 4. Swagger UI와 Redoc

FastAPI는 API 문서를 자동으로 생성해주는 Swagger UI와 Redoc을 지원합니다.

- **Swagger UI**: API 문서와 테스트 인터페이스를 제공합니다. [Swagger UI](http://localhost:8081/docs)에서 API 엔드포인트를 확인하고 테스트할 수 있습니다.

```
http://localhost:8081/docs
```

- **Redoc**: 또 다른 형식의 API 문서를 제공합니다.

```
http://localhost:8081/redoc
```

브라우저에서 해당 URL을 입력하면, `GET` 요청을 통해 서버와 통신하며 필요한 정보를 받을 수 있습니다. 응답에는 상태 코드와 콘텐츠 타입 등의 헤더 정보도 포함됩니다.

---

## 5. Swagger UI 사용법

FastAPI에서는 API 문서를 작성할 때, 라우터에 설명을 추가할 수 있습니다. Swagger UI에서 라우터 설명과 태그를 사용할 수 있습니다.

### 예시:

```python
@app.get("/", summary="간단한 API", tags=["Simple"])
async def root():
    '''
    # 간단한 API 문서

    ## 설명

    이 API는 간단한 루트 API입니다.

    - **인자값1**은 ~~ 입니다.
    - **인자값2**는 @@ 입니다.
    '''
    return {"message": "Hello World"}
```

### 주요 속성 설명:

- **summary**: 라우터에 대한 간단한 설명을 작성합니다. Swagger UI에 표시됩니다.
- **tags**: 라우터를 태그로 분류하여, 여러 API를 그룹화할 수 있습니다.
- **주석을 사용한 문서화**: 함수 아래에 작성된 주석을 통해 마크다운 형식의 문서를 추가할 수 있습니다. 이 내용은 Swagger UI에 표시됩니다.

---

## 6. 실습 - Swagger UI 꾸미기

### 실습 목표

여러 라우터를 만들고, 태그로 분류한 뒤 마크다운 형식으로 문서를 정리합니다.

- 루트 라우터 (`/`)
- DA 라우터 (`/da`)
- DS 라우터 (`/ds`)
- DE 라우터 (`/de`)

모든 라우터는 "ALL"이라는 태그를 가지며, 추가적으로 각 라우터마다 고유의 태그를 가질 수 있습니다.

### 실행 후 Swagger UI 확인

1. 서버를 실행한 후 `http://localhost:8081/docs`에서 Swagger UI로 이동하여 API 명세를 확인합니다.
2. 각 라우터가 "ALL" 태그와 함께 분류되는 것을 확인할 수 있습니다.

### 실습: Curl을 사용한 요청

Swagger UI에서 제공하는 Curl 명령어를 사용하여 직접 서버에 요청을 보낼 수 있습니다. 예를 들어, `Try it out -> Execute`에서 나오는 Curl 명령어를 복사하여 터미널에서 실행해봅니다.

---
