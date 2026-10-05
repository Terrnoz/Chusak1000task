import random
import math

random.seed(42)

numbers = random.sample(range(1, 46), 6)
numbers.sort()
print("Выигрышные номера:", numbers)

total_combinations = math.comb(45, 6)
print(f"Всего комбинаций: {total_combinations:,}")
print(f"Вероятность угадать все 6: 1 к {total_combinations:,}")

random.seed(2026)
counts = {}
for _ in range(100_000):
    s = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
    counts[s] = counts.get(s, 0) + 1

most_common = max(counts, key=counts.get)
print(f"\nСамая частая сумма трёх кубиков: {most_common} ({counts[most_common]} раз)")