# -*- coding: utf-8 -*-

from datetime import date

from django.conf import settings
from django.utils.http import int_to_base36, base36_to_int
from django.utils.crypto import constant_time_compare, salted_hmac
from django.utils import six


class SignupTokenGenerator(object):
    def make_token(self, email):
        return self._make_token_with_timestamp(email, self._num_days(self._today()))

    def check_token(self, email, token):
        # Parse the token
        try:
            ts_b36, hash = token.split("-")
        except ValueError:
            return False

        try:
            ts = base36_to_int(ts_b36)
        except ValueError:
            return False

        # Check that the timestamp/uid has not been tampered with
        if not constant_time_compare(
                self._make_token_with_timestamp(email, ts),
                token):
            return False

        # Check the timestamp is within limit
        if (self._num_days(self._today()) - ts) > settings.SIGNUP_TIMEOUT_DAYS:
            return False

        return True

    def _make_token_with_timestamp(self, email, timestamp):
        # timestamp is number of days since 2001-1-1.  Converted to
        # base 36, this gives us a 3 digit string until about 2121
        ts_b36 = int_to_base36(timestamp)

        # We limit the hash to 20 chars to keep URL short
        key_salt = "website.accounts.registration.tokens.SignupTokenGenerator"

        # Ensure results are consistent across DB backends
        email = email.lower()

        value = (six.text_type(email) + six.text_type(timestamp))
        hash = salted_hmac(key_salt, value).hexdigest()[::2]
        return "%s-%s" % (ts_b36, hash)

    def _num_days(self, dt):
        return (dt - date(2001, 1, 1)).days

    def _today(self):
        # Used for mocking in tests
        return date.today()


token_generator = SignupTokenGenerator()
