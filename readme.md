这是一个python版本到的chatgtp聊天工具，该工具可以通过选择chatgtp的版本切换到chatgtp4.5
这样就可以不用去购买chatgtp4.5的月费用，而是根据使用流量来支付
这是一个简单的从openai拷贝过来的程序

你首先要有一个openai的账号，并在你计算的系统变量中hyt123保存Openai api key


程序中将会通过下面的代码，来读取
# 初始化OpenAI API
key = os.environ['hyt123']
os.environ['OPENAI_API_KEY'] = key


整个程序的使用办法如下
Install Python version 3.8 or above
run Python chat.py
