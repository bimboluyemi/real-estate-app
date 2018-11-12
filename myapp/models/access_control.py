from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_expiry_date = models.DateField()


class Role(models.Model):
    name = models.CharField(max_length=55)
    users = models.ManyToManyField(User, through='UserRole')

    def __str__(self):
        return self.name


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    date_assigned = models.DateField()

    def __str__(self):
        return ' | '.join([self.user.__str__(), self.role.__str__(), self.date_assigned.__str__()])


class Permission(models.Model):
    code = models.CharField(max_length=10)
    sysFeature = models.CharField(max_length=75)
    roles = models.ManyToManyField(Role, through='RolePermission')

    def __str__(self):
        return ' - '.join(self.code, self.sysFeature)


class RolePermission(models.Model):
    PERMISSION_TYPE = (
        ('read', 'Read'),
        ('write', 'Write'),
        ('update', 'Update'),
        ('delete', 'Delete')
    )
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    permissionType = models.CharField(max_length=20, choices=PERMISSION_TYPE)

    def __str__(self):
        return ' | '.join([self.role.__str__(), self.permission.__str__(), self.permissionType.__str__()])

