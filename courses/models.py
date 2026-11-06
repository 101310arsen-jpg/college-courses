from django.db import models


class Teacher(models.Model):
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    email = models.EmailField("Электронная почта", unique=True)
    phone = models.CharField("Телефон", max_length=20, blank=True)

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    title = models.CharField("Название курса", max_length=200)
    description = models.TextField("Описание", blank=True)
    hours = models.PositiveIntegerField("Количество часов", default=72)

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.PROTECT,
        related_name="courses"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title


class Student(models.Model):
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    email = models.EmailField("Электронная почта", unique=True)
    group = models.CharField("Группа", max_length=20)
    birth_date = models.DateField("Дата рождения", null=True, blank=True)

    courses = models.ManyToManyField(
        Course,
        related_name="students",
        blank=True
    )

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.group})"