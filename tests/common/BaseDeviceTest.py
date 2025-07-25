from pathlib import Path

from tests.common.yaml_util import YamlUtil


def _replace_context_vars(test_case, inter):
    """替换测试用例中的上下文变量（如 deviceId）"""
    # 定义需要替换的变量名列表
    context_vars = ["device_id", "sessionId"]
    for key in test_case:
        if isinstance(test_case[key], str):
            for var_name in context_vars:
                # 匹配完整的变量模板格式
                template_str = f'${{inter.context.get("{var_name}")}}'
                if template_str in test_case[key]:
                    # 获取上下文中的实际值
                    actual_value = inter.context.get(var_name)
                    if actual_value is not None:
                        # 进行替换
                        test_case[key] = test_case[key].replace(
                            template_str,
                            str(actual_value[0])
                        )
    return test_case


class BaseDeviceTest:
    def __init__(self, yaml_file):
        self.yaml_util = YamlUtil(Path(__file__).parent.parent.parent/ "tests" / "data" / yaml_file)
        self.test_cases = self.yaml_util.load_test_cases()

