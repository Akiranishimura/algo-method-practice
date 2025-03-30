"""
https://algo-method.com/tasks/b944f80497ab1eae

### 問題文
$N$ 人の生徒が試験を受けました。出席番号 $i \: (0 \leq i \leq N-1)$ 番の生徒の点数は $A_i$ 点でした。
平均点以上を取った人の出席番号を、小さいものから順に改行区切りで出力してください。
**平均点は整数とならない可能性があることに注意してください。**
<details><summary>ヒント</summary><div>
$N$ 個のデータ $A_0, A_1, \dots, A_{N-1}$ の平均値は $\dfrac{A_0 + A_1 + \dots + A_N}{N}$ と求められます。
</div></details>

### 入力例
#### 入力例 1
```IOExample
4
4 8 3 9
```
#### 出力例 1
```IOExample
1
3
```
#### 入力例 2
```IOExample
3
5 5 5
```
#### 出力例 2
```IOExample
0
1
2
```
#### 入力例 3
```IOExample
3
3 7 6
```
#### 出力例 3
```IOExample
1
2
```
"""

N = int(input())
list_A = list(map(int, input().split()))
mean_A = sum(list_A) / N
for i in range(len(list_A)):
    if list_A[i] >= mean_A:
        print(i)
