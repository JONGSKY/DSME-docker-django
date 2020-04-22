# DSME 선주교신 docker-django

### Environment 
- Ubuntu OS라고 가정한다.

### 해당 github를 docker로 실행시키는 방법
1. docker 설치하기 (root 권한을 준뒤에 스크립트로 설치)
```
curl -fsSL https://get.docker.com/ | sudo sh
```
2. docker sudo 없이 사용하기
```
sudo usermod -aG docker $USER # 현재 접속중인 사용자에게 권한주기
sudo usermod -aG docker your-user # your-user 사용자에게 권한주기
```
3. docker 설치후 버전 확인하기
```
docker version
```
4. 설치를 완료했다면 dockerhub에서 image 가져와서 실행시키기
```
docker run -d -p 8000:8000 --name system ljhljh0125/system:latest
```
5. 실행완료 후 http://127.0.0.1:8000/ 잘 실행되는지 확인하기 

