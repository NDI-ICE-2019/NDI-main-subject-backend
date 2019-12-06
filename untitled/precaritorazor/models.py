from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class User(models.Model):
    # lastname = models.CharField(max_length=200)
    # firstname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    pseudo = models.CharField(max_length=200)
    age = models.IntegerField(default=18)
    city = models.CharField(max_length=200)
    situation = models.CharField(max_length=200)
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.pseudo


class Organization(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    label = models.CharField(max_length=200)

    def __str__(self):
        return self.label


class Type(models.Model):
    label = models.CharField(max_length=200)

    def __str__(self):
        return self.label


class Aid(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1500)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Criteria(models.Model):
    label = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    aid = models.ForeignKey(Aid, on_delete=models.CASCADE)
    # op = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.label
