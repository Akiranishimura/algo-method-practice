"""
https://algo-method.com/tasks/4f1c991a95b1e04d

### 問題文
正の整数 $N$ が与えられます。
- $N$ が $3$ の倍数ならば、`Fizz` と出力してください
- $N$ が $5$ の倍数ならば、`Buzz` と出力してください
- ただし、$N$ が $3$ の倍数でも $5$ の倍数でもあるならば、`FizzBuzz` と出力してください
- それ以外の場合は、そのままの整数 $N$ を出力してください
![image](https://algo-method-public-production.s3.ap-northeast-1.amazonaws.com/images%2F587e55ae-8393-4c5e-9185-141def5507a4%2F%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88+2022-07-04+9.18.18.png)
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $100$ 以下の整数
### 出力
答えを出力してください。
"""

N = int(input())

multiple3 = N % 3 == 0
multiple5 = N % 5 == 0

if multiple3 and multiple5:
    print("FizzBuzz")
elif multiple3:
    print("Fizz")
elif multiple5:
    print("Buzz")
else:
    print(N)
