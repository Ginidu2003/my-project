name = input('Enter your name: ') 
gender = input('Male or Female: ') 
martial = input('Married or Single: ') 
if gender == 'Female': 
  if martial == 'Married':
      print('Mrs. ' + name)
  else:
      print('Miss ' + name)
else: 
      print('Mr. ' + name)