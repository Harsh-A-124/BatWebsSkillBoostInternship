from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def comment_upvoted(context,userid,comment):
    comment_dict = context["comment_dict"]
    if comment.upvotes.filter(id=userid).exists():
        comment_dict[comment]['upvoted'] = True
        context["comment_dict"] = comment_dict
        return True
    else:
        comment_dict[comment]['upvoted'] = False
        context["comment_dict"] = comment_dict
        return False
@register.simple_tag(takes_context=True)
def comment_downvoted(context,userid,comment):
    comment_dict = context["comment_dict"]
    if comment.downvotes.filter(id=userid).exists():
        comment_dict[comment]['downvoted'] = True
        context["comment_dict"] = comment_dict
        return True
    else:
        comment_dict[comment]['downvoted'] = False
        context["comment_dict"] = comment_dict
        return False
    
@register.simple_tag(takes_context=True)
def comment_upvotes(context,comment):
    comment_dict = context["comment_dict"]
    curr_upvotes = comment_dict[comment]['upvotes']
    return curr_upvotes
    
@register.simple_tag(takes_context=True)
def comment_downvotes(context,comment):
    comment_dict = context["comment_dict"]
    curr_downvotes = comment_dict[comment]['downvotes']
    return curr_downvotes