import reflex as rx
from ..ui.base import base_page

def pricing_page() -> rx.Component:
    my_child = rx.vstack(        
            rx.heading('Procing page',size='9'),
            rx.text(
                "Here we go again!",  
            ),        
        spacing="5",
            justify="center",
            min_height="85vh",
            text_align='center',
            align='center',
    )
    return base_page(my_child)