FastAPI의 Request Parameter 다루기

Path parameter

- /example/{id}
- 순서에 유의

Query parameter

- example/job?id=3&pageIndex=1&sort=ascending
- ? 뒤는 모두 변수.

Request Body

- json 으로 보냄
- pydantic(데이터 수록, 변환 검증)

Form

- web 에서 보냄
- pydantic(데이터 수록, 변환 검증)

## Path parameter 실습

**요구 사항:**

1. ybigta/{team} **라우터**를 생성하시오.

• team은 ds, da, de라는 세 가지 문자열을 **Enum**으로 매핑하여 처리합니다.

2. **DA 팀이 크롤링한 4000개의 이미지**를 다음 경로에 저장합니다: ybigta/da/crawling/imgs/{id}

• id는 int 타입의 값이며, 해당 ID로 이미지를 요청할 수 있도록 라우팅합니다.

**조건:**

1. ybigta/da/crawling/imgs/{id} **라우터**에서 id를 받아 해당 이미지를 f 문자열 포맷으로 반환합니다. 예를 들어, /imgs/1로 요청 시 "Image 1"과 같은 형식으로 반환됩니다.

2. ybigta/da/crawling/imgs/all **라우터**에서 모든 이미지를 조회할 수 있는 기능을 구현합니다.

3. 라우터의 순서와 구현 방식을 고려하여 작성하세요.

## Query parameter 실습

### 실습 문제: Ybigta 팀의 프로젝트와 연도 검색 (Query Parameter 실습)

#### 문제 설명:

Ybigta의 팀에 속한 프로젝트 정보를 조회하는 API를 만드세요. 팀 이름과 연도를 **쿼리 파라미터**로 받아, 해당 팀에서 특정 연도에 진행한 프로젝트 목록을 반환하는 기능을 구현합니다.

#### 요구 사항:

1. **`/projects/` 라우터를 만드세요.**

- 팀 이름은 `ds`, `da`, `de` 중 하나를 **쿼리 파라미터**로 받습니다.

- 연도는 선택적인 **쿼리 파라미터**로 받고, 해당 팀이 그 해에 진행한 프로젝트 목록을 반환합니다.

- 연도가 제공되지 않으면, 해당 팀의 모든 프로젝트 목록을 반환합니다.

2. 데이터는 다음과 같은 형식의 **딕셔너리** 자료 구조로 제공됩니다:

```python

project_data = {

"ds": {2023: ["DS Project 1", "DS Project 2"], 2024: ["DS Project 3"]},

"da": {2023: ["DA Project 1"], 2024: ["DA Project 2", "DA Project 3"]},

"de": {2023: ["DE Project 1", "DE Project 2"], 2024: ["DE Project 3"]}

}

```

3. **쿼리 파라미터**:

- 팀 이름: `team` (필수)

- 연도: `year` (선택)

#### 예시:

1. **전체 프로젝트 조회**:

```

GET /projects/?team=ds

```

- 응답: `["DS Project 1", "DS Project 2", "DS Project 3"]`

2. **특정 연도 프로젝트 조회**:

```

GET /projects/?team=da&year=2023

```

- 응답: `["DA Project 1"]`
