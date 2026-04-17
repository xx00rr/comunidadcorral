from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Resident
from .forms import ResidentForm
from units.models import Unit
from accounts.decorators import tenant_required


@login_required
@tenant_required
def resident_list(request):
    residents = Resident.objects.filter(
        unit__organization=request.organization
    ).select_related('unit')
    status_filter = request.GET.get('status', 'active')
    if status_filter:
        residents = residents.filter(status=status_filter)
    q = request.GET.get('q', '')
    if q:
        residents = residents.filter(
            first_name__icontains=q
        ) | residents.filter(last_name__icontains=q)
    return render(request, 'residents/list.html', {
        'residents': residents,
        'status_filter': status_filter,
        'q': q,
    })


@login_required
@tenant_required
def resident_detail(request, pk):
    resident = get_object_or_404(
        Resident, pk=pk, unit__organization=request.organization
    )
    return render(request, 'residents/detail.html', {'resident': resident})


@login_required
@tenant_required
def resident_create(request, unit_pk=None):
    unit = None
    if unit_pk:
        unit = get_object_or_404(Unit, pk=unit_pk, organization=request.organization)
    form = ResidentForm(request.POST or None, organization=request.organization, initial_unit=unit)
    if form.is_valid():
        resident = form.save()
        messages.success(request, f'Residente {resident.full_name} registrado.')
        return redirect('resident_detail', pk=resident.pk)
    return render(request, 'residents/form.html', {'form': form, 'action': 'Registrar', 'unit': unit})


@login_required
@tenant_required
def resident_edit(request, pk):
    resident = get_object_or_404(
        Resident, pk=pk, unit__organization=request.organization
    )
    form = ResidentForm(request.POST or None, instance=resident, organization=request.organization)
    if form.is_valid():
        form.save()
        messages.success(request, 'Residente actualizado.')
        return redirect('resident_detail', pk=resident.pk)
    return render(request, 'residents/form.html', {'form': form, 'resident': resident, 'action': 'Editar'})


@login_required
@tenant_required
def resident_delete(request, pk):
    resident = get_object_or_404(
        Resident, pk=pk, unit__organization=request.organization
    )
    if request.method == 'POST':
        resident.delete()
        messages.success(request, 'Residente eliminado.')
        return redirect('resident_list')
    return render(request, 'residents/confirm_delete.html', {'resident': resident})
