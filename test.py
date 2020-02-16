import requests
import PySimpleGUI as sg

form = sg.FlexForm("Ваш лучший район")
layout = [
    [sg.Text('Оцените важность каждого из критериев вашего будущего района:', size=(61, 1))],
    [sg.Text('      Экология', size=(55, 1)), sg.InputCombo((1, 2, 3, 4, 5), 1, size=(20, 5))],
    [sg.Text('      Транспорт', size=(55, 1)), sg.InputCombo((1, 2, 3, 4, 5), 1, size=(20, 5))],
    [sg.Text('      Развлечения', size=(55, 1)), sg.InputCombo((1, 2, 3, 4, 5), 1, size=(20, 5))],
    [sg.Text('      Инфраструктура', size=(55, 1)), sg.InputCombo((1, 2, 3, 4, 5), 1, size=(20, 5))],
    [sg.Text('      Спорт', size=(55, 1)), sg.InputCombo((1, 2, 3, 4, 5), 1, size=(20, 5))],
    [sg.Text('      Адаптированность для людей с ограниченными возможностями', size=(55, 1)),
     sg.InputCombo((1, 2, 3, 4, 5), 1, size=(20, 5))],
    [sg.Submit('Продолжить')]
]
button, values = form.Layout(layout).Read()
x = values[0]
x1 = values[1]
x2 = values[2]
x3 = values[3]
x4 = values[4]
x5 = values[5]
UB = 0
UZ = 0
SB = 0
SZ = 0
C = [55.75370903771494, 37.61981338262558]
r = requests.get("https://apidata.mos.ru/v1/datasets/2447/features?api_key=b01807af35c61a47f615a4501ea2fb51")
r1 = requests.get("https://apidata.mos.ru/v1/datasets/916/features?api_key=b01807af35c61a47f615a4501ea2fb51")
r2 = requests.get("https://apidata.mos.ru/v1/datasets/2269/features?api_key=b01807af35c61a47f615a4501ea2fb51")
r3 = requests.get("https://apidata.mos.ru/v1/datasets/3227/features?api_key=b01807af35c61a47f615a4501ea2fb51")
r4 = requests.get("https://apidata.mos.ru/v1/datasets/495/features?api_key=b01807af35c61a47f615a4501ea2fb51")
r5 = requests.get("https://apidata.mos.ru/v1/datasets/912/features?api_key=b01807af35c61a47f615a4501ea2fb51")
r6 = requests.get("https://apidata.mos.ru/v1/datasets/1389/features?api_key=b01807af35c61a47f615a4501ea2fb51")
r7 = requests.get("https://apidata.mos.ru/v1/datasets/517/features?api_key=b01807af35c61a47f615a4501ea2fb51")
r8 = requests.get("https://apidata.mos.ru/v1/datasets/1181/features?api_key=b01807af35c61a47f615a4501ea2fb51")
r9 = requests.get("https://apidata.mos.ru/v1/datasets/61481/features?api_key=b01807af35c61a47f615a4501ea2fb51")
r10 = requests.get("https://apidata.mos.ru/v1/datasets/1362/features?api_key=b01807af35c61a47f615a4501ea2fb51")
r11 = requests.get("https://apidata.mos.ru/v1/datasets/61221/features?api_key=b01807af35c61a47f615a4501ea2fb51")
r12 = requests.get("https://apidata.mos.ru/v1/datasets/1385/features?api_key=b01807af35c61a47f615a4501ea2fb51")
r13 = requests.get("https://apidata.mos.ru/v1/datasets/890/features?api_key=b01807af35c61a47f615a4501ea2fb51")
r14 = requests.get("https://apidata.mos.ru/v1/datasets/897/features?api_key=b01807af35c61a47f615a4501ea2fb51")
r15 = requests.get("https://apidata.mos.ru/v1/datasets/1232/features?api_key=b01807af35c61a47f615a4501ea2fb51")
r16 = requests.get("https://apidata.mos.ru/v1/datasets/60622/features?api_key=b01807af35c61a47f615a4501ea2fb51")
r17 = requests.get("https://apidata.mos.ru/v1/datasets/1251/features?api_key=b01807af35c61a47f615a4501ea2fb51")
r18 = requests.get("https://apidata.mos.ru/v1/datasets/886/features?api_key=b01807af35c61a47f615a4501ea2fb51")
for j in range(len(r.json()['features'])):
    k = r.json()['features'][j]['geometry']['coordinates']
    i = r.json()['features'][j]['properties']['Attributes']
    if k[1] < C[0] and k[0] < C[1]:
        if i['SurveillanceZoneCharacteristics'] == 'Жилые территории':
            UZ = UZ + 1 * x
        else:
            UZ = UZ - 1 * x
    if k[1] > C[0] and k[0] < C[1]:
        if i['SurveillanceZoneCharacteristics'] == 'Жилые территории':
            SZ = SZ + 1 * x
        else:
            SZ = SZ - 1 * x
    if k[1] < C[0] and k[0] > C[1]:
        if i['SurveillanceZoneCharacteristics'] == 'Жилые территории':
            UB = UB + 1 * x
        else:
            UB = UB - 1 * x
    if k[1] > C[0] and k[0] > C[1]:
        if i['SurveillanceZoneCharacteristics'] == 'Жилые территории':
            SB = SB + 1 * x
        else:
            SB = SB - 1 * x
for i in range(len(r1.json()['features'])):
    k = r1.json()['features'][i]['geometry']['coordinates']
    if k[1] < C[0] and k[0] < C[1]:
        UZ = UZ + 1 * x1
    if k[1] > C[0] and k[0] < C[1]:
        SZ = SZ + 1 * x1
    if k[1] < C[0] and k[0] > C[1]:
        UB = UB + 1 * x1
    if k[1] > C[0] and k[0] > C[1]:
        SB = SB + 1 * x1
for i in range(len(r2.json()['features'])):
    k = r2.json()['features'][i]['geometry']['coordinates']
    if k[1] < C[0] and k[0] < C[1]:
        UZ = UZ + 0.1 * x2
    if k[1] > C[0] and k[0] < C[1]:
        SZ = SZ + 0.1 * x2
    if k[1] < C[0] and k[0] > C[1]:
        UB = UB + 0.1 * x2
    if k[1] > C[0] and k[0] > C[1]:
        SB = SB + 0.1 * x2
for i in range(len(r3.json()['features'])):
    k = r3.json()['features'][i]['geometry']['coordinates']
    if k[1] < C[0] and k[0] < C[1]:
        UZ = UZ + 0.1 * x2
    if k[1] > C[0] and k[0] < C[1]:
        SZ = SZ + 0.1 * x2
    if k[1] < C[0] and k[0] > C[1]:
        UB = UB + 0.1 * x2
    if k[1] > C[0] and k[0] > C[1]:
        SB = SB + 0.1 * x2
for i in range(len(r4.json()['features'])):
    k = r4.json()['features'][i]['geometry']['coordinates'][0]
    if k[1] < C[0] and k[0] < C[1]:
        UZ = UZ + 0.1 * x2
    if k[1] > C[0] and k[0] < C[1]:
        SZ = SZ + 0.1 * x2
    if k[1] < C[0] and k[0] > C[1]:
        UB = UB + 0.1 * x2
    if k[1] > C[0] and k[0] > C[1]:
        SB = SB + 0.1 * x2
for i in range(len(r5.json()['features'])):
    k = r5.json()['features'][i]['geometry']['coordinates']
    if k[1] < C[0] and k[0] < C[1]:
        UZ = UZ + 0.01 * x3
    if k[1] > C[0] and k[0] < C[1]:
        SZ = SZ + 0.01 * x3
    if k[1] < C[0] and k[0] > C[1]:
        UB = UB + 0.01 * x3
    if k[1] > C[0] and k[0] > C[1]:
        SB = SB + 0.01 * x3
for i in range(len(r6.json()['features'])):
    k = r6.json()['features'][0]['geometry']['coordinates']
    if k[1] < C[0] and k[0] < C[1]:
        UZ = UZ + 0.1 * x3
    if k[1] > C[0] and k[0] < C[1]:
        SZ = SZ + 0.1 * x3
    if k[1] < C[0] and k[0] > C[1]:
        UB = UB + 0.1 * x3
    if k[1] > C[0] and k[0] > C[1]:
        SB = SB + 0.1 * x3
for i in range(len(r7.json()['features'])):
    k = r7.json()['features'][i]['geometry']['coordinates']
    k = k[0]
    if k[1] < C[0] and k[0] < C[1]:
        UZ = UZ + 0.1 * x3
    if k[1] > C[0] and k[0] < C[1]:
        SZ = SZ + 0.1 * x3
    if k[1] < C[0] and k[0] > C[1]:
        UB = UB + 0.1 * x3
    if k[1] > C[0] and k[0] > C[1]:
        SB = SB + 0.1 * x3
for i in range(len(r8.json()['features'])):
    k = r8.json()['features'][i]['geometry']['coordinates'][0]
    if k[1] < C[0] and k[0] < C[1]:
        UZ = UZ + 0.1 * x3
    if k[1] > C[0] and k[0] < C[1]:
        SZ = SZ + 0.1 * x3
    if k[1] < C[0] and k[0] > C[1]:
        UB = UB + 0.1 * x3
    if k[1] > C[0] and k[0] > C[1]:
        SB = SB + 0.1 * x3
for i in range(len(r9.json()['features'])):
    k = r9.json()['features'][i]['geometry']['coordinates']
    if k[1] < C[0] and k[0] < C[1]:
        UZ = UZ + 0.1 * x5
    if k[1] > C[0] and k[0] < C[1]:
        SZ = SZ + 0.1 * x5
    if k[1] < C[0] and k[0] > C[1]:
        UB = UB + 0.1 * x5
    if k[1] > C[0] and k[0] > C[1]:
        SB = SB + 0.1 * x5
for i in range(len(r10.json()['features'])):
    k = r10.json()['features'][i]['geometry']['coordinates']
    if k[1] < C[0] and k[0] < C[1]:
        UZ = UZ + 0.1 * x5
    if k[1] > C[0] and k[0] < C[1]:
        SZ = SZ + 0.1 * x5
    if k[1] < C[0] and k[0] > C[1]:
        UB = UB + 0.1 * x5
    if k[1] > C[0] and k[0] > C[1]:
        SB = SB + 0.1 * x5
for i in range(len(r11.json()['features'])):
    k = r11.json()['features'][i]['geometry']['coordinates']
    if k[1] < C[0] and k[0] < C[1]:
        UZ = UZ + 0.1 * x5
    if k[1] > C[0] and k[0] < C[1]:
        SZ = SZ + 0.1 * x5
    if k[1] < C[0] and k[0] > C[1]:
        UB = UB + 0.1 * x5
    if k[1] > C[0] and k[0] > C[1]:
        SB = SB + 0.1 * x5
for i in range(len(r12.json()['features'])):
    k = r12.json()['features'][i]['geometry']['coordinates']
    if k[1] < C[0] and k[0] < C[1]:
        UZ = UZ + 0.1 * x4
    if k[1] > C[0] and k[0] < C[1]:
        SZ = SZ + 0.1 * x4
    if k[1] < C[0] and k[0] > C[1]:
        UB = UB + 0.1 * x4
    if k[1] > C[0] and k[0] > C[1]:
        SB = SB + 0.1 * x4
for i in range(len(r13.json()['features'])):
    k = r13.json()['features'][i]['geometry']['coordinates']
    if k[1] < C[0] and k[0] < C[1]:
        UZ = UZ + 0.1 * x4
    if k[1] > C[0] and k[0] < C[1]:
        SZ = SZ + 0.1 * x4
    if k[1] < C[0] and k[0] > C[1]:
        UB = UB + 0.1 * x4
    if k[1] > C[0] and k[0] > C[1]:
        SB = SB + 0.1 * x4
for i in range(len(r14.json()['features'])):
    k = r14.json()['features'][i]['geometry']['coordinates']
    k = k[0][0]
    if k[1] < C[0] and k[0] < C[1]:
        UZ = UZ + 0.1 * x4
    if k[1] > C[0] and k[0] < C[1]:
        SZ = SZ + 0.1 * x4
    if k[1] < C[0] and k[0] > C[1]:
        UB = UB + 0.1 * x4
    if k[1] > C[0] and k[0] > C[1]:
        SB = SB + 0.1 * x4
for i in range(len(r15.json()['features'])):
    k = r15.json()['features'][i]['geometry']['coordinates']
    if k[1] < C[0] and k[0] < C[1]:
        UZ = UZ + 0.1 * x4
    if k[1] > C[0] and k[0] < C[1]:
        SZ = SZ + 0.1 * x4
    if k[1] < C[0] and k[0] > C[1]:
        UB = UB + 0.1 * x4
    if k[1] > C[0] and k[0] > C[1]:
        SB = SB + 0.1 * x4
for i in range(len(r16.json()['features'])):
    k = r16.json()['features'][i]['geometry']['coordinates']
    if k[1] < C[0] and k[0] < C[1]:
        UZ = UZ + 0.1 * x4
    if k[1] > C[0] and k[0] < C[1]:
        SZ = SZ + 0.1 * x4
    if k[1] < C[0] and k[0] > C[1]:
        UB = UB + 0.1 * x4
    if k[1] > C[0] and k[0] > C[1]:
        SB = SB + 0.1 * x4
for i in range(len(r17.json()['features'])):
    k = r17.json()['features'][i]['geometry']['coordinates']
    if k[1] < C[0] and k[0] < C[1]:
        UZ = UZ + 0.1 * x4
    if k[1] > C[0] and k[0] < C[1]:
        SZ = SZ + 0.1 * x4
    if k[1] < C[0] and k[0] > C[1]:
        UB = UB + 0.1 * x4
    if k[1] > C[0] and k[0] > C[1]:
        SB = SB + 0.1 * x4
for i in range(len(r18.json()['features'])):
    k = r18.json()['features'][i]['geometry']['coordinates']
    if k[1] < C[0] and k[0] < C[1]:
        UZ = UZ + 0.1 * x4
    if k[1] > C[0] and k[0] < C[1]:
        SZ = SZ + 0.1 * x4
    if k[1] < C[0] and k[0] > C[1]:
        UB = UB + 0.1 * x4
    if k[1] > C[0] and k[0] > C[1]:
        SB = SB + 0.1 * x4
print(int(UZ), int(SZ), int(UB), int(SB))
