# python read_work.py
import json

def main():

    with open("work.json", "r", encoding="UTF-8") as f_in:
        data = json.load(f_in)

        print(f"(^q^) {json.dumps(data)}")

if __name__ == "__main__":
    main()
