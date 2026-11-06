# 44th github project --> Workout Timer
print('----------Workout Timer----------')
import time


def countdown(label, seconds):
    print(f"\n{label} - {seconds}s")
    remaining = seconds
    while remaining > 0:
        print(f"\r{label}: {remaining:02d}s", end="", flush=True)
        time.sleep(1)
        remaining -= 1
    print(f"\r{label}: done!      ")


def main():
    print("WORKOUT TIMER")

    try:
        work = int(input("Work seconds: "))
        rest = int(input("Rest seconds: "))
        rounds = int(input("Rounds: "))
    except ValueError:
        print("Enter whole numbers.")
        return

    if work <= 0 or rest < 0 or rounds <= 0:
        print("Invalid values.")
        return

    for i in range(1, rounds + 1):
        print(f"\n--- Round {i}/{rounds} ---")
        countdown("Work", work)
        if rest > 0 and i < rounds:
            countdown("Rest", rest)

    print("\nWorkout complete!")


main()