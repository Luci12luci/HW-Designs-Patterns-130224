class Pasta:
    def __init__(self):
        self.pasta = None
        self.sauce = None
        self.topping = None
        self.dressing = None

#
class PastaBuilder:
    def __init__(self):
        self.pasta = None

    def create_pasta(self):
        self.pasta = Pasta()

    def add_type(self, pasta_type):
        self.type = pasta_type

    def add_sauce(self, sauce):
        self.sauce = sauce

    def add_dressing(self, dressing):
         self.dressing = dressing

    def add_topping(self, topping):
        self.topping = topping


class Spaghetti(Pasta):
    def __init__(self):
        self.type = None
        self.sauce = None
        self.dressing = None
        self.topping = None

    def add_type(self, pasta_type):
        self.type = pasta_type

    def add_sauce(self, sauce):
        self.sauce = sauce

    def add_dressing(self, dressing):
        self.dressing = dressing

    def add_topping(self, topping):
        self.topping = topping

builder = PastaBuilder()

builder.create_pasta()
builder.add_type("spaghetti")
builder.add_sauce("bolognese")
builder.add_dressing("none")
builder.add_topping("cheese")
spaghetti = builder.type()
print(spaghetti)