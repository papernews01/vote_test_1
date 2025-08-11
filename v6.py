import random

def roll_dice(num_rolls):
    results = {}
    for _ in range(num_rolls):
        roll = random.randint(1, 6) + random.randint(1, 6)
        results[roll] = results.get(roll, 0) + 1
    return results

rolls = int(input("Сколько раз бросить кубики? "))
stats = roll_dice(rolls)
for sum_val, count in sorted(stats.items()):
    print(f"Сумма {sum_val}: {count} раз ({count/rolls*100:.1f}%)")