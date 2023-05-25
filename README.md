# HobbyHub

[ ]권준혁\
[x]김신혜\
[ ]최충현\
[ ]추연선\
[X]임지혜

## local 개발 환경 setting

1. 가상환경 설정

```
# 가상환경 생성 및 접속
$ python -m venv venv
$ source . venv/bin/activate

# 설치항목
$ pip install -r requirements.txt

# 커밋 메세지 템플릿 설정
$ git config --global commit.template ./.github/.gitmessage.txt
```

2. 브랜치 설정

```
# main 브랜치에서 분깃
$ git checkout -b develop
$ git checkout -b feature/{생성할 브랜치 이름} develop

# 브랜치 구분
main : 배포용 [merge 금지]
develop : 개발용
hotfix : 버그 혹은 오류 수정용
```

3. 커밋

```
# 커밋 메세지 입력
git add { 내가 수정하고 커밋할 내용만 }
git commit

```
