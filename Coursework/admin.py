from django.contrib import admin
# from .models import Post
from .models import Name_cours, Scientific_leader, Field, Student


admin.site.register(Student)
admin.site.register(Scientific_leader)
admin.site.register(Field)
admin.site.register(Name_cours)