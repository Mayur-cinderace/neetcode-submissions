class CountSquares:

    def __init__(self):
        self.coord = []
        self.freq = defaultdict(int)
    def add(self, point: List[int]) -> None:
        self.coord.append(point)
        self.freq[tuple(point)] += 1
    def count(self, point: List[int]) -> int:
        x = point[0]
        y = point[1]
        x_cand = []
        y_cand = []
        
        for pt in self.coord:
            if pt[0] == x and pt[1] == y:
                continue
            elif pt[0] == x:
                x_cand.append(pt)
            elif pt[1] == y:
                y_cand.append(pt)

        count = 0

        for x_c in x_cand:
            for y_c in y_cand:
                if abs(y_c[0]-x_c[0]) == abs(y_c[1]-x_c[1]):
                    if (y_c[0], x_c[1])in self.freq:
                        count += 1*self.freq[(y_c[0], x_c[1])]
        
        return count




# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)