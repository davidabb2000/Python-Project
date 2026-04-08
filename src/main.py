from service import RegisterService

import os

# Ruta absoluta relativa a la ubicación de file.py
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "records.json")

def print_record(r, i):
    print(
        f"[{i}] ID: {r['id']:<6} | "
        f"Nombre: {r['name']:<20} | "
        f"Correo: {r['email']:<25} | "
        f"Edad: {r['age']:<4} | "
        f"Estatus: {r['status']}"
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
    print("\n──── Creando usuarios ────────────────────────────────")
    try_create(service, id="1", name="",  email="peter@gmail.com",  age=42, status="casado")
    try_create(service, id="2", name="Carlos Gomez", email="carlos@gmail.com", age=34, status="soltero")
    try_create(service, id="3", name="Maria Perez",  email="maria@gmail.com",  age=27, status="viudo")

    # ── Duplicate ID ───────────────────────────────────────────
    print("\n──── Intentando duplicar ID ─────────────────────────")
    try_create(service, id="1", name="Luis Torres", email="luis@gmail.com", age=30, status="soltero")

    # ── Invalid fields ─────────────────────────────────────────
    print("\n──── Usuarios invalidos ──────────────────────────────────")
    try_create(service, id="4", name="Ana",  email="not-an-email",   age=25,  status="soltero")
    try_create(service, id="5", name="John", email="john@gmail.com", age=200, status="casado")

    # ── Final listing ──────────────────────────────────────────
    print("\n──── Usuarios en memoria ────────────────────────")
    records = service.list_records()
    for i, r in enumerate(records, start=1):
        print_record(r, i)

    print(f"\n  Total: {len(records)} record(s)")
    print(f"  ID registradas: {service._ids}")
    print("  Informacion guardada en: data/records.json")


if __name__ == "__main__":
    main()