from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Unit
from .forms import UnitForm
from accounts.decorators import tenant_required


@login_required
@tenant_required
def unit_list(request):
    units = Unit.objects.filter(organization=request.organization).select_related()
    status_filter = request.GET.get('status', '')
    type_filter = request.GET.get('type', '')
    if status_filter:
        units = units.filter(status=status_filter)
    if type_filter:
        units = units.filter(unit_type=type_filter)
    return render(request, 'units/list.html', {
        'units': units,
        'status_filter': status_filter,
        'type_filter': type_filter,
        'unit_types': Unit.UNIT_TYPES,
        'statuses': Unit.STATUS,
    })


@login_required
@tenant_required
def unit_detail(request, pk):
    unit = get_object_or_404(Unit, pk=pk, organization=request.organization)
    residents = unit.residents.all().order_by('-status', 'last_name')
    return render(request, 'units/detail.html', {'unit': unit, 'residents': residents})


@login_required
@tenant_required
def unit_create(request):
    form = UnitForm(request.POST or None)
    if form.is_valid():
        unit = form.save(commit=False)
        unit.organization = request.organization
        unit.save()
        messages.success(request, f'Unidad {unit.identifier} creada.')
        return redirect('unit_detail', pk=unit.pk)
    return render(request, 'units/form.html', {'form': form, 'action': 'Crear'})


@login_required
@tenant_required
def unit_edit(request, pk):
    unit = get_object_or_404(Unit, pk=pk, organization=request.organization)
    form = UnitForm(request.POST or None, instance=unit)
    if form.is_valid():
        form.save()
        messages.success(request, 'Unidad actualizada.')
        return redirect('unit_detail', pk=unit.pk)
    return render(request, 'units/form.html', {'form': form, 'unit': unit, 'action': 'Editar'})


@login_required
@tenant_required
def unit_delete(request, pk):
    unit = get_object_or_404(Unit, pk=pk, organization=request.organization)
    if request.method == 'POST':
        unit.delete()
        messages.success(request, 'Unidad eliminada.')
        return redirect('unit_list')
    return render(request, 'units/confirm_delete.html', {'unit': unit})
