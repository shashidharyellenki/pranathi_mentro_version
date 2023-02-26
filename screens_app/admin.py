from django.contrib import admin
from  . models import Courses, Evaluation
# Register your models here.


class CoursesAdmin(admin.ModelAdmin):
    list_display=('id', 'Course_name')
    list_display_links=('Course_name',)
admin.site.register(Courses, CoursesAdmin)


class EvaluationAdmin(admin.ModelAdmin):
    list_display=('id', 'email')
    list_display_links=('email',)
admin.site.register(Evaluation, EvaluationAdmin)