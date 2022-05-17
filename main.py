
print('Welcome to Business Name Generator')

first_name = input('What is your first name?\n')

favourite_colour = input('What is your favourite colour?\n')

business_name = first_name[:3] + favourite_colour[-4:]

print('Your business name is {} Enterprise'.format(business_name))