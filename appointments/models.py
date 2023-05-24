from django.db import models


class Client(models.Model):
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.phone_number


class Master(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.IntegerField(default=30)

    def __str__(self):
        return self.name


class Saloon(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Slot(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    saloon = models.ForeignKey(Saloon, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()

    def __str__(self):
        return self.start_datetime
