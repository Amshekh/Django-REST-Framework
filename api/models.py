from django.db import models

# Creating Company model

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=75)
    company_location = models.CharField(max_length=75)
    company_type = models.CharField(max_length=100, choices=
                                    (('IT', 'IT'),
                                     ('Non IT', 'Non IT'),
                                     ('SaaS', 'SaaS'),
                                     ('CSP', 'CSP'),
                                     ('Mobile Phone based Company', 'Mobile Phone based Company'),
                                    ))
    company_aboutus = models.TextField()
    date_added = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.company_name    # to add more fields:  return self.company_name + ' -- ' + company_location
  

# Creating Employee model

class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    emp_post = models.CharField(max_length=75, choices=(
        ('Full Stack Python Web Developer', 'Full Stack Python Web Developer'),
        ('Python Programmer', 'Python Programmer'),
        ('Data Analyst', 'Data Analyst'),
        ('Software Engineer', 'Software Engineer'),
        ('Software Tester', 'Software Tester'),
        ('Web Developer', 'Web Developer'),
        ('Java Developer', 'Java Developer'),
        ('PL/SQL Developer', 'PL/SQL Developer'),
        ('Front-End Developer', 'Front-End Developer'),
        ('Game Developer', 'Game Developer'),
        ('Graphic Designer', 'Graphic Designer'),
    ))
    emp_address = models.CharField(max_length=100)
    emp_ctc = models.CharField(max_length=12)

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
