# 🧰 Stockwise API

API REST desarrollada con **Django + Django REST Framework (DRF)** para la gestión de inventarios.  
Permite administrar **Productos** y **Categorías**, cumpliendo con todas las funcionalidades solicitadas en la consigna del curso.

---

## 👨‍💻 Desarrollado por
**Carlos Alberto Valeriano Colán**  
Estudiante de Diseño y Desarrollo de Software – Tecsup

---

## 🚀 Tecnologías utilizadas
- Python 3.10+
- Django 4.2+
- Django REST Framework 3.14+
- Django Filter 23.1+

---

## ⚙️ Instalación y ejecución

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/<tu-usuario>/stockwise_api.git
cd stockwise_api
2️⃣ Crear y activar entorno virtual
bash
Copiar código
python -m venv venv
venv\Scripts\activate     # En Windows
# source venv/bin/activate  # En Linux / macOS
3️⃣ Instalar dependencias
bash
Copiar código
pip install -r requirements.txt
4️⃣ Ejecutar migraciones
bash
Copiar código
python manage.py makemigrations
python manage.py migrate
5️⃣ Iniciar el servidor
bash
Copiar código
python manage.py runserver
La API estará disponible en:
👉 http://127.0.0.1:8000/api/

🧩 Entidades principales
🏷️ Categorías
Representan los grupos o tipos de productos del inventario.

Campo	Tipo	Descripción
id	Integer	Identificador único
name	String	Nombre de la categoría
description	Text	Descripción opcional
products_count	Integer	Cantidad de productos (solo lectura)

📦 Productos
Representan los artículos o ítems del inventario.

Campo	Tipo	Descripción
id	Integer	Identificador único
name	String	Nombre del producto
quantity	Integer	Cantidad disponible
price	Decimal	Precio del producto
category	ForeignKey	Relación con una categoría
category_name	String	Nombre de la categoría (solo lectura, campo personalizado)

🔗 Relación entre entidades
Cada producto pertenece a una categoría (ForeignKey con on_delete=models.CASCADE).
Esto significa que si se elimina una categoría, también se eliminan los productos asociados.

📚 Endpoints principales
Categorías (/api/categories/)
Método	Ruta	Descripción
GET	/api/categories/	Lista todas las categorías
POST	/api/categories/	Crea una nueva categoría
GET	/api/categories/{id}/	Muestra detalle de una categoría
PUT/PATCH	/api/categories/{id}/	Edita una categoría
DELETE	/api/categories/{id}/	Elimina una categoría

Productos (/api/products/)
Método	Ruta	Descripción
GET	/api/products/	Lista todos los productos
POST	/api/products/	Crea un nuevo producto
GET	/api/products/{id}/	Muestra detalle de un producto
PUT/PATCH	/api/products/{id}/	Edita un producto
DELETE	/api/products/{id}/	Elimina un producto
GET	/api/products/?search=texto	Búsqueda por nombre de producto o categoría

🔍 Ejemplos de uso (en Postman o navegador)
➕ Crear categoría
POST /api/categories/

json
Copiar código
{
  "name": "Electrónica",
  "description": "Dispositivos y gadgets"
}
➕ Crear producto
POST /api/products/

json
Copiar código
{
  "name": "Mouse inalámbrico",
  "quantity": 50,
  "price": "29.99",
  "category": 1
}
🔍 Buscar productos
GET /api/products/?search=mouse
GET /api/products/?search=Electrónica

❌ Eliminar producto
DELETE /api/products/1/

