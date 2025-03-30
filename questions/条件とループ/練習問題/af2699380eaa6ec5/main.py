"""
https://algo-method.com/tasks/af2699380eaa6ec5

### 問題文
$N$ 個の正の整数 $A_0, A_1, \dots, A_{N-1}$ が与えられます。
これら $N$ 個の整数の平均値を求めてください。
ただし、答えは**小数点以下を切り捨てて**出力してください。

### 入力例
#### 入力例 1
```IOExample
3
31 41 59
```
#### 出力例 1
```IOExample
43
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

import math

N = int(input())
list_A = list(map(int, input().split()))
mean = sum(list_A) / len(list_A)
print(int(math.floor(mean)))
