from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, email, first_name, last_name, username, password):
        if not phone_number:
            raise ValueError('user must have phone number')

        if not email:
            raise ValueError('user must have email')

        if not username:
            raise ValueError('user must have username')
        if not first_name:
            raise ValueError('user must have first name')
        if not last_name:
            raise ValueError('user must have last name')

        user = self.model(phone_number=phone_number, email=self.normalize_email(email), first_name=first_name,
                          last_name=last_name, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, email, first_name, last_name, username, password):
        user = self.create_user(phone_number, email, first_name, last_name, username, password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
