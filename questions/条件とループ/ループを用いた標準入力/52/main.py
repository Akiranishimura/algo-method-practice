"""
https://algo-method.com/tasks/52

### 問題文
$N$ 個の正の整数 $A_0, A_1, \dots, A_{N-1}$ が与えられます。$N$ 個の整数の一の位を改行区切りで順に出力してください。

### 入力例
#### 入力例 1
```IOExample
3
31 41 59
```
#### 出力例 1
```IOExample
1
1
9
```
"""

N = int(input())
list = input().split()
for num in list:
    print(int(int(num) % 10))
