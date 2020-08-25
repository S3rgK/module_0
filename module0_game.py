#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np


# In[12]:


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Среднее количество попыток, которое использует ваш алгоритм равно {score}.")


# In[15]:


def game_core_v4(number):
    '''Бинарный поиск: последовательное двукратное уменьшение интервала поиска.
       Функция принимает загаданное число и возвращает число попыток'''
    
    attempts = 1
    low = 0
    high = 101
    predict = (low + high) // 2     # середина начального поискового интервала

    while number != predict:
        if predict > number:
            high = predict      # устанавливаем угадываемое число верхней границей интервала
            predict = predict - ((high-low) // 2)       # двукратно уменьшаем полученный интервал
        elif predict < number:
            low = predict       # устанавливаем угадываемое число нижней границей интервала
            predict = predict + ((high-low) //2 )   # двукратно уменьшаем полученный интервал
        attempts += 1

    return(attempts) # выход из цикла, если угадали


# In[16]:


# v4 check
score_game(game_core_v4)


# %%
