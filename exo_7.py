def fid(liste):
    
    if len(liste)==sum(liste):
        return True
    else:
        return False
        
print(fid([1,1,1,1,1,1,1,1]))