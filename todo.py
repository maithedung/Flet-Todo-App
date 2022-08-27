from flet import FloatingActionButton, TextField, icons, Column, Row, UserControl, Tabs, Tab, Text, OutlinedButton
from task import TaskControl


class TodoAppControl(UserControl):
    def __init__(self):
        super().__init__()
        self.new_task = TextField(
            hint_text='Whats needs to be done?',
            expand=True
        )
        self.add_button = FloatingActionButton(
            icon=icons.ADD,
            on_click=self.add_clicked
        )
        self.clear_completed_button = OutlinedButton(
            text='Clear completed',
            on_click=self.clear_clicked
        )
        self.items_left = Text('0 items left')
        self.tab_all = Tab(text='all')
        self.tab_active = Tab(text='active')
        self.tab_completed = Tab(text='completed')
        self.filter = Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[
                self.tab_all,
                self.tab_active,
                self.tab_completed
            ]
        )
        self.title = Text(
            value='Todos',
            style='headlineMedium'
        )

        self.title_view = Row(
            controls=[
                self.title
            ],
            alignment='center'
        )
        self.clear_completed = Row(
            alignment='spaceBetween',
            vertical_alignment='center',
            controls=[
                self.items_left,
                self.clear_completed_button
            ]
        )
        self.head_view = Row(
            controls=[
                self.new_task,
                self.add_button
            ]
        )
        self.tasks = Column()
        self.filter_view = Column(
            spacing=25,
            controls=[
                self.filter,
                self.tasks,
                self.clear_completed
            ]
        )

    def add_clicked(self, e):
        task = TaskControl(self.new_task.value, self.task_status_change, self.task_delete)
        self.tasks.controls.append(task)
        self.new_task.value = ''
        self.update()

    def clear_clicked(self, e):
        for task in self.tasks.controls[:]:
            if task.completed:
                self.task_delete(task)

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()

    def tabs_changed(self, e):
        self.update()

    def task_status_change(self, task):
        self.update()

    def update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        for task in self.tasks.controls:
            task.visible = (
                status == 'all'
                or (status == 'active' and task.completed is False)
                or (status == 'completed' and task.completed)
            )
        super().update()

    def build(self):
        view = Column(
            width=600,
            controls=[
                self.title_view,
                self.head_view,
                self.filter_view
            ]
        )
        return view
