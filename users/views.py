from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from . import models, middlewares, forms


# register
class RegistrationView(CreateView):
    form_class = forms.CustomRegistrationForm
    template_name = "users/register.html"
    success_url = "/login/"

    def form_valid(self, form):
        response = super().form_valid(form)
        age = form.cleaned_data["age"]
        if age < 5:
            self.object.squad = "Зародыш"
        elif 0 <= age <= 7:
            self.object.squad = "Малютка"
        elif 7 <= age <= 18:
            self.object.squad = "Подросток"
        elif 18 <= age <= 50:
            self.object.squad = "Взрослый"
        else:
            self.object.squad = "Возрастная группа не определена"
        self.object.save()
        return response


# authorization
class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "users/login.html"

    def get_success_url(self):
        return reverse("users:user_list")


# Logout
class AuthLogoutView(LogoutView):
    next_page = reverse_lazy("users:login")


class UserListView(ListView):
    template_name = "users/user_list.html"
    model = models.CustomUser

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["squad"] = getattr(self.request, "squad", "Возраст не определен")
        return context
