"""
1から100までの数字を出力
3の倍数のときは数字の代わりにFizzと出力
5の倍数のときは数字の代わりにBuzzと出力
15の倍数のときは数字の代わりにFizzBuzzと出力
"""

for num in range(1, 101):
    string = ''

    # 15の倍数のときは数字の代わりにFizzBuzzと出力
    if num % 3 == 0 and num % 5 == 0:
        string = "FizzBuzz"
    # 3の倍数のときは数字の代わりにFizzと出力
    elif num % 3 == 0:
        string = "Fizz"
    # 5の倍数のときは数字の代わりにBuzzと出力
    elif num % 5 == 0:
        string = "Buzz"
    # 3, 5どちらの倍数でもない時は、その数字を出力
    else:
        string = str(num)

    print(string)