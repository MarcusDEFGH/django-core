from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import PostModel
# Create your views here.


@login_required(login_url='/login')
def post_model_detail_view(request, id=None):
    
    # first way to do it
    # try:
    #     obj = PostModel.objects.get(id=id)
    # except:
    #     raise Http404

    # second way to do it
    # qs = PostModel.objects.filter(id=id)
    # obj = None
    # if not qs.exists() and qs.count() != 1:
    #     raise Http404
    # else:
    #     obj = qs.first()

    # third way in one line
    obj = get_object_or_404(PostModel, id=id)
    context = {
        "object": obj
    }
    template_path = 'blog/detail-view.html'
    return render(request, template_path, context)


@login_required(login_url='/login')
def post_model_list_view(request):
    qs = PostModel.objects.all()
    template_path = 'blog/list-view.html'
    context = {
        'queryset': qs
    }
    return render(request, template_path, context)
