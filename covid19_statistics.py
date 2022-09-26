def normalize_data(n_cases, n_people, scale):
    # TODO: 모집단 당 사례 수 계산
    norm_cases = []
    for i in range (len(n_cases)):
        norm_cases.append(n_cases[i] / n_people[i] * scale)
    return norm_cases

regions  = ['Seoul', 'Gyeongi', 'Busan', 'Gyeongnam', 'Incheon', 'Gyeongbuk', 'Daegu', 'Chungnam', 'Jeonnam', 'Jeonbuk', 'Chungbuk', 'Gangwon', 'Daejeon', 'Gwangju', 'Ulsan', 'Jeju', 'Sejong']
n_people = [9550227,  13530519, 3359527,     3322373,   2938429,     2630254, 2393626,    2118183,   1838353,   1792476,    1597179,   1536270,   1454679,   1441970, 1124459, 675883,   365309] # 2021-08
n_covid  = [    644,       529,      38,          29,       148,          28,      41,         62,        23,        27,         27,        33,        16,        40,      20,      5,        4] # 2021-09-21

sum_people = 0
for i in range (len(n_people)):
    sum_people += n_people[i]
sum_covid  = 0
for i in range (len(n_covid)):
    sum_covid += n_covid[i]
norm_covid = normalize_data(n_covid, n_people, 1000000) # 100만명 당 걸린 인구 비율

# Print population by region
print('### Korean Population by Region')
print('* Total population:', sum_people)
print() # Print an empty line
print('| Region | Population | Ratio (%) |')
print('| ------ | ---------- | --------- |')
for i in range (len(n_people)):
    ratio = n_people[i] / sum_people * 100
    print('| %s | %d | %.1f |' % (regions[i], n_people[i], ratio))
print()

# TODO: 지역별 코로나19 신규 사례 인쇄
# COVID-19 New Cases by Region
print('### Korean COVID-19 New Cases by Region')
print('* Total population:', sum_covid)
print() # Print an empty line
print('| Region | New Cases | Ratio (%) | New Cases / 1M |')
print('| ------ | --------- | --------- | -------------- |')
for i in range (len(n_covid)):
    ratio = n_covid[i] / sum_covid * 100
    print('| %s | %d | %.1f | %.1f |' % (regions[i], n_covid[i], ratio, norm_covid[i]))
print()
