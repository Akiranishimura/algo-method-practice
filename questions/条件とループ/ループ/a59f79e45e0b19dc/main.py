"""
https://algo-method.com/tasks/a59f79e45e0b19dc

### 問題文
カメのアルルは卓球を $5$ 試合行いました。
試合結果は `o` と `x` のみからなる長さ $5$ の文字列 $S$ で表され、$S$ の各文字は各試合の勝敗を表します。たとえば $S$ が `oxxox` の場合、アルルの試合結果が順に 勝ち・負け・負け・勝ち・負け であったことを意味します。
アルルの勝利数を求めてください。
### 入力例
#### 入力例 1
```IOExample
oxxox
```
#### 出力例 1
```IOExample
2
```
#### 入力例 2
```IOExample
ooooo
```
#### 出力例 2
```IOExample
5
```
"""

S = input()
win_count = 0
for result in S:
    if result == "o":
        win_count += 1
print(win_count)
