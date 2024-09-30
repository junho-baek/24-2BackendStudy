## path parameter

```python
from fastapi import FastAPI, Path
from enum import Enum

app = FastAPI()

# Enum 설정
class TeamEnum(str, Enum):
    ds = "ds"
    da = "da"
    de = "de"

# 1. ybigta/{team} 라우터
@app.get("/ybigta/{team}", summary="팀 정보 조회", tags=["Team"])
async def get_team_info(team: TeamEnum):
    return {"team": team.value, "message": f"{team.value.upper()} 팀의 정보를 반환합니다."}

# 2. DA 팀 크롤링 이미지 조회


# 모든 이미지 조회
@app.get("/ybigta/da/crawling/imgs/all", summary="모든 이미지 조회", tags=["DA"])
async def get_all_images():
    return {"message": "All images have been fetched."}

# ID로 이미지 조회
@app.get("/ybigta/da/crawling/imgs/{id}", summary="이미지 조회", tags=["DA"])
async def get_image_by_id(id: int = Path(..., title="이미지 ID", ge=1, le=4000)):
    return {"message": f"Image {id}"}


```

## query parameter

---

### 실습 코드:

```python
from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

# 팀별 프로젝트 데이터 (팀 이름: {연도: [프로젝트 목록]})
project_data = {
    "ds": {2023: ["DS Project 1", "DS Project 2"], 2024: ["DS Project 3"]},
    "da": {2023: ["DA Project 1"], 2024: ["DA Project 2", "DA Project 3"]},
    "de": {2023: ["DE Project 1", "DE Project 2"], 2024: ["DE Project 3"]}
}

@app.get("/projects/")
async def get_projects(team: str, year: Optional[int] = None):
    # 팀 이름이 데이터에 없으면 에러 메시지 반환
    if team not in project_data:
        return {"error": "Team not found"}

    # 연도를 제공하면 해당 팀의 해당 연도 프로젝트만 반환
    if year:
        projects = project_data[team].get(year, [])
        return {f"{team} 팀 {year}년 프로젝트": projects}

    # 연도가 제공되지 않으면 해당 팀의 모든 프로젝트 반환
    all_projects = []
    for y, projects in project_data[team].items():
        all_projects.extend(projects)

    return {f"{team} 팀의 모든 프로젝트": all_projects}
```

---

#### 실습 목표:

- **쿼리 파라미터**를 통해 팀 이름과 연도를 전달하는 방법을 연습합니다.
- **Optional 파라미터**를 사용하여 선택적으로 연도를 입력받고, 연도가 주어지지 않으면 전체 프로젝트를 반환하는 로직을 구현합니다.

#### 테스트 예시:

1. **전체 프로젝트 조회**:

   ```
   GET /projects/?team=ds
   ```

   결과:

   ```json
   {
     "ds 팀의 모든 프로젝트": ["DS Project 1", "DS Project 2", "DS Project 3"]
   }
   ```

2. **특정 연도 프로젝트 조회**:

   ```
   GET /projects/?team=da&year=2024
   ```

   결과:

   ```json
   {
     "da 팀 2024년 프로젝트": ["DA Project 2", "DA Project 3"]
   }
   ```
