liste=[1,3,8,9,(1,4)]
liste1=[2,8,"SA",5,8]
def tr_ind(liste):
    return [liste.index(i) for i in liste]
print(tr_ind(liste))
print(tr_ind(liste1))