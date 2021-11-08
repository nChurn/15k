import tkinter as tk

root = tk.Tk()

root.geometry("400x150")


name_var = tk.StringVar()
passw_var = tk.StringVar()
google_sheet = tk.StringVar()
name_of_sheet = tk.StringVar()

def submit():
    name = name_var.get()
    password = passw_var.get()
    email = google_sheet.get()
    name_of_sheet_ = name_of_sheet.get()
    from main import get_data
    d = {"URL":name,"TOKEN":password,"Google":email,'Name_of_sheet':name_of_sheet_}
    get_data(d)
    name_var.set("")


name_label = tk.Label(root, text='URL', font=('calibre', 10, 'bold'))


name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'))

passw_label = tk.Label(root, text='TOKEN', font=('calibre', 10, 'bold'))

passw_entry = tk.Entry(root, textvariable=passw_var, font=('calibre', 10, 'normal'), show='*')

google_label = tk.Label(root, text='Google Sheet Token', font=('calibre', 10, 'bold'))


google_entry = tk.Entry(root, textvariable=google_sheet, font=('calibre', 10, 'normal'))


google_name_sheet_label = tk.Label(root, text='Name of Sheet', font=('calibre', 10, 'bold'))


google_name_sheet_entry = tk.Entry(root, textvariable=name_of_sheet, font=('calibre', 10, 'normal'))

sub_btn = tk.Button(root, text='Submit', command=submit)


name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
passw_label.grid(row=1, column=0)
passw_entry.grid(row=1, column=1)
google_label.grid(row=2,column=0)
google_entry.grid(row=2,column=1)

google_name_sheet_label.grid(row=3,column=0)
google_name_sheet_entry.grid(row=3,column=1)

sub_btn.grid(row=4, column=1)


root.mainloop()