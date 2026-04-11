# Estructura del proyecto

gestion-info/
├─ README.md                         
├─ requirements.txt
├─ .gitignore
├─ data/
│  └─ records.json                # o registros.csv / registros.txt
└─ src/
      ├─ main.py                    # punto de entrada
      ├─ menu.py                    # interfaz de consola
      ├─ service.py                 # CRUD
      ├─ file.py                    # leer y guardar
      ├─ validate.py                # validaciones
      └─ integration.py             # faker

# Instalacion
1. Asegúrate de tener Python 3.8+ instalado.
2. Clona o descarga el proyecto.
3. Instala las dependencias: `pip install -r requirements.txt`
4. Ejecuta el programa: `python src/main.py`

# Pruebas
Para ejecutar las pruebas, usa:
```
python -m pytest tests/
```
Asegúrate de tener pytest instalado (incluido en requirements.txt).

# Uso
Ejecuta el programa y selecciona las opciones del menú:
- Crear, listar, buscar, actualizar o eliminar registros.
- Generar registros falsos usando Faker (opción 6).

Los registros se almacenan en `data/records.json`.

# Creditos/Autores
Quien mantiene el proyecto y contribuciones

# Licencia
Informacion sobre el uso permitido del codigo