# rent_bike
# rent_bike

1. Run `docker-compose build`

1. override docker.compose.override, for example:

    ```services:

    python:
        volumes:
        - /home/dawid/Pulpit/rent_bike/rent_bike/backend:/backend

    react:
        volumes:
        - /home/dawid/Pulpit/rent_bike/rent_bike/frontend:/frontend
    ```

1. Run `docker-compose up`

1. Create database:
    1. login to python container:
    `docker-compose exec python bash`
    1. `python3 manage.py migrate`

