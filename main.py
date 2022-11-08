# this inputs the what is your name for user name
user_name = input('What is your name?')
# this inputs the age using int and asks how old are you
user_age = int(input('How old are you?'))
# this creates year separated by dash to indicate the range for users age and the calculations
year_born = 2020 - user_age
# This prints Hello then users name and says you were born
print('Hello', user_name, '!', 'You were born in', year_born, '.')
