from django.views.generic import TemplateView




class HomeView(TemplateView):

    template_name = 'main/home.html'

class IndexView(TemplateView):

    template_name = 'main/index.html'

class ProjetoAlzhmaView(TemplateView):

    template_name = 'main/projeto.html'

class InfoSiteView(TemplateView):

    template_name = 'main/info_site.html'




