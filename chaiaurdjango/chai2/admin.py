from django.contrib import admin
from .models import ChaiVariety, ChaiReview, ChaiCertificate, Store
# Register your models here.


# Customizing the admin interface
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 1

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display= ('name', 'type', 'date_added')
    inlines  = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'locatotion')
    filter_horizontal = ('chai_varities',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number', 'issued_date', 'valid_until')

admin.site.register(ChaiVariety, ChaiVarietyAdmin)
admin.site.register(ChaiReview)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
admin.site.register(Store, StoreAdmin)