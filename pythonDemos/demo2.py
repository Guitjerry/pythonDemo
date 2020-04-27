## 递归
def fact(x):
    if x == 1:
        return  1
    else:
        return x * fact(x-1)

def sumAll(arry):
    #基线条件
    if len(arry) == 0:
        return 0
    else:
        lastArry = arry[0]
        del arry[0]
        return lastArry+sumAll(arry)

if __name__ == '__main__':
    print(fact(8))
    print(sumAll([1,5,7,9,22]))