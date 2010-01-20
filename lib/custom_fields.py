'''
Created on 19 Jan 2010

@author: euan
'''
from django.db.models.fields import files

class FieldFile(files.FieldFile):
    ""
    
    def _get_path(self):
        self._require_file()
        return self.storage.path('/'+self.name)
    path = property(_get_path)

    def _get_url(self):
        self._require_file()
        return self.storage.url('/'+self.name)
    url = property(_get_url)
    
#==============================================================================
class FileField(files.FileField):
    ""
    attr_class = FieldFile
    
