from django.db import models

class Certificate(models.Model):
    name_title = models.CharField(max_length=5, choices=[('Mr.', 'Mr.'), ('Ms.', 'Ms.'), ('Mrs.', 'Mrs.')], default='Mr.')
    name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    college_name = models.CharField(max_length=255)
    from_date = models.DateField()
    to_date = models.DateField()
    Department = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    guide_title = models.CharField(max_length=5, choices=[('Mr.', 'Mr.'), ('Ms.', 'Ms.'), ('Mrs.', 'Mrs.')], default='Mr.')
    guide_name = models.CharField(max_length=255)
    guide_designation = models.CharField(max_length=255)
    guide_location = models.CharField(max_length=255)
    guide_co_title = models.CharField(max_length=5, choices=[('Mr.', 'Mr.'), ('Ms.', 'Ms.'), ('Mrs.', 'Mrs.')], default='Mr.')
    guide_co_name = models.CharField(max_length=255)
    guide_co_designation = models.CharField(max_length=255)
    guide_co_location = models.CharField(max_length=255)
    date = models.DateField()

    # New status field with choices for completed and pending
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('pending', 'Pending'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.name
