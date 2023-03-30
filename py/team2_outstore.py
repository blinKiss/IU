import pandas as pd
import re

df = pd.read_csv('./IU/data/서울시 인터넷 쇼핑몰 100개 평가 정보.csv')
# 2년치만 선택
df_s = df[df['평가년도'] >= 2021].iloc[:, :5]
df_s = df_s.drop(columns='연번')

# 도메인명이 인터넷 주소가 아닌 데이터 찾기
domain = re.compile('[가-힣]+')
# temp = df_s[df_s['도메인명'].str.contains(domain)]
temp = df_s[~df_s['도메인명'].str.contains(
    '[\.(com|co|net)$]')]  # 신기한 정규식 ~ = not을 의미
# print(temp)

# 도메인명이 한글인 데이터를 인터넷 주소로 변경
df_s.loc[df_s['도메인명'] == '쿠팡 모바일앱', '도메인명'] = 'www.coupang.com'
df_s.loc[df_s['도메인명'] == '쿠팡이츠 모바일앱', '도메인명'] = 'www.coupangeats.com'
df_s.loc[df_s['도메인명'] == '요기요 모바일앱', '도메인명'] = 'www.yogiyo.com'
df_s.loc[df_s['도메인명'] == '배민 모바일앱', '도메인명'] = 'www.baemin.com'
df_s.loc[df_s['도메인명'] == 'GRIP 모바일앱', '도메인명'] = 'www.grip.show'
df_s.loc[df_s['도메인명'] == '배달의 민족 모바일앱', '도메인명'] = 'www.baemin.com'
df_s.loc[df_s['도메인명'] == '티몬 모바일앱', '도메인명'] = 'www.tmon.co.kr'
# print(df_s)

print(df_s.to_csv('./IU/data/team2_outstore.csv', mode='w', index=None))
