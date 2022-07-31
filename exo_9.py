


def test(liste):
 return all([liste[i]!=liste[i+1] for i in range (len(liste)-1)])

print(test([1,2,3,4,8,9,1,1,3]))
print(test([1,5,8,5,8]))