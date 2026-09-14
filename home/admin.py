from django.contrib import admin
from .models import Project, Certification, Contact, Technology, Experience


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = ('title','category','created_at',)


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):

    list_display = ('title','issuer','issue_date',)
    search_fields = ('title','issuer','credential_id','description',)
    ordering = ('-issue_date',)



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('name','email','subject','created_at',)
    search_fields = ('name','email','subject','message',)
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):

    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title','company','start_date','end_date',)
    search_fields = ('job_title','company','location','description',)
    filter_horizontal = ('technologies',)
    ordering = ('-start_date',)