import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog, scrolledtext
import openai
from openai import OpenAI
import os
# 初始化OpenAI API
key = os.environ['hyt123']
os.environ['OPENAI_API_KEY'] = key
client = OpenAI()

# 创建主窗口
root = tk.Tk()
root.title("OpenAI Chat Modal")


# 创建模态框
def show_modal():
    var = tk.StringVar(root)
    # 发送消息到OpenAI并显示回复
    def clear_screen():
        chat_box.delete('1.0', 'end')
    def send_message():
        user_message = message_entry.get()
        sys_des = seed_entry.get();
        if not sys_des:
            sys_des = "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."
        if user_message:
            chat_box.insert(tk.END, f"Me: {user_message}\n")
            response = client.chat.completions.create(
                model=var.get(),
                messages=[{"role": "system", "content": sys_des},
                          {"role": "user", "content": user_message}
                        ]
            )
            chat_box.insert(tk.END, f"AI: {response.choices[0].message.content}\n\n")
            message_entry.delete(0, tk.END)

    root.title("OpenAI Chat")
    # 模态框大小
    root.geometry("800x500")
    # 创建输入框
    row = 5
    tk.Label(root, text="OpenAI模式").place(x=10, y=row, width=200, height=30)
    model_entry = ttk.Combobox(root, textvariable=var)
    model_entry['values'] = ('gpt-3.5-turbo', 'gpt-4-turbo-preview')
    model_entry.place(x=250, y=row, width=400, height=30)
    model_entry.current(0)
    row += 35

    tk.Label(root, text="系统角色描述（必须用英语）").place(x=10, y=row, width=250, height=30)
    seed_entry = tk.Entry(root)
    seed_entry.place(x=250, y=row, width=1000, height=30)
    seed_entry.insert(0,"You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.")
    row += 35
    # 输入框
    send_button = tk.Button(root, text="发送", command=send_message)
    send_button.place(x=70, y=row, width=100, height=30)
    message_entry = tk.Entry(root)
    message_entry.place(x=250, y=row, width=400, height=30)
    row += 35
    # 创建对话显示区域
    logHeight=500
    chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=700, height=logHeight)
    chat_box.place(x=50, y=row, width=700, height=logHeight)
    row += logHeight + 10
    #  清除按钮
    tk.Button(root, text="清屏", command=clear_screen).place(x=50, y=row, width=100, height=30)

# 运行主循环
show_modal()
root.mainloop()