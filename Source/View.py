import tkinter as tk
from tkinter import ttk
from Constant import VERSION_APP


class View(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.parent.title("File Deployer KEOLIS V{}".format(VERSION_APP))

        # MENU
        self.menu = tk.Menu(self.parent)
        self.parent.config(menu=self.menu)

        self.menu.menu_options = tk.Menu(self.menu)
        self.menu.add_cascade(label="Options", menu=self.menu.menu_options)

        # FRAME SERVER CONFIGURATION
        self.label_frame_config = tk.LabelFrame(
            self.parent, text="Configuration serveur")
        self.label_frame_config.grid(row=0, column=0, sticky='w', pady=5)

        self.label_frame_config.list_serv = tk.Listbox(
            self.label_frame_config, height=5, selectbackground="blue", width=67, selectmode='multiple', activestyle='dotbox')
        self.label_frame_config.list_serv.grid(row=0, column=0, sticky='w')

        self.label_frame_config.scrollb = ttk.Scrollbar(
            self.label_frame_config)
        self.label_frame_config.scrollb.grid(
            row=0, column=1, sticky='nsew')

        self.label_frame_config.frame_action = tk.Frame(
            self.label_frame_config)
        self.label_frame_config.frame_action.grid(
            row=1, column=0, sticky='w')

        self.label_frame_config.frame_action.button_add = tk.Button(
            self.label_frame_config.frame_action, text="Ajouter nouveau serveur", bg='green', width=25)
        self.label_frame_config.frame_action.button_add.grid(
            row=0, column=0)

        self.label_frame_config.frame_action.button_delete = tk.Button(
            self.label_frame_config.frame_action, text="Supprimer serveur sélectionné", bg='red', width=25)
        self.label_frame_config.frame_action.button_delete.grid(
            row=0, column=1)

        self.tab = ttk.Notebook(self.parent, width=420)
        self.tab.grid(row=1, column=0, sticky='w', pady=10)

        # FRAME DELETE
        self.tab.frame_delete = tk.Frame(
            self.parent)

        self.tab.frame_delete.label_desc = tk.Label(
            self.tab.frame_delete, text="Entrer le nom du fichier à supprimer des serveurs :")
        self.tab.frame_delete.label_desc.grid(row=0, column=0, sticky='w')

        self.tab.frame_delete.entry_delete = tk.Entry(
            self.tab.frame_delete, width=50)
        self.tab.frame_delete.entry_delete.grid(row=1, column=0, sticky='w')

        self.tab.frame_delete.button_preview = tk.Button(
            self.tab.frame_delete, text="Prévisualiser les opérations", bg='orange', width=40, font='Arial 10 bold')
        self.tab.frame_delete.button_preview.grid(
            row=2, column=0, sticky='ew', pady=5)

        self.tab.frame_delete.button_delete = tk.Button(
            self.tab.frame_delete, text="Supprimer", bg='red', width=40, font='Arial 12 bold')
        self.tab.frame_delete.button_delete.grid(
            row=3, column=0, sticky='ew', pady=5)

        # FRAME DEPLOY
        self.tab.frame_deploy = tk.Frame(
            self.parent)

        self.tab.frame_deploy.label_desc = tk.Label(
            self.tab.frame_deploy, text="Rechercher le fichier à déployer :")
        self.tab.frame_deploy.label_desc.grid(row=0, column=0, sticky='w')

        self.tab.frame_deploy.button_search = tk.Button(
            self.tab.frame_deploy, text="Rechercher", bg='lightblue')
        self.tab.frame_deploy.button_search.grid(row=1, column=0, sticky='w')

        self.tab.frame_deploy.label_selected_file = tk.Label(
            self.tab.frame_deploy, text="Aucun fichier selectionné")
        self.tab.frame_deploy.label_selected_file.grid(
            row=1, column=1, sticky='w')

        self.tab.frame_deploy.button_preview = tk.Button(
            self.tab.frame_deploy, text="Prévisualiser les opérations", bg='orange', width=40, font='Arial 10 bold')
        self.tab.frame_deploy.button_preview.grid(
            row=2, column=0, sticky='ew', columnspan=2, pady=5)

        self.tab.frame_deploy.button_deploy = tk.Button(
            self.tab.frame_deploy, text="Déployer", bg='green', width=40, font='Arial 12 bold')
        self.tab.frame_deploy.button_deploy.grid(
            row=3, column=0, sticky='ew', columnspan=2, pady=5)

        self.tab.add(self.tab.frame_delete, text="Supprimer")
        self.tab.add(self.tab.frame_deploy, text="Déployer")

        # LOG WINDOW
        self.frame_log_window = tk.LabelFrame(
            self.parent, text="Log window:")
        self.frame_log_window.grid(
            row=2, column=0, sticky='w')
        self.frame_log_window.text_log = tk.Text(
            self.frame_log_window, bg='white', width=50)
        self.frame_log_window.text_log.grid(
            row=0, column=0)
        self.frame_log_window.scrollb = ttk.Scrollbar(
            self.frame_log_window)
        self.frame_log_window.scrollb.grid(
            row=0, column=1, sticky='nsew')
