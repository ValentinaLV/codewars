op = {"sum": lambda x, y: x + y,
      "sub": lambda x, y: x - y}

print(op["sum"](10, 15))  # 25
print(op["sub"](10, 15))  # -5
