from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest
from django.core.exceptions import ValidationError


class SquadMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == "/register/" and request.method == "POST":
            age = int(request.POST.get("age"))
            if age < 5:
                return HttpResponseBadRequest("Вы еще маленький")
            elif age >= 0 and age <= 7:
                request.squad = "Зародыш"
            elif age >= 7 and age <= 18:
                request.squad = "Подросток"
            elif age >= 18 and age <= 50:
                request.squad = "Взрослый"
            else:
                return HttpResponseBadRequest("Вы слишком старый")
        elif request.path == "/register/" and request.method == "GET":
            setattr(request, "squad", "Группа не определена")
