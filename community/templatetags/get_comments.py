from django import template

register = template.Library()


@register.filter(name="get_comments")
def get_comments(post, user):
    comments = user.comments_set.filter(post=post)
    return comments
