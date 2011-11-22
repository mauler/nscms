#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.template import Library, Node, TemplateSyntaxError

register = Library()

class RangeNode(Node):
    def __init__(self, parser, range_args, context_name):
        self.template_parser = parser
        self.range_args = range_args
        self.context_name = context_name

    def render(self, context):

        resolved_ranges = []
        for arg in self.range_args:
            compiled_arg = self.template_parser.compile_filter(arg)
            resolved_ranges.append(compiled_arg.resolve(context, ignore_failures=True))
        context[self.context_name] = range(*resolved_ranges)
        return ""

@register.tag
def mkrange(parser, token):
    """
    Accepts the same arguments as the 'range' builtin and creates
    a list containing the result of 'range'.

    Syntax:
        {% mkrange [start,] stop[, step] as context_name %}

    For example:
        {% mkrange 5 10 2 as some_range %}
        {% for i in some_range %}
          {{ i }}: Something I want to repeat\n
        {% endfor %}

    Produces:
        5: Something I want to repeat
        7: Something I want to repeat
        9: Something I want to repeat
    """

    tokens = token.split_contents()
    fnctl = tokens.pop(0)

    def error():
        raise TemplateSyntaxError, "%s accepts the syntax: {%% %s [start,] " +\
                "stop[, step] as context_name %%}, where 'start', 'stop' " +\
                "and 'step' must all be integers." %(fnctl, fnctl)

    range_args = []
    while True:
        if len(tokens) < 2:
            error()

        token = tokens.pop(0)

        if token == "as":
            break

        range_args.append(token)

    if len(tokens) != 1:
        error()

    context_name = tokens.pop()

    return RangeNode(parser, range_args, context_name)

from django.template import Library, Node

class SplitListNode(Node):
    def __init__(self, list_string, chunk_size, new_list_name):
        self.list = list_string
        self.chunk_size = chunk_size
        self.new_list_name = new_list_name

    def split_seq(self, seq, size):
        """ Split up seq in pieces of size, from
        http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/425044"""
        return [seq[i:i+size] for i in range(0, len(seq), size)]

    def render(self, context):
        context[self.new_list_name] = self.split_seq(context[self.list], int(self.chunk_size))
        return ''

def split_list(parser, token):
    """<% split_list list as new_list 5 %>"""
    bits = token.contents.split()
    if len(bits) != 5:
        raise TemplateSyntaxError, "split_list list as new_list 5"
    return SplitListNode(bits[1], bits[4], bits[3])

split_list = register.tag(split_list)

def startswith(value, arg):
    if value is not None:
        return value.startswith(arg)
    else:
        return False
startswith.is_safe = False
register.filter(startswith)

def endswith(value, arg):
    if value is not None:
        return value.endswith(arg)
    else:
        return False
endswith.is_safe = False
register.filter(endswith)

@register.filter
def get(d, key, default=''):
    """
    Usage:

    view:

    some_dict = {'keyA':'valueA','keyB':{'subKeyA':'subValueA','subKeyB':'subKeyB'},'keyC':'valueC'}
    keys = ['keyA','keyC']
    template:
    {{ some_dict|get:"keyA" }}
@register.filter(name='lookup')
def lookup(dict, index):
    if index in dict:
        return dict[index]
    return ''
    {{ some_dict|get:"keyB"|get:"subKeyA" }}
    {% for key in keys %}{{ some_dict|get:key }}{% endfor %}
    """
    try:
        return d.get(key,default)
    except:
        return default

@register.filter
def str_in(target, part):
    return target.find(part) >= 0

@register.filter
def str_split(target, separator=None):
    return target.split(separator)

@register.filter(name='dict_lookup')
def dict_lookup(dict, index):
    if index in dict:
        return dict[index]
    return ''

