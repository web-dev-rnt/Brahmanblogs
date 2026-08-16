from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
# ... (rest of the file remains the same)
class CustomUser(AbstractUser):
    # ... (rest of the class remains the same)
    def set_password(self, password):
        self.password = make_password(password)
    def save(self, *args, **kwargs):
        if not self.pk:
            self.set_password(self.password)
        super().save(*args, **kwargs)
