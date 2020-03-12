class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return (f"name: {self.name} \n description: {self.description} ")

    def on_take(self):
        pass


class Rock(Item):
    def __init__(self, name, description):
        super().__init__("rock", "this is a small rock")

    def __str__(self):
        return (f"name: {self.name} \n description: {self.description} ")


class Sword(Item):
    def __init__(self, name, description):
        super().__init__("sword", "this is an old sword")


class Coin(Item):
    def __init__(self, name, description):
        super().__init__("sword", "this is an coin")


class Key(Item):
    def __init__(self, name, description):
        super().__init__("key", "this is an silver key")
