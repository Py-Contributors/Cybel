FROM python:3.9
LABEL maintainer="deepak008@live.com"
copy . .
workdir .
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]