from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .forms import PostModelForm
from django.shortcuts import redirect
from .models import PostModel
# Create your views here.


@login_required(login_url='/admin/login')
def post_model_create_view(request):

    # if request.method == 'post':
    #     # print(request.POST)
    #     form = PostModelForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit=False)
    #         print(form.cleaned_data)


    form = PostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "Created a new blog post!")
        return redirect("/blog/{id}/".format(id=obj.id))

    context = {
        "form": form
        }
    template = "blog/create-view.html"
    return render(request, template, context)


@login_required(login_url='/admin/login')
def post_model_update_view(request, id):

    # if request.method == 'post':
    #     # print(request.POST)
    #     form = PostModelForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit=False)
    #         print(form.cleaned_data)

    obj = get_object_or_404(PostModel, pk=id)
    form = PostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "Updated {}".format(obj.title))
        return redirect("/blog/".format(id=obj.id))

    context = {
        "form": form
        }
    template = "blog/update-view.html"
    return render(request, template, context)


@login_required(login_url='/admin/login')
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


@login_required(login_url='/admin/login')
def post_model_delete_view(request, id=None): 
    obj = get_object_or_404(PostModel, id=id)
    title = obj.title
    if request.method == 'POST':
        obj.delete()
        messages.success(request, "Deleted post.")
        return redirect("/blog/")
    context = {
        "object": obj
    }
    template_path = 'blog/delete-view.html'
    return render(request, template_path, context)


@login_required(login_url='/admin/login')
def post_model_list_view(request):
    qs = PostModel.objects.all()
    template_path = 'blog/list-view.html'
    context = {
        'queryset': qs
    }
    return render(request, template_path, context)
