ukoly = []

def hlavni_menu():
    while True:
        print("\nSprávce úkolů – Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        
        volba = input("Vyberte možnost (1-4): ")

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Konec programu.")
            break
        else:
            print(f"{volba} je neplatná volba. Zkuste to prosím znovu.")

def pridat_ukol():
    while True:
        nazev = input("Zadejte název úkolu: ").strip()
        if not nazev:
            print("Název úkolu nesmí být prázdný. Zkuste to znovu.")
            continue

        popis = input("Zadejte popis úkolu: ").strip()
        if not popis:
            print("Popis úkolu nesmí být prázdný. Zkuste to znovu.")
            continue

        ukoly.append({"nazev": nazev, "popis": popis})
        print("Úkol byl úspěšně přidán.")
        break

def zobrazit_ukoly():
    if not ukoly:
        print("Žádné úkoly nejsou uloženy.")
    else:
        print("\nSeznam úkolů:")
        for index, ukol in enumerate(ukoly, start=1):
            print(f"{index}. {ukol['nazev']} – {ukol['popis']}")

def odstranit_ukol():
    if not ukoly:
        print("Nejsou žádné úkoly k odstranění.")
        return

    zobrazit_ukoly()
    
    try:
        volba = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
        if 1 <= volba <= len(ukoly):
            odstraneny = ukoly.pop(volba - 1)
            print(f"Úkol '{odstraneny['nazev']}' byl odstraněn.")
        else:
            print("Neplatné číslo úkolu. Zkuste to znovu.")
    except ValueError:
        print("Zadejte platné číslo.")

# Spuštění hlavního menu
hlavni_menu()
