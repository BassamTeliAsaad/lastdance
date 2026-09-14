#SZÁMLAKEZELÉS

#GLOBAL VALTOZOK
egyenleg=0
pin=1234
hasznalatidij=1000
adatfajl="szamla.txt"
jogosult=False


#MŰKÖDÉS
hibasbelepes=2

pk=int(input("Kérem adja meg a PIN kódot: "))
if pk==pin:
        jogosult=True
        print("Jogosultság ellenőrzése sikeres.")

while(jogosult==False and hibasbelepes>0):
    pk=int(input("Kérem adja meg a PIN kódot: "))
    print("Jogosultság ellenőrzése sikertelen.")

    hibasbelepes-=1
    if pk==pin:
        jogosult=True
        print("Jogosultság ellenőrzése sikeres.")

if not jogosult:
    print("Túl sok hibás próbálkozás.") 

# funkciovalaszto menu
cim = "\nSZAMLAKEZELO PROGRAM\n==========================\n"
menu = [
    "1. Egyenleg lekérdezése",
    "2. Pénz kivétel/átutalás",
    "3. Pénz betét",
    "---------------",
    "4. Tranzakciótörténet",
    "9. Kilépés"
]

menupontok = [1,2,3,4,9]
print(cim)
for me in menu:
    print(f"{me}\n")

valasztas = int(input("Valassz tevekenyseget: "))


while valasztas not in menupontok:
    print(f"\nÉrvénytelen választás. ")
    print(cim)
    for me in menu:
        print(f"{me}\n")
    valasztas = int(input("Kérlek válassz újra: "))

if valasztas == 1:
     egyenleg()
elif valasztas == 2:
     utalas()
elif valasztas == 3:
     pass
elif valasztas == 4:
     pass
elif valasztas == 9:
     exit()

def egyenleg():
     print(f"Az egyenleged: {egyenleg} Ft")

def utalas(utalas_osszeg):
     print(f"Pénz átutalás: {utalas_osszeg} Ft")

def penzbetet(betet_osszeg):
     print(f"Pénz betét: {betet_osszeg} Ft")

#Összes tranzakció
def tortenet():
     print("Tranzakciótörténet: ")