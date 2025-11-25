from django import template

register = template.Library()


@register.filter
def user_voted(subject, user):
    if not user.is_authenticated:
        return False
    return subject.user_voted(user)
