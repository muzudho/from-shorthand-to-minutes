# python shorthand_to_work.py
import json

def main():
    # 議事録
    minute = []

    with open("input.txt", "r", encoding="UTF-8") as f_in:
        lines = f_in.readlines()
        for line in lines:
            #print(f"（＾～＾） {line}")

            # めんどくさいんでタブはざっくりスペース 4つに変換
            line = line.replace("\t", "    ")

            # 発言者名と発言の行
            if line.startswith(" "):
                pair = line.split(" ", maxsplit=2)
                speaker = pair[0]
                # 改行は \r\n と仮定
                statement = pair[1].split("\r\n")
                minute.append({"speaker":speaker, "statement":statement})
            # それ以外
            else:
                line = line.strip()
                statement = line.split("\r\n")
                minute.append({"speaker":"", "statement":statement})


    with open("work.json", "w", encoding="UTF-8") as f_out:
        json.dump(minute, f_out)

if __name__ == "__main__":
    main()
