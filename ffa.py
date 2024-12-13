class Grafo:
    def __init__(self, tam):
        self.matrizAdyacencia = [[0] * tam for _ in range(tam)]
        self.tam = tam
        self.datosVertices = [''] * tam

    def anadirArista(self, u, v, c):
        self.matrizAdyacencia[u][v] = c

    def anadirVertice(self, vertice, nombre):
        if 0 <= vertice < self.tam:
            self.datosVertices[vertice] = nombre

    def busqPrimeroEnProfundidad(self, s, t, visitados=None, camino=None):
        if visitados is None:
            visitados = [False] * self.tam
        if camino is None:
            camino = []

        visitados[s] = True
        camino.append(s)

        if s == t:
            return camino

        for ind, val in enumerate(self.matrizAdyacencia[s]):
            if not visitados[ind] and val > 0:
                caminoResultado = self.busqPrimeroEnProfundidad(ind, t, visitados, camino.copy())
                if caminoResultado:
                    return caminoResultado

        return None

    def fordFulkerson(self, origen, destino):
        capMaxima = 0

        camino = self.busqPrimeroEnProfundidad(origen, destino)
        while camino:
            flujoCamino = float("Inf")
            for i in range(len(camino) - 1):
                u, v = camino[i], camino[i + 1]
                flujoCamino = min(flujoCamino, self.matrizAdyacencia[u][v])

            for i in range(len(camino) - 1):
                u, v = camino[i], camino[i + 1]
                self.matrizAdyacencia[u][v] -= flujoCamino
                self.matrizAdyacencia[v][u] += flujoCamino

            capMaxima += flujoCamino

            nombresCamino = [self.datosVertices[node] for node in camino]
            print("Camino:", " -> ".join(nombresCamino))
            print("     Flujo:", flujoCamino)

            camino = self.busqPrimeroEnProfundidad(origen, destino)

        return capMaxima

def tratarCaso(f):

    g = Grafo(int(next(f)))
    nombreVertices = next(f).split()
    for i, nombre in enumerate(nombreVertices):
        g.anadirVertice(i, nombre)

    numAristas = int(next(f))
    for i in range(numAristas):
        o, d, c = next(f).split()
        g.anadirArista(int(o), int(d), int(c))

    origen, destino = next(f).split()

    print("Estudiando grafo con la siguiente matriz de adyacencia:")
    [print(*line) for line in g.matrizAdyacencia]
    print()
    print("\nLa capacidad maxima encontrada es %d \n" % g.fordFulkerson(int(origen ), int(destino)))
    print("=============================================================")

with open('casos.in', 'r') as f:
    numCasos = int(next(f))
    i = 0
    while i < numCasos:
        tratarCaso(f)
        i+=1