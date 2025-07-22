import subprocess
import os

def generate_allure_report():
    # 确保当前路径正确（可根据你的项目调整）
    result_dir = "./allure-results"
    report_dir = "./allure-report"

    # 检查结果目录是否存在
    if not os.path.exists(result_dir):
        print(f"[ERROR] 测试结果目录不存在: {result_dir}")
        return

    try:
        # 构建 Allure 命令
        cmd = ["allure", "generate", result_dir, "-o", report_dir, "--clean"]
        print(f"[INFO] 生成 Allure 报告中...")

        subprocess.run(cmd, check=True)
        print(f"[SUCCESS] Allure 报告已生成在 {report_dir}")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] 生成 Allure 报告失败: {e}")

if __name__ == "__main__":
    generate_allure_report()
