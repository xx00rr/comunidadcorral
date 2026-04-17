from django.db import models


class Resident(models.Model):
    ROLES = [
        ('owner', 'Propietario'),
        ('tenant', 'Arrendatario'),
        ('family', 'Familiar'),
        ('other', 'Otro'),
    ]
    STATUS = [
        ('active', 'Activo'),
        ('inactive', 'Inactivo'),
    ]

    unit = models.ForeignKey(
        'units.Unit',
        on_delete=models.CASCADE,
        related_name='residents',
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    identification = models.CharField(max_length=20, blank=True, help_text='RUT, DNI, etc.')
    role = models.CharField(max_length=20, choices=ROLES, default='tenant')
    status = models.CharField(max_length=20, choices=STATUS, default='active')
    move_in_date = models.DateField(null=True, blank=True)
    move_out_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def organization(self):
        return self.unit.organization

    class Meta:
        ordering = ['last_name', 'first_name']
