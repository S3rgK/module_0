import numpy as np
number = np.random.randint(1,101)    # загадали число
print ("Загадано число от 1 до 100")
for count in range(1,101):         # более компактный вариант счетчика
    if number == count: break    # выход из цикла, если угадали      
print (f"Вы угадали число {number} за {count} попыток.")