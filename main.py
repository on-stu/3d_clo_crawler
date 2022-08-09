import csv
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def convertTableToJson(tableData):
    table_data = [[cell.text for cell in row("td")]
                         for row in BeautifulSoup(tableData)("tr")]
    return table_data


def convertTable(table_string):
    table_object = BeautifulSoup(table_string,  "html.parser")
    trs = table_object.find_all("tr")
    result = []

    for tr in trs:
        tds = tr.find_all("td")
        tr_value = []
        for td in tds:
            td_input = td.find("input")
            tr_value.append(td_input.get('value'))

        result.append(tr_value)
    return result

driver = webdriver.Chrome()
chrome_options = Options()
chrome_options.add_experimental_option("detach", False)


item_number = "001"

col_names=["원단구분", "용도", "혼용율", "구성원사/번수", "밀도", "조직", "후가공", "상품명", "단위면적당 무게", "두께", "경사 스트레치 강도", "위사 스트레치 강도", "바이어스 스트레치 강도"]
data={}

url = 'https://www.digitalfabric.co.kr/login'
driver.get(url)
driver.find_element(By.NAME, 'mem_userid').send_keys('beautifuldays76')
driver.find_element(By.NAME, 'mem_password').send_keys('ehdgoanf1!')
driver.find_element(By.XPATH, '//button[@type="submit"]').click()
result = []

sleep(1)
for i in range(1, 1000):
    print('processing : {} / {}'.format(i, 1000))
    index = i
    if(i < 10):
        index = "00{}".format(i)
    elif(9<i<100):
        index = "0{}".format(i)
    url = 'https://www.digitalfabric.co.kr/item/KITECH_{}'.format(index)
    driver.get(url)
    if(driver.title == "404 Page Not Found"):
        print("product number ({}) is not found".format(i))
    else:
        html = driver.page_source
        bsObject = BeautifulSoup(html, "html.parser")

        # 원단구분
        data[col_names[0]] = bsObject.find('div', {'class': 'detail-divide detail-divide-2'}).find('option', {'selected': True}).get('value')

        # 용도
        checkedId = bsObject.find_all('div', {'class': 'detail-divide'})[0].find('input', {'checked': True}).get('id')
        data[col_names[1]] = bsObject.find_all('div', {'class': 'detail-divide'})[0].find('label', {'for': checkedId}).get_text()

        # 혼용율
        data[col_names[2]] = bsObject.find_all('div', {'class': 'detail-divide'})[1].find('input').get('value')

        # 구성원사 / 번수
        yarn_count = bsObject.find_all('div', {'class': 'detail-divide'})[2].find('input').get('value')
        data[col_names[3]] = yarn_count

        # 밀도
        density = bsObject.find_all('div', {'class': 'detail-divide'})[3].find('input').get('value')
        data[col_names[4]] = density

        # 조직
        structure = bsObject.find_all('div', {'class': 'detail-divide'})[3].find_all('input')[1].get('value')
        data[col_names[5]] = structure

        # 후가공
        finishing = bsObject.find_all('div', {'class': 'detail-divide'})[4].find_all('input')[0].get('value')
        data[col_names[6]] = finishing

        # 상품명
        product_name = bsObject.find_all('div', {'class': 'detail-divide'})[5].find_all('input')[1].get('value')
        data[col_names[7]] = product_name

        #단위 면적 당 무게
        weight = driver.find_element(By.XPATH, '//input[@id="clo_mg"]').get_attribute('value')
        data[col_names[8]] = weight

        #두께
        thick = driver.find_element(By.XPATH, '//input[@id="clo_mm"]').get_attribute('value')
        data[col_names[9]] = thick

        #경사 스트레치 강도
        stretch_col = bsObject.find_all('div', {'class': 'col-md-6 col-sm-6 col-xs-12 mb-2'})[0].find_all('table')[0]
        table_list = convertTable(str(stretch_col))
        data[col_names[10]] = str(table_list)


        #위사 스트레치 강도
        stretch_row = bsObject.find_all('div', {'class': 'col-md-6 col-sm-6 col-xs-12 mb-2'})[1].find_all('table')[0]
        table_list = convertTable(str(stretch_row))
        data[col_names[11]] = str(table_list)

        #바이어스 스트레치 강도
        stretch_bias = bsObject.find_all('div', {'class': 'col-xs-12 mb-0'})[2].find_all('table')[0]
        table_list = convertTable(str(stretch_bias))
        data[col_names[12]] = str(table_list)
        result.append(data)        
        
        data={}

with open('outputWithStretch.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, col_names)
    dict_writer.writeheader()
    dict_writer.writerows(result)

print('done')
