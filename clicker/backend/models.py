from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Core(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    coins = models.IntegerField(default=0)
    click_power = models.IntegerField(default=1)
    autoclick_power = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.user}, coins: {self.coins}, power: {self.click_power}"

    def click(self, times=1) -> None:
        self.coins += self.click_power * times
        self.save()

    def increace_autoclick(self) -> None:
        self.autoclick_power += 1
        self.autoclick_price = int(self.autoclick_price * 1.55)
        self.save()

    
    def set_coins(self, value) -> None:
        self.coins = int(value)
        self.save()





#идея в том, что при каждой покупке буста увеличивается его цена
class Boost(models.Model):
    name = models.CharField(max_length=50, null=False, default="Безымянный препарат")
    number =  models.IntegerField()
    core = models.ForeignKey(Core, on_delete=models.CASCADE)
    power = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def use_boost(self, increase_percentage=0.2):
        if self.core.coins >= self.price:
            self.core.coins -= self.price
            self.core.click_power += self.power
            # self.price = int(self.price * increase_percentage)
            self.price = int(self.price * (1 + increase_percentage * self.number))
            self.core.save()
            self.save()
            return "good"
        return "bad"

    def __str__(self) -> str:
        return f"{self.core.user.username}, №{self.number}, price:{self.price}, power:{self.power}"
    

class AutoBoost(models.Model):
    name = models.CharField(max_length=50, null=False, default="Эффективный препарат")
    number =  models.IntegerField(default=0)
    core = models.ForeignKey(Core, on_delete=models.CASCADE)
    power = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def use_boost(self, power_ip=1.4, price_ip=1.55):
        if self.core.coins >= self.price:
            self.core.coins -= self.price
            self.core.autoclick_power += self.power
            self.power = int(self.power * power_ip)
            self.price = int(self.price * price_ip)
            self.core.save()
            self.save()
            return "good"
        return "bad"


    def __str__(self) -> str:
        return f"{self.core.user.username}, №{self.number}, price:{self.price}, power:{self.power}"
    





