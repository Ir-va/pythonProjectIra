from random import*
student=input('your name: ')

try:
    level=int(input('выбери уровень 1-5: '))
except:
    level=1
    print('установлен первый уровень')
if level<1 or level>5:
    level = 1
    print('установлен первый уровень')

print(f'Хорошо, {student}. Тебе задачка.')

min=10**(level-1)
max=10**level-1

point=0
for i in range(5):
    a=randint(min,max)
    b=randint(min,max)

    print(f'{student}, сколько будет {a} + {b}?', end='')
    correct_answer=a+b
    student_answer=input()

    if student_answer==str(correct_answer):
        print('правильно.')
        point+=1
    else:
        print(f'не правильно, правильный ответ: {correct_answer}.')

if point==5:
    print('твоя оценка пять')
elif point == 4:
    print('твоя оценка четыре')
elif point==3:
    print('твоя оценка три')
else:
    print('твоя оценка два')





