nums: list[int] = [1, 2, 3, 4, 5, 6]


def binary_search(lst: list[int], target: int) -> int:
    """Binary search"""
    left: int = 0
    right: int = len(lst) - 1  # Index posledního prvku

    while left <= right:
        mid: int = (
            left + (right - left) // 2
        )  # Správný výpočet středu
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1  # Posuň levý ukazatel doprava
        else:
            right = mid - 1  # Posuň pravý ukazatel doleva

    return -1  # Pokud prvek není nalezen
