import reflex as rx
from .. import navegation
#from .nav import navegation
from ..navegation import routes


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.link(
                        rx.image(
                            src="/favicon.ico",
                            width="2.25em",
                            height="auto",
                            border_radius="25%",
                    ),
                    href='/'
                    ),
                    rx.link(
                    rx.heading(
                        "Reflex", size="7", weight="bold"
                    ),
                    href='/'
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", navegation.routes.HOME_ROUTE),
                    navbar_link("About",navegation.routes.ABOUT_ROUTE), #addig the routes created it
                    navbar_link("Pricing", navegation.routes.PRICING_ROUTE),
                    navbar_link("Contact", navegation.routes.CONTACT_ROUTE),
                    spacing="5",
                ),
                rx.hstack(
                    rx.button(
                        "Sign Up",
                        size="3",
                        variant="outline",
                    ),
                    rx.button("Log In", size="3"),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.link(
                        rx.image(
                            src="/favicon.ico",
                            width="2em",
                            height="auto",
                            border_radius="25%",
                    ),
                    href='/'
                    ),
                    rx.link(
                        rx.heading(
                            "Reflex", size="6", weight="bold"
                    ),
                    href='/'
                    ),
                    align_items="center",
                    
                    
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home",
                                     on_click=navegation.navState.to_home),
                        rx.menu.item("About",
                                     on_click=navegation.navState.to_about_us),
                        rx.menu.item("Pricing",
                                     on_click=navegation.navState.to_pricing),
                        rx.menu.item("Contact",
                                    on_click=navegation.navState.to_contact),
                        rx.menu.separator(),
                        rx.menu.item("Log in"),
                        rx.menu.item("Sign up"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
       # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
        id='principal-nav',
    )