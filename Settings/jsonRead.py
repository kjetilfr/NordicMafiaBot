import json

profileLoaded = ""


def smallLoad():
    f = open('./Settings/settings.json')
    data = json.load(f)
    f.close()
    return data[profileLoaded]


def loadProfile():
    load = int(input("Last inn profil: (1 for å laste profil, 0 for å lage ny/edit profil): "))
    global profileLoaded
    if load == 1:
        #load profile
        f = open('./Settings/settings.json')

        data = json.load(f)
        for item in data:
            print(item)
        f.close()
        profile = input("Select profile: ")
        profileLoaded = profile

        return data[profile]
    else:
        f = open('./Settings/settings.json')
        data = json.load(f)
        for item in data:
            print(item)
        f.close()
        # new profile
        profileName = input("Profile Name: ")
        profileLoaded = profileName

        Menytimer = input("Menytimer: (1 for ja, 0 for nei) ")
        Headless = input("Headless: (1 for ja, 0 for nei) (ANBEFALER 0, HAR ALDRI PRØVD 1 SÅ KAN VERE DU BLIR BANNED): ")
        Proxy = int(input("Use Proxy: 1 for ja 0 for nei: "))
        if Proxy == 1:
            ProxyIP = input("IP address of proxy (HTTP eller HTTPS proxy IKKJE bruk SOCKS4/5): ")
            ProxyPort = input("Port for proxy: ")

        Brukernavn = input("Brukernavn: ")
        Passord = input("Passord: ")

        Kriminalitet = input("Kriminalitet: (0 for ingen, 1 for gammel dame, 2 for spilleautomat, 3 for bensinstasjon, 4 for postbanke eller 5 for verditransport): ")
        Utpressing = int(input("Utpressing: (0 for tilfelding person, 1 for spesifikk person): "))
        if Utpressing == 1:
            UtpressingPerson = input("Dersom ja brukernavn på den som skal utpresses: ")
        Fightclub = input("Fightclub: (0 for ingen, 1 for 11 pullups, 2 for 5 benkpress eller 3 for 25 pushups): ")
        Fightclub_fight = input("Legge ut fight? (0 for nei, 1 for ja: ")
        if Fightclub_fight == 1:
            Fightclub_belop = input("Belop for fightclub fight (minimum 100 kr): ")
        Biltyveri = input("Biltyveri: (0 for ingen, 1 for bil på gata, 2 for privat parkeringsplass, 3 for bilnøkler eller 4 for offentlig parkeringsplass): ")
        Fengsel = input("Bryte ut folk fra fengsel: (1 for ja, 0 for nei) ")
        Hasjplantasje = input("Hasjplantasje: (1 for å invistere i hasj, 0 for å sette penger i banken): ")
        OrganisertKrim = input("Organisert Kriminalitet: (1 for ja, 0 for nei): ")
        CDG = input("CDG: (1 for ja, 0 for nei): ")
        Livvakt = input("Livvakt utleiie: (1 for ja, 0 for nei): ")
        if CDG == 1:
            CDGPerson = input("Brukernavn på den som skal utpresses: ")
            Gangsters = input("Gangsters på den som skal sendes: ")
        Filmproduksjon = input("Filmproduksjon: (1 for ja, 0 for nei) (DU MÅ MINST HA 40 MILLIONER FOR Å LAGE FILM): ")

        LongTimeout = input("Skal botten ta ei lang pause?: (1 for ja, 0 for nei): ")
        LongTimeoutInHours = input("Dersom ja hvor lenge skal botten ta pause (i timer): ")
        LongTimeoutStart = input("Når klokkeslett skal botten ta pause (HH:MM:SS format): ")

        with open("./Settings/settings.json", "r+") as f:
            data = json.load(f)
            #data  = profileName
            data[profileName][0]['Proxy'] = Proxy
            if Proxy == 1:
                data[profileName][0]['ProxyIP'] = ProxyIP
                data[profileName][0]['ProxyPort'] = ProxyPort
            else:
                data[profileName][0]['ProxyIP'] = "NaN"
                data[profileName][0]['ProxyPort'] = "NaN"
            data[profileName][0]['Menytimer'] = int(Menytimer)
            data[profileName][0]['Headless'] = int(Headless)

            data[profileName][1]['Brukernavn'] = Brukernavn
            data[profileName][1]['Passord'] = Passord

            data[profileName][2]['Kriminalitet'] = int(Kriminalitet)
            data[profileName][2]['Utpressing'] = int(Utpressing)
            if Utpressing == 1:
                data[profileName][2]['UtpressingPerson'] = UtpressingPerson
            data[profileName][2]['Fightclub'] = int(Fightclub)
            data[profileName][2]['Fightclub_fight'] = int(Fightclub_fight)
            data[profileName][2]['Fightclub_belop'] = int(Fightclub_belop)
            data[profileName][2]['Biltyveri'] = int(Biltyveri)
            data[profileName][2]['Fengsel'] = int(Fengsel)
            data[profileName][2]['Hasjplantasje'] = int(Hasjplantasje)
            data[profileName][2]['Livvakt'] = int(Livvakt)
            data[profileName][2]['Organisert Kriminalitet'] = int(OrganisertKrim)
            data[profileName][2]['Filmproduksjon'] = int(Filmproduksjon)
            if CDG == 1:
                data[profileName][2]['CDG'] = int(CDG)
                data[profileName][2]['CDGPerson'] = CDGPerson
                data[profileName][2]['Gangstere'] = Gangsters

            data[profileName][3]['LongTimeout'] = int(LongTimeout)
            data[profileName][3]['LongTimeoutTimerInHours'] = int(LongTimeoutInHours)
            data[profileName][3]['LongTimeoutTimerStart'] = LongTimeoutStart

            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            f.close()
        # reopen file
        f = open('./Settings/settings.json')

        data = json.load(f)
        f.close()
        return data[profileName]
