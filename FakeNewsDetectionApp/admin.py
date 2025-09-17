from django.contrib import admin

from FakeNewsDetectionApp.models import ComplaintTable, FeedbackTable, LoginTable, UserTable

# Register your models here.
admin.site.register(LoginTable)
admin.site.register(UserTable)
admin.site.register(ComplaintTable)
admin.site.register(FeedbackTable)

