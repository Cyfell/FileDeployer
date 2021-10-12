import logging
import os
import tkinter
import shutil
from tkinter import filedialog
from Model import Model
from Logger import log_controller, log_formatter
from View import View


class TextHandler(logging.Handler):
    def __init__(self, text):
        # run the regular Handler __init__
        logging.Handler.__init__(self)
        # Store a reference to the Text it will log to
        self.text = text

    def emit(self, record):
        msg = self.format(record)
        self.text.configure(state='normal')
        self.text.insert(tkinter.END, msg + '\n')
        self.text.configure(state='disabled')
        # Autoscroll to the bottom
        self.text.yview(tkinter.END)


class Controller:
    def __init__(self, root):
        self.view = View(root)
        self.model = Model()

        th = TextHandler(
            self.view.frame_log_window.text_log)
        th.setFormatter(log_formatter)
        log_controller.addHandler(th)

        # Binding
        self.view.label_frame_config.list_serv.config(
            listvariable=self.model.server_list_var)

        self.view.tab.frame_deploy.label_selected_file.config(
            textvariable=self.model.deploy_filename)

        self.view.menu.menu_options.add_command(
            label="Quitter", command=root.destroy)

        self.view.frame_log_window.scrollb.config(
            command=self.view.frame_log_window.text_log.yview)
        self.view.frame_log_window.text_log['yscrollcommand'] = self.view.frame_log_window.scrollb.set

        self.view.label_frame_config.scrollb.config(
            command=self.view.label_frame_config.list_serv.yview)
        self.view.label_frame_config.list_serv['yscrollcommand'] = self.view.label_frame_config.scrollb.set

        # Callback
        self.view.label_frame_config.frame_action.button_add.config(
            command=self.on_click_add_serv)
        self.view.label_frame_config.frame_action.button_delete.config(
            command=self.on_click_del_serv)
        self.view.tab.frame_delete.button_preview.config(
            command=self.on_click_preview_delete)
        self.view.tab.frame_delete.button_delete.config(
            command=self.on_click_delete_files)
        self.view.tab.frame_deploy.button_preview.config(
            command=self.on_click_preview_deploy)
        self.view.tab.frame_deploy.button_deploy.config(
            command=self.on_click_deploy_files)
        self.view.tab.frame_deploy.button_search.config(
            command=self.on_click_search_file)

    def on_click_add_serv(self):
        log_controller.debug("Clic on ADD SERV detected")
        dirselect = filedialog.askdirectory()
        if dirselect:
            log_controller.info(
                "New server directory selected by user: {}".format(dirselect))
            self.model.add_serv(dirselect)

    def on_click_del_serv(self):
        log_controller.debug("Clic on DEL SERV detected")
        # Getting selected servers
        index_selected_servs = self.view.label_frame_config.list_serv.curselection()

        # Check if no current selection
        if (not index_selected_servs):
            log_controller.info("No server selected, nothing happend")
        else:
            for iter in range(len(index_selected_servs)):
                index_selected = self.view.label_frame_config.list_serv.curselection()[
                    0]
                log_controller.info(
                    "Deleting server '{}' from the list".format(self.model.server_list[index_selected]))
                self.model.remove_serv(index_selected)

    def on_click_preview_delete(self):
        log_controller.debug("Clic on PREV DEL detected")
        # Get filename in entry and current server list
        self.delete_file(
            self.model.server_list, self.view.tab.frame_delete.entry_delete.get(), True)

    def on_click_delete_files(self):
        log_controller.debug("Clic on DEL FILES detected")
        # Get filename in entry and current server list
        self.delete_file(
            self.model.server_list, self.view.tab.frame_delete.entry_delete.get(), False)

    def check_user_input(self, directories, filename):
        result = True
        if (not filename):
            log_controller.warning(
                "No filename specified by user, nothing happens")
            result = False

        elif(len(directories) == 0):
            log_controller.warning(
                "No directories specified by user, nothing happens")
            result = False

        return result

    def delete_file(self, directories, filename, preview=True):
        if (self.check_user_input(directories, filename) == True):
            # check if file exist on servers
            for dir in directories:
                if os.path.isfile(os.path.join(dir, filename)):
                    log_controller.info("Deleting file '{}'".format(
                        os.path.join(dir, filename)))
                    if (not preview):
                        # delete it
                        os.remove(os.path.join(dir, filename))

    def on_click_preview_deploy(self):
        log_controller.debug("Clic on PREV DEPLOY detected")
        self.deploy_file(self.model.server_list,
                         self.model.deploy_filename.get(), False)

    def on_click_deploy_files(self):
        log_controller.debug("Clic on DEPLOY FILES detected")
        self.deploy_file(self.model.server_list,
                         self.model.deploy_filename.get(), True)

    def deploy_file(self, directories, filepath, preview=True):
        if (self.check_user_input(directories, filepath) == True):
            # check if file exist on servers
            for dir in directories:
                if os.path.isfile(filepath):
                    log_controller.info("copying file '{}' to directory '{}'".format(
                        filepath, dir))
                    if (not preview):
                        # delete it
                        shutil.copyfile(filepath, os.path.join(
                            dir, os.path.basename(filepath)))

    def on_click_search_file(self):
        log_controller.debug("Clic on SEARCH FILES detected")
        selected_filename = filedialog.askopenfilename()
        self.model.update_deploy_filename(selected_filename)
