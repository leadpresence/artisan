from django.core.exceptions import ValidationError

#validate phone number
def phone_validation(value):
    if len(str(value))==10 :
        return value
    else:
        raise ValidationError('please enter a valid phone number exempt the first 0')
 