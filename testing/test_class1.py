#class TestDemlOne:
import pytest
import yaml



def get_data(local,a):
    with open(local) as f:
        res = yaml.safe_load(f)
        print(type(res.keys()))
        return [list(res.keys()),list(res.values())]

def step(a,b):
    for i in range(len(a)):
        if a[i] == "method1":
            print(f"执行方法1：{b[i]}")
        elif a[i] == "method2":
            print(f"执行方法1：{b[i]}")
        else:
            print(f"无此func{b[i]}")



def test_dome1(conn_db):
    yongli = get_data("./data.yml",1)
    step(yongli[0],yongli[1])
    print("执行test_dome1")
    print(f"输出fixture返回值:{conn_db}")

def test_rerun():
    pytest.assume(True)
    pytest.assume(False)
