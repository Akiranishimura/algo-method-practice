"""
https://algo-method.com/tasks/69f3b6db966d9cdb

### 問題文
ある検定試験は $1$ 級から $5$ 級までの $5$ 段階の級があります。
それぞれの級の合格基準は下記の表の通りです。
|級|合格基準|
|:--:|:--:|
|$1$ 級|$90$ 点以上|
|$2$ 級|$80$ 点以上|
|$3$ 級|$70$ 点以上|
|$4$ 級|$70$ 点以上|
|$5$ 級|$70$ 点以上|
$N$ 人の学生が、この検定試験を受けました。
学生 $i \: (0 \leq i \leq  N-1)$ は $A_i$ 級の試験を受験し、点数が $B_i$ 点でした。
試験に合格した学生の人数を出力してください。

### 入力例
#### 入力例 1
```IOExample
3
3 85
4 53
1 90
```
#### 出力例 1
```IOExample
2
```
#### 入力例 2
```IOExample
2
2 75
3 75
```
#### 出力例 2
```IOExample
1
```
"""

N = int(input())
success = 0
for i in range(N):
    A, B = map(int, input().split())
    if A == 1 and B >= 90:
        success += 1
    elif A == 2 and B >= 80:
        success += 1
    elif (A == 3 or A == 4 or A == 5) and B >= 70:
        success += 1

print(success)
