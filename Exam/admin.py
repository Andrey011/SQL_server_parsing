from django.contrib import admin
from .models import Name, Date_of_exam, Date_of_reexam

admin.site.register(Name)
admin.site.register(Date_of_exam)
admin.site.register(Date_of_reexam)
