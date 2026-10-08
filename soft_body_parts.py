class vertex:
    x = 0
    y = 0
    velocity = 0

    def __init__(self, x , y) -> None:
        self.x = x
        self.y = y



class spring_edge:
    vertex_a = 0
    vertex_b = 0

    def __init__(self, vertex_a, vertex_b) -> None:
        self.vertex_a = vertex_a
        self.vertex_b = vertex_b

class blob:
    ...