import pymysql
import logging

from tests.logger.logger import Logger

# 配置日志，便于调试和问题追踪
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = Logger()
class DatabaseConnector:
    """
    一个用于连接和操作MySQL数据库的类。
    封装了数据库的连接、断开、查询和数据操作。
    """

    def __init__(self, host, user, password, db_name, port=29306, charset='utf8mb4'):
        """
        初始化数据库连接器。

        Args:
            host (str): 数据库主机地址。
            user (str): 数据库用户名。
            password (str): 数据库密码。
            db_name (str): 数据库名称。
            port (int, optional): 数据库端口。默认为 3306。
            charset (str, optional): 数据库编码。默认为 'utf8mb4'。
        """
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name
        self.port = port
        self.charset = charset
        self.conn = None
        self.cursor = None
        logging.info(f"DatabaseConnector initialized for DB: {self.db_name}@{self.host}:{self.port}")

    def connect(self):
        """
        建立数据库连接。
        """
        try:
            self.conn = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db_name,
                port=self.port,
                charset=self.charset,
                cursorclass=pymysql.cursors.DictCursor # 返回字典形式的查询结果，更易读
            )
            self.cursor = self.conn.cursor()
            logging.info("Successfully connected to the database.")
            return True
        except pymysql.Error as e:
            logging.error(f"Failed to connect to database: {e}")
            self.conn = None
            self.cursor = None
            return False

    def disconnect(self):
        """
        关闭数据库连接。
        """
        if self.cursor:
            self.cursor.close()
            self.cursor = None
            logging.info("Database cursor closed.")
        if self.conn:
            self.conn.close()
            self.conn = None
            logging.info("Database connection closed.")

    def execute_query(self, sql_query, params=None):
        """
        执行SQL查询语句 (SELECT)。

        Args:
            sql_query (str): 要执行的SQL查询字符串。
            params (tuple/list, optional): SQL查询中的参数。默认为 None。

        Returns:
            list: 查询到的所有行，每行是一个字典。
        """
        if not self.conn or not self.cursor:
            logging.warning("Database not connected. Attempting to connect...")
            if not self.connect():
                return []

        try:
            logging.debug(f"Executing query: {sql_query} with params: {params}")
            self.cursor.execute(sql_query, params)
            result = self.cursor.fetchall()
            logging.info(f"Query executed successfully. Rows returned: {len(result)}")
            return result
        except pymysql.Error as e:
            logging.error(f"Error executing query '{sql_query}': {e}")
            return []
        except Exception as e:
            logging.error(f"An unexpected error occurred during query execution: {e}")
            return []

    def execute_update(self, sql_statement, params=None):
        """
        执行SQL更新、插入或删除语句 (INSERT, UPDATE, DELETE)。

        Args:
            sql_statement (str): 要执行的SQL语句字符串。
            params (tuple/list, optional): SQL语句中的参数。默认为 None。

        Returns:
            int: 影响的行数。如果执行失败，返回 -1。
        """
        if not self.conn or not self.cursor:
            logging.warning("Database not connected. Attempting to connect...")
            if not self.connect():
                return -1

        try:
            logging.debug(f"Executing update: {sql_statement} with params: {params}")
            self.cursor.execute(sql_statement, params)
            self.conn.commit()  # 提交事务
            affected_rows = self.cursor.rowcount
            logging.info(f"Update executed successfully. Affected rows: {affected_rows}")
            return affected_rows
        except pymysql.Error as e:
            self.conn.rollback() # 回滚事务
            logging.error(f"Error executing update '{sql_statement}': {e}")
            return -1
        except Exception as e:
            self.conn.rollback() # 回滚事务
            logging.error(f"An unexpected error occurred during update execution: {e}")
            return -1

    def fetch_one(self, sql_query, params=None):
        """
        执行SQL查询语句，并获取单行结果。

        Args:
            sql_query (str): 要执行的SQL查询字符串。
            params (tuple/list, optional): SQL查询中的参数。默认为 None。

        Returns:
            dict/None: 查询到的单行数据（字典形式），如果没有结果则返回 None。
        """
        if not self.conn or not self.cursor:
            logging.warning("Database not connected. Attempting to connect...")
            if not self.connect():
                return None

        try:
            logging.debug(f"Fetching one: {sql_query} with params: {params}")
            self.cursor.execute(sql_query, params)
            result = self.cursor.fetchone()
            logging.info(f"Fetch one executed. Result: {'Found' if result else 'Not found'}")
            return result
        except pymysql.Error as e:
            logging.error(f"Error fetching one row with query '{sql_query}': {e}")
            return None
        except Exception as e:
            logging.error(f"An unexpected error occurred during fetch_one execution: {e}")
            return None

    def __enter__(self):
        """
        上下文管理器入口，支持 'with' 语句。
        """
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        上下文管理器出口，确保连接被关闭。
        """
        self.disconnect()