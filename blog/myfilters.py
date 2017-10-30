from django import template

register = template.Library()


def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})


register.filter('addclass', addclass)
