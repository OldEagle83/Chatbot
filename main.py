bot_name = 'Myr'
birth_year = 2020
msg = ['Please, remind me your name.', 'Let me guess your age.', 'Enter remainders of dividing your age by 3, 5 and 7.',
       'Now I will prove to you that I can count to any number you want.', 'Completed, have a nice day!',
       'Let\'s test your programming knowledge.']

q1 = ['How do we dynamically reference a variable ie num1, num2 etc?', '4']
a1 = ['1. [num + i] Where i is 1, 2, 3', '2. num%s %i Where i is 1, 2, 3', '3. {num + i} Where i is 1, 2, 3',
      '4. By using the globals() function']


def ageCalc(remainder3, remainder5, remainder7):
    age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    return age

def quiz(q):
    print(globals()['q%s' % q][0])
    for a in globals()['a%s' % q]:
        print(a)
    answer = input()
    while answer != globals()['q%s' % q][1]:
        print('Please, try again.')
        answer = input()
    return True



print(f'Hello! My name is {bot_name}.')
print(f'I was created in {birth_year}.')
print(msg[0])
your_name = input()
print(f'What a great name you have, {your_name}!')
print(msg[1])
print(msg[2])
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
your_age = ageCalc(remainder3, remainder5, remainder7)
print(f'Your age is {your_age}; that\'s a good time to start programming!' )
print(msg[3])
num = int(input())
for i in range(0, num+1):
    print(f'{i} !')
print(msg[4])
print(msg[5])
if quiz(1):
    print('Congratulations, have a nice day!')
