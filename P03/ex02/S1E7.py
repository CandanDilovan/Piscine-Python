from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, name, is_alive=True):
        self.first_name = name
        self.is_alive = is_alive
        self.familly_name = "Baratheon"
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self):
        self.is_alive = False

    def __str__(self):
        return self

    def __repr__(self):
        vect = [f"{self.first_name}", f"{self.eyes}", f"{self.hairs}"]
        return (f"Vector: ({vect[0]}, {vect[1]}, {vect[2]})")


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, name, is_alive=True):
        self.familly_name = "Lannister"
        self.first_name = name
        self.is_alive = is_alive
        self.eyes = 'blue'
        self.hairs = 'light'

    @staticmethod
    def create_lannister(name, is_alive=True):
        return Lannister(name, is_alive)

    def die(self):
        self.is_alive = False

    def __str__(self):
        return self

    def __repr__(self):
        vect = [f"{self.first_name}", f"{self.eyes}", f"{self.hairs}"]
        return (f"Vector: ({vect[0]}, {vect[1]}, {vect[2]})")
