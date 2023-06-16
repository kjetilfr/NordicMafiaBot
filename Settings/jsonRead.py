import json


def smallLoad():
    f = open('./Settings/settings.json')
    data = json.load(f)
    f.close()
    return data



def loadProfile():
    load = int(input("Last inn profil: (1 for å laste profil, 0 for å lage ny profil) "))

    if load == 1:
        f = open('./Settings/settings.json')

        data = json.load(f)

        f.close()
        return data
    else:
        Menytimer = input("Menytimer: (1 for ja, 0 for nei) ")
        Headless = input("Headless: (1 for ja, 0 for nei) (ANBEFALER 0, HAR ALDRI PRØVD 1 SÅ KAN VERE DU BLIR BANNED) ")

        Brukernavn = input("Brukernavn: ")
        Passord = input("Passord: ")

        Kriminalitet = input("Kriminalitet: (0 for ingen, 1 for gammel dame, 2 for spilleautomat, 3 for bensinstasjon, 4 for postbanke eller 5 for verditransport) ")
        Utpressing = input("Utpressing: (0 for tilfelding person, 1 for spesifikk person) ")
        if Utpressing == 1:
            UtpressingPerson = input("Dersom ja brukernavn på den som skal utpresses: ")
        Fightclub = input("Fightclub: (0 for ingen, 1 for 11 pullups, 2 for 5 benkpress eller 3 for 25 pushups) ")
        Biltyveri = input("Biltyveri: (0 for ingen, 1 for bil på gata, 2 for privat parkeringsplass, 3 for bilnøkler eller 4 for offentlig parkeringsplass) ")
        # Hasjplantasje = input("Hasjplantasje: (Sett til 0 kommer senere) ")
        # OrganisertKrim = input("Organisert Kriminalitet: (Sett til 0 kommer senere) ")

        LongTimeout = input("Skal botten ta ei lang pause?: (1 for ja, 0 for nei) ")
        LongTimeoutInHours = input("Dersom ja hvor lenge skal botten ta pause (i timer): ")
        LongTimeoutStart = input("Når klokkeslett skal botten ta pause (HH:MM:SS format): ")

        with open("./Settings/settings.json", "r+") as f:
            data = json.load(f)
            data['settings'][0]['Menytimer'] = int(Menytimer)
            data['settings'][0]['Headless'] = int(Headless)

            data['settings'][1]['Brukernavn'] = Brukernavn
            data['settings'][1]['Passord'] = Passord

            data['settings'][2]['Kriminalitet'] = int(Kriminalitet)
            data['settings'][2]['Utpressing'] = int(Utpressing)
            if Utpressing == 1:
                data['settings'][2]['UtpressingPerson'] = UtpressingPerson
            data['settings'][2]['Fightclub'] = int(Fightclub)
            data['settings'][2]['Biltyveri'] = int(Biltyveri)
            # data['settings'][2]['Hasjplantasje'] = int(Hasjplantasje)
            # data['settings'][2]['Organisert Kriminalitet'] = int(OrganisertKrim)

            data['settings'][3]['LongTimeout'] = int(LongTimeout)
            data['settings'][3]['LongTimeoutTimerInHours'] = int(LongTimeoutInHours)
            data['settings'][3]['LongTimeoutTimerStart'] = LongTimeoutStart

            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            f.close()
            # reopen file
            f = open('./Settings/settings.json')

            data = json.load(f)
            f.close()
            return data
