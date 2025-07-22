import yaml
class YamlUtil:
    def __init__(self, file_path):
        self.path = None
        self.file_path = file_path
    def load_test_cases(self):
        with open(self.file_path, 'r') as file:
            data = yaml.safe_load(file)
            return data.get('test_cases', [])

    def save_test_cases(self, test_cases):
        with open(self.file_path, 'w') as file:
            yaml.safe_dump({'test_cases': test_cases}, file, sort_keys=False)

    def update_test_case(self, test_case, actual_code, test_cases):
        """更新测试用例的实际状态码并保存"""
        test_case['actual_code'] = actual_code
        for i, case in enumerate(test_cases):
            if case == test_case:
                test_cases[i] = test_case
                break
        self.save_test_cases(test_cases)

