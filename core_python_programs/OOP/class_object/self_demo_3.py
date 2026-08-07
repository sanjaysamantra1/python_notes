class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"Year:{self.year} Brand:{self.brand} Model:{self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()