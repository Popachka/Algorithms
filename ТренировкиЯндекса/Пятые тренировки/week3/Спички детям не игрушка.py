import math

class Match:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.xc = (x1 + x2) / 2.0
        self.yc = (y1 + y2) / 2.0
        self.len = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.ang = math.atan2(abs(y2 - y1), abs(x2 - x1))

    def distance_to(self, p):
        return math.sqrt((abs(p[0] - self.xc)) ** 2 + (abs(p[1] - self.yc)) ** 2)

    def transfer_vector_to(self, p):
        return p[0] - self.xc, p[1] - self.yc

    def center(self):
        return self.xc, self.yc

    def __eq__(self, other):
        if not isinstance(other, Match):
            return False
        return self.len == other.len and self.ang == other.ang

    def __hash__(self):
        return hash((self.len, self.ang))

if __name__ == "__main__":
    # Read the number of matches
    n = int(input())

    # Read the coordinates of matches for image 1
    image1 = {}
    for _ in range(n):
        coords = list(map(int, input().split()))
        new_match = Match(*coords)
        if new_match in image1:
            image1[new_match].append(new_match)
        else:
            image1[new_match] = [new_match]

    # Read the coordinates of matches for image 2
    distances = {}
    transfer_vectors = {}
    no_match = True
    for _ in range(n):
        coords = list(map(int, input().split()))
        new_match = Match(*coords)

        if new_match in image1:
            no_match = False
            found_matches = image1[new_match]
            for match in found_matches:
                vector = new_match.transfer_vector_to(match.center())
                if vector in transfer_vectors:
                    transfer_vectors[vector] += 1
                else:
                    transfer_vectors[vector] = 1

    if no_match:
        print("No matches found")
    else:
        print("Transfer vectors and their frequencies:")
        for vector, frequency in transfer_vectors.items():
            print(vector, frequency)
