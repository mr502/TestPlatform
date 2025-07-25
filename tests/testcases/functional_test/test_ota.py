from pathlib import Path
import pytest

from tests.common.yaml_util import YamlUtil
from tests.testcases.functional_test.conftest import inter_ota

class T1estOta:
    yaml_util = YamlUtil(Path(__file__).parent.parent.parent / "data" / "ota_locate.yaml")
    test_cases_ota_locate = yaml_util.load_test_cases()

    @pytest.mark.parametrize("test_case", test_cases_ota_locate)
    @pytest.mark.usefixtures("inter_ota")
    def test_ota_locate(self, inter_ota, test_case):
        response = inter_ota.get("/ota/locate", headers=test_case)
        print(test_case)
        print(response.json())



    yaml_util = YamlUtil(Path(__file__).parent.parent.parent / "data" / "ota_device.yaml")
    test_cases_ota_device = yaml_util.load_test_cases()

    @pytest.mark.parametrize("test_case", test_cases_ota_device)
    @pytest.mark.usefixtures("inter_ota")
    def test_ota_device(self, inter_ota,test_case):
        response = inter_ota.post("/ota",headers=test_case)
        print(response)

    yaml_util = YamlUtil(Path(__file__).parent.parent.parent / "data" / "ota_apply_token_by_deviceId.yaml")
    test_cases_ota_apply_token = yaml_util.load_test_cases()
    @pytest.mark.parametrize("test_case", test_cases_ota_apply_token)
    @pytest.mark.usefixtures("inter_ota_backend")
    def test_apply_token(self,  inter_ota_backend,test_case):
        response = inter_ota_backend.post("/device/applyToken",params=test_case)
        print(test_case)
        print(response)


