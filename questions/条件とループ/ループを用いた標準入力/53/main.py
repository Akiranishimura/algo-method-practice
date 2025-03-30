"""
https://algo-method.com/tasks/53

### 問題文
$N$ 個の正の整数 $A_0, A_1, \dots, A_{N-1}$ が与えられます。$N$ 個の整数の合計値を求めてください。

### 入力例
#### 入力例 1
```IOExample
3
10 20 30
```
#### 出力例 1
```IOExample
60
```
"""

N = int(input())
list = input().split()
sum = 0
for num in list:
    sum += int(num)
print(sum)