import os
from threading import Thread
from urllib.request import urlopen

import pandas as pd
import requests
from PIL import Image

URL = "https://dog.ceo/api/breeds/image/random"


def get_dogs(url, name):
    dogs_r = requests.get(url).json()
    dogs_url = (dogs_r['message'])
    im_name = f'dogs_imege/{name}.jpeg'
    with Image.open(urlopen(dogs_url)) as im:
        im = im.resize((500, 500))
        im.save(im_name)


def im_rotate(imeg, num):
    im = Image.open(imeg)
    im_list = [im.rotate(0 - (360 / num) * i) for i in range(1, num + 1)]
    im = im.convert("L")
    im_list1 = [im.rotate(0 - (360 / num) * i) for i in range(1, num + 1)]
    im_list += im_list1

    name_gif = os.path.splitext(imeg)[0] + '_rotated.gif'
    im.save(name_gif, save_all=True, append_images=im_list[0:], duration=300, loop=0)


NUM = 10
tr_list = [Thread(target=get_dogs, args=(URL, f'dog{i}')) for i in range(1, NUM)]
for tr in tr_list:
    tr.start()
for tr in tr_list:
    tr.join()

im_rotate("dogs_imege/dog1.jpeg", 10)


def calc_mnozhitel(temp, krep):
    mnogitel = pd.read_excel('АКТ П-18 и Тех.прогон раздельно.xlsm', sheet_name='а1', engine='openpyxl', index_col=0)
    t1 = int(temp)
    t2 = t1 + 1
    t0 = t2 - temp
    k1 = int(krep)
    k2 = k1 + 1
    k0 = k2 - krep
    A1 = mnogitel.loc[t2, k1].iloc[0]
    A2 = mnogitel.loc[t1, k1].iloc[0]
    A = A1 + t0 * (A2 - A1)
    B1 = mnogitel.loc[t2, k1].iloc[1]
    B2 = mnogitel.loc[t1, k1].iloc[1]
    B = B1 + t0 * (B2 - B1)
    return round(A - (A - B) * k0, 4)


mnog = (calc_mnozhitel(20.8, 96.35))

df1 = pd.DataFrame([[mnog], ])
df1.to_excel("output1.xlsx", header=False, index=False, startrow=1, startcol=1)
