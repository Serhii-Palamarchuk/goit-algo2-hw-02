"""
Завдання 2: Оптимізація черги 3D-принтера в університетській лабораторії
Жадібний алгоритм
"""

from typing import List, Dict
from dataclasses import dataclass


@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int


@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int


def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    """
    Оптимізує чергу 3D-друку згідно з пріоритетами та обмеженнями принтера

    Args:
        print_jobs: Список завдань на друк
        constraints: Обмеження принтера

    Returns:
        Dict з порядком друку та загальним часом
    """
    # Конвертуємо словники в dataclass об'єкти
    jobs = [PrintJob(**job) for job in print_jobs]
    printer = PrinterConstraints(**constraints)

    # Сортуємо завдання тільки за пріоритетом (1 - найвищий, 3 - найнижчий)
    # При однаковому пріоритеті зберігаємо вхідний порядок (стабільне сортування)
    jobs.sort(key=lambda x: x.priority)

    print_order = []
    total_time = 0
    remaining_jobs = jobs.copy()

    while remaining_jobs:
        # Створюємо нову групу для друку
        current_batch = []
        current_volume = 0
        current_max_time = 0

        # Жадібно додаємо завдання в поточну групу
        jobs_to_remove = []

        for job in remaining_jobs:
            # Перевіряємо, чи можемо додати завдання в поточну групу
            can_add = (
                len(current_batch) < printer.max_items
                and current_volume + job.volume <= printer.max_volume
            )

            if can_add:
                current_batch.append(job)
                current_volume += job.volume
                current_max_time = max(current_max_time, job.print_time)
                jobs_to_remove.append(job)

        # Якщо нічого не додали, додаємо хоча б перше завдання
        # (навіть якщо воно перевищує обмеження)
        if not current_batch and remaining_jobs:
            job = remaining_jobs[0]
            current_batch.append(job)
            current_max_time = job.print_time
            jobs_to_remove.append(job)

        # Видаляємо оброблені завдання
        for job in jobs_to_remove:
            remaining_jobs.remove(job)

        # Додаємо ID завдань до порядку друку
        for job in current_batch:
            print_order.append(job.id)

        # Час друку групи = максимальний час серед моделей у групі
        total_time += current_max_time

    return {"print_order": print_order, "total_time": total_time}


# Тестування
def test_printing_optimization():
    """Тестування оптимізації черги 3D-друку"""

    # Тест 1: Моделі однакового пріоритету
    test1_jobs = [
        {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 1, "print_time": 150},
    ]

    # Тест 2: Моделі різних пріоритетів
    test2_jobs = [
        {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},  # лабораторна
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},  # дипломна
        {
            "id": "M3",
            "volume": 120,
            "priority": 3,
            "print_time": 150,
        },  # особистий проєкт
    ]

    # Тест 3: Перевищення обмежень об'єму
    test3_jobs = [
        {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
        {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
        {"id": "M3", "volume": 180, "priority": 2, "print_time": 120},
    ]

    constraints = {"max_volume": 300, "max_items": 2}

    print("Тест 1 (однаковий пріоритет):")
    result1 = optimize_printing(test1_jobs, constraints)
    print(f"Порядок друку: {result1['print_order']}")
    print(f"Загальний час: {result1['total_time']} хвилин")
    print()

    print("Тест 2 (різні пріоритети):")
    result2 = optimize_printing(test2_jobs, constraints)
    print(f"Порядок друку: {result2['print_order']}")
    print(f"Загальний час: {result2['total_time']} хвилин")
    print()

    print("Тест 3 (перевищення обмежень):")
    result3 = optimize_printing(test3_jobs, constraints)
    print(f"Порядок друку: {result3['print_order']}")
    print(f"Загальний час: {result3['total_time']} хвилин")
    print()

    # Додатковий тест 4: Складний випадок з багатьма завданнями
    print("=" * 60)
    print("Тест 4 (складний випадок з багатьма завданнями):")
    test4_jobs = [
        {"id": "M1", "volume": 50, "priority": 3, "print_time": 60},
        {"id": "M2", "volume": 80, "priority": 1, "print_time": 120},
        {"id": "M3", "volume": 100, "priority": 2, "print_time": 90},
        {"id": "M4", "volume": 120, "priority": 1, "print_time": 150},
        {"id": "M5", "volume": 70, "priority": 2, "print_time": 80},
        {"id": "M6", "volume": 90, "priority": 3, "print_time": 100},
    ]

    result4 = optimize_printing(test4_jobs, constraints)
    print(f"Порядок друку: {result4['print_order']}")
    print(f"Загальний час: {result4['total_time']} хвилин")
    print()

    # Пояснення результату тесту 4
    print("Пояснення:")
    print("1. Пріоритет 1 (дипломні): M2 (80см³, 120хв), M4 (120см³, 150хв)")
    print("2. Пріоритет 2 (лабораторні): M3 (100см³, 90хв), M5 (70см³, 80хв)")
    print("3. Пріоритет 3 (особисті): M1 (50см³, 60хв), M6 (90см³, 100хв)")
    print()
    print("Групування:")
    print("- Група 1: M2 + M4 = 200см³, час = max(120, 150) = 150хв")
    print("- Група 2: M3 + M5 = 170см³, час = max(90, 80) = 90хв")
    print("- Група 3: M1 + M6 = 140см³, час = max(60, 100) = 100хв")
    print(f"- Загальний час: 150 + 90 + 100 = 340хв")


if __name__ == "__main__":
    print("=" * 60)
    print("Завдання 2: Оптимізація черги 3D-принтера")
    print("Жадібний алгоритм")
    print("=" * 60)
    print()
    test_printing_optimization()
