import reflex as rx
from ..ui.base import base_page

def abou_us() -> rx.Component:
    my_child = rx.vstack(        
            rx.heading('About us',size='9'),
            rx.text(
                "Here we go!",  
            ),        
        spacing="5",
            justify="center",
            min_height="85vh",
            text_align='center',
            align='center',
    )
    return base_page(my_child)