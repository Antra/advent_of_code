from utils import get_data
file = '2021/puzzle12/input.txt'
data = get_data(file)

# data = ['start-A',
#         'start-b',
#         'A-c',
#         'A-b',
#         'b-d',
#         'A-end',
#         'b-end']

# data = ['dc-end',
#         'HN-start',
#         'start-kj',
#         'dc-start',
#         'dc-HN',
#         'LN-dc',
#         'HN-end',
#         'kj-sa',
#         'kj-HN',
#         'kj-dc']


# data = ['fs-end',
#         'he-DX',
#         'fs-he',
#         'start-DX',
#         'pj-DX',
#         'end-zg',
#         'zg-sl',
#         'zg-pj',
#         'pj-he',
#         'RW-he',
#         'fs-DX',
#         'pj-RW',
#         'zg-RW',
#         'start-pj',
#         'he-WI',
#         'zg-he',
#         'pj-fs',
#         'start-RW']


class Graph(object):
    def __init__(self, name='graph') -> None:
        self.name = name
        self.graph = {}
        self.visited = {}
        self.paths = 0
        self.can_visit_twice = False

    def get_size(self):
        return len(self.graph.keys())

    def get_paths(self):
        return self.paths

    def get_visited(self):
        return self.visited

    def __repr__(self) -> str:
        return f'< Graph, vertices: {self.get_size()} >'

    def add_edge(self, a, b):
        self.graph[a] = self.graph.get(a, [])
        self.graph[a].append(b)
        self.graph[b] = self.graph.get(b, [])
        self.graph[b].append(a)
        self.visited[a] = 0
        self.visited[b] = 0

    def _print_paths_util(self, a, dest, visited, path):
        if a.islower():
            visited[a] += 1
        path.append(a)

        if a == dest:
            self.paths += 1
            print(path)
        else:
            for neighbour in self.graph[a]:
                caves_visited_more_than_once = len(
                    {k for k, v in graph.visited.items() if v > 1})
                if (neighbour.isupper() or visited[neighbour] == 0 or (self.can_visit_twice and caves_visited_more_than_once == 0)) and (a != 'end' and neighbour != 'start'):
                    self._print_paths_util(neighbour, dest, visited, path)

        path.pop()
        visited[a] = 0 if not self.can_visit_twice else visited[a] - 1

    def print_paths(self, start, dest, can_visit_twice=False):
        self.can_visit_twice = can_visit_twice
        path = []
        visited = self.get_visited()
        self._print_paths_util(start, dest, visited, path)

        print(self.paths)


graph = Graph()
for path in data:
    graph.add_edge(path.split('-')[0], path.split('-')[1])

graph.graph
# part 1
graph.print_paths('start', 'end')
# part 2 (this takes a while!)
graph.print_paths('start', 'end', can_visit_twice=True)
