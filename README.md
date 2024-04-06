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

