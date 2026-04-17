from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from units.models import Unit
from residents.models import Resident
from .decorators import tenant_required


@login_required
def dashboard(request):
    if not request.organization and not request.user.is_superuser:
        return redirect('no_org')

    if request.user.is_superuser:
        from organizations.models import Organization
        orgs = Organization.objects.all()
        return render(request, 'dashboard/superadmin.html', {'orgs': orgs})

    org = request.organization
    units = Unit.objects.filter(organization=org)
    total_units = units.count()
    occupied = units.filter(status='occupied').count()
    available = units.filter(status='available').count()
    maintenance = units.filter(status='maintenance').count()
    residents = Resident.objects.filter(unit__organization=org, status='active').count()

    return render(request, 'dashboard/index.html', {
        'total_units': total_units,
        'occupied': occupied,
        'available': available,
        'maintenance': maintenance,
        'active_residents': residents,
    })


@login_required
def no_org(request):
    return render(request, 'accounts/no_org.html')
