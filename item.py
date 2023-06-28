name = input('What is your name? ')
if name.lower() == 'joshua':
    print('Error')
    exit()
gender = input('What is your gender? (m/f) ')
if gender.lower() == 'm':
    partner = "girlfriend"
elif gender.lower() == 'f':
    partner = "boyfriend"
else:
    print('Error')
    exit()
partner_name = input(f'Who is your {partner}? (This will not be recorded.) ')
if partner_name.lower() == 'joshua':
    print('Error')
    exit()
print(f'{name} is gay.')
print(f'{partner_name} is also gay and is as retarded as you are!')
