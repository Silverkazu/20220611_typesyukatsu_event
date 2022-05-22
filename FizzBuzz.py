"""
1から100までの数字を出力
3の倍数のときは数字の代わりにFizzと出力
5の倍数のときは数字の代わりにBuzzと出力
15の倍数のときは数字の代わりにFizzBuzzと出力
"""
begin_num = 1
end_num = 100
for num in range(begin_num, end_num+1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)