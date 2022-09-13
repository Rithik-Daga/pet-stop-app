from django import template

register = template.Library()


@register.filter(name="is_liked")
def is_liked(post, user):
    temp = post.liked_by.filter(profile=user)

    if len(temp) == 0:
        return False

    return True
