import os
import time
import subprocess
import sys

if os.path.exists('AAA.txt'):
        os.remove('AAA.txt')

# 设置间隔时间 (毫秒)
t = 100  # 修改这个值以控制脚本之间的间隔时间

# 获取用户输入，只询问一次
phone = input("请输入变量 phone: ")

# 获取当前目录下的所有 py 文件，排除 AAA.py
scripts = [f for f in os.listdir('.') if f.endswith('.py') and f != 'AAA.py']

# 按名称排序
scripts.sort()

# 打印所有可运行的脚本
print("\n可运行的脚本：")
for script in scripts:
    print(script)

# 指定已有虚拟环境的路径
venv_path = './.venv'  # 根据实际情况修改路径

# 激活虚拟环境
if os.name == 'nt':
    activate_script = os.path.join(venv_path, 'Scripts', 'activate_this.py')
else:
    activate_script = os.path.join(venv_path, 'bin', 'activate_this.py')


# 在当前环境中执行激活脚本
exec(open(activate_script).read(), dict(__file__=activate_script))

# 使用虚拟环境在死循环中运行子脚本
try:
    while True:  # 死循环
        for script in scripts:
            print(f"正在运行脚本: {script}，并传递参数 phone: {phone}")
            subprocess.Popen([sys.executable, script, phone])  # 启动脚本，并传递参数
            time.sleep(t / 1000)  # 等待 t 毫秒
        if os.path.exists('AAA.txt'):
            os.remove('AAA.txt')
except KeyboardInterrupt:
    print("停止运行所有脚本...")
