from flask import Flask, jsonify, request
import os, csv

app = Flask(__name__)

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
    return jsonify(products)

#Update Products Route
@app.route("/update_product", methods=["PUT"])
def update_product():
    return

#
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
                "added_date": row[4]
            }
            products.append(product)

    return products

    
if __name__ == '__main__':
    app.run()