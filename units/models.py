from django.db import models


class Unit(models.Model):
    UNIT_TYPES = [
        ('apartment', 'Departamento'),
        ('room', 'Pieza'),
        ('cabin', 'Cabaña'),
        ('house', 'Casa'),
        ('office', 'Oficina'),
        ('other', 'Otro'),
    ]
    STATUS = [
        ('available', 'Disponible'),
        ('occupied', 'Ocupado'),
        ('maintenance', 'Mantención'),
    ]

    organization = models.ForeignKey(
        'organizations.Organization',
        on_delete=models.CASCADE,
        related_name='units',
    )
    identifier = models.CharField(max_length=50, help_text='Ej: A-12, Cabaña 3, Pieza 7')
    unit_type = models.CharField(max_length=20, choices=UNIT_TYPES, default='apartment')
    status = models.CharField(max_length=20, choices=STATUS, default='available')
    floor = models.CharField(max_length=10, blank=True)
    area_m2 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.get_unit_type_display()} {self.identifier}'

    @property
    def current_resident(self):
        return self.residents.filter(status='active').first()

    class Meta:
        ordering = ['identifier']
        unique_together = ('organization', 'identifier')
