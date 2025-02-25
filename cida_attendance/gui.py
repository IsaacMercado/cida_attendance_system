from tkinter import *
from tkinter import messagebox, ttk

from cida_attendance.config import load_config, save_config


def create_app():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()

    # User
    ttk.Label(frm, text="User:").grid(column=0, row=0)
    user = StringVar()
    user.set(load_config()["user"])
    user_entry = ttk.Entry(frm, textvariable=user)

    user_entry.grid(column=1, row=0)

    # Password
    ttk.Label(frm, text="Password:").grid(column=0, row=1)
    password = StringVar()
    # password.set(load_config()["password"])
    password_entry = ttk.Entry(frm, textvariable=password, show="*")
    password_entry.grid(column=1, row=1)

    # IP
    ttk.Label(frm, text="IP:").grid(column=0, row=2)
    ip = StringVar()
    ip.set(load_config()["ip"])
    ip_entry = ttk.Entry(frm, textvariable=ip)
    ip_entry.grid(column=1, row=2)

    # Port
    ttk.Label(frm, text="Port:").grid(column=0, row=3)
    port = StringVar()
    port.set(load_config()["port"])
    port_entry = ttk.Entry(frm, textvariable=port)
    port_entry.grid(column=1, row=3)

    # URI DB
    ttk.Label(frm, text="URI DB:").grid(column=0, row=4)
    uri_db = StringVar()
    uri_db.set(load_config()["uri_db"])
    uri_db_entry = ttk.Entry(frm, textvariable=uri_db)
    uri_db_entry.grid(column=1, row=4)

    # Name
    ttk.Label(frm, text="Name:").grid(column=0, row=5)
    name = StringVar()
    name.set(load_config()["name"])
    name_entry = ttk.Entry(frm, textvariable=name)
    name_entry.grid(column=1, row=5)

    def save():
        save_config(uri_db.get(), user.get(), password.get(), ip.get(), int(port.get()), name.get())
        messagebox.showinfo("Save", "Configuration saved")
        root.destroy()

    ttk.Button(frm, text="Save", command=save).grid(column=1, row=6)

    def quit():
        root.destroy()

    ttk.Button(frm, text="Quit", command=quit).grid(column=0, row=6)

    return root


def main():
    root = create_app()
    root.mainloop()


if __name__ == "__main__":
    main()
