"""
https://algo-method.com/tasks/2584a3191b8e097d

### 問題文
繰り返し構文を活用して、次の $10$ 個の整数の総和を計算し出力するプログラムを作成してください。
```IOExample
3, 1, 4, 1, 5, 9, 2, 6, 5, 3
```"""

list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
sum = 0
for num in list:
    sum += num
print(sum)
