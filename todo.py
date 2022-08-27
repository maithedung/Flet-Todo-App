from flet import Checkbox, FloatingActionButton, TextField, icons, Column, Row, UserControl


class TodoAppControl(UserControl):
    def __init__(self):
        super().__init__()
        self.new_task = TextField(hint_text='Whats needs to be done?', expand=True)
        self.head_view = Row(
            controls=[
                self.new_task,
                FloatingActionButton(icon=icons.ADD, on_click=self.add_click)
            ]
        )
        self.tasks_view = Column()

    def add_click(self, e):
        cb = Checkbox(label=self.new_task.value)
        self.tasks_view.controls.append(cb)
        self.new_task.value = ''
        self.update()

    def build(self):
        view = Column(
            width=600,
            controls=[
                self.head_view,
                self.tasks_view
            ]
        )
        return view
