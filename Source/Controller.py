from Model import Model
from View import View


class Controller:
    def __init__(self, root):
        self.model = Model()
        self.view = View(root)

        # # Binding
        # self.view.value_label.config(textvariable=self.model.val)

        # # Callback
        # self.view.add_one_btn.config(command=self.model.add_one)
        # self.view.reset_btn.config(command=self.model.reset)
