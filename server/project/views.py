"""project views."""
from django.views import generic


class ProjectListView(generic.TemplateView):

    view_name = 'project_index'
    template_name = 'project/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
