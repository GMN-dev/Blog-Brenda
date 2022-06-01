from django.contrib import admin
from .models import Post as PostSystem
from .models import Category as CategorySystem
# from .models import categoryModel as CategorySystem

# Register your models here.
admin.site.register(PostSystem)
admin.site.register(CategorySystem)
# admin.site.register(CategorySystem)