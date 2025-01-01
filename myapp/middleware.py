from django.shortcuts import HttpResponse,HttpResponseRedirect
from django.urls import resolve
from django.utils.deprecation import MiddlewareMixin
from .models import View,Post
from django.utils.timezone import now

def CheckUserActivityDateMiddleware(get_response):
    def wrapper(request):
        if request.user.is_authenticated:
            last_activity = request.session.get('last_activity')
            current_time = now().timestamp()
            if last_activity and current_time - last_activity > 604800:
                request.session.flush()
                return HttpResponseRedirect('/signin')
            request.session['last_activity'] = current_time
        response = get_response(request)
        return response
    return wrapper

class PageViewMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        page_name = request.path
        ip = request.META.get('REMOTE_ADDR')

        if not page_name.startswith('/admin'):
            try:
                match = resolve(request.path)
                if match.url_name == 'post': 
                    post_id = match.kwargs.get('id')

                    post = Post.objects.get(id=post_id)
                    
                    page, created = View.objects.get_or_create(client_ip=ip, path=page_name, post=post)
                    
                    if created:
                        page.view=1
                        page.save()
            except Post.DoesNotExist:
                return HttpResponse("This Post Does not Exist!")
            except Exception as e:
                return HttpResponse(f"An error occurred: {str(e)}")
        return None