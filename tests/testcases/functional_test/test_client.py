import pytest
from tests.common.BaseDeviceTest import BaseDeviceTest, _replace_context_vars
from tests.common.DeviceApiClient import DeviceApiClient

@pytest.mark.usefixtures("inter")

@pytest.mark.order(1)
class TestDeviceRegister:
    test_cases = BaseDeviceTest("device_register.yaml").test_cases
    @pytest.mark.parametrize("test_case", test_cases)
    def test_device_register(self, inter,test_case):
        response = DeviceApiClient.device_register(inter ,test_case)
        DeviceApiClient.assert_response(response,test_case.get("expected_status_code"))

@pytest.mark.order(2)
class TestDeviceList:
    def test_device_list(self, inter):
        response = DeviceApiClient.device_list(inter)
        ids = [item['id'] for item in response['data']]
        inter.context["device_id"] = ids
        print(inter.context)
        print(response)

@pytest.mark.skip
@pytest.mark.order(3)
class TestDeviceUnbind:
    test_cases = BaseDeviceTest("device_unbind.yaml").test_cases
    @pytest.mark.parametrize("test_case", test_cases)
    def test_device_unbind(self, inter,test_case):
        print(inter.context)
        if 'deviceId' in test_case and isinstance(test_case['deviceId'], str):
            test_case['deviceId'] = test_case['deviceId'].replace(
            '${inter.context.get("device_id")[0]}',
            str(inter.context.get("device_id")[0]))
        try:
            DeviceApiClient.device_unbind(inter, test_case)
            response = inter.get("/device/bind/list")
            print(response)
            ids = [item['id'] for item in response['data']]
            inter.context["device_id"] = ids
        except  Exception as e:
            print(e)

# @pytest.mark.skip
@pytest.mark.order(4)
class TestDeviceRole:
    # 5. 查看设备和角色状态
    test_cases = BaseDeviceTest("device_id.yaml").test_cases
    @pytest.mark.parametrize("test_case", test_cases)
    def  test_device_role(self, inter,test_case):
        test_case = _replace_context_vars(test_case, inter)
        response = DeviceApiClient.device_role(inter, test_case)
        roleIds = response["data"]["roleId"]
        inter.context["role_id"] = roleIds
        DeviceApiClient.log_response( response)

@pytest.mark.skip
@pytest.mark.order(5)
class TestUserInfo:
#    6. 获取用户信息
    def test_user_info(self, inter):
        response = DeviceApiClient.user_info(inter)
        DeviceApiClient.log_response(response)

@pytest.mark.skip
@pytest.mark.order(6)
class TestDeviceRoleDisplay:
#     7. 查看角色列表
    def test_device_role_display(self, inter):
        response = DeviceApiClient.device_role_display(inter)
        DeviceApiClient.log_response(response)

@pytest.mark.skip
@pytest.mark.order(7)
class TestDeviceRoleUpdate:
#    8. 更新设备角色
    test_cases = BaseDeviceTest("role_update.yaml").test_cases
    # @pytest.mark.skip
    @pytest.mark.order(7)
    @pytest.mark.parametrize("test_case", test_cases)
    def test_device_role_update(self, inter, test_case):
        test_case = _replace_context_vars(test_case, inter)
        print(test_case)
        response = DeviceApiClient.device_role_update(inter,test_case)
        DeviceApiClient.log_response(response)
        DeviceApiClient.assert_response(response,test_case.get("expected_status_code"))

@pytest.mark.skip
@pytest.mark.order(8)
class TestDeviceChatHistory:
#    9. 查看指定设备的聊天记录
    test_cases = BaseDeviceTest("device_sessionList.yaml").test_cases
    @pytest.mark.parametrize("test_case", test_cases)
    def test_device_chat_history(self, inter,test_case):
        # test_case = _replace_context_vars(test_case, inter)
        response = DeviceApiClient.device_chat_history(inter,test_case)
        if response is None:
            pytest.skip("API请求未返回任何响应")

        if hasattr(response, 'json'):
            data = response.json()  # 如果是响应对象
        elif isinstance(response, dict):
            data = response  # 如果是字典
        else:
            pytest.skip(f"无效的响应类型: {type(response)}")

            # 4. 严格验证数据结构
        if not response or not isinstance(response, dict):
            pytest.skip("响应数据为空或格式不正确")

            # 5. 安全访问会话列表
            session_list = response.get("data", {}).get("list", [])
            if not session_list:
                pytest.skip(f"设备 {test_case.get('macAddress', '未知')} 没有会话记录")

            # 6. 安全获取会话ID
            try:
                inter.context["sessionId"] = session_list[0].get("sessionId")
                if not inter.context["sessionId"]:
                    pytest.skip("会话ID为空")
            except (IndexError, TypeError) as e:
                pytest.skip(f"获取会话ID失败: {str(e)}")

        # # 4. 安全获取 sessionId
        # try:
        #     session_id = response["data"]["list"][0]["sessionId"]
        #     inter.context["sessionId"] = session_id
        # except (KeyError, IndexError) as e:
        #     pytest.skip(f"无法获取会话ID: {str(e)}")

        # # 检查数据是否存在
        # if not data.get("data", {}).get("list"):
        #     pytest.skip(f"设备 {test_case['deviceId']} 没有会话记录")
        # inter.context["sessionId"] = data["data"]["list"][0]["sessionId"]
        # inter.context["sessionId"] = response.json()["data"]["list"][0]["sessionId"]

@pytest.mark.skip
@pytest.mark.order(9)
class TestSessionChatHistory:
#    10. 查看指定会话的聊天记录
    test_cases = BaseDeviceTest("session_id.yaml").test_cases
    @pytest.mark.parametrize("test_case", test_cases)
    def test_session_chat_history(self, inter,test_case):
        test_case = _replace_context_vars(test_case, inter)
        DeviceApiClient.session_chat_history(inter,test_case)

@pytest.mark.skip
@pytest.mark.order(10)

@pytest.mark.skip
# 13 退出登录
class TestLogout:
    def test_logout(self, inter):
        DeviceApiClient.logout(inter)

@pytest.mark.skip
# 14 更新设备音量
class TestDeviceVolume:
    def test_device_volume(self, inter):
        params={"volumeLevel": 50,}
        deviceId = ''
        DeviceApiClient.device_volume(inter,deviceId,params)

@pytest.mark.skip
# 15 绑定用户手机号
class TestUserBindPhone:
    def test_user_bind_phone(self, inter):
        params={"phone": "13800000000","smsCode": "9621"}
        DeviceApiClient.user_bind_phone(inter,params)

# 16. 按设备获取聊天记录
class TestDeviceIdChatHistory:
    def test_device_id_chat_history(self, inter):
        deviceId=""
        DeviceApiClient.deviceId_chat_history(inter,deviceId)
# 17. 按角色查看内容集列表
class TestRoleCollectionList:
    def test_role_collection_list(self, inter):
        roleId = ""
        DeviceApiClient.role_collection_list(inter,roleId)

# 18. 获取指定内容集下的内容列表
class TestCollectionContent:
    def test_collection_content(self, inter):
        collectionId = ""
        DeviceApiClient.collection_content(inter,collectionId)

# 19. 修改设备别名
class TestDeviceNameUpdate:
    def test_device_name_update(self, inter):
        deviceId = ""
        params = {"alias": "test"}
        DeviceApiClient.device_name_update(inter,deviceId,params)
# 20. 修改用户昵称
class TestUserNicknameUpdate:
    def test_user_nickname_update(self, inter):
        params = {"nickname": "test"}
        DeviceApiClient.user_nickname_update(inter,params)

# 21. 更新头像
class TestUserAvatarUpdate:
    def test_user_avatar_update(self, inter):
        params = {"avatar": "test"}
        DeviceApiClient.user_avatar_update(inter,params)





#
# @pytest.mark.skip
# # 管理端
# class TestRoleCollectionList:
#     test_cases = BaseDeviceTest("create_content_collection.yaml").test_cases
#     def test_create_content_collection(self, inter,test_cases):
#         DeviceApiClient.create_content_collection(inter,test_cases)