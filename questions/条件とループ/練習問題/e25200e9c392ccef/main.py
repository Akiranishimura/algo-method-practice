"""
https://algo-method.com/tasks/e25200e9c392ccef

### 問題文
カメのアルルは最初 $N$ 円を持っていました。
これから $K$ 日間の収入・支出の記録が与えられます。$i \: (0 \leq i \leq K-1)$ 日目には、次のように所持金が変化しました。
- $C_i = 1$ の場合、所持金が $A_i$ 円増加した。
- $C_i = 2$ の場合、所持金が $A_i$ 円減少した。
最終的なアルルの所持金を出力してください。ただし、所持金が $0$ 円 **未満** になった時点がある場合、はじめて所持金が $0$ 円未満になったのは何日目か出力してください。

### 入力例
#### 入力例 1
```IOExample
10 3
1 7
2 12
1 8
```
#### 出力例 1
```IOExample
13
```
#### 入力例 2
```IOExample
10 3
1 8
2 20
1 10
```
#### 出力例 2
```IOExample
1
```
#### 入力例 3
```IOExample
100 4
2 100
1 10
1 10
2 21
```
#### 出力例 3
```IOExample
3
```
"""

N, K = map(int, input().split())

for i in range(K):
    C, A = map(int, input().split())
    if C == 1:
        N += A
    else:
        N -= A
    if N < 0:
        print(i)
        break
if(not N < 0):
    print(N)
