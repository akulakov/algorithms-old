
def is_div(a):
    return x%a==0

for x in range(1,101):
    print(x, ' ',
          'Crackle' if is_div(3) else '',
          'Pop' if is_div(5) else '',
          sep='')
