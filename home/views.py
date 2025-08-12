from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.db.models import Q
from .models import Task

def index(request):
    q = (request.GET.get("q") or "").strip()
    show = request.GET.get("show", "all")
    tasks = Task.objects.all()
    if q:
        tasks = tasks.filter(Q(title__icontains=q) | Q(notes__icontains=q))
    if show == "open":
        tasks = tasks.filter(done=False)
    elif show == "done":
        tasks = tasks.filter(done=True)
    counts = {
        "all": Task.objects.count(),
        "open": Task.objects.filter(done=False).count(),
        "done": Task.objects.filter(done=True).count(),
    }
    context = {"tasks": tasks, "q": q, "show": show, "counts": counts}
    return render(request, "index.html", context)

@require_POST
def add(request):
    title = (request.POST.get("title") or "").strip()
    notes = (request.POST.get("notes") or "").strip()
    if title:
        Task.objects.create(title=title, notes=notes)
    return redirect("index")

@require_POST
def toggle(request, task_id: int):
    t = get_object_or_404(Task, pk=task_id)
    t.done = not t.done
    t.completed_at = timezone.now() if t.done else None
    t.save(update_fields=["done", "completed_at"])
    return redirect("index")

@require_POST
def delete(request, task_id: int):
    t = get_object_or_404(Task, pk=task_id)
    t.delete()
    return redirect("index")