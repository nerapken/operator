FROM python:3.7.12-alpine3.15
COPY . /opt
RUN pip install -r /opt/requirements.txt
WORKDIR /opt
CMD "python" "api/main.py"
