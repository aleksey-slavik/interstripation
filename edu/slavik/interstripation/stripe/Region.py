class Region:

    def __init__(self, vertical, horizontal):
        self.x1 = vertical.startAt
        self.y1 = horizontal.startAt
        self.x2 = vertical.endAt
        self.y2 = horizontal.endAt

    def removeRegion(self, surface):
        for i in range(self.x1, self.x2):
            for j in range(self.y1, self.y2):
                surface.matrix[i, j] = -1

        return surface

    def __repr__(self):
        return str(self.__dict__)
