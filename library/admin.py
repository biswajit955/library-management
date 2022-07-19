from django.contrib import admin
from .models import Book ,MyUser
# Register your models here.

@admin.register(MyUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass


class BookAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book, BookAdmin)



