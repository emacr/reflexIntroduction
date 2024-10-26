import reflex as rx
from .ui.base import base_page
from rxconfig import config
#from .pages.about import abou_us
from . import navegation,pages


class State(rx.State):

    label = 'welcome to reflex'

    def handle_title_input_change(self,value):
        self.label=value

    #end of state class

def index() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.vstack(
       # rx.color_mode.button(position="top-right"),
        rx.vstack(
           # rx.heading(State.label, "Welcome to Reflex!", size="9"), # i add the lable that i declare in the state
            rx.heading(State.label,size='9'),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            # rx.link('go to about', href='/about'),
            # rx.link(
            # rx.button('click here for pricing'), 
            # href='/pricing'
            rx.link('go to about', href=navegation.routes.ABOUT_ROUTE),
            rx.link(
            rx.button('click here for pricing'), 
            href=navegation.routes.PRICING_ROUTE
            ),
            #add the value to the input and the event to change it with the label
            rx.input(
                default_value=State.label,
                on_change= State.handle_title_input_change
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            
        ), #with my child return now i can make changes to i couldn if i write them if rx.fragment
        spacing="5",
            justify="center",
            min_height="85vh",
            text_align='center',
            align='center',
    )
    return base_page(my_child)



app = rx.App()
app.add_page(index)
#app.add_page(pages.abou_us, route='/about') # i use it this way cause i imported= from . import pages
#app.add_page(pages.pricing_page, route='/pricing')
app.add_page(pages.pricing_page, route=navegation.routes.PRICING_ROUTE)
app.add_page(pages.abou_us, route=navegation.routes.ABOUT_ROUTE)
app.add_page(pages.contact_page, route= navegation.routes.CONTACT_ROUTE)
