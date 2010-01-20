from django.utils import safestring

from lib import utils

from app.models import Publication

def getContent(request, template='blog/entry.html', extra_context={}):
        
    context = { 'content' :  safestring.mark_safe(Publication.objects.get(id=2).my_field) }
    
    context.update(extra_context)
    
    return utils.Response(request, template, context)