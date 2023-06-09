from django.db import models


# Create your models here.

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')

    ## добавляем поле рубрики в модель Bb, которое будет внешним ключем с моделью Rubric
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-published']

## Создаем модель рубрики для сортировки объявлений по полю рубрика
class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    class Meta():
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
## Переопределяем метод, чтоб выводилось человеческое строковое представление названия в панели админа
    def __str__(self):
        return self.name

