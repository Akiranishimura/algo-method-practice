"""
https://algo-method.com/tasks/3c5f9db3a7dd3e75

### 問題文
$N$ 人の生徒が試験を受けました。
出席番号 $i \: (0 \leq i \leq N-1)$ 番の生徒の中間試験の点数は $A_i$ 点、期末試験の点数は $B_i$ 点でした。
各生徒の点数は、次のうち大きい方の値になります。
- 期末試験の点数
- 期末試験と中間試験の点数を足して $2$ で割った値
また、評定は点数に基づいて下記の表で決まります。
|点数|評定|
|:--:|:--:|
|$90$ 点以上|S|
|$80$ 点以上 $90$ 点未満|A|
|$70$ 点以上 $80$ 点未満|B|
|$60$ 点以上 $70$ 点未満|C|
|$60$ 点未満|F|
各生徒の評定を求めてください。

### 入力例
#### 入力例 1
```IOExample
3
70 90
80 60
100 10
```
#### 出力例 1
```IOExample
S
B
F
```
"""

N = int(input())


def meanOrB(mean: int, B: int):
    if mean >= B:
        return mean
    else:
        return B


for i in range(N):
    A, B = map(int, input().split())
    mean = (A + B) / 2
    points = meanOrB(mean, B)
    if points >= 90:
        print("S")
    elif points >= 80:
        print("A")
    elif points >= 70:
        print("B")
    elif points >= 60:
        print("C")
    else:
        print("F")
