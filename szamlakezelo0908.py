# SZAMLAKEZELES

# GLOBAL VALTOZOK
egyenleg=0                  # Kezdeti egyenleg
pin=1234                    # Helyes PIN kod
hasznalatidij=1000         # Hasznalati dij
adatfajl="szamla.txt"      # Adatfajl neve
jogosult=False             # Alapbol nincs jogosultsag


# MUKODES
hibasbelepes=2             # Hibas probalkozasok szama

# PIN bekerese
pk=int(input("Kerem adja meg a PIN kodot: "))

# Ellenorzi hogy helyes-e a PIN
if pk==pin:
        jogosult=True
        print("Jogosultsag ellenorzese sikeres.")

# Addig ker PIN-t amig nincs jogosultsag
# es van meg hibas probalkozas
while(jogosult==False and hibasbelepes>0):

    # PIN ujboli bekerese
    pk=int(input("Kerem adja meg a PIN kodot: "))

    print("Jogosultsag ellenorzese sikertelen.")

    # Csokkenti a probalkozasok szamat
    hibasbelepes-=1

    # Ellenorzi hogy most helyes-e a PIN
    if pk==pin:
        jogosult=True
        print("Jogosultsag ellenorzese sikeres.")

# Ha nem sikerult a belepes
if not jogosult:
    print("Tul sok hibas probalkozas.")


# FUNKCIOVALASZTO MENU

# Menu cime
cim = "\nSZAMLAKEZELO PROGRAM\n==========================\n"

# Menu pontok
menu = [
    "1. Egyenleg lekerdezese",
    "2. Penzi kivetel/atutalas",
    "3. Penz betet",
    "---------------",
    "4. Tranzakciotortenet",
    "9. Kilepes"
]

# Ervenyes menupontok
menupontok = [1,2,3,4,9]

# Menu kiirasa
print(cim)

# Vegigmegy a menu lista elemein
for me in menu:
    print(f"{me}\n")

# Bekeri a menupontot
valasztas = int(input("Valassz tevekenyseget: "))


# Addig ker uj valasztast amig ervenytelen
while valasztas not in menupontok:

    print(f"\nErvenytelen valasztas. ")

    # Menu ujboli kiirasa
    print(cim)
    for me in menu:
        print(f"{me}\n")

    # Uj valasztas bekerese
    valasztas = int(input("Kerlek valassz ujra: "))


# A valasztott menupont vegrehajtasa

if valasztas == 1:
     # Egyenleg lekerdezese
     egyenleg()

elif valasztas == 2:
     # Penz atutalasa
     utalas()

elif valasztas == 3:
     # Penz betet
     pass

elif valasztas == 4:
     # Tranzakciotortenet
     pass

elif valasztas == 9:
     # Program kilepes
     exit()


# FUGGVENYEK

# Egyenleg lekerdezese
def egyenleg():

     # Kiirja az aktualis egyenleget
     print(f"Az egyenleged: {egyenleg} Ft")


# Penz atutalasa
def utalas(utalas_osszeg):

     # Kiirja az atutalt osszeget
     print(f"Penz atutalas: {utalas_osszeg} Ft")


# Penz befizetese
def penzbetet(betet_osszeg):

     # Kiirja a befizetett osszeget
     print(f"Penz betet: {betet_osszeg} Ft")


# OSSZES TRANZAKCIO

# Tranzakciotortenet megjelenitese
def tortenet():

     # Tranzakciotortenet kiirasa
     print("Tranzakciotortenet: ")