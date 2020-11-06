# rent_bike

The application is made for the needs of bike rental companies, and shows which bikes are available.


```
1. Run `docker-compose build`

2. override docker.compose.override, for example:

    ```services:

    python:
        volumes:
        - /home/dawid/Pulpit/rent_bike/rent_bike/backend:/backend

    react:
        volumes:
        - /home/dawid/Pulpit/rent_bike/rent_bike/frontend:/frontend
    ```

3. Run `docker-compose up`

4. Create database:
    a) login to python container:
    `docker-compose exec python bash`
    b) `python3 manage.py migrate`
```
