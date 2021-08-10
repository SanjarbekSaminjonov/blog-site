from django.http import request
from accounts.models import CustomUser
from accounts.forms import CustomUserChangeForm
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Post
from .const import Const
from .forms import PostForm

# Create your views here.


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['regions'] = dict(Const.regions)
        context['categories'] = dict(Const.categories)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(BlogListView, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-id")
        return qs


class BlogDetailView(DetailView):
    model = Post
    template_name = 'detail.html'


def BlogCreateView(request):
    error = ""
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = CustomUser.objects.get(id=request.user.id)
            form.save()
            return redirect('home')
        else:
            error = "Forma to'ldirishda xatolik!"

    form = PostForm()
    context = {
        "form": form,
        "error": error
    }
    return render(request, 'create_post.html', context)


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')


class BlogEditView(UpdateView):
    model = Post
    template_name = 'edit.html'
    fields = ['title', 'body', 'image', 'region', 'category']


def BlogRegionListView(request, pk):
    region = dict(Const.regions)[pk]
    object_list = Post.objects.filter(region=pk)[::-1]
    context = {
        'object_list': object_list,
        'region': region
    }
    return render(request, 'region_filter.html', context)


def BlogCategoryListView(request, pk):
    category = dict(Const.categories)[pk]
    object_list = Post.objects.filter(category=pk)[::-1]
    context = {
        'object_list': object_list,
        'category': category
    }
    return render(request, 'category_filter.html', context)


def profile(request):
    skills = Post.objects.filter(author__username=request.user)[::-1]
    return render(request, "profile.html", {"skills": skills})


def BlogEditUserView(request):
    error = ""
    if request.method == "POST":
        form = CustomUserChangeForm(
            request.POST, instance=CustomUser.objects.get(id=request.user.id))
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            error = "Forma to'ldirishda xatolik!"

    form = CustomUserChangeForm(
        instance=CustomUser.objects.get(id=request.user.id))
    context = {
        "form": form,
        "error": error
    }
    return render(request, 'edit_profile.html', context)
