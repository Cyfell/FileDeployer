import logging
import tkinter
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

        self.view.menu.menu_options.add_command(
            label="Quitter", command=exit)

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
        pass

    def on_click_del_serv(self):
        log_controller.debug("Clic on DEL SERV detected")
        pass

    def on_click_preview_delete(self):
        log_controller.debug("Clic on PREV DEL detected")
        pass

    def on_click_delete_files(self):
        log_controller.debug("Clic on DEL FILES detected")
        pass

    def on_click_preview_deploy(self):
        log_controller.debug("Clic on PREV DEPLOY detected")
        pass

    def on_click_deploy_files(self):
        log_controller.debug("Clic on DEPLOY FILES detected")
        pass

    def on_click_search_file(self):
        log_controller.debug("Clic on SEARCH FILES detected")
        pass
