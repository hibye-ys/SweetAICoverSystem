# Python 이미지 사용
FROM python:3.10

# 작업 디렉토리 설정
WORKDIR /usr/src/app

# 현재 디렉토리의 내용을 이미지로 복사
COPY ./requirements.txt ./requirements.txt

# 필요한 라이브러리 설치
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y ffmpeg

COPY . .

# FastAPI 애플리케이션 실행
ENTRYPOINT ["python", "run_server.py"]
