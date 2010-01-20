'''
Created on 06 Nov 2009

@author: euan
'''
import types
import datetime

from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponse
from django.template import loader, RequestContext

import settings

#------------------------------------------------------------------------------
def formatDate(unformated_date):
    """
    Standardise the formating of dates so they all look the same
    """
    formated_date = datetime.datetime.strftime(unformated_date, '%d %b %Y')
        
    if formated_date[0] == '0':
        formated_date = formated_date[1:]
    
    return formated_date
    
#------------------------------------------------------------------------------
def compareById(x, y):
    """
    Simple comparator.
    Sorts by id
    """
    if x.id>y.id:
        return 1
    elif x.id==y.id:
        return 0
    else: # x<y
        return -1
                            
#------------------------------------------------------------------------------
def capitalizeEachWord(sentance):
    """
    Camel-case with spaces
    """
    words = sentance.split(' ')
    capital_words = []
    for word in words:
        capital_words.append(word.capitalize())
            
    new_sentance = ' '.join(capital_words)
    return new_sentance

#------------------------------------------------------------------------------
def ensure_unicode(the_string):
    """
    Just checking...
    """
    if not type(the_string) == types.UnicodeType:
        the_string = unicode(str(the_string))
    
    return the_string

#------------------------------------------------------------------------------
def paginate(request, list, page_name,):
    """
    Those numbers at the bottom of a list
    """
    
    if not list:
        return None, None
    
    # Remember the amount of rows to display
    try:
        rows =  int(request.POST.get('page_limit', request.session['page_limit']))
    except:
        rows = settings.PAGE_LIMIT
    
    request.session['page_limit'] = rows
    
    # Crunch!
    paginator = Paginator(list, rows)
    
    # Get the last page number viewed (for that page) and return to that same page.
    try:
        page = int(request.GET.get('page', request.session[page_name]))
    except:
        page = 1

    request.session[page_name] = page

    # If page request (9999) is out of range, deliver last page of results.
    try:
        # Select the page
        paginated_list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        # Number possibly too big! Show the last page
        paginated_list = paginator.page(paginator.num_pages)
    
    setattr(paginated_list,'page_limit', paginator.per_page)
    
    return paginated_list

#==============================================================================
class Response(HttpResponse):
    """
    Just a simpler shortcut to respond...
    """
    #--------------------------------------------------------------------------
    def __init__(self, request, template, variables, *args, **kwargs):
        super(Response, self).__init__(loader.get_template(template).render(RequestContext(request,variables)), *args, **kwargs)
