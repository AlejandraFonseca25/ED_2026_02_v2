from PIL import Image, ImageDraw
from IPython.display import display


class Heap:

    def __init__(self):
        self.arreglo = [float('-inf')]

    def insert(self, valor, imagen=False):
        self.arreglo.append(valor)
        ih = len(self.arreglo) - 1
        ip = ih // 2
        while self.arreglo[ip] > self.arreglo[ih]:
            self.arreglo[ip], self.arreglo[ih] = self.arreglo[ih], self.arreglo[ip]
            ih = ip
            ip = ip // 2
        if imagen:
            self.mostrar()

    def _bajar(self, ip):
        while 2*ip < len(self.arreglo):
            im = 2*ip
            if 2*ip + 1 < len(self.arreglo) and self.arreglo[2*ip + 1] < self.arreglo[im]:
                im = 2*ip + 1
            if self.arreglo[ip] > self.arreglo[im]:
                self.arreglo[ip], self.arreglo[im] = self.arreglo[im], self.arreglo[ip]
                ip = im
            else:
                break

    def remove_smallest(self, imagen=False):
        if len(self.arreglo) == 1:
            return None
        minimo = self.arreglo[1]
        valor = self.arreglo.pop()
        if len(self.arreglo) > 1:
            self.arreglo[1] = valor
            self._bajar(1)
        if imagen:
            self.mostrar()
        return minimo

    def build_heap(self, lista, imagen=False):
        self.arreglo = [float('-inf')] + list(lista)
        ip = len(lista) // 2
        while ip >= 1:
            self._bajar(ip)
            ip -= 1
        if imagen:
            self.mostrar()

    def mostrar(self):
        a = self.arreglo
        n = len(a) - 1
        niveles = max(n.bit_length(), 1)
        ancho = max(2 ** (niveles - 1) * 50, 200)
        alto = niveles * 80 + 20
        img = Image.new('RGB', (ancho, alto), 'white')
        d = ImageDraw.Draw(img)
        pos = {}
        for i in range(1, n + 1):
            nivel = i.bit_length() - 1
            pos[i] = ((i - 2 ** nivel + 0.5) * ancho / 2 ** nivel, 40 + nivel * 80)
        for i in range(2, n + 1):
            d.line([pos[i // 2], pos[i]], fill='black', width=2)
        for i in range(1, n + 1):
            x, y = pos[i]
            d.ellipse([x - 20, y - 20, x + 20, y + 20], fill='lightblue', outline='black', width=2)
            d.text((x, y), str(a[i]), fill='black', anchor='mm')
        display(img)
