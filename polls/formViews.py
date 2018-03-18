from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from polls.models import Question, Choice

def form(request, questionId):
    p = get_object_or_404(Question, pk=questionId)

    try:
        choice = request.POST['choice']
        choiceSet = p.choice_set
        selected_choice = choiceSet.get(pk= choice)
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'form.html', {
            'question': p,
            'error_message': "You didn't select a choice",
        })

    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))