import { useEffect, useState } from "react";

export default function App() {
  const [productos, setProductos] = useState([]);
  const [cargando, setCargando] = useState(true);
  const [error, setError] = useState(null);

  // URL de tu API de FastAPI corriendo en Docker
  const API_URL = "http://localhost:8000/productos";

  useEffect(() => {
    fetch(API_URL)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Error al conectar con la API de productos");
        }
        return response.json();
      })
      .then((data) => {
        setProductos(data);
        setCargando(false);
      })
      .catch((err) => {
        setError(err.message);
        setCargando(false);
      });
  }, []);

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col justify-center items-center p-6 font-sans">
      <div className="w-full max-w-4xl bg-white rounded-2xl shadow-xl p-8">
        {/* Encabezado Centrado */}
        <header className="text-center mb-8 border-b border-gray-100 pb-6">
          <h1 className="text-3xl font-extrabold text-green-700 tracking-tight">
            Gestión de Productos
          </h1>
          <p className="text-sm text-gray-500 mt-2">
            Proyecto SENA - Integración FastAPI + Docker + React (Vite)
          </p>
        </header>

        {/* Estado: Cargando */}
        {cargando && (
          <div className="flex flex-col items-center justify-center py-12 animate-pulse">
            <div className="rounded-full bg-blue-500 h-10 w-10 mb-4"></div>
            <p className="text-gray-600 font-medium">
              Obteniendo productos desde la API...
            </p>
          </div>
        )}

        {/* Estado: Error de Conexión */}
        {error && (
          <div className="bg-red-50 border-l-4 border-red-500 p-4 rounded-md my-4 text-center">
            <p className="text-red-700 font-semibold">⚠️ Ocurrió un error:</p>
            <p className="text-red-600 text-sm mt-1">{error}</p>
            <p className="text-xs text-gray-400 mt-2">
              Revisa si tu contenedor Docker está activo en el puerto 8000.
            </p>
          </div>
        )}

        {/* Estado: Lista Vacía */}
        {!cargando && !error && productos.length === 0 && (
          <div className="text-center py-12 bg-gray-50 rounded-xl border border-dashed border-gray-300">
            <p className="text-gray-500 font-medium">
              No hay productos registrados en la base de datos.
            </p>
          </div>
        )}

        {/* Contenedor Principal: Tarjetas de Productos */}
        {!cargando && !error && productos.length > 0 && (
          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
            {productos.map(
              (
                producto: {
                  id: number;
                  nombre: string;
                  precio: number;
                  descripcion: string;
                  categoria: string;
                },
                index,
              ) => (
                <div
                  key={producto.id || index}
                  className="bg-white border border-gray-200 rounded-xl p-5 hover:shadow-md transition-shadow duration-200 flex flex-col justify-between"
                >
                  <div>
                    <div className="flex justify-between items-start mb-2">
                      <h3 className="text-lg font-bold text-gray-800 capitalize truncate">
                        {producto.nombre || "Producto sin nombre"}
                      </h3>
                      <span className="bg-blue-50 text-blue-700 text-xs font-semibold px-2.5 py-0.5 rounded-full">
                        {producto.categoria || "General"}
                      </span>
                    </div>
                    <p className="text-gray-600 text-sm line-clamp-3 mb-4">
                      {producto.descripcion || "Sin descripción disponible."}
                    </p>
                  </div>

                  <div className="border-t border-gray-100 pt-3 flex justify-between items-center mt-auto">
                    <span className="text-xl font-black text-green-600">
                      ${Number(producto.precio || 0).toLocaleString("es-CO")}
                    </span>
                  </div>
                </div>
              ),
            )}
          </div>
        )}

        {/* Pie de página informativo */}
        <footer className="mt-8 pt-4 border-t border-gray-100 text-center text-xs text-gray-400">
          Consumiendo:{" "}
          <code className="bg-gray-100 px-1 py-0.5 rounded text-red-500">
            {API_URL}
          </code>
        </footer>
      </div>
    </div>
  );
}
