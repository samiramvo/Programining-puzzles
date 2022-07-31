def palindrome(liste):
  return[mot==mot[::-1] for mot in liste]
 

print(palindrome(["palindrome","madamimadam","foo","eyes"]))