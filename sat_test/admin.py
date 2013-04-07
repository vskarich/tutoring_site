from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from sat_test.models import Test, Score

# Define an inline admin descriptor for UserProfile model
# which acts a bit like a singleton
class TestInline(admin.StackedInline):
    model = Test
    can_delete = False
    verbose_name_plural = 'test'

# Define a new User admin
class TestAdmin(UserAdmin):
    inlines = (UserProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)