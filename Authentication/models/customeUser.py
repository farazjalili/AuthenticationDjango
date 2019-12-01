from django.contrib.auth.models import AbstractUser


'''
 AbstractBaseUser provides the core implementation of a user model, including hashed passwords and tokenized password resets
'''


class CustomeUser(AbstractUser):
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=12)
    mobile = models.CharField(max_length=12)

    '''
        A string describing the name of the field on the user model that is used as the unique identifier. 
        This will usually be a username of some kind, but it can also be an email address, or any other unique identifier
    '''
    USERNAME_FIELD = 'username'
    '''
        A string describing the name of the email field on the User model. This value is returned by get_email_field_name().
    '''
    EMAIL_FIELD = 'email'
    '''
        A list of the field names that will be prompted for when creating a user via the createsuperuser management command. 
        The user will be prompted to supply a value for each of these fields. 
        It must include any field for which blank is False or undefined and may include additional fields you want prompted for when a user is created interactively. 
        REQUIRED_FIELDS has no effect in other parts of Django, like creating a user in the admin.
    '''
    REQUIRED_FIELDS = ['email']
