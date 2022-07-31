def list_cht(liste):
    numb=[]
    for i in range(len(liste)):
        if liste[i]<liste[i-1]:
            numb.append(i)
    return numb

num=[6,5,4,3,2,1]
num1=[1,19,5,15,5,25,5]
print(list_cht(num))
print(list_cht(num1))