from random import choices

from django.db import models

# Create your models here.
# from Util.DB import EnumField
# from Util.Utils import Gender


class Institute(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='')

    def __str__(self):
        return f'{ self.name }'

    class Meta:
        db_table = 'Institutes'
        verbose_name = 'Institute'
        verbose_name_plural = 'Institutes'


class Person(models.Model):
    firstName = models.CharField(max_length=25)
    fatherName = models.CharField(max_length=25)
    grandfatherName = models.CharField(max_length=25)
    familyName = models.CharField(max_length=25)

    GENDER = (('MALE', 'Male'), ('FEMALE', 'Female'))
    gender = models.CharField(max_length=6, choices=GENDER, null=True)
    birthday = models.DateField(null=True)
    nationality = models.CharField(max_length=25, null=True)
    nationalId = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)

    workId = models.CharField(max_length=25)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)

    rightThumbFingerprint = models.BinaryField()
    rightIndexFingerprint = models.BinaryField()
    rightMiddleFingerprint = models.BinaryField()
    rightRingFingerprint = models.BinaryField()
    rightLittleFingerprint = models.BinaryField()

    leftThumbFingerprint = models.BinaryField()
    leftIndexFingerprint = models.BinaryField()
    leftMiddleFingerprint = models.BinaryField()
    leftRingFingerprint = models.BinaryField()
    leftLittleFingerprint = models.BinaryField()

    fingerprintImagesDir = models.CharField(max_length=1000)

    RELATIONSHIP = (('EMPLOYEE', 'Employee'),
                    ('FATHER', 'Father'),
                    ('MOTHER', 'Mother'),
                    ('SUN', 'Sun'),
                    ('DAUGHTER', 'Daughter'),
                    ('HUSBAND', 'Husband'),
                    ('WIFE', 'Wife'),)
    relationship = models.CharField(max_length=10, choices=RELATIONSHIP)

    profilePicture = models.ImageField(default='defaultProfilePicture.jpg', upload_to='profilePictures')

    def __str__(self):
        return f'{ self.firstName } { self.familyName }'

    class Meta:
        db_table = 'People'
        verbose_name = 'Person'
        verbose_name_plural = 'People'


class Contact(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    CONTACT = (
        ('PHONE', ''),
        ('MAIL', ''),
        ('EMAIL', ''),
        ('FACEBOOK', ''),
        ('INSTAGRAM', ''),
        ('TWITTER', ''),
        ('VIBER', ''),
        ('OTHER', ''),
    )
    label = models.CharField(max_length=10)
    contact = models.CharField(max_length=1000)

    class Meta:
        db_table = 'Contacts'
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

