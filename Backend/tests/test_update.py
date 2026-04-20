import csv
from app import app, update_items

CSV_FILE = "products.csv"


# CSV setup
def reset_csv():
    data = [
        ["1", "poultry", "chicken", "17/04/2026", "15/04/2026"],
        ["2", "poultry", "liver", "17/04/2026", "15/04/2026"]
    ]

    with open(CSV_FILE, "w", newline="") as f:
        csv.writer(f).writerows(data)


# Helper function test

def test_update_items_success():
    reset_csv()

    result = update_items("1", "duck", "poultry", "20/04/2026")
    assert result is True

    with open(CSV_FILE) as f:
        rows = list(csv.reader(f))

    assert rows[0][2] == "duck"
    assert rows[0][1] == "poultry"
    assert rows[0][3] == "20/04/2026"


def test_update_items_not_found():
    reset_csv()

    result = update_items("999", "duck", "poultry", "20/04/2026")
    assert result is False


# Route test

def test_update_product_route_success():
    reset_csv()
    client = app.test_client()

    response = client.put("/update_product", json={
        "id": "1",
        "name": "duck",
        "category": "poultry",
        "expiry_date": "20/04/2026"
    })

    assert response.status_code == 200
    assert response.get_json()["Success"] == "Product updated successfully"


def test_update_product_route_not_found():
    reset_csv()
    client = app.test_client()

    response = client.put("/update_product", json={
        "id": "999",
        "name": "duck",
        "category": "poultry",
        "expiry_date": "20/04/2026"
    })

    assert response.status_code == 404
    assert response.get_json()["Error"] == "Product not found"