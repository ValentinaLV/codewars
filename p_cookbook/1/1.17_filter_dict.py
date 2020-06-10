prices = {'ACME': 45.23,
          'AAPL': 612.78,
          'IBM': 205.55,
          'HPQ': 37.20,
          'FB': 10.75
          }

# Создать словарь всех акций с ценами больше 200
d = {k: v for k, v in prices.items() if v > 200}
print(d)

# Создать словарь акций технологических компаний
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
d2 = {k: v for k, v in prices.items() if k in tech_names}
print(d2)
