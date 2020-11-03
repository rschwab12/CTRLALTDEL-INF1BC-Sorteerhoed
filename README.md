# Sorteerhoed
De sorteerhoed is een online vragenlijst/quiz die studenten van de Hogeschool Leiden helpt bij het kiezen van een specialisatie.  
Op basis van de gegeven antwoorden op de vragen zal de applicatie berekenen welke specialisatie het beste bij de student past.

Deze applicatie is gemaakt door de studenten van klas INF1BC/CTRL ALT DEL
## Benodigdheden
- Python 3.9.0
- De volgende modules
  ```sh
  $ pip3 install Flask
  $ pip3 install MySQL-connector
  ```
- Config.ini bestand (zie config.sample.ini)
- MySQL/MariaDB Server
- Sorteerhoed database

## Installatie

- Installeer de benodigde modules en de benodigde software
- Maak een database aan en importeer 1 van de 2 database bestanden (zie db map)
- Stel het configuratie bestand in met de juiste instellingen
- Controleer nog 1 keer of alles goed staat ingesteld.
- Start de applicatie met het onderstaande commando en surf in je browser naar http://127.0.0.1:5000/ om de applicatie te kunnnen gebruiken.

## Applicatie starten
```sh
python3 app.py
```