from http.client import responses

from tests.common.interkeys import Inter

inter = Inter()
class Testmsg:
    def test_send_sms(self):
        print(1)
        # response = inter.post("/sms/send", params={"mobile": "18810416252"})
        # print(response)


    def test_login(self):
        response = inter.post(url="/sms/login", params={"mobile": "18810416252", "smsCode": "3458"})
        # print(response.json())

