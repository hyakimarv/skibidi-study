#načtení od uživatele a typování
input("Sem zadas na e se chces zeptat")#A díky tomuhle načteš od uživatele
#Přetipování: podle toho co uživatel načítá
#pokud číslo: 
int(input("Zadejte cislo"))
#pokud string:
str(input("sem zadejte slova nebo věty"))
#pokud číslo s des. místem
float(input("Zadejte cislo"))

#if, elif a else
nalada=input("Jak se mas")
if nalada=="dobre":#if je pokud chci vedet konkretni vec jestli je zapsana v naladě
    print("To je skvele")
elif nalada=="mid":
    print("Aspon ze ne spatne")#elif  je neco mezi else a if muze porovnavat vic veci nez if 
else:
    print("snad se to zlepsi")#else je pokud se v proměné nevyskytuje ani jeden input z if a elif
#logicke operatory and, or, not
kocka="modra"
if kocka=="zelena" and "modra": # pri and kocka by musela mit obe barvy aby to bylo true
    print("kocka je modra a zelená")
if kocka=="zelena" or "modra":# pri or stačí jedna z podmínek
    print("kocka je bud modra nebo zelena")
if kocka==(not"zelena"):#not je opak podminky 
    print("kocka neni zelena")
    #jidloooooooooooo