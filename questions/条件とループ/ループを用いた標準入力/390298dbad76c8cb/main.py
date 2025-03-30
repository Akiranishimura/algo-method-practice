"""
https://algo-method.com/tasks/390298dbad76c8cb

### 問題文
$N$ 個の整数 $A_0, A_1, \ldots, A_{N-1}$ が一列に並んでいます。
これらの整数に対して、次の $Q$ 個の質問に答えてください。
---
各質問では整数値 $K \: (0 \leq K \leq N - 1)$ が与えられます。
最も左の整数を左から $0$ 番目と数えるとき、左から $K$ 番目の整数を出力してください。
すなわち、$A_K$ の値を出力してください。
---

### 入力例
#### 入力例 1
```IOExample
5 3
3 1 4 1 5
3
1
0
```
#### 出力例 1
```IOExample
1
1
3
```
#### 入力例 2
```IOExample
10 2
1 2 3 4 5 6 7 8 9 10
5
5
```
#### 出力例 2
```IOExample
6
6
```
"""

N, Q = map(int, input().split())
list_A = list(map(int, input().split()))
for i in range(Q):
    K = int(input())
    print(list_A[K])
