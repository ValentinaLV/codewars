def get_min_price_from_dict(prices: dict):
    return min(zip(prices.values(), prices.keys()))


def get_min_price_from_dict2(prices: dict):
    return prices[min(prices, key=lambda k: prices[k])]


def get_max_price_from_dict(prices: dict):
    return max(zip(prices.values(), prices.keys()))


def get_max_price_from_dict2(prices: dict):
    return prices[max(prices, key=lambda k: prices[k])]


def get_sorted_dict(prices: dict):
    return dict(sorted(zip(prices.keys(), prices.values())))


prices = {'ACME': 45.23,
          'AAPL': 612.78,
          'IBM': 205.55,
          'HPQ': 37.20,
          'FB': 10.75
          }

print(get_min_price_from_dict(prices))
print(get_min_price_from_dict2(prices))
print(get_max_price_from_dict(prices))
print(get_max_price_from_dict2(prices))
print(get_sorted_dict(prices))
