class Heap:
    def __init__(self):
        self.arreglo = [float('-inf')]

    def insert(self, valor):
        self.arreglo.append(valor)
        i = len(self.arreglo) - 1
        # Sube el valor mientras sea menor que su padre
        while i > 1 and self.arreglo[i] < self.arreglo[i // 2]:
            self.arreglo[i], self.arreglo[i // 2] = self.arreglo[i // 2], self.arreglo[i]
            i = i // 2

    def remove_smallest(self):
        if len(self.arreglo) <= 1:
            return None  # heap vacío

        smallest = self.arreglo[1]
        # Mueve el último elemento a la raíz
        last = self.arreglo.pop()
        if len(self.arreglo) > 1:
            self.arreglo[1] = last
            self._sift_down(1)

        return smallest

    def _sift_down(self, i):
        n = len(self.arreglo) - 1
        while True:
            izq, der = 2 * i, 2 * i + 1
            menor = i

            if izq <= n and self.arreglo[izq] < self.arreglo[menor]:
                menor = izq
            if der <= n and self.arreglo[der] < self.arreglo[menor]:
                menor = der

            if menor == i:
                break

            self.arreglo[i], self.arreglo[menor] = self.arreglo[menor], self.arreglo[i]
            i = menor

    def build_heap(self, lista):
        self.arreglo = [float('-inf')] + list(lista)
        n = len(self.arreglo) - 1
        for i in range(n // 2, 0, -1):
            self._sift_down(i)
