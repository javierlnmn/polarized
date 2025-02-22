from django.http.response import HttpResponse
from django.views.generic import ListView, View
from django.shortcuts import get_object_or_404, render

from .models import Subject, Vote


class SubjectListView(ListView):
    model = Subject
    template_name = 'subjects/subjects_list.html'
    paginate_by = 5
    ordering = ('-created_at', 'id')


class VotingView(View):

    def post(self, request, subject_id):
        if not request.user.is_authenticated:
            return HttpResponse(status=401)

        subject = get_object_or_404(Subject, id=subject_id)

        vote_value_str = request.POST.get('value')

        try: 
            vote_value = int(vote_value_str)
        except TypeError:
            return HttpResponse(status=400)

        if vote_value not in dict(Vote.VoteChoices.choices):
            return HttpResponse(status=400)

        vote, created = Vote.objects.get_or_create(
            subject=subject,
            user=request.user,
            defaults={'value': vote_value}
        )

        if not created and vote.value != vote_value:
            vote.value = vote_value
            vote.save()
        
        return render(request, 'subjects/components/subject_voting_item.html', {
            'subject': subject,
        })

    def delete(self, request, subject_id):
        if not request.user.is_authenticated:
            return HttpResponse(status=401)

        subject = get_object_or_404(Subject, id=subject_id)

        vote = Vote.objects.filter(subject=subject, user=request.user).first()
        if not vote:
            return HttpResponse(status=404)
        
        vote.delete()
        
        return render(request, 'subjects/components/subject_voting_item.html', {
            'subject': subject,
        })