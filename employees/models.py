from django.db import models

class employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    #photo = models.ImageField(upload_to='images')
    designation = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 11/06/24

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    


class employee_role(models.Model):
    role = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.role
    
class employee_dept(models.Model):
    dept = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.dept

