from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(User):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    phone_number = models.CharField(max_length=14, default="+996")
    age = models.PositiveIntegerField(default=18, validators=[MaxValueValidator(90), MinValueValidator(5)])
    gender = models.CharField(max_length=50, choices=GENDER)
    squad = models.CharField(max_length=50, default='Возрастная группа не определена')
    birth_date = models.DateField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)


@receiver(post_save, sender=CustomUser)
def set_squad(sender, instance, created, **kwargs):
    if created:
        print('Сигнал обработан успешно, пользователь зарегистрировался')
        age = instance.age
        if age < 5:
            instance.squad = 'Зародыш'
        elif age >= 0 and age <= 7:
            instance.squad = 'Малютка'
        elif age >= 7 and age <= 18:
            instance.squad = 'Подросток'
        elif age >= 18 and age <= 50:
            instance.squad = 'Взрослый'
        else:
            instance.squad = 'Возрастная группа не определена'
        instance.save()
