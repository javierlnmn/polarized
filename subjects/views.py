from django.views.generic import ListView
from .models import Subject


class SubjectListView(ListView):
    model = Subject
    template_name = 'subjects/subjects_list.html'
    # context_object_name = 'page_obj'
    paginate_by = 5
