from flet import Checkbox, TextField, icons, Column, Row, UserControl, IconButton, colors


class TaskControl(UserControl):
    def __init__(self, task_name):
        super().__init__()
        self.task_name = task_name
        self.display_task = Checkbox(value=False, label=self.task_name)
        self.edit_name = TextField(expand=1)
        self.edit_button = IconButton(
            icon=icons.CREATE_OUTLINED,
            tooltip='Edit To-Do',
            on_click=self.edit_clicked
        )
        self.delete_button = IconButton(
            icon=icons.DELETE_OUTLINE,
            tooltip='Delete To-Do',
            on_click=self.delete_clicked
        )
        self.display_button = Row(
            spacing=0,
            controls=[
                self.edit_button,
                self.delete_button
            ]
        )
        self.display_view = Row(
            alignment='spaceBetween',
            vertical_alignment='center',
            controls=[
                self.display_task,
                self.display_button
            ]
        )
        self.update_button = IconButton(
            icon=icons.DONE_OUTLINE_OUTLINED,
            icon_color=colors.GREEN,
            tooltip='Update To-Do',
            on_click=self.save_clicked
        )
        self.edit_view = Row(
            visible=False,
            alignment='spaceBetween',
            vertical_alignment='center',
            controls=[
                self.edit_name,
                self.update_button
            ]
        )

    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def build(self):
        view = Column(
            controls=[
                self.display_view,
                self.edit_view
            ]
        )

        return view
