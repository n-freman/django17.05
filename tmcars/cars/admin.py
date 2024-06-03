from django.contrib import admin
from django.utils.html import mark_safe

from .models import Post, CarCharacteristic


class PostAdminConfig(admin.ModelAdmin):
    list_display = ['title', 'price_', 'image_']

    def price_(self, instance):
        return f'{instance.price} TMT'
    
    def image_(self, instance):
        return mark_safe(f'''
        <img
            src={instance.image.url}
            alt={instance.title}
            height=80 />
        ''')


admin.site.register(Post, PostAdminConfig)
admin.site.register(CarCharacteristic)
