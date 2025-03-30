"""
https://algo-method.com/tasks/56

### 問題文
$N$ 個の正整数 $A_0, A_1, \dots, A_{N-1}$ が与えられます。
$N$ 個の整数のうち、$3$ の倍数であるものを改行区切りで全て出力してください。

### 入力例
#### 入力例 1
```IOExample
3
27 18 28
```
#### 出力例 1
```IOExample
27
18
```
#### 入力例 2
```IOExample
3
31 41 59
```
#### 出力例 2
```IOExample

```
"""

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

for num in list:
    if int(num) % 3 == 0:
        print(num)
