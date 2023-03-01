from django.db import models


class NestedMenu(models.Model):
    """Nested menu data"""
    name = models.CharField(verbose_name='название', max_length=20, unique=True, db_index=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = 'Древовидное меню'
        verbose_name_plural = 'Древовидные меню'


class MenuItemContainer(models.Model):
    """A menu item"""
    name = models.CharField(verbose_name='название', max_length=20, unique=True)
    label = models.CharField(verbose_name='метка', max_length=20)

    url = models.CharField(verbose_name='относительный url адрес', max_length=50, blank=True, null=True)
    url_name = models.CharField(verbose_name='имя url', max_length=20, blank=True, null=True)

    menu = models.ForeignKey(verbose_name='меню', to=NestedMenu, on_delete=models.CASCADE)
    parent_item = models.ForeignKey(
        verbose_name='родительский контейнер',
        to='MenuItemContainer',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.label}"
    
    class Meta:
        verbose_name = "элемент меню"
        verbose_name_plural = "элементы меню"
