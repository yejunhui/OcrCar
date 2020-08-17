import openFile
import ocrCar
import time

'车场数据'
data = {}
'单价/hour'
unit = 5
'时长'
time1 = 0
'最低收费'
d=1.5

while 1:
    try:
            f = openFile.get_file_content(input('文件名称：'))
            res = ocrCar.ocrClinet(f)
            res = res['words_result']['number']
            if res in data :
                time1 = (time.time()-data[res])
                price = unit/3600*time1
                if price < 1:
                    price = d
                del data[res]
                tips = '离场'
            else:
                data[res] = time.time()
                price = 0
                tips = '进场'

            print('车牌：',
                  res,
                  time.localtime(time.time()),
                  tips,
                  '停车时长：',
                  time1,
                  '收费：',
                  price,
                  '元！')
    except:
        print('车牌识别出错，请扫码进场！谢谢！')