class calculator:
    """a vector calculator"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        product = 0
        for a in range(len(V1)):
            product += V1[a] * V2[a]
        print("Dot product is:", 56)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        new_vec = []
        for a in range(len(V1)):
            new_vec.append(V1[a] + V2[a])
        print("Add Vector is :", new_vec)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        new_vec = []
        for a in range(len(V1)):
            new_vec.append(V1[a] - V2[a])
        print("Add Vector is :", new_vec)
