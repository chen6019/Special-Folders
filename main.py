import tkinter as tk
import subprocess
from tkinter import messagebox
import os
import sys

def on_closing():
    save_state(appdata_path)
    root.destroy()
    sys.exit()
def open_folder(folder_name):
    try:
        result = subprocess.run(f'explorer shell:{folder_name}', shell=True)
        if result.returncode == 1:
            message_label.config(text=f'  成功打开 {folder_name}  ')
            if auto_quit.get() == 1:
                on_closing()
    except Exception as e:
        messagebox.showinfo("错误", f'错误代码: {result.returncode}')


def save_state(appdata_path):
    os.makedirs(appdata_path, exist_ok=True)
    state_file_path = os.path.join(appdata_path, 'state.txt')
    with open(state_file_path, 'w') as f:
        f.write(str(auto_quit.get()))

def load_state(appdata_path):
    state_file_path = os.path.join(appdata_path, 'state.txt')
    if os.path.exists(state_file_path):
        with open(state_file_path, 'r') as f:
            state = f.read()
            auto_quit.set(int(state))

appdata_path = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'SpecialFolders')

root = tk.Tk()
root.title("特殊文件夹")
root.protocol("WM_DELETE_WINDOW", on_closing)

message_label = tk.Label(root, text=" 请选择需要打开的特殊文件夹")
message_label.grid(row=0, column=0)

# 创建一个复选框控件作为自动退出的选项
auto_quit = tk.IntVar()
auto_quit_check = tk.Checkbutton(root, text="自动退出", variable=auto_quit)
auto_quit_check.grid(row=0, column=1, padx=5, pady=10)
load_state(appdata_path)
button = tk.Button(root, text="当前应用数据", command=lambda: os.startfile(appdata_path))
button.grid(row=0, column=2, padx=5, pady=10)

button = tk.Button(root, text="所有应用程序", command=lambda: open_folder("appsfolder"))
button.grid(row=1, column=0, padx=5, pady=10)
button = tk.Button(root, text="网络连接", command=lambda: open_folder("ConnectionsFolder"))
button.grid(row=1, column=1, padx=5, pady=10)
button = tk.Button(root, text="收藏夹", command=lambda: open_folder("favorites"))
button.grid(row=1, column=2, padx=5, pady=10)

button = tk.Button(root, text="Windows字体", command=lambda: open_folder("fonts"))
button.grid(row=2, column=0, padx=5, pady=10)
button = tk.Button(root, text="开始菜单", command=lambda: open_folder("start menu"))
button.grid(row=2, column=1, padx=5, pady=10)
button = tk.Button(root, text="发送到", command=lambda: open_folder("sendto"))
button.grid(row=2, column=2, padx=5, pady=10)

button = tk.Button(root, text="当前用户启动", command=lambda: open_folder("startup"))
button.grid(row=3, column=0, padx=5, pady=10)
button = tk.Button(root, text="全局启动", command=lambda: open_folder("common startup"))
button.grid(row=3, column=1, padx=5, pady=10)
button = tk.Button(root, text="IE历史", command=lambda: open_folder("History"))
button.grid(row=3, column=2, padx=5, pady=10)

button = tk.Button(root, text="最近使用文件", command=lambda: open_folder("recent"))
button.grid(row=4, column=0, padx=5, pady=10)
button = tk.Button(root, text="快捷方式", command=lambda: open_folder("Application Shortcuts"))
button.grid(row=4, column=1, padx=5, pady=10)
button = tk.Button(root, text="低权限本地应用数据", command=lambda: open_folder("LocalAppDataLow"))
button.grid(row=4, column=2, padx=5, pady=10)

button = tk.Button(root, text="应用程序数据", command=lambda: open_folder("AppData"))
button.grid(row=5, column=0, padx=5, pady=10)
button = tk.Button(root, text="本地应用数据", command=lambda: open_folder("Local AppData"))
button.grid(row=5, column=1, padx=5, pady=10)
# button = tk.Button(root, text="测试", command=lambda: open_folder("Local AppData"))
# button.grid(row=8, column=2, padx=5, pady=10)
message_label = tk.Label(root, text="打开失败可能会打开文档文件夹")
message_label.grid(row=8, column=0, columnspan=3)

message = tk.Label(root, text="")
message.grid(row=9, column=0, columnspan=3)

root.mainloop()