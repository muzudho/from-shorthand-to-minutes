# python format_work_to_plaintext.py
import json

def main():

    with open("work.json", "r", encoding="UTF-8") as f_in:
        document = json.load(f_in)

    with open("output.txt", "w", encoding="UTF-8") as f_out:
        f_out.write("""\
＜＜＜＜ここから＞＞＞＞
""")
        previous_speaker = ""
        is_summary = False

        for record in document:
            speaker = record["speaker"].strip()
            statement = record["statement"].strip()

            #print(f"■ {json.dumps(record, ensure_ascii=False)}")

            #
            # スマホはワードラップが多くなり、行頭が見つけづらくなる。インデントは逆効果
            #
            # "［１．］" みたいなやつは、そのまま出す
            if speaker.startswith("［"):
                f_out.write(f"\n\n\n{speaker}{statement}\n")
                is_summary = False

            # "＝＝＝＝"　みたいなやつは、そのまま出す
            elif speaker.startswith("＝"):
                f_out.write(f"{speaker}{statement}\n")
                is_summary = False

            # 発言者が要約のとき、そのまま出す
            elif speaker == "要約":
                f_out.write(f"\n　■{speaker}　　{statement}\n")
                is_summary = True

            # 要約が続くとき、そのまま出す
            elif is_summary:
                f_out.write(f"{speaker}{statement}\n")

            # 発言者が変わる時、行頭に改行２つと空白１つを入れて、発言者名を付けようかな。次の発言とつながるように、改行はしないでおこ
            elif speaker != "" and previous_speaker != speaker:
                print(f"(^q^) speaker：［{speaker}］　previous_speaker：［{previous_speaker}］　発言者が変わる時、１行開ける")
                f_out.write(f"\n\n　■{speaker}　　{statement}")
                is_summary = False

            # 発言者が同じとき、「　／」で、つなげよかな
            elif statement != "":
                print(f"(^q^) speaker：［{speaker}］　previous_speaker：［{previous_speaker}］　発言者同じ")
                f_out.write(f"　／{statement}")
                is_summary = False

            else:
                print(f"(^q^) empty statement")
                is_summary = False

            previous_speaker = speaker

        f_out.write("""\
＜＜＜＜ここまで＞＞＞＞
""")

if __name__ == "__main__":
    main()
