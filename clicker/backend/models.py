from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Core(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    coins = models.IntegerField(default=0)
    click_power = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.user}, coins: {self.coins}, power: {self.click_power}"

    def click(self) -> None:
        self.coins += self.click_power
        self.save()



#идея в том, что при каждой покупке буста увеличивается его цена
class Boost(models.Model):
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




