"""Generate reproducible synthetic star-schema CSVs for Power BI. Python standard library only."""
import csv
import random
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "data"
SEED = 20261028


def write(name, fields, rows):
    ROOT.mkdir(parents=True, exist_ok=True)
    with (ROOT / name).open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def generate():
    rng = random.Random(SEED)
    dates = [date(2024, 1, 1) + timedelta(days=i) for i in range((date(2026, 12, 31) - date(2024, 1, 1)).days + 1)]
    write("dim_date.csv", ["Date", "Year", "MonthNumber", "MonthName", "YearMonth", "Quarter"],
          [{"Date": d.isoformat(), "Year": d.year, "MonthNumber": d.month,
            "MonthName": d.strftime("%B"), "YearMonth": d.strftime("%Y-%m"),
            "Quarter": f"Q{(d.month - 1) // 3 + 1}"} for d in dates])
    regions = ["Sudeste", "Sul", "Nordeste", "Centro-Oeste", "Norte"]
    customers = [{"CustomerID": i, "CustomerName": f"Cliente {i:03d}",
                  "Segment": ["SMB", "Mid-Market", "Enterprise"][i % 3],
                  "Region": regions[i % len(regions)]} for i in range(1, 151)]
    write("dim_customer.csv", list(customers[0]), customers)
    products = [{"ProductID": i, "ProductName": f"Produto {i:02d}",
                 "Category": ["Software", "Consultoria", "Treinamento", "Suporte"][i % 4],
                 "StandardCost": 45 + (i * 17) % 180,
                 "ListPrice": 180 + (i * 43) % 650} for i in range(1, 17)]
    write("dim_product.csv", list(products[0]), products)
    sellers = [{"SellerID": i, "SellerName": name, "Team": "Inside Sales" if i <= 3 else "Field Sales"}
               for i, name in enumerate(["Marina", "Rafael", "Camila", "Bruno", "Luiza", "Diego"], 1)]
    write("dim_seller.csv", list(sellers[0]), sellers)
    orders = []
    for i in range(1, 2401):
        product = products[rng.randrange(len(products))]
        quantity = rng.randint(1, 6)
        discount = [0, 0.05, 0.1, 0.15][rng.randrange(4)]
        orders.append({"OrderID": i, "Date": dates[rng.randrange(len(dates))].isoformat(),
                       "CustomerID": rng.randint(1, 150), "ProductID": product["ProductID"],
                       "SellerID": rng.randint(1, 6), "Quantity": quantity,
                       "UnitPrice": product["ListPrice"], "UnitCost": product["StandardCost"],
                       "DiscountPct": discount,
                       "Status": "Cancelled" if i % 17 == 0 else "Completed"})
    write("fact_sales.csv", list(orders[0]), orders)
    goals = [{"Year": year, "RevenueTarget": target} for year, target in
             [(2024, 1100000), (2025, 1250000), (2026, 1450000)]]
    write("fact_targets.csv", ["Year", "RevenueTarget"], goals)
    return len(orders)


if __name__ == "__main__":
    print(f"Generated {generate()} synthetic sales rows in {ROOT}")
