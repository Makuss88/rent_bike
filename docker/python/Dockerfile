FROM python

COPY ./rent_bike /rent_bike

WORKDIR /rent_bike

RUN pip3 install -r requimentes.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]