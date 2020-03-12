FROM python:3.6

COPY ./backend /backend

WORKDIR /backend

RUN pip3 install -r requimentes.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]