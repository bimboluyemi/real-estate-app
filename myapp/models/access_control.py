from django.db import models


class User(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    email = models.EmailField(max_length=75)

    def __str__(self):
        return ' '.join([self.firstName, self.lastName])


class Password(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=25)
    encryptedPassword = models.CharField(max_length=255)
    salt = models.CharField(max_length=255)
    userAccountExpiryDate = models.DateField()
    passwordMustChange = models.BooleanField()
    passwordReset = models.BooleanField()


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
    SYSTEM_FEATURES = (
        ('UM', 'User Management'),
        ('RM', 'Role Management'),
        ('FM', 'Feature Management')
    )
    sysFeature = models.CharField(max_length=75, choices=SYSTEM_FEATURES)
    roles = models.ManyToManyField(Role, through='RolePermission')

    def __str__(self):
        return self.sysFeature.__str__()


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

