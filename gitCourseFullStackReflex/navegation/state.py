import reflex as rx
#import navegation
from .. import navegation
#import routes
#create a class to add routes for methods that doesnt allow links, like menus
class navState(rx.State):
    def to_home(self):
        return rx.redirect(navegation.routes.HOME_ROUTE)
    def to_about_us(self):
        return rx.redirect(navegation.routes.ABOUT_ROUTE)
    def to_pricing(self):
        return rx.redirect(navegation.routes.PRICING_ROUTE)
    def to_contact(self):
        return rx.redirect(navegation.routes.CONTACT_ROUTE)