# Форматирование строк
# Использование %:
print('количество участников первой команды %s!' %(team1_num))
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))
# Использование format():
print('количество задач решённых командой {}.'.format(score_2))
print('Волшебники данных решили задачи за {} с!'.format(team1_time))
# Использование f-строк:
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')