from bs4 import BeautifulSoup
import requests

# 気象庁の天気ページ
osaka_weather_url = 'https://www.jma.go.jp/jp/week/331.html'

# 気象情報を取得
Page = requests.get(osaka_weather_url)  # ←のURLを関数の引数に設定する
soup = BeautifulSoup(Page.text, 'lxml')
weather_box = soup.find('table', {'class': 'forecast-top'})
dates = '#infotablefont > tbody > tr:nth-child(1)'
weather_dates = weather_box.find_all('tr')[0]
weather_status = weather_box.find_all('tr')[1]
weather_rain = weather_box.find_all('tr')[2]
weather_credit = weather_box.find_all('tr')[3]
weather_highest = weather_box.find_all('tr')[4]
weather_lowest = weather_box.find_all('tr')[5]

# 情報出力
print('大阪府の週間天気予報')
print('----------------------------------------')
print('| 日付 | 天気    | 降水 | 信頼 | 最高 | 最低')
for i in range(1, 7):
    print('| ' + weather_dates.find_all('th')[i].text, end=' | ')
    print(weather_status.find_all('td')[i].text.replace('\n', ''), end=' | ')
    # 絵文字
    print(weather_rain.find_all('td')[i].text.replace('/', '')[0:2] + '%', end=' | ')
    print(weather_credit.find_all('td')[i].text, end=' | ')
    print(weather_highest.find_all('td')[i].text[0:2], end=' | ')
    print(weather_lowest.find_all('td')[i].text[0:2])

print('----------------------------------------')
