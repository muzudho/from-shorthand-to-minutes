# python format_work.py
import json

def main():

    with open("work.json", "r", encoding="UTF-8") as f_in:
        document = json.load(f_in)

    with open("output.txt", "w", encoding="UTF-8") as f_out:
        f_out.write("""\
－－－－－－－－－－－－＋
　　　　　　　　　　　　｜
""")

        for record in document:
            speaker = record["speaker"]
            statement = record["statement"]

            f_out.write(f"　　　　　　　　　 {speaker}　｜　")

            is_first = True
            for statement_line in statement:
                #print(f"(...) {json.dumps(statement_line, ensure_ascii=False)}")
                if is_first:
                    is_first = False
                    f_out.write(f"{statement_line}\n")
                else:
                    f_out.write(f"　　　　　　　　　　　　｜　{statement_line}\n")

        f_out.write("""\
　　　　　　　　　　　　｜
－－－－－－－－－－－－＋
""")

if __name__ == "__main__":
    main()
