import poggyasz1


print("III/A,B")
csomag_lista=poggyasz1.fajlbeolvasas()
print(f"\tA poggyászok száma: {len(csomag_lista)}")
# az elso csomag szelessege???
# print(f"Az első csomag szélessége: {csomag_lista[0].a}") # azert a mert a Csomag.py ban az "a" jelenti a szelesseget

print("III/C")
atlag = poggyasz1.poggyasz_atlagsuly(csomag_lista)
print(f"\t Az 51 cm-es poggyászok átlag súlya: {round(atlag)} g")

max_index= poggyasz1.legmagasabb_poggyasz(csomag_lista)
print(f"\t A legmagasabb poggyász meretei: {csomag_lista[max_index].a}x{csomag_lista[max_index].b}x{csomag_lista[max_index].c}x{csomag_lista[max_index].m}")