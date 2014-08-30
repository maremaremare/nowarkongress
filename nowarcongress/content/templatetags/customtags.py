# -*- coding: utf-8 -*-
from django import template
from django.utils.safestring import mark_safe

register = template.Library()
@register.filter
def to_class_name(value):
    return value.__class__.__name__



Stateful = {}
def do_set(parser, token):
    _, key = token.split_contents()
    nodelist = parser.parse(('endset',))
    parser.delete_first_token()  # from the example -- why?
    return SetStatefulNode(key,nodelist)

class SetStatefulNode(template.Node):
    def __init__(self, key, nodes):
        Stateful[key] = nodes
    def render(self, context):
        return ''
register.tag('set', do_set)

def do_get(parser, token):
    tag_name, key = token.split_contents()
    return GetStatefulNode(key)

class GetStatefulNode(template.Node):
    def __init__(self, key):
       self.key = key
    def render(self, context):
        return ''.join( [x.render(context) for x in Stateful[self.key]] )

register.tag('get', do_get)


def no_dumb_chars(value):
    newval = value.replace('&laquo;', u'«').replace('&mdash;', u'—').replace('&hellip;', u'…').replace('&raquo;', u'»').replace('&nbsp;', ' ').replace('&ndash;', u'–').replace('  ', ' ')
    return newval
register.filter('no_dumb_chars', no_dumb_chars)


def moderated(value):
    newlist = []
    for x in value:
        if x.get_moderation_status() == 1:
            newlist.append(x)
    return newlist
register.filter('moderated', moderated)

import random


def shuffle(arg):
    tmp = [i for i in arg]
    random.shuffle(tmp)
    return tmp

register.filter('shuffle', shuffle)
