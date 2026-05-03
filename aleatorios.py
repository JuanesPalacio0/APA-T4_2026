"""

Clases:
    - Aleat: Iterador de números pseudoaleatorios configurable.

Funciones:
    - aleat: Generador que permite reinicio con .send().

Ejecuta los tests unitarios al correr el módulo directamente.
"""

class Aleat:
    """
    Clase Aleat que implementa un generador de números aleatorios
    en el rango 0 <= x_n < m usando el método LGC.

    Atributos:
    - m: Módulo del algoritmo.
    - a: Multiplicador.
    - c: Incremento.
    - x: Estado interno (último valor generado).

    Métodos:
    - __next__: Genera el siguiente número pseudoaleatorio.
    - __call__: Reinicia la secuencia con una nueva semilla.

    >>> rand = Aleat(m=32, a=9, c=13, X0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    16
    29
    18
    15

    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    18
    15
    20
    1
    """

    def __init__(self, *, m=2**48, a=25214903917, c=11, X0=1212121):
        self.m = m
        self.a = a
        self.c = c
        self.x = X0

    def __next__(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __call__(self, X0):
        self.x = X0


def aleat(*, m=2**48, a=25214903917, c=11, X0=1212121):
    """
    Generador aleatorio usando LGC. Permite reinicio con .send().

    Argumentos:
    - m: módulo (por defecto 2^48)
    - a: multiplicador (por defecto estándar POSIX)
    - c: incremento (por defecto 11)
    - X0: semilla inicial

    >>> rand = aleat(m=64, a=5, c=46, X0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    34
    24
    38
    44

    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    44
    10
    32
    14
    """
    x = X0
    while True:
        x = (a * x + c) % m
        new_seed = yield x
        if new_seed is not None:
            x = new_seed


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
