from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
                                        PermissionsMixin,
                                        BaseUserManager)
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is "UserManager"
    """

    def create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Email', unique=True)
    first_name = models.CharField('First Name', max_length=30)
    last_name = models.CharField('Last Name', max_length=30)
    group = models.CharField('Group', max_length=6)
    faculty = models.CharField('Faculty', max_length=60)
    is_staff = models.BooleanField('Is Staff', default=False, help_text='If user is staff')  # NoQa
    is_active = models.BooleanField('Is Active', default=True, help_text='Is user is active')  # NoQa
    date_joined = models.DateTimeField('Date Joined', default=timezone.now)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['date_joined']

    def __str__(self):
        return self.email


class Faculties(models.Model):
    name = models.CharField('Название факультета', max_length=200, db_index=True)

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'

    def __str__(self):
        return self.name


class Groups(models.Model):
    faculty = models.ForeignKey(Faculties, on_delete=models.CASCADE)
    name = models.CharField('Название группы', max_length=7, db_index=True)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name


class News(models.Model):
    date = models.DateField('Дата', auto_now=False)
    title = models.CharField('Заголовок', max_length=30, db_index=True)
    text = models.TextField('Текст', max_length=1000, db_index=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title


class DuelParticipatingNow(models.Model):
    id = models.AutoField(primary_key=True)
    firstPeople = models.CharField('Участник №1', max_length=60, db_index=True, unique=True)
    groupFirst = models.CharField('Группа уч. №1', max_length=60, db_index=True)
    secondPeople = models.CharField('Участник №2', max_length=60, db_index=True)
    groupSecond = models.CharField('Группа уч. №2', max_length=60, db_index=True)
    acceptDuel = models.BooleanField('Дуэль подтв.', default=False)

    class Meta:
        verbose_name = 'Текущая пара оппонентов'
        verbose_name_plural = 'Текущие пары оппонентов'

    def __int__(self):
        return self.firstPeople


class CommandParticipatingNow(models.Model):
    name = models.CharField('Название команды', max_length=60, db_index=True, unique=True)
    group = models.CharField('Уч. группа', max_length=60, db_index=True, unique=True)
    firstPeople = models.CharField('Участник №1', max_length=60, db_index=True, unique=True)
    secondPeople = models.CharField('Участник №2', max_length=60, db_index=True, unique=True)
    thirdPeople = models.CharField('Участник №3', max_length=60, db_index=True, unique=True)
    fourthPeople = models.CharField('Участник №4', max_length=60, db_index=True, unique=True,
                                    null=True, blank=True)
    fifthPeople = models.CharField('Участник №5', max_length=60, db_index=True, unique=True,
                                   null=True, blank=True)

    class Meta:
        verbose_name = 'Текущая команда мушкетеров'
        verbose_name_plural = 'Текущие команды мушкетеров'

    def __str__(self):
        return self.name


class LastWinners(models.Model):
    name = models.CharField('Название команды (для мушкетеров)', max_length=60, db_index=True,
                            unique=True, null=True, blank=True)
    group = models.CharField('Уч. группа (для мушкетеров)', max_length=60, db_index=True, unique=True)
    lineOne = models.CharField('уч. №1 или побед. №1 (для мушкетеров/дуэлей)',
                               max_length=30, db_index=True)
    lineTwo = models.CharField('уч. №2 или побед. №2 (для мушкетеров/дуэлей)',
                               max_length=30, db_index=True, null=True, blank=True)
    lineThree = models.CharField('уч. №3 или побед. №3 (для мушкетеров/дуэлей)',
                                 max_length=30, db_index=True, null=True, blank=True)
    lineFour = models.CharField('уч. №4 или побед. №4 (для мушкетеров/дуэлей)',
                                max_length=30, db_index=True, null=True, blank=True)
    lineFive = models.CharField('уч. №5 или побед. №5 (для мушкетеров/дуэлей)',
                                max_length=30, db_index=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Победители прошлого семестра'
        verbose_name_plural = 'Победители прошлого семестра'

    def __str__(self):
        return self.group


class Archive(models.Model):
    CHOICES = (
        ('Осенний', 'Осенний'),
        ('Весенний', 'Весенний')
    )
    year = models.CharField('Учебный год', max_length=7, db_index=True)
    semester = models.CharField('Семестр', max_length=8, db_index=True, choices=CHOICES)
    musketeers = models.CharField('Мушкетеры', max_length=300, db_index=True)
    duel = models.CharField('Дуэли', max_length=300, db_index=True)
    groups = models.CharField('Лучшие группы', max_length=300, db_index=True)

    class Meta:
        verbose_name = 'Архив'
        verbose_name_plural = 'Архив'

    def __str__(self):
        return self.year
