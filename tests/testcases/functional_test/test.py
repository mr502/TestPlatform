from tests.common.interkeys import Inter

inter = Inter("","")
def test_device_unbind():

    response = inter.post(url="/device/unbind", params={"deviceId": "SN000mengrui"})
    #98e2f85faab33779959e242e5ac36f26    bcd9a5d0bf522e338818031bfb9356a1    c3e5eba05d841063c6de757a18174b98
    # roleid  a55b6c7d8e9f0a1b2c3d4e5f6a7b8c92
    # response = inter.get("/device/bind/list")
    # print(len(response.json()["data"]))
    # print(response.json())

def test_device_role():
    response = inter.get("/device/bcd9a5d0bf522e338818031bfb9356a1")
    print(response.json())
    print(response.json())

