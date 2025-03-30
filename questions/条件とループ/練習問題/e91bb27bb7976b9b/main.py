"""
https://algo-method.com/tasks/e91bb27bb7976b9b

### 問題文
$N$ 個の正の整数 $A_0, A_1, \dots, A_{N-1}$ が与えられます。
これら $N$ 個の整数を末尾から順に、一行ずつ出力してください。
#
### 入力例
#### 入力例 1
```IOExample
3
31 41 59
```
#### 出力例 1
```IOExample
59
41
31
```
#### 入力例 2
```IOExample
1
50
```
#### 出力例 2
```IOExample
50
```
"""

N = int(input())
list_A = list(map(int, input().split()))
list_A.reverse()
for A in list_A:
    print(A)