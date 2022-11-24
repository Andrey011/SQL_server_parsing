from django.contrib import admin
# from .models import Post
from .models import Name, Number_of_student, Year_of_born, Address, Place_of_work, Title_of_diplome

admin.site.register(Name)
admin.site.register(Number_of_student)
admin.site.register(Year_of_born)
admin.site.register(Address)
admin.site.register(Place_of_work)
admin.site.register(Title_of_diplome)
