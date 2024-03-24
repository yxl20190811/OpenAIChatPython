ChatGTP Python 工具
这是一个 Python 版本的 ChatGTP 聊天工具。该工具允许用户切换到 ChatGTP 4.5 版本，而无需购买 ChatGTP 4.5 的月费用，而是根据使用流量进行支付。这是一个简单的从 OpenAI 拷贝过来的程序。

准备工作
首先，你需要拥有一个 OpenAI 的账号。
在你的计算机系统变量中，设置环境变量 hyt123，并将你的 OpenAI API Key 保存在其中。
python
Copy code
import os

key = os.environ['hyt123']
os.environ['OPENAI_API_KEY'] = key
使用方法
安装 Python 版本 3.8 或以上。
运行 Python 文件 chat.py。
