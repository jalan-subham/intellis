from django.db import models
from django.utils.timezone import now


class IncidentType(models.Model):
    type_name = models.CharField(max_length=50)  # e.g., "Trespassing", "Fire"
    respondents = models.ManyToManyField("Respondent", related_name="incident_types")  # Respondents for this type

    def __str__(self):
        return f"{self.type_name}"


class Camera(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)
    rtsp_url = models.URLField(max_length=200)  # Updated to URLField for clarity

    def __str__(self):
        return self.name


class Respondent(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Incident(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=now)  
    incident_type = models.ForeignKey("IncidentType", on_delete=models.CASCADE, null=True)  
    camera = models.ForeignKey("Camera", on_delete=models.CASCADE) 
    resolved = models.BooleanField(default=False)
    resolver = models.ForeignKey("Respondent", on_delete=models.CASCADE, null=True, blank=True)  

    def __str__(self):
        return f"Incident {self.id} - {self.incident_type}"
