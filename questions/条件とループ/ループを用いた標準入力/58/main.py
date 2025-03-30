"""
https://algo-method.com/tasks/58

### 問題文
$N$ 個の文字列 $S_0, S_1 \dots, S_{N-1}$ が与えられます。
$N$ 個の文字列の頭文字をつないでできる文字列を出力してください。

### 入力例
#### 入力例 1
```IOExample
4
hyper
text
transfer
protocol
```
#### 出力例 1
```IOExample
http
```
"""

N = int(input())
all = ""
for i in range(0, N):
    all += input()[0]
print(all)
