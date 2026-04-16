from flask import Flask, jsonify, request
import os, csv

app = Flask(__name__)

#Add Product Route
app.route("/add_product", methods=["POST"])
def add_product():
    return

#Read Products Route
app.route("/read_products")
def read_products():
    return

#Delete Product Route
app.route("/delete_product", methods=["DELETE"])
def delete_product():
    return

#Update Products Route
app.route("/update_product", methods=["PUT"])
def update_product():
    return

def read_file():
    products = []

    infile = request.files['products.csv']
    rtfile = os.fdopen(infile.stream.fileno(), 'rt')
    csvreader = csv.reader(rtfile)

    for line in csvreader:
        entry = line.split(",")

        products.append(entry)

    
if __name__ == '__main__':
    app.run()