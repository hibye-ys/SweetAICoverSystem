
FROM python:3.10


WORKDIR /usr/src/app


COPY ./requirements.txt ./requirements.txt


RUN pip install -r requirements.txt

RUN apt update && apt install -y ffmpeg

COPY . .


ENTRYPOINT [ "python", "vc_inference_server.py" ]
