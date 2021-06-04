import requests


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