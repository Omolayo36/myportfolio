from django.contrib.auth import logout


class AutoTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            last_activity = requst.session.get('last_activity')
            if last_activity:
                idle_time = timezone.now() - last_activity
                if idle_time.seconds > settings.AUTO_LOGOUT_DELAY:
                    logout(request)
                    del request.session['last_activity']
                    request.session['last_activity'] = timezone.now()
        return response