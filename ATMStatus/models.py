from django.db import models

from django.core.validators import RegexValidator, validate_slug


class AtmTerminalIdDetails(models.Model):
    s_n = models.IntegerField()
    atm_terminal_id = models.CharField(max_length=8)

    def __str__(self):
        return self.atm_terminal_id


class AtmDetails(models.Model):
    CHOICES = [('OffSite', 'OffSite'), ('OnSite', 'OnSite'), ]
    s_n = models.IntegerField()
    branch_name = models.CharField(max_length=100)
    branch_code = models.IntegerField(unique=True)
    atm_terminal_id = models.ForeignKey(
        AtmTerminalIdDetails, on_delete=models.CASCADE, null=True)
    atm_location = models.CharField(
        choices=CHOICES, default='OnSite', max_length=7,)
    atm_address = models.CharField(max_length=100, null=True)
    atm_ip_address = models.CharField(max_length=12)
    switch_ip_address = models.CharField(max_length=12)
    switch_port_number = models.IntegerField(default=24023)
    atm_installed_date = models.DateField()

    def __str__(self):
        return self.branch_name


class AtmIssueDetails(models.Model):
    CHOICES = [('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')]
    s_n = models.IntegerField(null=True)
    #branch_name = models.ForeignKey(AtmDetails,on_delete=models.CASCADE, null=True, related_name='AtmDetails_branch_name')
    branch_code = models.ForeignKey(
        AtmDetails, on_delete=models.CASCADE, null=True, related_name='AtmDetails_branch_code')
    atm_terminal_id = models.ForeignKey(
        AtmTerminalIdDetails, on_delete=models.CASCADE, null=True)
    problem = models.CharField(max_length=2083, null=True)
    remarks = models.CharField(max_length=2083, null=True)
    atm_issue_priority = models.CharField(
        choices=CHOICES, default='Medium', max_length=6)
