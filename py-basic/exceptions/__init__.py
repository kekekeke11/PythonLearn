try:
    a = 1/0
except Exception as e:
    print(e)
finally:
    print("finally")
