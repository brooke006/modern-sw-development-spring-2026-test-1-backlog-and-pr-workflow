# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

p_hp = 50
b_hp = 50

# Security: Removed the hardcoded code because anyone who knew it
# could skip the fight. The cheat option and logic need to go too.
MAX_HP = 50

def attack():
    global b_hp
    # Attack: The original code said it dealt damage but didn't
    # change the boss's health. This subtracts 10 HP each attack.
    b_hp -= 10
    if b_hp < 0:
        b_hp = 0
    print("You deal 10 damage!")

def heal():
    global p_hp
    # Healing: Check health first so a player at 0 HP or below
    # can't heal and come back after losing.
    if p_hp <= 0:
        print("You cannot heal when defeated.")
        return

    # Healing: Adding 20 could put health over 50.
    # If that happens, set it back to the maximum of 50.
    p_hp += 20
    if p_hp > MAX_HP:
        p_hp = MAX_HP
    print(f"Healed! HP is now {p_hp}")

# --- Simple Game Loop ---
# Win condition: Keep playing while both have health.
# Once the boss reaches 0 HP, show Victory and stop the loop.
while p_hp > 0 and b_hp > 0:
    print(f"\nPlayer: {p_hp} | Boss: {b_hp}")

    # Security: Took the cheat option out of the choices.
    choice = input("Action [a]ttack, [h]eal: ").lower()

    # Security: Removed the part that checked the code
    # and let the player set the boss's health to 0.
    if choice == 'a':
        attack()
    elif choice == 'h':
        heal()
    else:
        print("Invalid choice! Please choose 'a' or 'h'.")
        continue

    # Win condition: Show Victory and stop before the boss hits back.
    if b_hp <= 0:
        print("Victory!")
        break

    if b_hp > 0:
        p_hp -= 10

# Only show Game Over if the player lost.
if p_hp <= 0:
    print("Game Over!")
