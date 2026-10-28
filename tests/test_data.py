import csv
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from generate_data import generate, ROOT as DATA_ROOT


def load(name):
    with (DATA_ROOT / name).open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


class TestDataset(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        generate()

    def test_dimensions(self):
        self.assertEqual(len(load("dim_customer.csv")), 150)
        self.assertEqual(len(load("dim_product.csv")), 16)
        self.assertEqual(len(load("dim_seller.csv")), 6)
        self.assertEqual(len(load("fact_targets.csv")), 3)
        self.assertEqual(len(load("dim_date.csv")), 1096)

    def test_fact_integrity(self):
        rows = load("fact_sales.csv")
        self.assertEqual(len(rows), 2400)
        self.assertEqual(len({r["OrderID"] for r in rows}), 2400)
        self.assertEqual(sum(r["Status"] == "Cancelled" for r in rows), 141)
        for r in rows:
            self.assertIn(int(r["CustomerID"]), range(1, 151))
            self.assertIn(int(r["ProductID"]), range(1, 17))
            self.assertIn(int(r["SellerID"]), range(1, 7))
            self.assertGreater(int(r["Quantity"]), 0)
            self.assertGreaterEqual(float(r["UnitPrice"]), float(r["UnitCost"]))

    def test_recognized_revenue(self):
        rows = load("fact_sales.csv")
        revenue = sum(int(r["Quantity"]) * float(r["UnitPrice"]) * (1 - float(r["DiscountPct"]))
                      for r in rows if r["Status"] == "Completed")
        self.assertGreater(revenue, 0)
        self.assertEqual(sum(r["Status"] == "Completed" for r in rows), 2259)


if __name__ == "__main__":
    unittest.main()
