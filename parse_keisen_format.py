# python parse_keisen_format.py
#
# こんなやつを解析して JSON 形式へ変換
#
# """
# 　　　　　　　　　　　　｜
# 　　　　　　　　　要約　｜　会計の話し
# 　　　　　　　　　　　　｜　新規会員の話し
# 　　　　　　　　　　　　｜
#
# ［１．］　　　　　　　　｜
# 　　　　　　　　　　　　｜
# 　　　　　　　むずでょ　｜　１１時になったので運営委員会を始めます
# 　　　　　　　　　　　　｜
# """
#
import json
import re

def main():
    # 議事録
    minute = []

    with open("input.txt", "r", encoding="UTF-8") as f_in:
        lines = f_in.readlines()
        for line in lines:
            print(f"（＾～＾）　原文　［{line}］")

            # 末尾の改行は削除
            # めんどくさいんでタブはざっくりスペース 1つに変換
            line = line.rstrip().replace("\t", ' ')
            print(f"（＾～＾）　末尾の改行を削除、タブはスペース１つへ変換　［{line}］")

            # 連続したスペースがあれば１つにまとめたい
            line = re.sub(r"\s+", ' ', line)
            print(f"（＾～＾）　連続したスペースを１つに変換　［{line}］")

            # 空行はパス
            if line == "":
                pass

            # それ以外
            else:
                # 縦線でスプリット

                line = line.strip()
                print(f"（...）それ以外　［{line}］")

                pair = line.split("｜", maxsplit=2)

                # 罫線の左側
                speaker = pair[0].strip()
                print(f"（＾～＾）発言者名　［{speaker}］")

                    # 罫線の右側
                if len(pair) < 2:
                    statement = ""
                else:
                    statement = pair[1].strip()

                print(f"（＾～＾）発言　　　［{statement}］")

                minute.append({"speaker":"", "statement":statement})


    with open("work.json", "w", encoding="UTF-8") as f_out:
        json.dump(minute, f_out, ensure_ascii=False)

if __name__ == "__main__":
    main()
