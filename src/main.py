from service import RegisterService

import os

# Ruta absoluta relativa a la ubicación de file.py
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "records.json")

def print_record(r, i):
    print(
        f"[{i}] ID: {r['id']:<6} | "
        f"Name: {r['name']:<20} | "
        f"Email: {r['email']:<25} | "
        f"Age: {r['age']:<4} | "
        f"Status: {r['status']}"
    )


def try_create(service, **kwargs):
    try:
        service.create_record(**kwargs)
        print(f"  ✓ Record created → ID='{kwargs.get('id')}'")
    except ValueError as e:
        print(f"  ✗ Rejected → ID='{kwargs.get('id')}'\n    {e}")


def main():
    service = RegisterService()

    # ── Valid records ──────────────────────────────────────────
    print("\n──── Creating records ────────────────────────────────")
    try_create(service, id="1", name="Peter Smith",  email="peter@gmail.com",  age=42, status="married")
    try_create(service, id="2", name="Carlos Gomez", email="carlos@gmail.com", age=34, status="widowed")
    try_create(service, id="3", name="Maria Perez",  email="maria@gmail.com",  age=27, status="single")

    # ── Duplicate ID ───────────────────────────────────────────
    print("\n──── Attempting duplicate ID ─────────────────────────")
    try_create(service, id="1", name="Luis Torres", email="luis@gmail.com", age=30, status="single")

    # ── Invalid fields ─────────────────────────────────────────
    print("\n──── Invalid fields ──────────────────────────────────")
    try_create(service, id="4", name="Ana",  email="not-an-email",   age=25,  status="single")
    try_create(service, id="5", name="John", email="john@gmail.com", age=200, status="married")

    # ── Final listing ──────────────────────────────────────────
    print("\n──── Records in memory & file ────────────────────────")
    records = service.list_records()
    for i, r in enumerate(records, start=1):
        print_record(r, i)

    print(f"\n  Total: {len(records)} record(s)")
    print(f"  Registered IDs (set): {service._ids}")
    print("  Data saved to → data/records.json")


if __name__ == "__main__":
    main()