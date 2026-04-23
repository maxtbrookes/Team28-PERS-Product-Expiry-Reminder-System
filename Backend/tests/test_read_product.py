import csv
from app import app, update_items

CSV_FILE = "products.csv"


# CSV setup - reset the csv
def reset_csv():
    data = [
        ["1", "poultry", "chicken", "17/04/2026", "15/04/2026", "0"],
        ["2", "poultry", "liver", "17/04/2026", "15/04/2026", "1"]
    ]

    with open(CSV_FILE, "w", newline="") as f:
        csv.writer(f).writerows(data)


# Helper function tests
def test_read_success():
    reset_csv()

    with open(CSV_FILE) as f:
        rows = list(csv.reader(f))

    assert rows[0][2] == "chicken"
    assert rows[0][1] == "poultry"
    assert rows[0][3] == "17/04/2026"
    assert rows[1][2] == "liver"


# Route tests
def test_read_route_success():
    reset_csv()
    client = app.test_client()

    response = client.get("/read_products")

    assert response.status_code == 200
