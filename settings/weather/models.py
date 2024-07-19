from django.db import models
from django.contrib.auth import get_user_model


user = get_user_model()
# Create your models here.
class SearchHistory(models.Model):
    name = models.CharField('название пункта', max_length=80)
    additional_info = models.CharField('дополнительная информация', max_length=80, blank=True, null=True)
    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Ширина')
    last_visited = models.DateTimeField(auto_now=True)
    counter = models.IntegerField('Количество посещений', default=1)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    class Meta:
        db_table = 'search_history'
        unique_together = [['longitude', 'latitude']]

    def __str__(self):
        return self.name

