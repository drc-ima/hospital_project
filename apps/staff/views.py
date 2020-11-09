from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . import forms
from . import models


@login_required()
def dashboard(request):
    return render(request, template_name='staff/dashboard.html')


@login_required()
def complaints(request):
    my_complaints = models.Complaint.objects.filter(created_by=request.user)
    form = forms.ComplaintForm

    context = {
        'object_list': my_complaints,
        'form': form
    }

    if request.method == 'POST':
        form = forms.ComplaintForm(request.POST)
        form.instance.created_by = request.user
        form.instance.is_seen = False
        form.instance.status = 0
        form.save()

    return render(request, template_name='staff/complaints.html', context=context)

@login_required()
def cancel_complaint(request, id):
    complaint = models.Complaint.objects.get(id=id)

    if complaint.status == 0:
        complaint.status = 2
        complaint.save()

    return redirect(reverse_lazy('staff:complaints'))

