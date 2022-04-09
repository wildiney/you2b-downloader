FROM python:3.8-slim

WORKDIR /home/app_user

COPY requirements.txt . 

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install youtube-dl

COPY . . 

CMD ["python","app.py"]