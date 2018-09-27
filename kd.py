import requests
import json
def kd(danhao):
    url = "http://www.kuaidi100.com/autonumber/autoComNum?text=" + str(danhao)
    json_str = requests.get(url).text
    json1 = json.loads(json_str)
    data = json1.get('auto')
    company = str(data[0]["comCode"]) #读取键值对中的快递公司并转换成字符串

    url2 = "http://m.kuaidi100.com/query?type=" + company + "&postid=" + str(danhao) #在请求数据中加入快递公司
    json_str2 = requests.get(url2).text
    json2 = json.loads(json_str2)
    data2 = json2.get('data')

    for i in range(len(data2)):
        del data2[i]['ftime']
        for j in data2[i].values():
            print(j)
