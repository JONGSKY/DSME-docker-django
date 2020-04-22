# docker 실행 방법


#### docker build
```
docker build [OPTIONS] PATH | URL | -
```
- docker build시 -t 옵션을 이용하면 name 설정이 가능
```
docker build -t system .
```

#### docker run
```
docker run [OPTIONS] IMAGE[:TAG|@DIGEST] [COMMAND] [ARG...]
```
- docker 실행시 8000번 포트를 열어두었기 때문에 -p 8000:8000 옵션 넣어줌
```
docker run -d -p 8000:8000 --name system jongsky/system:latest
```
