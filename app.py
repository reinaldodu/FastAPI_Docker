from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="API de Productos",
    description="Documentación de la API para la gestión de productos.",
    version="1.0.0"
)

# Activar la API para ser consumida desde otro dominio
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # permite cualquier origen (CodePen incluido)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Modelo Pydantic
class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    descripcion: str
    categoria: str

# "Base de datos" simulada
productos = {
    1: {
        "id": 1, 
        "nombre": "Laptop Pro 15", 
        "precio": 3500.0, 
        "categoria": "Tecnología", 
        "descripcion": "Computadora portátil de alto rendimiento ideal para desarrollo de software y diseño gráfico.",
        "stock": 15
    },
    2: {
        "id": 2, 
        "nombre": "Teclado Mecánico RGB", 
        "precio": 120.0, 
        "categoria": "Periféricos", 
        "descripcion": "Teclado con switches mecánicos silenciosos y retroiluminación personalizada.",
        "stock": 40
    },
    3: {
        "id": 3, 
        "nombre": "Mouse Ergonómico Inalámbrico", 
        "precio": 45.5, 
        "categoria": "Periféricos", 
        "descripcion": "Mouse inalámbrico de alta precisión con batería recargable y diseño ergonómico.",
        "stock": 50
    },
    4: {
        "id": 4, 
        "nombre": "Monitor 4K UltraWide", 
        "precio": 900.0, 
        "categoria": "Tecnología", 
        "descripcion": "Pantalla de 34 pulgadas ideal para multitarea y visualización de código sin esfuerzo.",
        "stock": 8
    },
    5: {
        "id": 5, 
        "nombre": "Audífonos con Cancelación de Ruido", 
        "precio": 150.0, 
        "categoria": "Audio", 
        "descripcion": "Auriculares inalámbricos con cancelación activa de ruido para máxima concentración.",
        "stock": 25
    },
    6: {
        "id": 6, 
        "nombre": "Webcam Full HD 1080p", 
        "precio": 200.0, 
        "categoria": "Tecnología", 
        "descripcion": "Cámara web de alta definición con micrófono integrado para reuniones del SENA y streaming.",
        "stock": 18
    },
    7: {
        "id": 7, 
        "nombre": "Micrófono de Condensador USB", 
        "precio": 180.0, 
        "categoria": "Audio", 
        "descripcion": "Micrófono de estudio plug-and-play ideal para podcasts, locución y videollamadas claras.",
        "stock": 12
    },
    8: {
        "id": 8, 
        "nombre": "Silla Ergonómica de Oficina", 
        "precio": 650.0, 
        "categoria": "Mobiliario", 
        "descripcion": "Silla con soporte lumbar ajustable y reposabrazos 3D para largas jornadas de programación.",
        "stock": 10
    },
    9: {
        "id": 9, 
        "nombre": "Escritorio Elevable Eléctrico", 
        "precio": 1200.0, 
        "categoria": "Mobiliario", 
        "descripcion": "Mesa de trabajo ajustable en altura con memoria de posiciones para trabajar de pie o sentado.",
        "stock": 5
    },
    10: {
        "id": 10, 
        "nombre": "Disco Duro Externo 2TB SSD", 
        "precio": 250.0, 
        "categoria": "Almacenamiento", 
        "descripcion": "Unidad de estado sólido portátil ultra rápida para respaldos seguros de tus proyectos.",
        "stock": 30
    },
    11: {
        "id": 11, 
        "nombre": "Hub USB-C Multi-puerto", 
        "precio": 60.0, 
        "categoria": "Accesorios", 
        "descripcion": "Adaptador 7 en 1 con puertos HDMI, USB 3.0 y lector de tarjetas SD para laptops modernas.",
        "stock": 45
    },
    12: {
        "id": 12, 
        "nombre": "Lámpara de Escritorio Inteligente", 
        "precio": 85.0, 
        "categoria": "Accesorios", 
        "descripcion": "Iluminación LED regulable con control de temperatura de color para reducir la fatiga visual.",
        "stock": 22
    }
}

# Ruta raíz
@app.get("/")
def root():
    return {"message": "API FastAPI en Docker funcionando"}

# Listar los productos
@app.get("/productos")
def get_productos():
    return list(productos.values())

# Listar un producto
@app.get("/productos/{producto_id}")
def get_producto(producto_id: int):
    if producto_id not in productos:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return productos[producto_id]

# Crear un producto
@app.post("/productos")
def create_producto(producto: Producto):
    if producto.id in productos:
        raise HTTPException(status_code=400, detail="El ID ya existe")
    productos[producto.id] = producto.dict()
    return {"message": "Producto creado", "item": producto}

# Actualizar un producto
@app.put("/productos/{producto_id}")
def update_producto(producto_id: int, producto: Producto):
    if producto_id not in productos:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    if producto_id != producto.id:
        raise HTTPException(status_code=400, detail="El ID del producto no coincide con la URL")

    productos[producto_id] = producto.dict()
    return {"message": "Producto actualizado", "item": producto}

# Eliminar un producto
@app.delete("/productos/{producto_id}")
def delete_producto(producto_id: int):
    if producto_id not in productos:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    eliminado = productos.pop(producto_id)
    return {"message": "Producto eliminado", "item": eliminado}
