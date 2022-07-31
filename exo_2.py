liste1=[1,3,6,7,8,8,0,8]
liste2=[1,5,7,8,9]
def cin(liste):
    som=0
    for i in liste:
        if i==liste[4]:
            som+=1 
            
        if len(liste)==8 and som==3:
            return True
    return False  
print(cin(liste1))
print(cin(liste2))