class BubbleSortVisualizer:
    def __init__(self, title):
        self.title = title
        self.array = []

    def setup(self, array):
        self.array = array

    def get_main_module(self):
        return self.array

    def draw(self):
        print(f"{self.title}: {self.array}")

    def end(self):
        return False

class Dummy:
    def __init__(self, title):
        self.title = title

    def setup(self, module):
        pass

    def get_main_module(self):
        return []

    def draw(self):
        pass

    def end(self):
        return False