from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, name,email, password=None):
        if not email:
            raise ValueError("user most have a Email")
        
        user = self.model(
            name=name,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, name, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            password=password,
        )
        user.is_staff =True
        self.is_superuser = True

        user.save(using=self._db)

        return user