# Sorteerhoed
Sorteerhoed opdracht voor school
Website URL: https://ctrl.alt-del.nl/  
Sorteerhoed URL: http://sorteerhoed.ctrl.alt-del.nl/  
Hogeschool Leiden Informatica URL: https://www.hsleiden.nl/informatica  

## Installatie flask
Flask voor python installeren: (Windows / macOS)
- https://flask.palletsprojects.com/en/1.1.x/installation/#installation
- ```sh
  $ pip3 install Flask
  ```

## Configuratie
- Maak een bestand in de applicatie folder aan met de naam config.ini
- In dit plak je de volgende content:
    ```ini
    [MYSQL]
    host = {database-host}
    port = {database-port}
    username = {database-username}
    password = {database-password}
    database = {database-database}
    ```
- Pas de velden die {} bevatten aan naar de daadwerkelijke database gegevens
    - Voorbeeld: ```host = {database-host}```
    - Word dus: ```host = localhost```

## Flask op webserver (ubuntu)
- https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04
- https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-18-04
