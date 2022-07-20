# from curses import wrapper
# from requests import request

from django.shortcuts import redirect

def id_required(func):
   

    def redirect_url():
        return redirect('index')

    def wrapper_func(request,*args,**kwargs):
        if 'userid' in request.COOKIES:
            return func(request,*args,**kwargs)
        else:
            return redirect_url()
    return wrapper_func

   
