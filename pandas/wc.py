# %%
import sys
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud


def get_noun(text):

    okt = Okt()
    noun = okt.nouns(text)
    for i, v in enumerate(noun):
        if len(v) < 2:
            noun.pop(i)
    count = Counter(noun)
    noun_list = count.most_common(100)
    return noun_list


def visualize(noun_list, mas):

    wc = WordCloud(
        font_path="/mnt/c/Users/junhyeok/AppData/Local/Microsoft/Windows/Fonts/Binggrae-Bold.ttf",
        background_color="white",
        width=1000,
        height=1000,
        max_words=100,
        max_font_size=300,
        random_state=1,
        mask=mas,
        mode="RGB",
        contour_color="steelblue",
    )
    wc.generate_from_frequencies(dict(noun_list))
    wc.to_file("keywords.png")
    return wc


#%%
if __name__ == "__main__":
    # filename = sys.argv[1]
    filename = "text.txt"
    f = open(filename, "r", encoding="utf-8")
    text = f.read()
    noun_list = get_noun(text)
    # visualize(noun_list)
# %%
import csv

file = open("noun_list.csv", mode="w", encoding="utf-8-sig")
writer = csv.writer(file)
writer.writerows([[*noun] for noun in noun_list])
# %%
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

mask = np.array(Image.open("image.jpg"))
wc = visualize(noun_list, mask)
plt.figure(figsize=[10, 10])
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
# %%