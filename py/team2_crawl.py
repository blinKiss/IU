import re
import requests
import pandas as pd
# import oracledb
from bs4 import BeautifulSoup


URL = 'https://lovelyshoes.co.kr'

# html 텍스트 가져오기
txt1 = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"}).text

# 상품 종류별 탭으로 나누기 0 은 관계없고 1은 BEST, 마지막은 자체제작이라 종류가 아니므로 제외
txt_split = txt1.split('<div class="swiper-slide">')[2:-1]

# 리스트에 넣어주기위해 리스트 생성 price2, 3 = 판매가, 할인가
prod_kind, prod_code, prod_name, prod_image, prod_price2, prod_price3, prod_content = [
], [], [], [], [], [], []

# 정규식사용 시 문자열 앞에 r(raw string)을 붙이면 ex) \s를 \\s 이렇게 쓰지 않고도 사용 가능
# 해당 r"anchorBoxId_(\d+)" 는 "anchorBoxId_" 문자열 뒤에 오는 (\d+) 를 찾아서 그룹화 해줌 // 스티커 메모에 추가

# 반복문으로 리스트에 추가
for temp in txt_split:
    # beautifulsoup으로 변환
    soup = BeautifulSoup(temp, 'html.parser')

    # 종류
    kind_temp = soup.select_one('p.tab_tit').text.split('/')
    prod_kind.append(kind_temp)

    # 코드
    get_code = re.compile(r"anchorBoxId_(\d+)")
    code_temp = get_code.findall(temp)
    prod_code.append(code_temp)

    # 이름
    name_temp = [n.get_text() for n in soup.select('span.name > span')]
    prod_name.append(name_temp)

    # 이미지
    image_temp = [i.get('src') for i in soup.select('img[src]')]
    prod_image.append(image_temp)

    # 판매가
    price2_temp = [p2.get_text().replace(',', '').replace('원', '') for p2 in soup.select(
        'ul.xans-element-.xans-product li:nth-child(2) strong.title.displaynone ~ span:nth-child(2)')]
    prod_price2.append(price2_temp)

    # 할인가
    sale_temp = soup.select(
        'ul.xans-element-.xans-product li.xans-record- strong.title.displaynone ~ span:nth-child(2)')
    price3_temp = [s.get_text() for s in sale_temp]
    # print(price3_temp)
    prod_price3.append(price3_temp)

    # 내용
    content_temp = [c.get_text() for c in soup.select(
        'ul.xans-element-.xans-product li:nth-child(1) strong.title.displaynone ~ span:nth-child(2)')]
    prod_content.append(content_temp)


for pc in range(len(prod_content)):
    prod_content[pc] = ([pr.replace('\r\n', ' ') for pr in prod_content[pc]])

# 할인가 부분에 빈 곳이 있어 판매가를 넣어줌 - ex)판매가 만원 할인 X > 판매가 만원 할인가 만원
count = 0
dc = re.compile(r'\d+원')
for pp3 in prod_price3:

    for j in range(0, 36, 3):
        if len(pp3) < 36:
            pp3.append('')

        if not dc.search(pp3[j+2]):

            pp3.insert(j+2, pp3[j+1])
        # print(pp3[j:j+3])

    pp3 = [p.replace(',', '').replace('원', '') for p in pp3 if p != '']
    prod_price3[count] = pp3
    count += 1

# 할인가 마지막 수정
prod_price3 = [final[2::3] for final in prod_price3]

# 종류를 '/' 문자열로 구분해서 병합
count2 = 0
for k in prod_kind:
    if len(k) > 1:
        k = k[0] + '/' + k[1]
    else:
        k = k[0]
    prod_kind[count2] = [k]
    count2 += 1

# 데이터 프레임으로 변환 enumerate ? 좋은듯? // 스티커 메모에 추가
df = pd.DataFrame(columns=['prod_code', 'kind', 'name',
                  'image', 'price2', 'price3', 'content'])
for i, pk in enumerate(prod_kind):
    cod = prod_code[i]
    nam = prod_name[i]
    img = prod_image[i]
    p2 = prod_price2[i]
    p3 = prod_price3[i]
    con = prod_content[i]

    temp_data = pd.DataFrame(
        {'prod_code': cod, 'kind': pk*len(p2), 'name': nam, 'image': img, 'price2': p2, 'price3': p3, 'content': con})
    df = pd.concat([df, temp_data])

# 문자열 숫자로 변환
df[['prod_code', 'price2', 'price3']] = df[[
    'prod_code', 'price2', 'price3']].apply(pd.to_numeric)

# CSV로 저장
print(df.to_csv('./IU/data/team2_crawl.csv', mode='w', index=None))

# DB에 저장
# csv 파일 오라클에 임포트 // 겹치는 상품이 있어서 prod_code 의 primary key 해제
