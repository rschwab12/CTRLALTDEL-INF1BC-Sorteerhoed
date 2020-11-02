def get_promotekst(specialisatie):
    # Retrieve promotion text for final result
    if specialisatie == "fict":
        return 'Jij bent analytisch, doelgericht en vasthoudend. Je houdt van rechercheren en onderzoeken en voelt je verantwoordelijk voor het bevorderen van een veilige maatschappij en het verminderen van criminaliteit. Je bent innovatief en nieuwsgierig naar de nieuwste technologieën en de mogelijkheden die ze bieden.<br> Je kunt goed omgaan met mensen en weet ze naar waarde in te schatten. Je hebt er plezier in om slimme wegen te vinden die leiden naar oplossingen voor ingewikkelde zaken.<br> Met Forensisch ICT heb je carrièrekansen bij politie, justitie, defensie maar ook in de particuliere markt! <br><br>Meer weten over Forensisch ICT? <a href="https://www.hsleiden.nl/informatica/opbouw-studie/forensisch-ict.html" target="_blank"><b>Klik hier!</b></a>'
    elif specialisatie == "bdm":
        return 'Jij bent nieuwsgierig en analytisch ingesteld. Je bent niet bang om veel met data te werken, sterker nog, jij haalt hier je plezier uit! Je bent een data-tovenaar, van modelleren tot analyseren en adviseren, met data krijg jij alles voor elkaar. Je vindt het leuk om onderzoek te doen en gaat werken met Artificial Intelligence.<br> Jouw kennis en vaardigheden helpen bedrijven te verbeteren en optimaliseren.<br> Met Business Data Management kan je bijvoorbeeld aan de slag als data-analist of als Business Intelligence consultant. <br><br>Meer weten over Business Data Management? <a href="https://www.hsleiden.nl/informatica/opbouw-studie/business-data-management.html" target="_blank"><b>Klik hier!</b></a>'
    elif specialisatie == "iat":
        return 'Jij bent creatief en hebt geen vrees voor technologie. Je bent nieuwsgierig naar de nieuwste ontwikkelingen in technologie, social media en mogelijkheden van gebruikersinteractie.<br> Je bent kritisch en kan je goed verplaatsen in gebruikers.<br> Je kunt goed luisteren naar de wensen en belangen van verschillende partijen en samenwerken in multidisciplinaire teams.<br> Met Interactie Technologie kan je aan de slag als bijvoorbeeld Interaction designer of als Desktoppublisher.<br><br>Meer weten over Interactie Technologie? <a href="https://www.hsleiden.nl/informatica/opbouw-studie/interactie-technologie.html" target="_blank"><b>Klik hier!</b></a>'
    elif specialisatie == "se":
        return 'Jij hebt een sterk analytisch vermogen. Je bent creatief en ontwerpt en programmeert graag. Je hebt er plezier in om slimme oplossingen voor ingewikkelde problemen te bedenken.<br> Je beschikt over de nodige sociale vaardigheden om samen met anderen te bedenken welk product het beste past bij de wensen van een bedrijf of instelling.<br> Met Software Engineering kan je aan de slag als bijvoorbeeld Software Engineer, Back-end developer, Front-end developer, Technical Designer of als Database Engineer. <br><br>Meer weten over Software Engineering? <a href="https://www.hsleiden.nl/informatica/opbouw-studie/software-engineering.html" target="_blank"><b>Klik hier!</b></a>'

def get_specialisatie_naam(afkorting):
    # Retrieve full name of specialisation
    if afkorting == "fict":
        return "Forensisch ICT"
    elif afkorting == "bdm":
        return "Business Data Management"
    elif afkorting == "iat":
        return "Interactie Technologie"
    elif afkorting == "se":
        return "Software Engineering"
