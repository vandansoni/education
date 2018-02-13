from django.contrib import admin
from school_mgmt.models import *

# Register your models here.


class UniversityAdmin(admin.ModelAdmin):
	actions = ['enable']

	fieldsets = (
	    ('University data', {'fields': ('name', 'website', 'Logo')}),
	    ('Date', {'fields': ('created_date',)}),
	    ('Permission', {'fields': ('is_active', )}),
	)

	exclude = ('modified_date',)

	search_fields = ('name',)
	ordering = ('-created_date',)
	list_display = ('name', 'website')
	list_display_links = ('name', 'website')
	list_filter = ('name', )

	def enable(self, request, queryset):
		queryset.update(is_active=True)

class SchoolAdmin(admin.ModelAdmin):
	actions = ['enable']

	fieldsets = (
	    ('School data', {'fields': ('owner', 'university', 'name', 'website', 'Logo')}),
	    ('Date', {'fields': ('created_date',)}),
	    ('Permission', {'fields': ('is_active', )}),
	)

	exclude = ('modified_date',)

	search_fields = ('name',)
	ordering = ('-created_date',)
	list_display = ('owner', 'university', 'name','owner')
	list_display_links = ('owner', 'university', 'name')
	list_filter = ('name', )

	def enable(self, request, queryset):
		queryset.update(is_active=True)


class AddressAdmin(admin.ModelAdmin):
	#actions = ['enable']

	fieldsets = (
	    ('Address data', {'fields': ('street_1', 'street_2', 'city', 'state', 'country', 'zipcode', 'mobile')}),
	    # ('Date', {'fields': ('created_date',)}),
	    # ('Permission', {'fields': ('is_active', )}),
	)

	# exclude = ('modified_date',)

	# search_fields = ('name',)
	# ordering = ('-created_date',)
	# list_display = ('owner', 'university', 'name')
	# list_display_links = ('owner', 'university', 'name')
	# list_filter = ('name', )

	# def enable(self, request, queryset):
	# 	queryset.update(is_active=True)

class StudentAdmin(admin.ModelAdmin):
	actions = ['enable']

	fieldsets = (
	    ('School data', {'fields': ('school', 'first_name', 'roll_number', 'email', 'address')}),
	    ('Date', {'fields': ('created_date', 'date_of_birth')}),
	    ('Permission', {'fields': ('is_active', )}),
	)

	exclude = ('modified_date',)

	search_fields = ('first_name', 'roll_number')
	ordering = ('-created_date',)
	list_display = ('school', 'first_name', 'roll_number')
	list_display_links = ('school', 'first_name', 'roll_number')
	list_filter = ('roll_number', )

	def enable(self, request, queryset):
		queryset.update(is_active=True)


admin.site.register(University, UniversityAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Student, StudentAdmin)



