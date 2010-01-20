'''
Created on 19 Jan 2010

@author: euan
'''
from django.db import models
from django.contrib.admin import widgets as admin_widgets
from tinymce import widgets as tinymce_widgets

class HTMLField(models.TextField):
    """
    A large string field for HTML content. It uses the TinyMCE widget in
    forms.
    """
    #--------------------------------------------------------------------------
    def __init__(self, **kwargs):
        
        self.rows = kwargs.pop('rows', 30)
        self.cols = kwargs.pop('cols', 30)
                
        return super(HTMLField, self).__init__(**kwargs)
    
    #--------------------------------------------------------------------------    
    def formfield(self, **kwargs):
        defaults = {'widget': tinymce_widgets.TinyMCE(attrs={'cols': self.cols, 'rows': self.rows})}
        defaults.update(kwargs)

        # As an ugly hack, we override the admin widget
        if defaults['widget'] == admin_widgets.AdminTextareaWidget:
            defaults['widget'] = tinymce_widgets.AdminTinyMCE(attrs={'cols': self.cols, 'rows': self.rows})

        return super(HTMLField, self).formfield(**defaults)
