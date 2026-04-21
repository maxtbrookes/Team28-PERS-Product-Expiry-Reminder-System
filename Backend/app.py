from flask import Flask, jsonify, request
from flask_cors import CORS
import os, csv


app = Flask(__name__)
CORS(app)

#Add Product Route
@app.route("/add_product", methods=["POST"])
def add_product():
    return

#Read Products Route
@app.route("/read_products")
def read_products():
    products = read_file()
    return jsonify(products)

#Delete Product Route
@app.route("/delete_product", methods=["DELETE"])
def delete_product():
    products = read_file()

    data = request.get_json()
    id = data.get('id')

    for product in products:
        if id == product["id"]:
            if delete_item(id):
                return jsonify({"Success": "Product deleted successfully"}), 200
            else:
                return jsonify({"Error": "Product not deleted!"}), 500
    return jsonify({"Error": "Id does not exist"}), 404

#Update Products Route
@app.route("/update_product", methods=["PUT"])
def update_product():
    data = request.get_json()

    id = data.get("id")
    name = data.get("name")
    category = data.get("category")
    expiry_date = data.get("expiry_date")

    if update_items(id, name, category, expiry_date):
        return jsonify({"Success": "Product updated successfully"}), 200

    return jsonify({"Error": "Product not found"}), 404

#Read CSV file function
def read_file():
    products = []

    with open("products.csv", "r") as f:
        reader = csv.reader(f)

        for row in reader:
            product = {
                "id": row[0],
                "category": row[1],
                "name": row[2],
                "expiry_date": row[3],
                "added_date": row[4],
                "opened": row[5]
            }
            products.append(product)

    return products

#Delete an item from the CSV
def delete_item(id):
    is_deleted = False

    products = []
    with open('products.csv', 'r') as inp:
        for row in csv.reader(inp):
            if row[0] != id:
                products.append(row)
            else:
                is_deleted = True

    with open('products.csv', 'w', newline='') as out:
        writer = csv.writer(out)
        writer.writerows(products)
        return is_deleted

#Update the list based on update
def update_items(id, name, category, expiry_date):
    products = read_file()
    updated = False

    for product in products:
        if product["id"] == id:
            product["name"] = name
            product["category"] = category
            product["expiry_date"] = expiry_date
            updated = True
            break

    if updated:
        with open("products.csv", "w", newline="") as f:
            writer = csv.writer(f)

            for p in products:
                writer.writerow([
                    p["id"],
                    p["category"],
                    p["name"],
                    p["expiry_date"],
                    p["added_date"]
                ])
    return updated

    
if __name__ == '__main__':
    app.run()