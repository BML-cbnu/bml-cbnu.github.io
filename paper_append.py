import os
import pandas as pd

df = pd.read_csv("./_data/sheets/pub.tsv", sep="\t")

while 1:
    # df.head()
    # df.iloc[0][2]
    new_data = {}
    print(
        """종류를 선택해주세요
        0. International Journal
        1. International Conference
        2. Domestic Journal
        3. Domestic Conference
        4. Awards
        5. 기타(새로 입력)"""
    )
    classes = [
        "International Journal",
        "International Conference",
        "Domestic Journal",
        "Domestic Conference",
        "Awards",
    ]

    flag = int(input())
    if flag == 5:
        new_data["class"] = input("\n개제처를 입력해주세요.\n")
    else:
        new_data["class"] = classes[flag]

    new_data["date"] = input("\n개제일을 입력해주세요.\n예시 : 2023-01-01\n")

    contents = (
        input("\n저자를 입력해주십시오.\n예시 : Han JS, Jeon YG, Oh M, Lee G, Nahmgoong H\n") + ". "
    )
    contents += (
        input("\n제목을 입력해주십시오.\n예시 : Prediction Base on Multi-source Data Integration\n")
        + ". "
    )
    contents += (
        input(
            "\n개제처와 페이지를 입력해주십시오.\n예시 : Nature Communications, 2022 Jun 7; 13(1):1-16 \n"
        )
        + ". "
    )

    new_data["contents"] = contents
    new_data["state"] = "complete"
    print("\t".join(new_data.values()))

    print("\n(0) 저장 , (1) 다시 입력, (2) 종료")
    flag = int(input())
    if flag == 0 and input("\n저장하시겠습니까? (1)") == "1":
        df_s = df.append(new_data, ignore_index=True)
        df_s = df_s.sort_values(
            by=["class", "date"], ascending=False, ignore_index=True
        )

        # display_side_by_side(df, df_s)
        # row 생략 없이 출력
        # pd.set_option("display.max_rows", None)
        # col 생략 없이 출력
        # pd.set_option("display.max_columns", None)
        # print(df_s)

        df_s.to_csv("./_data/sheets/pub.tsv", sep="\t", index=None)
        print("\n저장에 성공하였습니다")
        exit(0)
    elif flag == 2:
        exit(0)

