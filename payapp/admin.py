from django.contrib import admin
from .models import Book, BuyingHistory


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    list_display_links = ('title',)


@admin.register(BuyingHistory)
class BuyingHistoryAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'created_at', 'stripe_id')
    list_display_links = ('book',)
