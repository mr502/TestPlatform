# import os
#
# import pytest
#
# pytest.main()
#
# os.system('allure generate ./allure-results -o ./allure-report')
import subprocess
import os
import shutil
import sys

RESULT_DIR = "allure-results"
REPORT_DIR = "allure-report"

def clean_directories():
    print("📦 正在清理旧的报告目录...")
    shutil.rmtree(RESULT_DIR, ignore_errors=True)
    shutil.rmtree(REPORT_DIR, ignore_errors=True)

def run_pytest():
    print("🧪 正在运行 pytest 测试用例...")
    result = subprocess.run(["pytest", f"--alluredir={RESULT_DIR}"])
    # if result.returncode != 0:
    #     print("❌ pytest 执行失败")
    #     sys.exit(1)

def generate_allure_report():
    print("📊 正在生成 Allure 报告...")
    result = subprocess.run(["allure", "generate", RESULT_DIR, "-o", REPORT_DIR, "--clean"])
    if result.returncode != 0:
        print("❌ Allure 报告生成失败")
        sys.exit(1)

def open_allure_report():
    print("🌐 正在打开 Allure 报告...")
    result = subprocess.run(["allure", "open", REPORT_DIR])
    if result.returncode != 0:
        print("❌ 打开 Allure 报告失败")
        sys.exit(1)

def main():
    clean_directories()
    run_pytest()
    generate_allure_report()
    open_allure_report()
    print("✅ 全部完成！报告已在浏览器中打开")

if __name__ == "__main__":
    main()
