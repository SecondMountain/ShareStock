from flask import Flask
import requests
from bs4 import BeautifulSoup
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

def price_sum(price):
    sum=0
    for item in price.replace(".",""):
        sum+=int(item)
    return sum


def lenAppend(num_str):
    # if num_str.__len__()==3:
    #     return num_str
    if num_str.__len__()<3:
        num_str = '0'+num_str
        return lenAppend(num_str)
    else: return num_str


def reverse(num_str):
    num_str = list(num_str)
    for index ,item in enumerate(num_str):
        num_str[index] = '1' if item == '0' else '0'
    return num_str


if __name__ == '__main__':
    price_yesterday = '5.65' #昨天收市价
    price_today = '5.54' #今天收市价
    price_sum_yesterday = price_sum(price_yesterday)
    price_sum_today = price_sum(price_today)
    up = price_sum_yesterday%8
    down = price_sum_today%8
    up1= up = 8 if up==0 else up
    down1 = down = 8 if down==0 else down
    change = (price_sum_yesterday+price_sum_today)%6
    change = 6 if change==0 else change
    #从下到上依次是初爻、二爻、三爻、四爻、五爻、六爻
    if change>3:
        up1 = str(bin(up1-1)).replace("0b","")
        up1 = lenAppend(up1)
        change = change-4
        up1 = list(up1)
        up1[change] = '1'if up1[change]=='0'else '0'
        up1 = "".join(up1)
        up1 = int(up1,2)+1
    else:
        down1 = str(bin(down1 - 1)).replace("0b", "")
        down1 = lenAppend(down1)
        change = change - 1
        down1 = list(down1)
        down1[change]  = '1' if down1[change] == '0' else '0'
        down1="".join(down1)
        down1 = int(down1,2)+1
    up2=up
    down2 =down
    up2 = str(bin(up2-1)).replace("0b","")
    up2 = lenAppend(up2)
    up2 = reverse(str(up2))
    up2 = "".join(up2)
    up2 = int(up2, 2) + 1
    down2 = str(bin(down2 - 1)).replace("0b", "")
    down2 = lenAppend(down2)
    down2 = reverse(down2)
    down2 = "".join(down2)
    down2 = int(down2, 2) + 1
    # print(up1)
    # print(down1)
    # exit(0)

    gua = open("static/"+str(up)+str(down),encoding='utf-8')
    hugua = open("static/"+str(up2)+str(down2),encoding='utf-8')
    biangua = open("static/"+str(up1)+str(down1),encoding='utf-8')
    print('========原始卦========')
    for line in gua.readlines():
        print(line,end="")
    print('\n\n\n\n\n\n========互卦========')
    for line in hugua.readlines():
        print(line,end="")
    print('\n\n\n\n\n\n========变卦========')
    for line in biangua.readlines():
        print(line,end="")
