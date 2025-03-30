"""
https://algo-method.com/tasks/59

### 問題文
$N$ 個の文字列 $S_0, S_1, \dots, S_{N-1}$ が与えられます。
$N$ 個の文字列を前からすべてつなげてできる文字列の長さを出力してください。

### 入力例
#### 入力例 1
```IOExample
3
hello
algo
method
```
#### 出力例 1
```IOExample
15
```
"""

N = int(input())
sum = 0
for i in range(0, N):
    sum += len(input())
print(sum)
