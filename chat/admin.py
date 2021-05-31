from django.contrib import admin
from chat.models import chat_first_question_model,payment,Message, tip_model, QA_model,Message_cost
# Register your models here.
admin.site.register(chat_first_question_model)
admin.site.register(payment)
admin.site.register(Message)
admin.site.register(Message_cost)
admin.site.register(tip_model)
admin.site.register(QA_model)
