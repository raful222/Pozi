from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type


class AppTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return text_type(user.is_active) + text_type(user.pk) + text_type(timestamp)


token_generator = AppTokenGenerator()
#
#
# def send_activation_email(request, email, code):
#     context = {
#         'subject': _('Profile activation'),
#         'uri': request.build_absolute_uri(reverse('basic_app:activate', kwargs={'code': code})),
#     }
#
#     send_mail(email, 'activate_profile', context)
#
#
# def send_activation_change_email(request, email, code):
#     context = {
#         'subject': _('Change email'),
#         'uri': request.build_absolute_uri(reverse('basic_app:change_email_activation', kwargs={'code': code})),
#     }
#
#     send_mail(email, 'change_email', context)
