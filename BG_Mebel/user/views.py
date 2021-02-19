from django.contrib.auth.views import LoginView


class LoginUserView(LoginView):
    template_name = 'main/main.html'
    redirect_field_name = 'main/main.html'

