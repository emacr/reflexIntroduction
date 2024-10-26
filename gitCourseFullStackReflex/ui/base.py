import reflex as rx
from .nav import navbar


def base_page(child: rx.Component, *args, **kwargs) -> rx.Component:
        return rx.fragment( #renders nothing, if i make css changes here it doesnt work
            navbar(), #with the fragment the navbar is ajust it to the page
            rx.box(
            child,
            rx.color_mode.button(position="top-left", id='light-mode-btn',margin_top='40px'),
            rx.logo(), 
            id='my_base_container'  # i colocate ids justo to be easier to find it when i inspect the page looking for the component
            )
        )