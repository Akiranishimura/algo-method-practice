"""
https://algo-method.com/tasks/54

### 問題文
$N$ 個の正の整数 $A_0, A_1, \dots, A_{N-1}$ が与えられます。$N$ 個の整数を全て掛け合わせた値を求めてください。
#
### 入力例
#### 入力例 1
```IOExample
3
10 20 30
```
#### 出力例 1
```IOExample
6000
```
"""

N = int(input())
list = input().split()
product = 1
for num in list:
    product = product * int(num)
print(product)
