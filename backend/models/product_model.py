class Product:
    def __init__(self, sku, name, brand, category, unit, cost_price, selling_price):
        self.sku = sku
        self.name = name
        self.brand = brand
        self.category = category
        self.unit = unit
        self.cost_price = cost_price
        self.selling_price = selling_price

    # Database එකට තේරෙන විදිහට (Dictionary එකක් විදිහට) දත්ත ටික හදාගන්නවා
    def to_dict(self):
        return {
            "sku": self.sku,
            "name": self.name,
            "brand": self.brand,
            "category": self.category,
            "unit": self.unit,
            "cost_price": float(self.cost_price),
            "selling_price": float(self.selling_price)
        }