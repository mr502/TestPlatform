from pathlib import Path
import pytest
from tests.common.yaml_util import YamlUtil

#  设备注册 获取设备列表
class  TestDeviceRegister:
    yaml_util = YamlUtil(Path(__file__).parent.parent.parent / "data" / "device_register.yaml")
    test_cases_register = yaml_util.load_test_cases()
    @pytest.mark.parametrize("test_case", test_cases_register)
    @pytest.mark.usefixtures("inter")
    @pytest.mark.order(1)
    def test_device_register(self, inter, test_case):
        response = inter.post("/device/register",params=test_case)
        print(response["msg"])
    @pytest.mark.order(2)
    def test_device_list(self, inter):
        try:
            response = inter.get("/device/bind/list")
            print(response.json())
            ids = [item['id'] for item in response.json()['data']]
            inter.context["device_id"] = ids
            print(inter.context["device_id"])
        except Exception as e:
            print(e)


    yaml_util = YamlUtil(Path(__file__).parent.parent.parent / "data" / "device_unbind.yaml")
    test_cases_unbind = yaml_util.load_test_cases()
    @pytest.mark.order(3)
    @pytest.mark.parametrize("test_case", test_cases_unbind)
    def test_device_unbind(self, inter,test_case):
            if 'deviceId' in test_case and isinstance(test_case['deviceId'], str):
                test_case['deviceId'] = test_case['deviceId'].replace(
                '${inter.context.get("device_id")[0]}',
                str(inter.context.get("device_id")[0]))
                print(test_case)
            try:
                inter.post(url="/device/unbind", params=test_case)
                response = inter.get("/device/bind/list")
                ids = [item['id'] for item in response.json()['data']]
                inter.context["device_id"] = ids
                print(inter.context.get("device_id"))
            except  Exception as e:
                print(e)

    # @pytest.mark.order(4)
    # def test_device_list2(self, inter):
    #     response = inter.get("/device/bind/list")
    #     ids = [item['id'] for item in response.json()['data']]
    #     inter.context["device_id"] = ids
    #     print(inter.context["device_id"])


    # 5. 查看设备和角色状态

    yaml_util = YamlUtil(Path(__file__).parent.parent.parent / "data" / "device_id.yaml")
    test_cases_deviceId = yaml_util.load_test_cases()
    @pytest.mark.skip
    @pytest.mark.order(4)
    @pytest.mark.parametrize("test_case", test_cases_deviceId)
    def  test_device_role(self, inter,test_case):
        if 'deviceId' in test_case and isinstance(test_case['deviceId'], str):
            test_case['deviceId'] = test_case['deviceId'].replace(
                '${inter.context.get("device_id")}',
                str(inter.context.get("device_id"))
            )
        response = inter.get(f"/device/{test_case['deviceId']}")
        if response.json()["msg"]  == "success":
            inter.context["role_id"] = response.json()["data"]["roleId"]

        assert response.json()["msg"]  == "success" or response.status_code == 200
        print(response.json())
#    6. 获取用户信息
    @pytest.mark.skip
    @pytest.mark.order(5)
    def test_user_info(self, inter):
        response = inter.get("/user/info")
        print(response.json())
        assert response.json()["msg"]  == "success"
#     7. 查看角色列表
    @pytest.mark.skip
    @pytest.mark.order(6)
    def test_device_role_display(self, inter):
        response = inter.get("/role/display")
        print(response.json())
        assert response.json()["msg"]  == "success"

#    8. 更新设备角色
    yaml_util = YamlUtil(Path(__file__).parent.parent.parent / "data" / "role_update.yaml")
    test_cases_roleUpdate = yaml_util.load_test_cases()

    @pytest.mark.skip
    @pytest.mark.order(7)
    @pytest.mark.parametrize("test_case", test_cases_roleUpdate)
    def test_device_role_update(self, inter, test_case):
        if 'deviceId' in test_case and isinstance(test_case['deviceId'], str):
            test_case['deviceId'] = test_case['deviceId'].replace(
                '${inter.context.get("device_id")}',
                str(inter.context.get("device_id"))
            )
        device = inter.context.get("device_id")
        print(device)
        response = inter.put("/device/role",params=test_case)
        print(response.json())

#    9. 查看指定设备的聊天记录
    yaml_util = YamlUtil(Path(__file__).parent.parent.parent / "data" / "device_sessionList.yaml")
    test_cases_sessionList = yaml_util.load_test_cases()
    @pytest.mark.skip
    @pytest.mark.order(8)
    @pytest.mark.parametrize("test_case", test_cases_sessionList)
    def test_device_chat_history(self, inter,test_case):
        if 'deviceId' in test_case and isinstance(test_case['deviceId'], str):
            test_case['deviceId'] = test_case['deviceId'].replace(
                '${inter.context.get("device_id")}',
                str(inter.context.get("device_id"))
            )
        response = inter.get(f"/device/{test_case['deviceId']}/sessions?page=10&limit=10")
        data = response.json()
        # 检查数据是否存在
        if not data.get("data", {}).get("list"):
            pytest.skip(f"设备 {test_case['deviceId']} 没有会话记录")

        # 安全获取第一个会话ID
        inter.context["sessionId"] = data["data"]["list"][0]["sessionId"]
        inter.context["sessionId"] = response.json()["data"]["list"][0]["sessionId"]
        print(inter.context())

#    10. 查看指定会话的聊天记录
    yaml_util = YamlUtil(Path(__file__).parent.parent.parent / "data" / "session_id.yaml")
    test_cases_sessionId = yaml_util.load_test_cases()

    @pytest.mark.skip
    @pytest.mark.order(9)
    @pytest.mark.parametrize("test_case", test_cases_sessionId)
    def test_session_chat_history(self, inter,test_case):
        if 'sessionId' in test_case and isinstance(test_case['sessionId'], str):
            test_case['sessionId'] = test_case['sessionId'].replace(
                '${inter.context.get("sessionId")}',
                str(inter.context.get("sessionId"))
            )
        response = inter.get(f"/session/{test_case['sessionId']}/messages?page=10&limit=10")
        assert response.json()["msg"]  == "success" or response.status_code == 200
        print(inter.context)

    # @pytest.mark.order(10)
    # def test_device_list(self, inter):
    #     response = inter.get("/device/bind/list")
    #     print(response.json())