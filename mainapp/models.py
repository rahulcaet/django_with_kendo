from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=50)
    occupation = models.CharField(max_length=30)
    date_of_birth = models.DateField()

    """
    def as_dict(self):
        return {

            "name" : self.name,
            "occupation" : self.occupation,
            "date_of_birth": self.date_of_birth
        }

    """
