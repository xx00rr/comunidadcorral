from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Organization
from .forms import OrganizationForm


@login_required
def org_detail(request):
    if not request.organization:
        return redirect('no_org')
    org = request.organization
    return render(request, 'organizations/detail.html', {'org': org})


@login_required
def org_edit(request):
    if not request.organization:
        return redirect('no_org')
    if not request.user.is_org_admin and not request.user.is_superuser:
        messages.error(request, 'No tienes permisos para editar la organización.')
        return redirect('dashboard')
    org = request.organization
    form = OrganizationForm(request.POST or None, instance=org)
    if form.is_valid():
        form.save()
        messages.success(request, 'Organización actualizada.')
        return redirect('org_detail')
    return render(request, 'organizations/form.html', {'form': form, 'org': org})
