from django.db import models

class SWOT(models.Model):
    STRENGTH = 'Strength'
    WEAKNESS = 'Weakness'
    OPPORTUNITY = 'Opportunity'
    THREAT = 'Threat'

    SWOT_TYPE_CHOICES = [
        (STRENGTH, 'Strength'),
        (WEAKNESS, 'Weakness'),
        (OPPORTUNITY, 'Opportunity'),
        (THREAT, 'Threat'),
    ]

    type = models.CharField(max_length=20, choices=SWOT_TYPE_CHOICES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} - {self.description[:30]}"


class PESTEL(models.Model):
    POLITIQUE = 'Politique'
    ECONOMIQUE = 'Économique'
    SOCIO = 'Sociologique'
    TECHNO = 'Technologique'
    ENVIRONNEMENTAL = 'Environnemental'
    LEGAL = 'Légal'

    TYPE_CHOICES = [
        (POLITIQUE, 'Politique'),
        (ECONOMIQUE, 'Économique'),
        (SOCIO, 'Sociologique'),
        (TECHNO, 'Technologique'),
        (ENVIRONNEMENTAL, 'Environnemental'),
        (LEGAL, 'Légal'),
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} – {self.description[:30]}"


class StrategicObjective(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProcessMapping(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class RiskOpportunity(models.Model):
    RISK = 'Risk'
    OPPORTUNITY = 'Opportunity'
    TYPE_CHOICES = [
        (RISK, 'Risk'),
        (OPPORTUNITY, 'Opportunity'),
    ]

    process = models.ForeignKey(ProcessMapping, on_delete=models.CASCADE, related_name='risks_opps')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} on {self.process.name}"


class ActionPlan(models.Model):
    risk_opportunity = models.ForeignKey(RiskOpportunity, on_delete=models.CASCADE, related_name='action_plans')
    description = models.TextField()
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
    ], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Plan for {self.risk_opportunity}"
