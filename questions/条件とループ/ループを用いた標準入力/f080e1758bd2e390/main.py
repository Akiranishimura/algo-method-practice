"""
https://algo-method.com/tasks/f080e1758bd2e390

### 問題文
- $N$ 個の整数 $A_0, A_1, \ldots, A_{N-1}$ からなる整数列 $A$
- $M$ 個の整数 $B_0, B_1, \dots, B_{M-1}$ からなる整数列 $B$
が与えられます。
$A$ と $B$ それぞれに含まれる **正の整数** の個数を求め、$A$ の方が多い場合 `A`、$B$ の方が多い場合 `B`、どちらも同じ場合は `same` を出力してください。

### 入力例
#### 入力例 1
```IOExample
4 5
3 -1 4 5
5 -2 -4 -2 10
```
#### 出力例 1
```IOExample
A
```
#### 入力例 2
```IOExample
3 3
5 0 7
3 1 9
```
#### 出力例 2
```IOExample
B
```
#### 入力例 3
```IOExample
5 5
1 2 3 4 5
5 4 3 2 1
```
#### 出力例 3
```IOExample
same
```
"""

N, M = map(int, input().split())
list_A = map(int, input().split())
list_B = map(int, input().split())
positive_A = 0
positive_B = 0
for num in list_A:
    if num > 0:
        positive_A += 1
for num in list_B:
    if num > 0:
        positive_B += 1
if positive_B == positive_A:
    print("same")
elif positive_A > positive_B:
    print("A")
else:
    print("B")
