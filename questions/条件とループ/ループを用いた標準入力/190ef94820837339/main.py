"""
https://algo-method.com/tasks/190ef94820837339

### 問題文
$N$ 個の整数 $A_0, A_1, \ldots, A_{N-1}$ が一列に並んでいます。
最も左の整数を左から $0$ 番目と数えるとき、左から $K$ 番目の整数を出力してください。
すなわち、$A_K$ を出力してください。

### 入力例
#### 入力例 1
```IOExample
5 3
3 1 4 1 5
```
#### 出力例 1
```IOExample
1
```
#### 入力例 2
```IOExample
10 9
1 2 3 4 5 6 7 8 9 10
```
#### 出力例 2
```IOExample
10
```
"""

N, K = map(int, input().split())
list = input().split()
print(list[K])
