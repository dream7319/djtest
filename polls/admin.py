from django.contrib import admin
from polls.models import Question
# Register your models here.
#默认根据Question对象来生成表单
# admin.site.register(Question)

#手动指定表单
class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pubDate','questionText']
    # fieldsets = [
    #     (None,{'fields': ["questionText"]}),
    #     ('Date information', {'fields': ['pubDate']}),
    # ]
    #指定样式
    fieldsets = [
        (None, {'fields': ["questionText"]}),
        ('Date information', {'fields': ['pubDate'], 'classes': ['collapse']}),
    ]
    list_display = ('pubDate','questionText')
    list_filter = ['questionText']
    search_fields = ['questionText']
admin.site.register(Question,QuestionAdmin)