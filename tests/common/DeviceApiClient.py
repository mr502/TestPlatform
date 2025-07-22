
class DeviceApiClient:
    @staticmethod
    def device_register( inter, params):
        return inter.post("/device/register", params=params)

    # @staticmethod
    # def device_bound_macAddress(inter, params):
    #     return inter.post("/device/bound/macAddress", params=params)

    @staticmethod
    def device_list(inter,):
        return inter.get("/device/bind/list")

    @staticmethod
    def device_unbind(inter, params):
        return inter.post("/device/unbind",params=params)

    @staticmethod
    def device_role(inter, test_case):
        return inter.get(f"/device/{test_case['deviceId']}")

    @staticmethod
    def user_info(inter,):
        return inter.get("/user/info")

    @staticmethod
    def device_role_display(inter):
        return inter.get("/role/display")

    #  8 更新设备角色
    @staticmethod
    def device_role_update(inter,params):
        return inter.put("/device/role",params)

    @staticmethod
    def device_chat_history(inter,test_case):
        return inter.get(f"/device/{test_case['macAddress']}/sessions?page=10&limit=10")

    @staticmethod
    def session_chat_history(inter,test_case):
        return inter.get(f"/session/{test_case['sessionId']}/messages?page=10&limit=10")
    # 13. 退出登录
    @staticmethod
    def logout(inter):
        return inter.post("/user/logout")
    # 14. 更新设备音量
    @staticmethod
    def device_volume(inter,params,deviceId):
        return inter.put("/device/volume/"+deviceId,params)
    # 15 绑定用户手机号
    @staticmethod
    def user_bind_phone(inter,params):
        return inter.post("/user/bind-phone",params)
    # 16 按设备获取聊天记录
    @staticmethod
    def deviceId_chat_history(inter,deviceId):
        return inter.get(f"/chat-history/device/{deviceId}?page=10&limit=10")
    # 17 按角色查看内容集列表
    @staticmethod
    def role_collection_list(inter,roleId):
        return inter.get(f"/content-collection/role/{roleId}")

    # 18. 获取指定内容集下的内容列表
    @staticmethod
    def collection_content(inter,collectionId):
        return inter.get(f"/content/collection/{collectionId}?page=1&limit=10&keywords=?")
    # 19. 修改设备别名
    @staticmethod
    def device_name_update(inter,deviceId,params):
        return inter.put(f"/device/alias/{deviceId}",params)

    # 20. 修改用户昵称
    @staticmethod
    def user_nickname_update(inter,params):
        return inter.put("/user/nickname",params)

    # 21. 更新头像
    @staticmethod
    def user_avatar_update(inter,params):
        return inter.put("/user/avatar",params)

    @staticmethod
    def assert_response(response, expected_status_code):
        assert response["code"] == expected_status_code

    @staticmethod
    def log_response(response):
        print(f"Response: {response}")

    # 管理端
#     新建内容集
    @staticmethod
    def create_content_collection(inter,params):
        return inter.post("/content-collection",params)

