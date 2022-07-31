print("Entrez des chaines de caractères:")
a=str(input())
def seperate(liste):
    liste=list(liste)
    for i in liste:
        del i
    return liste
print(seperate(a))