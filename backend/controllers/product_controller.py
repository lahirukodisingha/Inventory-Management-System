from pymongo import MongoClient
from models.product_model import Product

# Database එක සම්බන්ධ කිරීම
client = MongoClient("mongodb://localhost:27017/")
db = client["inventory_management_db"]
products_collection = db["products"]

# 1. අලුත් භාණ්ඩයක් ඇතුලත් කිරීමේ Logic එක
def create_product(data):
    try:
        # ප්‍රොජෙක්ට් ප්‍රපෝසල් එකට අනුව අත්‍යවශ්‍ය දත්ත තිබේදැයි බැලීම
        required_fields = ["sku", "name", "brand", "category", "unit", "cost_price", "selling_price"]
        for field in required_fields:
            if field not in data or not data[field]:
                return {"error": f"Missing or empty required field: {field}"}, 400

        # SKU එක කලින්ම database එකේ තියෙනවද බලන්න (SKU එක unique විය යුතුයි)
        if products_collection.find_one({"sku": data["sku"]}):
            return {"error": "Product with this SKU already exists!"}, 400

        # Product Model එක භාවිතයෙන් අලුත් Object එකක් සෑදීම
        new_product = Product(
            sku=data["sku"],
            name=data["name"],
            brand=data["brand"],
            category=data["category"],
            unit=data["unit"],
            cost_price=data["cost_price"],
            selling_price=data["selling_price"]
        )

        # Database එකට Dictionary එකක් විදිහට සේව් කිරීම
        result = products_collection.insert_one(new_product.to_dict())
        return {"message": "Product added successfully!", "id": str(result.inserted_id)}, 201

    except Exception as e:
        return {"error": str(e)}, 500

# 2. තියෙන හැම භාණ්ඩයක්ම නැවත ලබාගැනීමේ Logic එක
def get_all_products():
    try:
        # Database එකේ තියෙන ඔක්කොම අරගෙන ලැයිස්තුවක් (List) සෑදීම
        # JSON වලට හරවන්න ලේසි වෙන්න MongoDB වල දෙන _id එක මෙතනදී අත්හරිනවා
        products = list(products_collection.find({}, {"_id": 0}))
        return {"products": products}, 200
    except Exception as e:
        return {"error": str(e)}, 500