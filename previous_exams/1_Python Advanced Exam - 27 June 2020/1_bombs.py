from collections import deque


def is_pouch_full(pouch):
    return pouch["datura"] >= 3 and pouch["cherry"] >= 3 and pouch["decoy"] >= 3


effects = deque([int(x) for x in input().split(", ")])
casings = deque([int(x) for x in input().split(", ")])

full_pouch = False
pouch = {"datura": 0, "cherry": 0, "decoy": 0}

while True:
    if not effects or not casings:
        break
    # Just peek
    current_effect, current_casing = effects[0], casings[-1]

    if current_effect + current_casing == 40:
        effects.popleft(), casings.pop()
        pouch["datura"] += 1

    elif current_effect + current_casing == 60:
        effects.popleft(), casings.pop()
        pouch["cherry"] += 1

    elif current_effect + current_casing == 120:
        effects.popleft(), casings.pop()
        pouch["decoy"] += 1

    else:
        casings[-1] -= 5

    if is_pouch_full(pouch):
        full_pouch = True
        break

# Print outcome
if full_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
# Print remaining materials
if effects:
    print("Bomb Effects: ", end="")
    print(*effects, sep=", ")
else:
    print("Bomb Effects: empty")
if casings:
    print("Bomb Casings: ", end="")
    print(*casings, sep=", ")
else:
    print("Bomb Casings: empty")
# Print bombs
print(f"Cherry Bombs: {pouch['cherry']}")
print(f"Datura Bombs: {pouch['datura']}")
print(f"Smoke Decoy Bombs: {pouch['decoy']}")
# print(effects, casings, pouch)
