# python parse_shorthand_to_work.py
import json
import re

def main():
    # 議事録
    minute = []

    with open("input.txt", "r", encoding="UTF-8") as f_in:
        lines = f_in.readlines()
        for line in lines:
            #print(f"（＾～＾）　原文　［{line}］")

            # 末尾の改行は削除
            # めんどくさいんでタブはざっくりスペース 1つに変換
            line = line.rstrip().replace("\t", ' ')
            #print(f"（＾～＾）　末尾の改行を削除、タブはスペース１つへ変換　［{line}］")

            # 連続したスペースがあれば１つにまとめたい
            line = re.sub(r"\s+", ' ', line)
            #print(f"（＾～＾）　連続したスペースを１つに変換　［{line}］")

            # 空行はパス
            if line == "":
                pass

            # 発言者名と発言の行
            elif not line.startswith(" "):
                #print(f"（＾～＾）発言者名と発言の行　［{line}］")
                pair = line.split(" ", maxsplit=2)
                speaker = pair[0]
                #print(f"（＾～＾）発言者名　［{speaker}］")

                if len(pair) < 2:
                    print(f"（＾～＾）発言なし　line:［{line}］")
                    minute.append({"speaker":speaker, "statement":""})

                else:
                    #print(f"（＾～＾）残り　　　［{pair[1]}］")
                    # 前後のスペースと改行を取り除く
                    statement = pair[1].strip()

                    minute.append({"speaker":speaker, "statement":statement})

            # それ以外
            else:
                line = line.strip()
                #print(f"（...）それ以外　［{line}］")
                statement = line.split("\r\n")
                for statement_line in statement:
                    minute.append({"speaker":"", "statement":statement_line})


    with open("work.json", "w", encoding="UTF-8") as f_out:
        json.dump(minute, f_out, ensure_ascii=False)

if __name__ == "__main__":
    main()
