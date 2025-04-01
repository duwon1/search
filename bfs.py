from dfs import my_graph

def my_bfs(graph, start_node):
    visit = list()
    queue = list()

    visit.append(start_node) # 방문한 노드들
    queue.extend(start_node) # 뒤집은 자식노드를 큐에 추가함

    while queue: # 모든 노드를 방문할때까지
        print(f"queue : {queue}")
        node = queue.pop(0) # 큐에서 아래서부터 꺼냄
        if node not in visit:
            print(f"현재 방문한 node : {node}")
            visit.append(node) # 방문한 노드를 추가
            queue.extend(graph[node]) # 자식노드를 큐에 추가함

    return visit


print(my_bfs(my_graph, 'G'))
