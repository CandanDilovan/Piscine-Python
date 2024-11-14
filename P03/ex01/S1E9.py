from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class"""
    first_name = None
    is_alive = True

    def __init__(self, name: str, is_alive=True):
        """Your docstring for Constructor"""
        if name:
            self.first_name = name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        pass


class Stark(Character):
    """Your docstring for Class"""
    def die(self):
        """Your docstring for Method"""
        self.is_alive = False
