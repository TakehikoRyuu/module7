# Позиционирование в файле.
def custom_write(file_name, strings):
    # запись
    with open(file_name, 'a', encoding='utf-8') as file:
        resul = {}  # битность строки
        for idx, string in enumerate(strings, 1):
            bit = (file.tell())
            resul[(idx, bit)] = string
            file.writelines(f'{string}\n')
    return resul


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

