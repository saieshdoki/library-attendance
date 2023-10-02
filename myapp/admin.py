from django.contrib import admin

# Register your models here.
from .models import Attendance,vacancies1,Books,student,papers,papers1
admin.site.register(Attendance)

admin.site.register(vacancies1)
admin.site.register(Books)
admin.site.register(student)
admin.site.register(papers)
admin.site.register(papers1)