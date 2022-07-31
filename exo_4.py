print("Entrez le nombre de tas de pierre:")
n=int(input())
def tas(n):
   liste=[n+2*i for i in range(n)]
   return liste
print(tas(n))    
