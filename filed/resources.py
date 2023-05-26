from import_export import resources
from .models import File
 
class FileResource(resources.ModelResource):
    class Meta:
        model = File