# 广度优先搜索
#需求:需要从广度优先搜索.png找出谁是牛奶供应商(m结尾的)
#技术栈:队列+散列表
#引入队列
from collections import deque
grapy = {}
grapy["you"] = ["ALICE", "BOB", "CLAIRE"]
grapy["ALICE"] = ["PEGGY"]
grapy["CLAIRE"] = ["TONNY", "THOM"]
grapy["BOB"] = ["PEGGY", "ANUT"]
grapy["ANUT"] = []
grapy["PEGGY"] = []
grapy["TONNY"] = []
grapy["THOM"] = []

#牛奶供应商判断
def person_is_seller(name):
    return name[-1] == 'M'

def serch(name):
    search_quere= deque()
    search_quere += grapy[name]
    searched = [] #是否检索过该名称
    while search_quere:
        person = search_quere.popleft()
        if not person in searched:
            if person_is_seller(person):
                print('找到牛奶供应商'+person)
                return True
            else:
                search_quere += grapy[person]
                searched.append(person)
    return False

if __name__ == '__main__':
    serch('you')