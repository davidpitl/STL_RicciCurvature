import networkit as nk
import trimesh

def import_stl_to_graph(filename):
    # Crear un nuevo grafo
    graph = nk.Graph()

    # Cargar el archivo STL
    mesh = trimesh.load_mesh(filename)

    # Obtener los vértices del archivo STL
    vertices = mesh.vertices

    # Crear los nodos del grafo
    for i, vertex in enumerate(vertices):
        graph.addNode()

    # Crear las aristas del grafo
    for face in mesh.faces:
        u, v, w = face
        graph.addEdge(u, v)
        graph.addEdge(v, w)
        graph.addEdge(w, u)

    return graph

# Ejemplo de uso
filename = "head.stl"
graph = import_stl_to_graph(filename)
print()
