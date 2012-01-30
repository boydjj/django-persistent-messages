from persistent_messages import notify
from persistent_messages import constants 

def add_message(request, level, message, extra_tags='', fail_silently=False, subject='', user=None, email=False, from_user=None, parent_msg=None, expires=None, close_timeout=None):
    """
    """
    if email:
        notify.email(level, message, extra_tags, subject, user, from_user)

    return request._messages.add(level, message, extra_tags, subject, user, from_user, parent_msg, expires, close_timeout)

def info(request, message, extra_tags='', fail_silently=False, subject='', user=None, email=False, from_user=None, parent_msg=None, expires=None, close_timeout=None):
    """
    """
    level = constants.INFO
    return add_message(request, level, message, extra_tags, fail_silently, subject, user, email, from_user, parent_msg, expires, close_timeout)

def warning(request, message, extra_tags='', fail_silently=False, subject='', user=None, email=False, from_user=None, parent_msg=None, expires=None, close_timeout=None):
    """
    """
    level = constants.WARNING
    return add_message(request, level, message, extra_tags, fail_silently, subject, user, email, from_user, parent_msg, expires, close_timeout)

def debug(request, message, extra_tags='', fail_silently=False, subject='', user=None, email=False, from_user=None, parent_msg=None, expires=None, close_timeout=None):
    """
    """
    level = constants.DEBUG
    return add_message(request, level, message, extra_tags, fail_silently, subject, user, email, from_user, parent_msg, expires, close_timeout)

def add_message_without_storage(to_user, from_user, level, message, extra_tags='', fail_silently=False, subject='', mail=False, expires=None, close_timeout=None):
    """
    Use this method to add message without having to pass a `request.storage`
    As we are not storing the message, there is no need to add `parent_msg`
    """
    from models import Message
    message = Message(user=to_user, level=level, message=message, extra_tags=extra_tags, subject=subject, from_user=from_user, expires=expires, close_timeout=close_timeout)
    return message.save()
