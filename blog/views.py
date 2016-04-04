from django.shortcuts import render

def post_list(require):
    return render(request, 'blog/post_list.html', {})
