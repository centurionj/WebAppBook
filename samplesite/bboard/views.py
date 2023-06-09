from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Bb, Rubric
from .forms import BbForm

# Create your views here.

def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)


## контроллер-класс сам выполняет большую часть действий по выводу и обработке формы
class BbCreateView(CreateView):
    template_name = 'bboard/create.html'  # путь к файлу шаблону
    form_class = BbForm                   # ссылка на класс формы связанной моделью
    #success_url = '/bboard/'             # перенаправление на заданный урл адрес
    success_url = reverse_lazy('index')   # принимет имя маршрута и значения всех входящих в маршрут урл
                                          # (если коротко то тоже самое, но только по названию функции)

    # переопределяем метод формирующий контекст шаблона
    def get_context_data(self, **kwargs):
        # в теле метода получаем контекст шаблона от метода базового класса, добавляем в него список рубрик
        # и возвращаем его в качестве результата
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
