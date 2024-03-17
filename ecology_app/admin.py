from django.contrib import admin

from ecology_app.models import Animal, NaturalResources, Utilize, Plant

# Register your models here.
admin.site.register(Animal)
admin.site.register(NaturalResources)
admin.site.register(Plant)
admin.site.register(Utilize)
