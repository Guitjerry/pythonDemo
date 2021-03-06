import aiohttp
#狄克斯特拉算法 ,适合计算有正向权重的最优路径
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

costs = {}
infinfy = float('inf')
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinfy

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = [] #记录处理过的点




#找出开销最低的节点
def find_lowest_cost_node(costs):
    lowest_const = float('inf')
    lower_cost_node = None
    for node in costs:
        cost = costs[node]
        if(cost < lowest_const and node not in processed):
            lowest_const = cost
            lower_cost_node = node
    print(lower_cost_node)
    return lower_cost_node



if __name__ == '__main__':
    # noinspection PyInterpreter
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        if node in graph.keys():
            neighbors = graph[node]
            for n in neighbors.keys():
                new_cost = cost + neighbors[n]
                if(costs[n] > new_cost):
                    costs[n] = new_cost
                    parents[n] = node
            processed.append(node)
            node = find_lowest_cost_node(costs)



