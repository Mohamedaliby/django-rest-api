from django.db import models

from accounts.models import User
from people.models import Person
from shared.models import Tag, Institute


class ServiceCenter(models.Model):
    code = models.IntegerField(unique=True, null=True)
    name = models.CharField(max_length=25)
    tags = models.ManyToManyField(Tag, blank=False)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'ServiceCenters'
        verbose_name = 'Service Center'
        verbose_name_plural = 'Service Centers'


class Fingerprints(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

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

    class Meta:
        db_table = 'Fingerprints'
        verbose_name = 'Fingerprints'
        verbose_name_plural = 'Fingerprints'


class FingerprintImage(models.Model):
    """ This created to implement multi fingerprint image for a single finger """
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='FingerprintImage')
    image = models.ImageField(
        default='fingerprint.jpg',
        upload_to='fingerprintImages'
    )


class Record(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    serviceCenter = models.ForeignKey(ServiceCenter, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    identified = models.BooleanField()
    date = models.DateField()
    status = models.IntegerField(default=0)
    notes = models.TextField(null=True)
