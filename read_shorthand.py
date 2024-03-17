# python read_shorthand.py

def main():
    with open("input.txt", "r", encoding="UTF-8") as f:
        lines = f.readlines()
        for line in lines:
            print(f"（＾～＾） {line}")

if __name__ == "__main__":
    main()
