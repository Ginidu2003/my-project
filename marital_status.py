Name = input('Enter your name: ') 
Gender = input('Male or Female: ') 
Martial = input('Married or Single: ') 
if Gender == 'Female': 
  if Martial == 'Married':
      print('Mrs. ' + Name)
  else:
      print('Miss ' + Name)
else: 
      print('Mr. ' + Name)

