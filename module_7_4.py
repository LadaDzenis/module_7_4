# Использование %
team1_num = 5
team2_num = 6
print('В команде Мастера кода участников: %s!' % team1_num)
print('В команде Мастера кода участников: %s и %s!' % (team1_num, team2_num))

# Использование format()
score_2 = 42
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print('Волшебники данных решили задачи за {team1_time} c!'.format(team1_time=18015.2))

# Использование f-строк
score_1 = 40
print(f'Команды решили {score_1} и {score_2} задач.')
challenge_result = 'победа команды Мастера кода!'
print(f'Результат битвы: {challenge_result}')
tasks_total = 82
time_avg = 350.4
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')