from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .forms import *
from django.views.generic import CreateView, ListView, DetailView, FormView
from django.views.generic.base import TemplateView
from .models import *
from .utils import DataMixin


class HomePageView(TemplateView):
    template_name = 'blog_app/home.html'


class AboutPageView(TemplateView):
    template_name = 'blog_app/about.html'


class BlogPageView(DataMixin, ListView):
    model = BlogPosts
    template_name = 'blog_app/blog.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(**kwargs)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return BlogPosts.objects.filter(is_published=True)


class CategoryListView(DataMixin, ListView):
    model = BlogPosts
    template_name = 'blog_app/blog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPosts.objects.filter(
            category__slug=self.kwargs['category_slug'],
            is_published=True
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            category_selected=context['posts'][0].category_id
        )

        return dict(list(context.items()) + list(c_def.items()))


class PostPageView(DetailView):
    model = BlogPosts
    template_name = 'blog_app/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'current_post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(posts=self.get_object()).order_by('-time_create')
        context['comments'] = comments

        if self.request.user.is_authenticated:
            context['form'] = CommentForm(instance=self.request.user)

        return context

    def post(self, request, *args, **kwargs):
        new_comment = Comment(
            comment_message=request.POST.get('comment_message'),
            author=self.request.user,
            posts=self.get_object()
        )
        new_comment.save()
        return self.get(self, request, *args, **kwargs)


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'blog_app/contact.html'
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('blog')


class SignupFormView(CreateView):
    form_class = SignupForms
    template_name = 'blog_app/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('blog')


class LoginFormView(LoginView):
    form_class = LoginForms
    template_name = 'blog_app/login.html'

    def get_success_url(self):
        return reverse_lazy('blog')


def logout_user(request):
    logout(request)
    return redirect('login')

