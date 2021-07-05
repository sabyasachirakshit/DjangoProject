from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class EmailAuthbackend(object):
    def authenticate(self,request,username=None,password=None):
        try:
            user=User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotException:
            raise ValidationError("Invalid Credentials")
