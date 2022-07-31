def chaine_isolé(liste):
    liste1=[]
    for i in liste:
        for j in i:
            if j==' ':
               liste1.append(True)

        liste1.append(False)
    return liste1        
    
liste1=['cat','car','fear','center']
liste2=['ca t','car','fea r','cente r']

print(chaine_isolé(liste1))
print(chaine_isolé(liste2))