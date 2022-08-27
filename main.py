import flet
from flet import Page
from todo import TodoAppControl


def main(page: Page):
    page.title = 'ToDo App'
    page.horizontal_alignment = 'center'
    page.update()

    # create application instance
    todo = TodoAppControl()

    # add application's root control to the page
    page.add(todo)


flet.app(target=main)
