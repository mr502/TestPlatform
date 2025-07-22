from pathlib import Path

import pytest
from zope.interface import interfacemethod

from tests.common.BaseDeviceTest import BaseDeviceTest
from tests.common.interkeys_with_ut import InterWithUT
from tests.common.yaml_util import YamlUtil
from tests.testcases.functional_test.conftest import inter_socket


class TestSocket:

    test_cases = BaseDeviceTest("socket_validate.yaml").test_cases
    @pytest.mark.parametrize("test_case", test_cases)
    @pytest.mark.usefixtures("inter_socket")
    def test_socket_validate(self,inter_socket,test_case):
        response = inter_socket.post("/device/validate",  params=test_case)

    test_cases = BaseDeviceTest("socket_config.yaml").test_cases
    @pytest.mark.parametrize("test_case", test_cases)
    @pytest.mark.usefixtures("inter_socket")
    def test_socket_config(self,inter_socket,test_case):
        response = inter_socket.post("/device/config",  params=test_case)

    test_cases = BaseDeviceTest("change_chat_history.yaml").test_cases
    @pytest.mark.parametrize("test_case", test_cases)
    @pytest.mark.usefixtures("inter_socket")
    def test_socket_change_chat_history(self,inter_socket,test_case):
        response = inter_socket.post("/device/chat-history/report",params=test_case)

    @pytest.mark.usefixtures("inter_socket")
    def test_change_memory(self):
        response = inter_socket().put("/device/saveMemory/testMacAddress",  params={"summaryMemory": "11summaryMemory"})

    @pytest.mark.usefixtures("inter_socket")
    def test_device_status_update(self):
        params={"batteryLevel": 13,"volumeLevel": 23,"status": 1 }
        response = inter_socket().put("/device/status/testMacAddress", params)
