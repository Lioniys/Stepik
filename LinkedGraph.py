class Vertex:
    def __init__(self):
        """
        _links - список связей с другими вершинами графа (список объектов класса Link)
        """
        self._links: list = []

    @property
    def links(self):
        return self._links


class Link:
    def __init__(self, v1, v2):
        """
        _v1, _v2 - ссылки на объекты класса Vertex, которые соединяются данной связью
        _dist - длина связи (по умолчанию 1); это может быть длина пути, время в пути и др
        """
        self._v1 = v1
        self._v2 = v2
        self._dist = 1

    def __eq__(self, other):
        return self.v1 in (other.v1, other.v2) and self.v2 in (other.v1, other.v2)


    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, x):
        self._dist = x


class LinkedGraph:
    def __init__(self):
        """
        _links - список из всех связей графа (из объектов класса Link)
        _vertex - список из всех вершин графа (из объектов класса Vertex)
        """
        self._links: list = []
        self._vertex: list = []

    def add_vertex(self, v):
        """Добавление новой вершины v в список _vertex (если она там отсутствует)"""
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        """Добавление новой связи link в список _links (если объект link с указанными вершинами в списке отсутствует)"""
        if link not in self._links:
            self._links.append(link)
        self.add_vertex(link.v1)
        self.add_vertex(link.v2)
        link.v1.links.append(link)
        link.v2.links.append(link)

    def find_path(self, start_v, stop_v):
        """Поиск кратчайшего маршрута из вершины start_v в вершину stop_v"""
        self.start_v = start_v
        self.stop_v = stop_v
        return self._next(self.start_v, None, [], [])

    def _dist_path(self, links):
        return sum([x.dist for x in links if x is not None])

    def _next(self, start_v, link_prew, c_path, c_links):
        c_path += [start_v]
        if link_prew:
            c_links += [link_prew]
        if start_v == self.stop_v:
            return c_path, c_links
        len_path = -1
        best_path = []
        best_links = []
        for link in start_v.links:
            path = []
            links = []
            if link.v1 not in c_path:
                path, links = self._next(link.v1, link, c_path[:], c_links[:])
            elif link.v2 not in c_path:
                path, links = self._next(link.v2, link, c_path[:], c_links[:])
            if self.stop_v in path and (len_path > self._dist_path(links) or len_path == -1):
                len_path = self._dist_path(links)
                best_path = path[:]
                best_links = links[:]
        return best_path, best_links


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2)
        self._dist = dist


map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))

map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))

map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))

print(len(map_metro._links))
print(len(map_metro._vertex))
path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
print(path[0])    # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
print(sum([x.dist for x in path[1]]))  # 7
