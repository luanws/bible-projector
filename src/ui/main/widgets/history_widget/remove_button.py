from src.widgets.icon_button_widget import IconButton


class RemoveButton(IconButton):
    def __init__(self, parent=None):
        super().__init__(
            parent=parent,
            icon_name='fa5s.times',
            active_color='#EC0059',
            color='#AAA',
        )
