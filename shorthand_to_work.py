# python shorthand_to_work.py

def main():
    with open("input.txt", "r", encoding="UTF-8") as f:
        lines = f.readlines()
        for line in lines:
            print(f"（＾～＾） {line}")

    with open("work.txt", "a", encoding="UTF-8") as f2:
        for line in lines:
            f2.write(f"（＾～＾） {line}")

if __name__ == "__main__":
    main()
