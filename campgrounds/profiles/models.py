from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):

    full_name = property(AbstractUser.get_full_name)

    def gravatar(self, size=80):
        import urllib, hashlib
        return "http://www.gravatar.com/avatar/%(hash)s?%(parameters)s" % {
            'hash': hashlib.md5(self.email.lower()).hexdigest(),
            'parameters': urllib.urlencode({'s':str(size)})
        }
