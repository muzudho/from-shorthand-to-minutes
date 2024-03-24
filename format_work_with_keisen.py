# python format_work_with_keisen.py
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

            #print(f"(...) {json.dumps(statement, ensure_ascii=False)}")

            # 発言者が変わる時、１行開ける
            if speaker != "" and previous_speaker != speaker:
                print(f"(^q^) speaker：［{speaker}］　previous_speaker：［{previous_speaker}］　発言者が変わる時、１行開ける")
                f_out.write("　　　　　　　　　　　　｜\n")

            else:
                print(f"(^q^) speaker：［{speaker}］　previous_speaker：［{previous_speaker}］　発言者同じ")

            # 発言者名が入っているとき
            if speaker != "":
                #print("(^q^) 発言の１行目：［{statement}］")
                f_out.write(f"　　　　　　　　　{speaker}　｜　{statement}\n")
            else:
                f_out.write(f"　　　　　　　　　　　　｜　{statement}\n")

            previous_speaker = speaker

        f_out.write("""\
　　　　　　　　　　　　｜
－－－－－－－－－－－－＋
""")

if __name__ == "__main__":
    main()
