# %%
import pandas as pd

df = pd.read_csv("./articles.csv")
df["tag"] = None
cnt = 0


def add_tag(df, tag):
    for idx, text in enumerate(df["text"]):
        if tag in text:
            if df.loc[idx, ["tag"]][0]:
                if tag in df.loc[idx, ["tag"]][0]:
                    break
                df.loc[idx, ["tag"]] = ", ".join(
                    df.loc[idx, ["tag"]]
                    .append(pd.Series([tag]), ignore_index=True)
                    .values
                )
            else:
                df.loc[idx, ["tag"]] = tag


# %%
add_tag(df, "학기")
add_tag(df, "학점")
add_tag(df, "신청")
add_tag(df, "전공")
add_tag(df, "과목")
add_tag(df, "학년")
add_tag(df, "졸업")
add_tag(df, "휴학")
add_tag(df, "복전")
add_tag(df, "수강신청")
add_tag(df, "복수")
add_tag(df, "수강")
add_tag(df, "계절")
add_tag(df, "복학")
add_tag(df, "장학금")
add_tag(df, "재수강")
add_tag(df, "등록금")
add_tag(df, "등록")
add_tag(df, "수료")
add_tag(df, "증명서")
add_tag(df, "봉사")
add_tag(df, "증원")
add_tag(df, "철회")
add_tag(df, "삼품")
add_tag(df, "3품")
add_tag(df, "복수전공")
add_tag(df, "아캠")
add_tag(df, "아이캠퍼스")
df.to_csv("articles_tagged.csv", encoding="utf-8-sig")
# %%
