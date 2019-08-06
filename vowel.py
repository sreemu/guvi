n=str(input())
list=['a','e','i','o','u']
symbol=['!','@','#','$','%']
if n in list:
   print('Vowel')
elif n in symbol:
    print('Invalid')
elif n is not list:
    print('Consonant')
    
