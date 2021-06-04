import requests
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

res = requests.get('https://api.helium.io/v1/hotspots/1128ugjnnNkX7zMsxCeaHdETLxFpYkGoUDAue7V8Hvpi6Ha3f1eQ/rewards/sum?min_time=-1%20day&bucket=day')
data1 = res.json()['data']
print(data1)
#total = data1['total']
#print (total)
for total in res.json()['data']:
    sym = total['total']
sym1 = str(round(sym, 2))

sym2 = sym1 + " HNT mined in the last 24 hours"
print (sym2)

text = (sym2, (255, 0, 0))

font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 16)
all_text = ""
for text_color_pair in text:
t = text_color_pair[0]
all_text = all_text + t

print(all_text)
width, ignore = font.getsize(all_text)
print(width)

im = Image.new("RGB", (width + 30, 16), "black")
draw = ImageDraw.Draw(im)

x = 0;
for text_color_pair in text:
t = text_color_pair[0]
c = text_color_pair[1]
print("t=" + t + " " + str(c) + " " + str(x))
draw.text((x, 0), t, c, font=font)
x = x + font.getsize(t)[0]

im.save("test.ppm")

os.system("./demo D0 test.ppm")