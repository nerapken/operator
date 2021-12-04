FROM python:3.9.9-alpine3.15
COPY . /opt
RUN . /opt/bin/activate && pip install -r /opt/requirements.txt
WORKDIR /opt
CMD . /opt/bin/activate && python api/main.py
