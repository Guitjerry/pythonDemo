#快速排序
#分而治之思想   分而治之是一种使用递归解决问题的算法，
# 主要的技巧是将一个大的复杂的问题划分为多个子问题，
# 而这些子问题可以作为终止条件，或者在一个递归步骤中得到解决，
# 所有子问题的解决结合起来就构成了对原问题的解决
def quickSort(array):
    if len(array)<2:
        return array
    else:
        #以第一个为基准，找出大于和小于的数组，分而治之递归调用
        privot  = array[0]
        less = [i for i in array[1:] if i<privot]
        big = [i for i in array[1:] if i>privot]
        return quickSort(less)+[privot]+quickSort(big)

if __name__ == '__main__':
    print(quickSort([8,49,10,7,2]))