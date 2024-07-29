from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse

from home.models import UserProfile

from .models import Blog, Enrollment
from home.models import Blog, UserProfile, Event



# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_id', 'title', 'date', 'author')


# class AttendanceAdmin(admin.ModelAdmin):
#     filter_horizontal = ('volunteer',)  # Displays the ManyToManyField as a horizontal filter
#     list_display = ('event', 'volunteers', 'present')  # Displays the selected values of the ManyToManyField in a readable format

#     def volunteers(self, obj):
#         return ", ".join([user.username for user in obj.volunteer.all()])  # Returns a comma-separated list of usernames




# Register your models here.


admin.site.register(UserProfile)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Enrollment)
# admin.site.register(Attendance,AttendanceAdmin)


class EventAdmin(admin.ModelAdmin):
    # Other configurations for your Event admin if any
    
    actions = ['go_to_attendance_list']
    
    def go_to_attendance_list(self, request, queryset):
        # Assuming you have a single event selected in the queryset
        if queryset.count() == 1:
            event = queryset.first()
            url = reverse('attendance', args=[event.e_id])
            return HttpResponseRedirect(url)

    go_to_attendance_list.short_description = "Go to attendance list"
admin.site.register(Event,EventAdmin)
