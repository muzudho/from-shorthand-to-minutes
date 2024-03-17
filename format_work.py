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
        previous_speaker = ""

        for record in document:
            speaker = record["speaker"]
            statement = record["statement"]
            is_first = True

            for statement_line in statement:
                #print(f"(...) {json.dumps(statement_line, ensure_ascii=False)}")

                # 発言者が変わる時、１行開ける
                if is_first and speaker != "" and previous_speaker != speaker:
                    print(f"(^q^) speaker：［{speaker}］　previous_speaker：［{previous_speaker}］　発言者が変わる時、１行開ける")
                    f_out.write("　　　　　　　　　　　　｜\n")
                else:
                    print(f"(^q^) speaker：［{speaker}］　previous_speaker：［{previous_speaker}］　発言者同じ")

                if is_first:
                    #print("(^q^) 発言の１行目：［{statement_line}］")
                    is_first = False
                    f_out.write(f"　　　　　　　　　{speaker}　｜　{statement_line}\n")
                else:
                    f_out.write(f"　　　　　　　　　　　　｜　{statement_line}\n")

            previous_speaker = speaker

        f_out.write("""\
　　　　　　　　　　　　｜
－－－－－－－－－－－－＋
""")

if __name__ == "__main__":
    main()
