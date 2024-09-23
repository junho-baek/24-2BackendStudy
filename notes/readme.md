## 가상환경 설정

> 참고 강의에서는 conda를 사용하지만, numpy 같은 툴은 be 공부에 굳이 필요 없으므로 pipenv로 파이썬 버전 설정과 패키지 관리함

```shell
pip install pipenv #설치 안되어 있으면 설치하기
pipenv --python 3.10 #통일된 fast api BE 환경을 위해서 파이썬 버전 3.10을 사용
```

#### 가상환경 실행 / 종료

```shell
# Run shell 가상환경 쉘을 만드는 방법
pipenv shell

# Rum custom commands 가상환경을 이용해서 커맨드를 실행만하고, 쉘은 활성화하지 않음.
pipenv run COMMANDS...


exit # 가상환경 종료
```
