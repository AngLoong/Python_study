"""
功能模块
"""

import numpy as np
import pandas as pd
import time
from mrs_read_plate import ReadPlate
from mrs_analysis import ana_stability
from mrs_file import export_plate_od_to_csv


def open_or_close_door():
    door = ReadPlate()
    door.door()


def input_id():
    ret = input("输入仪器编号")
    return ret

def measure_test(id):
    print("开始测量仪器......")
    read_plate = ReadPlate()
    read_plate.mode = 1
    read_plate.shake["strength"] = 2
    read_plate.shake["seconds"] = 60
    read_plate.filter["du"] = 1
    read_plate.filter["first_filter_num"] = 1
    read_plate.filter["second_filter_num"] = 4
    file_name = "./record/" + id + ".csv"
    measure_time = time.strftime("%Y/%m/%d %H:%M:%S",time.localtime())
    print(measure_time)
    read_plate.read_plate()
    print(read_plate.data)
    ser_time = pd.Series({"measure time:":measure_time,"":""})
    ser_time.to_csv(file_name,header=False)
    ser_temp = pd.Series({"filter num :":read_plate.filter["first_filter_num"]})
    ser_temp.to_csv(file_name,header=False,mode="a+")
    export_plate_od_to_csv(file_name,read_plate.data.tolist(),"a+")
    time.sleep(3)
    read_plate.shake["seconds"] = 0
    read_plate.filter["first_filter_num"] = 2
    read_plate.read_plate()
    print(read_plate.data)
    ser_temp = pd.Series({"filter num :":read_plate.filter["first_filter_num"]})
    ser_temp.to_csv(file_name,header=False,mode="a+")
    export_plate_od_to_csv(file_name,read_plate.data.tolist(),"a+")
    time.sleep(3)
    read_plate.shake["seconds"] = 0
    read_plate.filter["first_filter_num"] = 3
    read_plate.read_plate()
    print(read_plate.data)
    ser_temp = pd.Series({"filter num :":read_plate.filter["first_filter_num"]})
    ser_temp.to_csv(file_name,header=False,mode="a+")
    export_plate_od_to_csv(file_name,read_plate.data.tolist(),"a+")
    time.sleep(3)
    read_plate.shake["seconds"] = 0
    read_plate.filter["first_filter_num"] = 4
    read_plate.read_plate()
    print(read_plate.data)
    ser_temp = pd.Series({"filter num :":read_plate.filter["first_filter_num"]})
    ser_temp.to_csv(file_name,header=False,mode="a+")
    export_plate_od_to_csv(file_name,read_plate.data.tolist(),"a+")
    time.sleep(3)
    read_plate.filter["du"] = 2
    read_plate.filter["first_filter_num"] = 2
    read_plate.filter["second_filter_num"] = 4
    read_plate.mode = 3
    read_plate.kinetics["times"] = 50
    read_plate.kinetics["seconds"] = 3
    df_data = read_plate.read_kinetics()
    df_result = ana_stability(df_data)
    df_result.to_csv(file_name,mode="a+")
    print("测量结束!!!")


if __name__ == '__main__':
    id = input_id()
    open_or_close_door()
    while True if input("放入酶标板后，按y继续") != 'y' else False:
        pass
    measure_test(id)