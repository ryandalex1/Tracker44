from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['password1'].help_text = "Must be at least 8 characters"
        self.fields['password2'].help_text = "Confirm Password"
        self.fields['username'].help_text = None

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
