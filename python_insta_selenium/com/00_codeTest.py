
import pandas as pd

num = []
num.append([1,2])
num.append([3,4])
num.append([5,6])
pd.DataFrame(num).to_csv("test.csv", encoding="utf-8")


print(num)