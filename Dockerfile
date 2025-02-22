FROM python:3.11-alpine

RUN addgroup -S -g 1337 alarm && adduser -S -u 1337 alarm -G alarm

USER alarm:alarm

WORKDIR /alarm_app

COPY --chown=alarm:alarm . /alarm_app

RUN pip install --no-cache-dir -r requirements.txt

ENV ENV=PROD

CMD ["python", "alarm.py"]
