import csv
import re
from tempfile import tempdir

data_path = r'outputWithStretch.csv'
data_open = open(data_path)
data_read = csv.DictReader(data_open)

output_path = r'preprocessed.csv'


csv_data = []
result = []

col_names =['POLYESTER','NYLON','POLYURETHANE','RAYON','POLYPROPYLENE','MODAL',
            'POLYETHYLENE','COTTON','PTT','CUPRA','ACETATE','CORDURA','SILK','SPNDEX']

output_col_names = ['Fabric','ProductName','POLYESTER','NYLON','POLYURETHANE','RAYON','POLYPROPYLENE','MODAL','POLYETHYLENE','COTTON',
'PTT','CUPRA','ACETATE','CORDURA','SILK','SPNDEX','Weight','Thick', 'LastStretchLength', 'LastStretchForce']

def get_last_stretch(stretch):
    temp_list = stretch[1:-1]
    last_stretch_length = 0
    last_stretch_force = 0
    for temp_cord in temp_list.split("],"):
        temp_cord = "".join(temp_cord.split('['))
        temp_cord = "".join(temp_cord.split(']'))
        temp_cord = "".join(temp_cord.split(' '))
        temp_cord = "".join(temp_cord.split('\''))   
        cord = temp_cord.split(',')
        if(cord == ['0', '0']):
            break
        last_stretch_length = float(cord[0])
        last_stretch_force = float(cord[1])
    
    return last_stretch_length, last_stretch_force
        
def validate_ratio(ratio_dict):
    sum = 0
    for _, v in ratio_dict.items():
        sum += int(v)
    if(sum == 100):
        return True
    else:
        return False

def get_mixing_ratio(mix):
    elements = mix.split("%")
    temp_dict = {}
    for element in elements:
        label = re.sub(r'[^A-Z]', '', element)
        percentage = re.sub(r'[^0-9]', '', element)
        
        if(label in col_names):
            temp_dict[label] = percentage
    if validate_ratio(temp_dict):
        return temp_dict
    else:
        raise Exception()

for row in data_read:
    csv_data.append(row)
    temp_data = {}
    try:
        temp_data['Fabric'] = row['원단구분']
        temp_data['ProductName'] = row['상품명']
        ratio = get_mixing_ratio(row['혼용율']) 
        last_stretch_length, last_stretch_force = get_last_stretch(row['바이어스 스트레치 강도'])
        temp_data['LastStretchLength'] = last_stretch_length
        temp_data['LastStretchForce'] = last_stretch_force
        temp_data['Weight'] = row['단위면적당 무게']
        temp_data['Thick'] = row['두께']
        for col in col_names:
            try:
                temp_data[col] = ratio[col]
            except Exception as e:
                temp_data[col] = 0
        result.append(temp_data)
    except Exception as e:
        pass

# print(result[-1])
# exit()

with open('preprocessed.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, output_col_names)
    dict_writer.writeheader()
    dict_writer.writerows(result)
        

