from pathlib import Path

import pytest
import os

from tests.common.interkeys import Inter
from tests.common.interkeys_with_ut import InterWithUT
from tests.common.yaml_util import YamlUtil
from tests.logger.logger import Logger


# # 初始化日志记录器
# log_dir = './logs'
# if not os.path.exists(log_dir):
#     os.makedirs(log_dir)
# logger = Logger(log_file=os.path.join(log_dir, 'pytest.log'))

# 全局范围的fixture
# @pytest.fixture(scope="module")
# def test_login_pre():
#     logger.info("用例执行前")  # 前置代码 用例执行前 scope="module"
#     yield # 生成器
#     logger.info("用例执行后")  # 后置代码 用例执行后
@pytest.fixture(scope="module")
def inter():
    return Inter("http://47.108.207.38:8002/lumi","")
@pytest.fixture(scope="module")
def inter_ota():
    return InterWithUT("http://36.189.234.237:29305/lumi", "")
@pytest.fixture(scope="module")
def inter_ota_backend():
    return InterWithUT("http://xj7-5.s.filfox.io:29304/lumi", "6jXCoH2aVCoYMrr96gCK")
@pytest.fixture(scope="module")
def inter_socket():
    return InterWithUT("http://xj7-5.s.filfox.io:29304/lumi", "6jXCoH2aVCoYMrr96gCK")
