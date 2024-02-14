from django.db import models

class MinecraftTime(models.Model):
    minecraft_time = models.FloatField()
    real_time = models.FloatField()