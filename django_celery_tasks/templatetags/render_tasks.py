# coding: utf-8
# Be prepared for Python2/3
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

from django import template


register = template.Library()


@register.inclusion_tag('django_celery_tasks/tasks_table.html', takes_context=True)
def render_tasks(context, **kwargs):
    tasks = kwargs.get('tasks', context.get('tasks'))
    tasks_details_url = kwargs.get('tasks_details_url')
    result = {}
    if tasks:
        result['tasks'] = tasks
    if tasks_details_url:
        result['tasks_details_url'] = tasks_details_url
    return result
