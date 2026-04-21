import csv
from app import app, read_file

CSV_FILE = "products.csv"

def reset_csv():
    data = [                                         
        ["1", "poultry", "chicken", "17/04/2026", "15/04/2026, 0"],
        ["2", "poultry", "liver", "17/04/2026", "15/04/2026, 1"]
    ]
    with open(CSV_FILE, "w", newline="") as f:
        csv.writer(f).writerows(data)


def test_add_product_success():
    reset_csv()
    client = app.test_client()

    response = client.post("/add_product", json={
        "name": "duck",
        "category": "poultry",
        "expiry_date": "20/04/2026"
    })

    assert response.status_code == 201            
    assert response.get_json()["Success"] == "Product added successfully"  


def test_add_product_written_to_csv():
    reset_csv()
    client = app.test_client()

    client.post("/add_product", json={
        "name": "duck",                            
        "category": "poultry",
        "expiry_date": "20/04/2026"
    })

    products = read_file()                         
    last = products[-1]

    assert last["name"] == "duck"
    assert last["category"] == "poultry"
    assert last["expiry_date"] == "20/04/2026"
    assert last["id"] == "3"