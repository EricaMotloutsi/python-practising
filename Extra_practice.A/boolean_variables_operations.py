

username='Erica'

if username:
    print(f'Welcome back, {username}!')
else:
    print('Please enter your username.')



#Boolean Variables and logical operators
bonus_points = 4
cardio_completed = True 
strength_completed = False

bonus_points = cardio_completed + strength_completed

if bonus_points > 0:
    print(f"Great job! You've earned {bonus_points} bonus point(s) for today's workout!")
else:
    print("No bonus points today. Try completing a session to earn points!")