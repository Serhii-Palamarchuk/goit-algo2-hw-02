"""
Завдання 1: Пошук максимального та мінімального елементів
Метод "розділяй і володарюй"
"""

from typing import Tuple


def find_min_max(arr: list) -> Tuple[int, int]:
    """
    Знаходить мінімальний та максимальний елементи в масиві
    використовуючи метод "розділяй і володарюй".

    Args:
        arr: Масив чисел довільної довжини

    Returns:
        Кортеж (мінімум, максимум)

    Складність: O(n)
    """
    # Базові випадки
    n = len(arr)

    if n == 1:
        # Один елемент - він є і мінімумом, і максимумом
        return (arr[0], arr[0])

    if n == 2:
        # Два елементи - порівнюємо їх між собою
        if arr[0] < arr[1]:
            return (arr[0], arr[1])
        else:
            return (arr[1], arr[0])

    # Рекурсивний випадок: розділяємо масив на дві половини
    mid = n // 2

    # Знаходимо мін/макс для лівої половини
    left_min, left_max = find_min_max(arr[:mid])

    # Знаходимо мін/макс для правої половини
    right_min, right_max = find_min_max(arr[mid:])

    # Комбінуємо результати
    overall_min = min(left_min, right_min)
    overall_max = max(left_max, right_max)

    return (overall_min, overall_max)


def test_find_min_max():
    """Тестування функції пошуку мін/макс"""

    # Тест 1: Масив з 10 елементів
    test1 = [3, 7, 1, 9, 4, 6, 2, 8, 5, 0]
    min_val, max_val = find_min_max(test1)
    print(f"Тест 1: {test1}")
    print(f"Мінімум: {min_val}, Максимум: {max_val}")
    print(f"Очікується: Мінімум: 0, Максимум: 9")
    print()

    # Тест 2: Масив з негативними числами
    test2 = [-5, 3, -10, 15, 0, -3, 8]
    min_val, max_val = find_min_max(test2)
    print(f"Тест 2: {test2}")
    print(f"Мінімум: {min_val}, Максимум: {max_val}")
    print(f"Очікується: Мінімум: -10, Максимум: 15")
    print()

    # Тест 3: Масив з одним елементом
    test3 = [42]
    min_val, max_val = find_min_max(test3)
    print(f"Тест 3: {test3}")
    print(f"Мінімум: {min_val}, Максимум: {max_val}")
    print(f"Очікується: Мінімум: 42, Максимум: 42")
    print()

    # Тест 4: Масив з двома елементами
    test4 = [100, 50]
    min_val, max_val = find_min_max(test4)
    print(f"Тест 4: {test4}")
    print(f"Мінімум: {min_val}, Максимум: {max_val}")
    print(f"Очікується: Мінімум: 50, Максимум: 100")
    print()

    # Тест 5: Великий масив
    test5 = list(range(100, 0, -1))  # 100, 99, 98, ..., 1
    min_val, max_val = find_min_max(test5)
    print(f"Тест 5: Масив від 100 до 1 (100 елементів)")
    print(f"Мінімум: {min_val}, Максимум: {max_val}")
    print(f"Очікується: Мінімум: 1, Максимум: 100")
    print()

    # Тест 6: Масив з однаковими елементами
    test6 = [5, 5, 5, 5, 5]
    min_val, max_val = find_min_max(test6)
    print(f"Тест 6: {test6}")
    print(f"Мінімум: {min_val}, Максимум: {max_val}")
    print(f"Очікується: Мінімум: 5, Максимум: 5")


if __name__ == "__main__":
    print("=" * 60)
    print("Завдання 1: Пошук мінімального та максимального елементів")
    print("Метод 'розділяй і володарюй'")
    print("=" * 60)
    print()
    test_find_min_max()
