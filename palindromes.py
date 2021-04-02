import re
wyraz = input('Podaj wyraz: ')

# zamiana liter na male
w_male = wyraz.lower()
# usuniecie spacji
w_polaczone = w_male.replace(" ", "")
# biblioteka regular expressions, wyrzuca wszystko co nie jest literami A-Z i a-z
wyraz = re.sub('[^A-Za-z]+', '', w_polaczone)

if wyraz[::-1] == wyraz:
    print('Wyrażenie jest palindromem')
else:
    print('Wyrażenie nie jest palindromem')
