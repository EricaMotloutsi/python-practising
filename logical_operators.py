#Logical operators (and, or , not)

age = 17
has_student_id = True

if age < 18 and has_student_id:
    print('You are eligible for the student discount')
else:
    print('Sorry, you don\'t qualify for the student discount!')


first_time_user = False
has_promo_code = True 
if first_time_user or has_promo_code:
    print('Discount applied')
else:
    print('No dicount available.')

#not operator
profile_completed = False
if not profile_completed:
    print('Please complete your profile to access all features.')
else:
    print('Your profle is complete!')

age= 16
has_parental_consent = True 
if not (age>=18 or has_parental_consent):
    print('Youu cannot sign up without parental consent')
else:
    print('You are allowed to sign up.')
    