from rest_framework.authentication import TokenAuthentication


class CustomBearerTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'

    def authenticate_credentials(self, key):
        return super().authenticate_credentials(self.keyword + ' ' + key)