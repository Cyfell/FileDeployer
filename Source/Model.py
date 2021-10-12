import tkinter as tk


class Model:
    def __init__(self):
        self.val = tk.IntVar(0)
        self.server_list = []
        self.server_list_var = tk.StringVar(value=self.server_list)
        self.deploy_filename = tk.StringVar()

    def add_serv(self, serv):
        self.server_list.append(serv)
        self.server_list_var.set(self.server_list)

    def remove_serv(self, index):
        self.server_list.pop(index)
        self.server_list_var.set(self.server_list)

    def update_deploy_filename(self, filename):
        self.deploy_filename.set(filename)
