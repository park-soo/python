float('1.2345')
string = '23.12'
try:
    float(string)
except:
    print('fail to convert', end='')
    print(string)
else:
    print('ok')
finally:
    print('finally')