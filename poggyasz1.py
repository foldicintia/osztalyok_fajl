from Csomag import Csomag

def fajlbeolvasas():
    
    fajl=open("csomag.txt","r",encoding="UTF-8") # fajl megnyitas
    
    fajl.readline() # egy sort beolvas, ha nem mentjuk el valtozoba -> rogton el is dobtuk
    fajlbol_sorok_lista=fajl.readlines() # egyszerre olvassa az osszes sort, taroljuk a sorait egy str listaba
    
    fajl.close
    
    """
    1. MEGNYITOM A FAJLT OLVASASRA # fajl=open()
    2. BEOLVASOM A FEJLEC SORT, HA VAN # .readline()
    3. BEOOLVASOM AZ OSSZES SORT EGY LISTABA - str lista
    4. BEZAROM A FAJLT # fajl.close
    5. A SOROKAT ATALAKITOM OBJEKTUMOKKA -- SZETSZEDEM A BENNE LEVO ADATOKAT
        5/1. LETREHOZOM AZ OSZTALYT AMIBEN BEOLVASOM AZ ADATOKAT
        5/2.VEGIEGMEGYEK A LISTAN, ES MINDEN SORAT FELDOLGOZOM
            5/2/1. ELTUNTETEM A VEGEROL AZ ENTERT
            5/2/2. SZETVAGOM A SZEPARATOROK MENTEN
    """
    csomag_lista=[] # itt taroljuk az elkeszult csomag objektumainkat
    for i in range(0,len(fajlbol_sorok_lista),1):
        akt_elem=fajlbol_sorok_lista[i]
        sor_lista=akt_elem.strip().split("#")   # .strip() - tobbszoros szokozt tavolit el (az elejerol meg a vegerol) 
                                                # .split() - az elválasztójel mentén ("#") szetvalasztja az 
        a=int(sor_lista[0])
        b=int(sor_lista[1])
        c=int(sor_lista[2])
        m=int(sor_lista[3])
        csomag = Csomag(a,b,c,m)
        csomag_lista.append(csomag)

    return csomag_lista

def poggyasz_atlagsuly(lista):
    """C.	Határozza meg és írassa ki a konzolra a minta szerint, hogy mennyi az 51 cm széles pogyászok átlag súlya gramban. (1kg = 1000g) (4p)"""
    osszeg:int = 0
    db:int = 0 
    for i in range(0, len(lista),1):  # osszegzes tetele
        if lista[i].a == 51: 
            osszeg+=lista[i].m
            db+=1

    return 1000*osszeg/db # grammban keri az atlagot ezert szorozzuk be 1000-rel

def legmagasabb_poggyasz(lista):
    for i in range(0, len(lista), 1):
        max_ertek= 0
        max_index= 0   # azert kell az iindex mert minden adatara stzuksegunk lesz
        if max_ertek < lista[i].b:
            max_ertek = lista[i].b
            max_index = i

    return max_index