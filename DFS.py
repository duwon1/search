# 시작노드 'G'
my_graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

def my_dfs(graph, start_node):
    visit = list()

    visit.append(start_node) # 방문한 노드들
    child_node = graph[start_node] # 방문한 노드의 자식노드를 저장함
    child_node.reverse() # 자식노드를 뒤집음
    stack = child_node # 뒤집은 자식노드를 스택에 추가함

    while stack: # 모든 노드를 방문할때까지
        print(f"stack : {stack}")
        node = stack.pop()
        print(f"현재 방문한 node : {node}")
        if node not in visit:
            visit.append(node) # 방문한 노드를 추가
            child_node = graph[node] # 방문한 노드의 자식노드를 저장함
            child_node.reverse() # 자식노드를 뒤집음
            stack.extend(child_node) # 자식노드를 스택에 추가함 append할 경우 배열로 들어가서 2차원배열이 되버림.
                                     # extend를 통해 배열형태를 문자열로 각각 이어붙힘
                                     # ex) append : [1, 2, 3] 이거자체가 추가됨, extend : '1', '2', '3' 이렇게 풀어서 stack에 추가함
    print(visit)
    return


my_dfs(my_graph, 'G')

def my_bfs(graph, start_node):
    visit = list()

    visit.append(start_node) # 방문한 노드들
    child_node = graph[start_node] # 방문한 노드의 자식노드를 저장함
    child_node.reverse() # 자식노드를 뒤집음
    stack = child_node # 뒤집은 자식노드를 스택에 추가함

    while stack: # 모든 노드를 방문할때까지
        print(f"stack : {stack}")
        node = stack.pop()
        print(f"현재 방문한 node : {node}")
        if node not in visit:
            visit.append(node) # 방문한 노드를 추가
            child_node = graph[node] # 방문한 노드의 자식노드를 저장함
            child_node.reverse() # 자식노드를 뒤집음
            stack.extend(child_node) # 자식노드를 스택에 추가함 append할 경우 배열로 들어가서 2차원배열이 되버림.
            # extend를 통해 배열형태를 문자열로 각각 이어붙힘
            # ex) append : [1, 2, 3] 이거자체가 추가됨, extend : '1', '2', '3' 이렇게 풀어서 stack에 추가함
    print(visit)
    return


my_bfs(my_graph, 'G')
