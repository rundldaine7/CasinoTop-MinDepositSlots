import random

print("Слоты с минимальным депозитом - Демо!")
spins = 3
while spins > 0:
    spins -= 1
    result = random.choice(["Джекпот!", "Фриспин!", "Ещё спин!"])
    print(f"Спин {3 - spins}: {result}")
    if spins > 0:
        input("Нажми Enter для нового шанса...")
print("Крути с минимальным депозитом и побеждай в топ-казино!")
