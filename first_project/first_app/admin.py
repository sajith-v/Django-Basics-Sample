from django.contrib import admin
from first_app import models as myModel

admin.site.register(myModel.Topic);
admin.site.register(myModel.WebPage);
admin.site.register(myModel.AccessRecord);
admin.site.register(myModel.UserInfo);
# Register your models here.
