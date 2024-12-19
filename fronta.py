"""Fronta"""


class Fronta:
    """Implementace fronty (FIFO)"""

    def __init__(self) -> None:
        self.fronta: list = []

    def enqueue(self, item):
        """Přidat prvek do fronty"""
        self.fronta.append(item)

    def dequeue(self):
        """Odebrat prvek z fronty"""
        if self.is_empty():
            raise IndexError("Fronta je prázdná!")
        return self.fronta.pop(0)

    def is_empty(self) -> bool:
        """Je fronta prázdná?"""
        return len(self.fronta) == 0

    def size(self) -> int:
        """Velikost fronty"""
        return len(self.fronta)


if __name__ == "__main__":
    pass
