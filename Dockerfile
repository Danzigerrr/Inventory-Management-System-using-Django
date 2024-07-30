FROM python:3.11

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . code
WORKDIR /code

ENTRYPOINT [ "python", "./manage.py" ]
CMD [ "runserver", "0.0.0.0:8000" ]