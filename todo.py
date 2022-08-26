import flet
from flet import Checkbox, FloatingActionButton, Page, TextField, icons, Column, Row


def main(page: Page):
    def add_click(e):
        cb = Checkbox(label=new_task.value)
        tasks_view.controls.append(cb)
        new_task.value = ''
        page.update()

    page.horizontal_alignment = 'center'
    new_task = TextField(hint_text='Whats needs to be done?', expand=True)
    tasks_view = Column()
    head_view = Row(
        controls=[
            new_task,
            FloatingActionButton(icon=icons.ADD, on_click=add_click)
        ]
    )

    view = Column(
        width=600,
        controls=[
            head_view,
            tasks_view
        ]
    )


    page.add(view)


flet.app(target=main)
