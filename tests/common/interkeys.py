import requests
from tests.logger.logger import Logger
logger = Logger()

class Inter:
    def __init__(self,base_url, token):
        """初始化Inter类
        Args:
            base_url: 基础URL
        """
        self.base_url = base_url
        self.base_url = self.base_url.rstrip('/')
        self.session = requests.Session()
        self.default_headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'}
        self.logger = Logger()
        self.context = {}  # 新增：用于保存公共参数

    def get(self, path, params=None, headers = None):
        """发送GET请求
        Args:
            path: API路径，例如 '/users'
            params: URL参数字典
        Returns:
            requests.Response对象
        """
        url = f"{self.base_url}{path}"
        final_headers = {**self.default_headers, **headers} if headers else self.default_headers

        try:
            response = self.session.get(url, params=params, headers=final_headers)
            response.raise_for_status()
            self.logger.info(f"GET请求成功: {url}")
            return response.json() # dict
        except requests.exceptions.RequestException as e:
            self.logger.error(f"GET请求错误: {e}")
            print(f"GET请求错误: {e}")
            raise

    def post(self, url="", path_params=None,params=None):
        # 处理路径参数
        if path_params:
            url = url.format(**path_params)
            # 处理路径参数
        if params:
            url = url.format(**params)
        full_url = self.base_url + url
        try:
            if isinstance(params, dict):
                response = self.session.post(full_url, json=params, headers=self.default_headers)
                logger.info(response.json())
                self.logger.info(f"post请求成功: {full_url}")

            else:
                response = self.session.post(full_url, data=params,headers=self.default_headers)
                logger.info(response.json())
                self.logger.info(f"post请求成功: {full_url}")
            return response.json()
        except Exception as e:
            logger.error(f"Error in POST request to {full_url}: {e}")
            raise

    def upload_file(self, url, file_path):
        """发送带有文件上传的POST请求
        Args:
            url: API路径，例如 '/upload'
            file_path: 文件路径
            params: URL参数字典
        Returns:
            requests.Response对象
        """
        full_url = self.base_url + url
        files = {'file': open(file_path, 'rb')}
        headers = self.default_headers.copy()
        headers.pop('Content-Type', None)  # 让requests库自动设置Content-Type为multipart/form-data
        try:
            response = self.session.post(full_url, files=files, headers=headers)
            response.raise_for_status()
            self.logger.info(f"文件上传成功: {full_url}")
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"文件上传错误: {e}")
            print(f"文件上传错误: {e}")
            raise

    def validation (self, response, expected_status_code, expected_data):
        """断言响应状态码和数据
        Args:
            response: requests.Response对象
            expected_status_code: 预期状态码
            expected_data: 预期数据
        """
        assert response.status_code == expected_status_code, f"预期状态码为{expected_status_code}，实际状态码为{response.status_code}"
        assert response.json() == expected_data, f"预期数据为{expected_data}，实际数据为{response.json()}"

    def put(self, path, params):
        """发送PUT请求
        Args:
            path: API路径，例如 '/users/1'
            data: 请求数据
        Returns:
            requests.Response对象
        """
        url = f"{self.base_url}{path}"
        try:
            response = self.session.put(url, json=params, headers=self.default_headers)
            response.raise_for_status()
            self.logger.info(f"PUT请求成功: {url}")
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"PUT请求错误: {e}")
            print(f"PUT请求错误: {e}")
            raise