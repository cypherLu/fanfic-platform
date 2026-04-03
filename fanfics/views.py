from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Fanfic, Chapter, Bookmark, Profile, Tag, Fandom, Category, Follow, Block, Like
from .forms import fanficForm, ChapterForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count


def kilig(request):
    search = request.GET.get('search')
    tag = request.GET.get('tag')
    fandom = request.GET.get('fandom')
    category = request.GET.get('category')
    order = request.GET.get('order')  # popular ou recent

    fanfics = Fanfic.objects.all()

    # 🔎 Busca por texto
    if search:
        fanfics = fanfics.filter(title__icontains=search)

    # Filter
    if tag:
        fanfics = fanfics.filter(tags__name__icontains=tag)

    if fandom:
        fanfics = fanfics.filter(fandoms__name__icontains=fandom)

    if category:
        fanfics = fanfics.filter(categories__name__icontains=category)

    #  Order
    if order == "popular":
        fanfics = fanfics.annotate(
            likes_count= Count("like")
        ).order_by("-likes_count")

    elif order == "recent":
        fanfics = fanfics.order_by("-created_at")

    #  Paginator
    paginator = Paginator(fanfics, 6)
    page = request.GET.get('page')
    fanfics = paginator.get_page(page)

    return render(request, 'kilig.html', {
        'fanfics': fanfics,
        'all_tags': Tag.objects.all(),
        'all_fandoms': Fandom.objects.all(),
        'all_categories': Category.objects.all(),
    })




def fanficView(request, id):
    fanfic_obj = get_object_or_404(
    Fanfic.objects.prefetch_related('chapters'),
    pk=id, is_public=True
)
    fanfic_chapters = fanfic_obj.chapters.order_by('order')
    return render(request, 'fanfic.html', {'fanfic': fanfic_obj,'fanfic_chapters':fanfic_chapters})


@login_required
def newFanfic(request):
    if request.method == 'POST':
        form = fanficForm(request.POST)
        if form.is_valid():
            fanfic = form.save(commit=False) 
            fanfic.author = request.user      
            fanfic.save()
            form.save_m2m()
            return redirect('fanfic-view', id=fanfic.id)
    else:
        form = fanficForm()

    return render(request, 'addfanfic.html', {'form': form})

@login_required
def editfanfic(request, id):
    fanfic = get_object_or_404(
    Fanfic.objects.prefetch_related('chapters'),
    pk=id
)
    if fanfic.author != request.user:
        return redirect('/')
    form = fanficForm(instance=fanfic)
    if (request.method == 'POST'):
        form = fanficForm(request.POST, instance=fanfic)
        if(form.is_valid()):
            form.save()
            return redirect('/')
        else:
                return render(request, 'editfanfic.html', {'form': form, 'fanfic': fanfic})
    else:
     return render(request, 'editfanfic.html', {'form': form, 'fanfic': fanfic})

@login_required
def deletefanfic(request, id):
    fanfic = get_object_or_404(Fanfic, pk=id)
    if fanfic.author != request.user:
        return redirect('/')
    fanfic.delete()
    messages.info(request, 'fanfic deleted successfully!')
    return redirect('/')

@login_required
def newchapter(request, id):

    fanfic = get_object_or_404(Fanfic, pk=id)
    if fanfic.author != request.user:
        return redirect('/')

    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            Chapter = form.save(commit=False)
            Chapter.fanfic = fanfic

            last_chapter = fanfic.chapters.order_by('-order').first()

            if last_chapter:
                Chapter.order = last_chapter.order + 1
            else:
                Chapter.order = 1

            Chapter.save()
            return redirect('fanfic-view', id=id)

    else:
        form = ChapterForm()

    return render(request, 'addchapter.html', {'form': form, 'fanfic': fanfic})

def read_chapter(request, fanfic_id, chapter_order):
    fanfic_obj = get_object_or_404(Fanfic, id=fanfic_id)

    chapter = get_object_or_404(
        Chapter,
        fanfic=fanfic_obj,
        order=chapter_order
    )

    # capítulo anterior
    prev_chapter = Chapter.objects.filter(
        fanfic=fanfic_obj,
        order__lt=chapter.order
    ).order_by('-order').first()

    # próximo capítulo
    next_chapter = Chapter.objects.filter(
        fanfic=fanfic_obj,
        order__gt=chapter.order
    ).order_by('order').first()

    return render(request, 'chapter.html', {
        'fanfic': fanfic_obj,
        'chapter': chapter,
        'prev_chapter': prev_chapter,
        'next_chapter': next_chapter
    })

@login_required
def dashboard(request):
    profile = request.user.profile

    form = ProfileForm(instance=profile)

    return render(request, 'dashboard.html', {
        'form': form,
        'fanfics': request.user.fanfics.all()
    })

@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'editprofile.html', {'form': form})


def profile_view(request, username):
    user_profile = get_object_or_404(User, username=username)
    fanfics = user_profile.fanfics.all()

    profile = Profile.objects.get(user=user_profile)

    return render(request, 'profile.html', {
        'profile_user': user_profile,
        'fanfics': fanfics,
        'profile': profile
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


@login_required
def toggle_follow(request, username):
    target = User.objects.get(username=username)

    #  verifica bloqueio
    if Block.objects.filter(blocker=target, blocked=request.user).exists():
        return redirect('/')

    follow, created = Follow.objects.get_or_create(
        follower=request.user,
        following=target
    )

    if not created:
        follow.delete()

    return redirect('profile', username=username)

@login_required
def toggle_like(request, id):
    f = Fanfic.objects.get(id=id)
    like, created = Like.objects.get_or_create(user=request.user, fanfic=f)

    if not created:
        like.delete()

    return redirect('fanfic-view', id=id)

@login_required
def toggle_bookmark(request, id):
    fanfic_obj = get_object_or_404(Fanfic, id=id)

    bookmark, created = Bookmark.objects.get_or_create(
        user=request.user,
        fanfic=fanfic_obj
    )

    if not created:
        bookmark.delete()

    return redirect('fanfic-view', id=fanfic_obj.id)