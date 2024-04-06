# ChatGPT-Python

欢迎使用开源的ChatGPT聊天工具，一个基于Python实现，允许用户体验多版本ChatGPT的项目。通过这款工具，你无需支付ChatGPT 4.5的月费，即可根据实际使用流量付费，享受到ChatGPT 4.5带来的强大聊天体验。

## 特色功能

- **版本灵活切换**：用户可便捷地在不同版本的ChatGPT间切换，目前支持至ChatGPT 4.5版本。
- **流量计费**：告别传统的月租费用，根据使用的流量计费，经济而高效。
- **简便快捷**：程序源自OpenAI官方示例，保证了使用的简易性和功能的可靠性。

## 准备工作

在使用这个聊天工具之前，请确保你已完成以下步骤：

- **OpenAI账号**：你需要拥有一个OpenAI账号。如果还没有，可以前往[OpenAI官网](https://openai.com/)注册。
- **API密钥配置**：将你的OpenAI API密钥保存到计算机的系统环境变量中。假设你的密钥名为hyt123，可以通过以下方式进行配置：

  ```bash
  # 在你的系统环境变量中添加OPENAI_API_KEY
  key = os.environ['hyt123']
  os.environ['OPENAI_API_KEY'] = key
  ```

## 安装指南

1. **安装Python**：确保你的系统已安装Python 3.8或更高版本。如果尚未安装，可以从[Python官网](https://www.python.org/)下载并安装。

2. **运行程序**：下载此工程后，通过命令行运行以下指令启动聊天程序：

   ```bash
   python chat.py
   ```

祝你使用愉快！随时体验ChatGPT的魔力，探索无限可能。

openai:
# ChatGPT-Python

Welcome to use the open-source ChatGPT chat tool, implemented in Python, which allows users to experience multiple versions of the ChatGPT project. With this tool, you can enjoy the powerful chat experience brought by ChatGPT 4.5 without paying the monthly fee, instead paying based on actual usage traffic.

## Key Features

- **Flexible Version Switching**: Users can easily switch between different versions of ChatGPT, currently supporting up to ChatGPT 4.5.
- **Traffic-based Billing**: Say goodbye to traditional monthly fees and pay based on the traffic you use, economical and efficient.
- **Simple and Convenient**: Derived from the official OpenAI example, ensuring ease of use and reliability of functionality.

## Prerequisites

Before using this chat tool, make sure you have completed the following steps:

- **OpenAI Account**: You need to have an OpenAI account. If you don't have one yet, you can register at [OpenAI official website](https://openai.com/).
- **API Key Configuration**: Save your OpenAI API key to the system environment variables on your computer. Assuming your key is hyt123, you can configure it as follows:

  ```bash
  # Add OPENAI_API_KEY to your system environment variables
  key = os.environ['hyt123']
  os.environ['OPENAI_API_KEY'] = key
  ```

## Installation Guide

1. **Install Python**: Make sure your system has Python 3.8 or higher installed. If not, you can download and install it from the [Python official website](https://www.python.org/).

2. **Run the Program**: After downloading this project, run the following command in the command line to start the chat program:

   ```bash
   python chat.py
   ```

Enjoy using it! Feel the magic of ChatGPT at any time and explore endless possibilities.

