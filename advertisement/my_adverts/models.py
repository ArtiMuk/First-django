from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=15)
    description=models.TextField('Описание')
    photo=models.ImageField('Изображение',upload_to='advertisement/')
    price=models.DecimalField('Цена', max_digits=10, decimal_places=2)
    creation_date=models.DateTimeField('Создано',auto_now_add=True)
    update_date=models.DateTimeField('Обновлено',auto_now=True)
    category=models.DecimalField('Категория', max_digits=10, decimal_places=2)
    location=models.CharField('Локация товара', max_length=255)
    auction=models.BooleanField('Торг', help_text='Отметьте, если торг уместен')
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)

    class Meta:
        db_table = 'advertisements'
        
    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'
    
    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.creation_date.date() == timezone.now().date():
            create_time=self.creation_date.strftime('%H:%M.%S')
            return format_html("""
            <span style="color:#37D000">Сегодня в {}</span> 
                             """, create_time)
        return self.creation_date.strftime('%d.%m.%Y в %H:%M.%S')

    @admin.display(description='Дата обновления')
    def updated_date(self):
        from django.utils import timezone
        if self.update_date.date() == timezone.now().date():
            upd_time=self.update_date.strftime('%H:%M.%S')
            return format_html("""
            <span style="color:#37D000">Сегодня в {}</span> 
                             """, upd_time)
        return self.update_date.strftime('%d.%m.%Y в %H:%M.%S')
    
    @admin.display(description='Фото')
    def mini_photo(self):
        if self.photo:
            return format_html(
                """<img src="{}" class="img-fluid rounded-start" width=60 height=60 alt="Card title"> 
                """, self.photo.url)