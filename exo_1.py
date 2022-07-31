liste=[19,45,93,19,5,5,5]
liste2=[24,637,78,14,15]
liste3=[19,5,19,5,5,5,4]
def rep(liste):
    som=som1=0
    for i in liste :
        if i==19:
           som+=1
        if i==5:
            som1+=1
                
        if som==2 and som1>=3:
             return True
        
    return False     
 
      
print(rep(liste))
print(rep(liste2))
print(rep(liste3))