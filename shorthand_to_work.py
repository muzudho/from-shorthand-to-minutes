# python shorthand_to_work.py

def main():
    array = []

    with open("input.txt", "r", encoding="UTF-8") as f:
        lines = f.readlines()
        for line in lines:
            #print(f"（＾～＾） {line}")
            array.append(line)

    with open("work.txt", "a", encoding="UTF-8") as f2:
        for line in array:
            f2.write(f"（＾～＾） {line}")

if __name__ == "__main__":
    main()
