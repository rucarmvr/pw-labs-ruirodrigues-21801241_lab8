from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect

from portfolio.models import Projetos, Home_projets, Home_Web, Web, About, Educacao, Certificados, \
    Interesses_hobbies, Licenciatura, Outras_Habilitacoes, Laboratorio, OutSystems, Cg, Lp1, Aed


def home_page_view(request):
    context = {'home': Home_projets.objects.all(), 'home_web': Home_Web.objects.all()}
    return render(request, 'portfolio/home.html', context)


def web_page_view(request):
    context = {'web': Web.objects.all()}
    return render(request, 'portfolio/web.html', context)


def about_page_view(request):
    context = {'about': About.objects.all()}
    return render(request, 'portfolio/about.html', context)


def projects_page_view(request):
    context = {'projects': Projetos.objects.all()}
    return render(request, 'portfolio/projects.html', context)


def contact_page_view(request):
    return render(request, 'portfolio/contact.html')


def licenciatura_page_view(request):
    context = {'licenciatura': Licenciatura.objects.all()}
    return render(request, 'portfolio/licenciatura/licenciatura.html', context)


def educacao_page_view(request):
    context = {'educacao': Educacao.objects.all()}
    return render(request, 'portfolio/licenciatura/educacao.html', context)


def certificados_page_view(request):
    context = {'certificados': Certificados.objects.all()}
    return render(request, 'portfolio/licenciatura/certificados.html', context)


def interesses_hobbies_page_view(request):
    context = {'interesses_hobbies': Interesses_hobbies.objects.all()}
    return render(request, 'portfolio/licenciatura/interesses_hobbies.html', context)


def fisica_page_view(request):
    context = {'fisica': Interesses_hobbies.objects.all()}
    return render(request, 'portfolio/licenciatura/fisica.html', context)


def outras_habilitacoes_page_view(request):
    context = {'outras_habilitacoes': Outras_Habilitacoes.objects.all()}
    return render(request, 'portfolio/licenciatura/outras_habilitacoes.html', context)


def laboratorio_page_view(request):
    context = {'laboratorio': Laboratorio.objects.all()}
    return render(request, 'portfolio/programacao_web/laboratorio.html', context)


def outsystems_page_view(request):
    context = {'outsystems': OutSystems.objects.all()}
    return render(request, 'portfolio/programacao_web/outsystems.html', context)


def cg_page_view(request):
    context = {'cg': Cg.objects.all()}
    return render(request, 'portfolio/projets/cg.html', context)


def lp1_page_view(request):
    context = {'lp1': Lp1.objects.all()}
    return render(request, 'portfolio/projets/lp1.html', context)


def aed_page_view(request):
    context = {'aed': Aed.objects.all()}
    return render(request, 'portfolio/projets/aed.html', context)


def login_page_view(request):
    return render(request, 'registration/login.html')

