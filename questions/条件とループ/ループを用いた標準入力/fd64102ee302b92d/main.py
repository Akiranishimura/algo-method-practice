"""
https://algo-method.com/tasks/fd64102ee302b92d

### 問題文
カメのアルルはスーパーマーケットで $N$ 個の商品を買いました。
$i \: (0 \leq i \leq N-1)$ 番目の商品について、価格は $1$ 個 $A_i$ 円で、アルルはこれを $B_i$ 個買いました。
アルルが買った商品の総額を求めてください。

### 入力例
#### 入力例 1
```IOExample
2
3 6
2 10
```
#### 出力例 1
```IOExample
38
```
#### 入力例 2
```IOExample
1
100 100
```
#### 出力例 2
```IOExample
10000
```
"""

N = int(input())
sum = 0
for i in range(N):
    A, B = map(int, input().split())
    sum += A * B

print(sum)
