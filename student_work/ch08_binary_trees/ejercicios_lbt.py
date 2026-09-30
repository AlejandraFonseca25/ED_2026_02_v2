from goodrich.ch08.linked_binary_tree import LinkedBinaryTree


def es_completo(T):
    """Retorna True si el LinkedBinaryTree T es completo."""
    if T.is_empty():
        return True

    cola = [T.root()]
    hay_hueco = False

    while cola:
        nodo = cola.pop(0)

        izquierdo = T.left(nodo)
        derecho = T.right(nodo)

        if izquierdo is None:
            hay_hueco = True
        else:
            if hay_hueco:
                return False
            cola.append(izquierdo)

        if derecho is None:
            hay_hueco = True
        else:
            if hay_hueco:
                return False
            cola.append(derecho)

    return True


def camino(T, p, q):
    """Retorna el camino de p a q como string: 'H -> D -> B -> E'."""
    ancestros_p = []
    actual = p
    while actual is not None:
        ancestros_p.append(actual)
        actual = T.parent(actual)

    camino_q = []
    actual = q

    while actual not in ancestros_p:
        camino_q.append(actual)
        actual = T.parent(actual)

    lca = actual
    camino_q.append(lca)

    # Parte p -> LCA.
    camino_p = []
    actual = p
    while actual != lca:
        camino_p.append(actual)
        actual = T.parent(actual)
    camino_p.append(lca)

    camino_q.reverse()

    posiciones = camino_p[:-1] + [lca] + camino_q[1:]
    return " -> ".join(str(pos.element()) for pos in posiciones)


if __name__ == "__main__":
    # tus pruebas (opcional)
    pass
