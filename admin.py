import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter
import sys
import tkinter.messagebox


def showframe(fra):
       for each in frame:
              if each != fra:
                    each.grid_remove()
       fra.grid(row = 1, column = 1, rowspan = 2, columnspan = 2)
def submit_info():
    tkinter.messagebox.showinfo(title='提交', message='提交成功！')

frame = []

if __name__=="__main__":
       root = tk.Tk()
       root.title("e考勤")
       root.geometry('900x500')
       root.resizable(width = False, height = False)

      
       frame_func = tk.Frame(root)
       frame_func.grid(row = 1, column = 0, padx = 20)
       v_func = tk.IntVar()
       v_func.set(1)
       radiobutton_link = tk.Radiobutton(frame_func, text = '签到设置', variable = v_func, value = 1, indicatoron = False, padx = 50, command = lambda:showframe(frame_check_setting))
       radiobutton_link.pack(fill = tk.X, padx = 15, pady = 15)
       radiobutton_check_signin = tk.Radiobutton(frame_func, text = '查看签到情况', variable = v_func, value = 2, indicatoron = False, padx = 50, command = lambda:showframe(frame_check_signin))
       radiobutton_check_signin.pack(fill = tk.X, padx = 15, pady = 15)
       radiobutton_user_info = tk.Radiobutton(frame_func, text = '更改用户信息', variable = v_func, value = 3, indicatoron = False, padx = 50, command = lambda:showframe(frame_user_info))
       radiobutton_user_info.pack(fill = tk.X, padx = 15, pady = 15)
       radiobutton_message_list = tk.Radiobutton(frame_func, text = '消息列表', variable = v_func, value = 4, indicatoron = False, padx = 50, command = lambda:showframe(frame_message_list))
       radiobutton_message_list.pack(fill = tk.X, padx = 15, pady = 15)
       frame_port = tk.Frame(root)
       frame_port.grid(row = 0, column = 1, columnspan = 2, pady = 35)       


       frame_check_setting = tk.LabelFrame(root, width = 630, height = 400, borderwidth = 5, relief = tk.SUNKEN)
       frame_check_setting.grid(row = 1, column = 1, rowspan = 2, columnspan = 2)  #初始化界面
       frame.append(frame_check_setting)
       tk.Label(frame_check_setting, text='时间范围设置').place(x=150,y=60)
       tk.Label(frame_check_setting, text='早：').place(x=150,y=90)
       var_morning = tk.StringVar()
       entry_morning = tk.Entry(frame_check_setting, textvariable=var_morning)
       entry_morning.place(x=240,y=90)
       tk.Label(frame_check_setting, text='中：').place(x=150,y=120)
       var_noon = tk.StringVar()
       entry_noon = tk.Entry(frame_check_setting, textvariable=var_noon)
       entry_noon.place(x=240,y=120)
       tk.Label(frame_check_setting, text='晚：').place(x=150,y=150)
       var_evening = tk.StringVar()
       entry_evening = tk.Entry(frame_check_setting, textvariable=var_evening)
       entry_evening.place(x=240,y=150)
       tk.Label(frame_check_setting, text='地点范围设置').place(x=150,y=180)
       tk.Label(frame_check_setting, text='中心地点：').place(x=150,y=210)
       var_place = tk.StringVar()
       entry_place = tk.Entry(frame_check_setting, textvariable=var_place)
       entry_place.place(x=240,y=210)
       tk.Label(frame_check_setting, text='半径：').place(x=150,y=240)
       var_radius = tk.StringVar()
       entry_radius = tk.Entry(frame_check_setting, textvariable=var_radius)
       entry_radius.place(x=240,y=240)
       #提交按钮
       check_submit = tk.Button(frame_check_setting, text='submit', command=submit_info)
       check_submit.place(x=270,y=300)

       frame_check_signin = tk.LabelFrame(root, width = 420, height = 370, borderwidth = 5, relief = tk.SUNKEN)
       frame.append(frame_check_signin)
       w_process = tk.Canvas(frame_check_signin, width = 420, height = 370)
       w_process.grid(row = 0, column = 0, rowspan = 10, columnspan = 10)
       w_process.create_rectangle(0, 0, 620, 400)
       tree = ttk.Treeview(frame_check_signin,height = 18, show="headings")#表格,show属性隐藏第一列表格
       tree.grid(row = 0, column = 0, padx = 10, pady = 5)
       tree["columns"]=("姓名","工号","打卡情况")
       tree.column("姓名",width=120)   #表示列,不显示
       tree.column("工号",width=120)
       tree.column("打卡情况",width=150)
       tree.heading("姓名",text="姓名")  #显示表头
       tree.heading("工号",text="工号")
       tree.heading("打卡情况",text="打卡情况")
       scrolly= ttk.Scrollbar(frame_check_signin,orient=VERTICAL,command=tree.xview)
       scrolly.grid(row = 0, column = 1, sticky=N+S)
       tree.configure(yscrollcommand=scrolly.set)

       frame_user_info = tk.LabelFrame(root, width = 620, height = 370, borderwidth = 5, relief = tk.SUNKEN)
       frame.append(frame_user_info)
       w_process = tk.Canvas(frame_user_info, width = 620, height = 370)
       w_process.grid(row = 0, column = 0, rowspan = 10, columnspan = 10)
       w_process.create_rectangle(0, 0, 620, 400)
       tree = ttk.Treeview(frame_user_info,height = 18, show="headings")#表格,show属性隐藏第一列表格
       tree.grid(row = 0, column = 0, padx = 10, pady = 5)
       tree["columns"]=("姓名","工号","备注")
       tree.column("姓名",width=120)   #表示列,不显示
       tree.column("工号",width=120)
       tree.column("备注",width=340)
       tree.heading("姓名",text="姓名")  #显示表头
       tree.heading("工号",text="工号")
       tree.heading("备注",text="备注")
       scrolly= ttk.Scrollbar(frame_user_info,orient=VERTICAL,command=tree.xview)
       scrolly.grid(row = 0, column = 1, sticky=N+S)
       tree.configure(yscrollcommand=scrolly.set)
       
       frame_message_list = tk.LabelFrame(root, width = 620, height = 370, borderwidth = 5, relief = tk.SUNKEN)
       frame.append(frame_message_list)
       w_process = tk.Canvas(frame_message_list, width = 620, height = 370)
       w_process.grid(row = 0, column = 0, rowspan = 10, columnspan = 10)
       w_process.create_rectangle(0, 0, 620, 400)
       tree = ttk.Treeview(frame_message_list,height = 18, show="headings")#表格,show属性隐藏第一列表格
       tree.grid(row = 0, column = 0, padx = 10, pady = 5)
       tree["columns"]=("姓名","工号","类型","理由","决定")
       tree.column("姓名",width=100)   #表示列,不显示
       tree.column("工号",width=100)
       tree.column("类型",width=100)
       tree.column("理由",width=100)
       tree.column("决定",width=180)
       tree.heading("姓名",text="姓名")  #显示表头
       tree.heading("工号",text="工号")
       tree.heading("类型",text="类型")
       tree.heading("理由",text="理由")
       tree.heading("决定",text="决定")
       scrolly= ttk.Scrollbar(frame_message_list,orient=VERTICAL,command=tree.xview)
       scrolly.grid(row = 0, column = 1, sticky=N+S)
       tree.configure(yscrollcommand=scrolly.set)
       
       root.mainloop()

