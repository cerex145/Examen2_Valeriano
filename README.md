# 🧰 Stockwise API

API REST desarrollada con **Django + Django REST Framework (DRF)** para la gestión de inventarios.  
Permite administrar **Productos** y **Categorías**.

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


## 🧩 Entidades principales

### 🏷️ Categorías
Representan los grupos o tipos de productos del inventario.

| Campo | Tipo | Descripción |
|--------|------|-------------|
| id | Integer | Identificador único |
| name | String | Nombre de la categoría |
| description | Text | Descripción opcional |
| products_count | Integer | Cantidad de productos (solo lectura) |

---

### 📦 Productos
Representan los artículos o ítems del inventario.

| Campo | Tipo | Descripción |
|--------|------|-------------|
| id | Integer | Identificador único |
| name | String | Nombre del producto |
| quantity | Integer | Cantidad disponible |
| price | Decimal | Precio del producto |
| category | ForeignKey | Relación con una categoría |
| category_name | String | Nombre de la categoría (solo lectura, campo personalizado) |

---

## 📚 Endpoints principales

### Categorías (/api/categories/)
| Método | Ruta | Descripción |
|---------|------|-------------|
| GET | /api/categories/ | Lista todas las categorías |
| POST | /api/categories/ | Crea una nueva categoría |
| GET | /api/categories/{id}/ | Muestra detalle de una categoría |
| PUT/PATCH | /api/categories/{id}/ | Edita una categoría |
| DELETE | /api/categories/{id}/ | Elimina una categoría |

---

### Productos (/api/products/)
| Método | Ruta | Descripción |
|---------|------|-------------|
| GET | /api/products/ | Lista todos los productos |
| POST | /api/products/ | Crea un nuevo producto |
| GET | /api/products/{id}/ | Muestra detalle de un producto |
| PUT/PATCH | /api/products/{id}/ | Edita un producto |
| DELETE | /api/products/{id}/ | Elimina un producto |

---

## 🔍 Ejemplos de uso

### ➕ Crear categoría
**POST** /api/categories/
```json
{
  "name": "Electrónica",
  "description": "Dispositivos y gadgets"
}
```

### ➕ Crear producto
**POST** /api/products/
```json
{
  "name": "Mouse inalámbrico",
  "quantity": 50,
  "price": "29.99",
  "category": 1
}
```

### 🔍 Buscar productos
**GET** /api/products/?search=mouse  
**GET** /api/products/?search=Electrónica

### ❌ Eliminar producto
**DELETE** /api/products/1/

---


---

## 🧪 Pruebas manuales recomendadas
1. Crear una categoría.  
2. Crear un producto asociado a esa categoría.  
3. Listar productos y verificar category_name.  
4. Editar un producto (PUT o PATCH).  
5. Eliminar un producto y confirmar que desaparece del listado.

---

## 🧰 Estructura del proyecto
```

├─ config/
│  ├─ settings.py
│  ├─ urls.py
├─ inventory/
│  ├─ models.py
│  ├─ serializers.py
│  ├─ views.py
│  ├─ urls.py
│  └─ tests.py
├─ manage.py
├─ requirements.txt
```
<img width="202" height="567" alt="image" src="https://github.com/user-attachments/assets/78a6bceb-c997-4350-a7e5-ffea2000b7d6" />

---
##Capturas del proyecto 

<img width="1919" height="1001" alt="image" src="https://github.com/user-attachments/assets/c3eab296-45b7-4626-8b2d-e86f803099a8" />
<img width="1919" height="1001" alt="image" src="https://github.com/user-attachments/assets/dd2a58a7-d54b-440c-9b62-da314a00c250" />
<img width="1873" height="611" alt="image" src="https://github.com/user-attachments/assets/9cca5e14-d621-474a-89a9-f183905752a4" />

## Video de la funcionalidad 
https://youtu.be/SIyzycQqVO0

## 🏁 Autor
**Carlos Alberto Valeriano Colán**  
📧 carlos.valeriano@tecsup.edu.pe  
🎓 Tecsup – Diseño y Desarrollo de Software  
📅 Octubre 2025

