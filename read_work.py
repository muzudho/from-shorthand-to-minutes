# python read_work.py
import json

def main():

    with open("work.json", "r", encoding="UTF-8") as f_in:
        document = json.load(f_in)

        for record in document:
            speaker = record["speaker"]
            print(f"(^q^) {speaker}")

            statement = record["statement"]
            for statement_line in statement:
                print(f"(...) {json.dumps(statement_line)}")

if __name__ == "__main__":
    main()
