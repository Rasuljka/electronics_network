from django.contrib import admin
from .models import ContactInfo, Product, NetworkNode, ProductStock


class ContactInfoInline(admin.TabularInline):
    model = ContactInfo
    extra = 1


class ProductInline(admin.TabularInline):
    model = ProductStock
    extra = 1


class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'supplier_link', 'debt', 'created_at')
    list_filter = ('contact_info__city',)
    inlines = [ProductInline]

    def supplier_link(self, obj):
        """Показывает ссылку на поставщика"""
        if obj.supplier:
            return f'<a href="/admin/network/networknode/{obj.supplier.id}/change/">{obj.supplier.name}</a>'
        return "Нет поставщика"
    supplier_link.allow_tags = True
    supplier_link.short_description = 'Поставщик'

    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        """Очищает задолженность"""
        for node in queryset:
            node.debt = 0
            node.save()
        self.message_user(request, "Задолженность перед поставщиком успешно очищена.")
    clear_debt.short_description = "Очистить задолженность перед поставщиком у выбранных объектов"


admin.site.register(ContactInfo)
admin.site.register(Product)
admin.site.register(NetworkNode, NetworkNodeAdmin)
admin.site.register(ProductStock)
