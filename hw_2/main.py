
from generate_latex import generate_latex_table

example_data = [
    ['Имя', 'Возраст', 'Город'],
    ['Иван', '30', 'Москва'],
    ['Петр', '25', 'Санкт-Петербург'],
    ['Мария', '28', 'Новосибирск'],
]

latex_code = generate_latex_table(example_data)

with open('table.tex', 'w') as f:
    f.write(latex_code)
