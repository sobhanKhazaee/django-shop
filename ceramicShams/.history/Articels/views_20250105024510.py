from django.shortcuts import render
from .models import ArticelCategories, Aticel, ArticelComments
from django.views.generic import ListView, DetailView

# Create your views here.


class ArticelsListView(ListView):
    template_name = "articels_list.html"
    model = Aticel
    context_object_name = "articels"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ArticelCategories.objects.all()
        return context

    def get_queryset(self):
        query = super(ArticelsListView, self).get_queryset()
        query = query.filter(is_active=True)
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(category__url__iexact=category_name)
        return query


class ArticelDetailsView(DetailView):
    template_name = 'articel_details.html'
    model = Aticel
    context_object_name = "articel"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articel: Aticel = kwargs.get('object')
        context['comments'] = ArticelComments.objects.filter(
            article_id=articel.id, parent= None).prefetch_related('articelcomments_set')
        context['categories'] = ArticelCategories.objects.all()
        return context


@login_required
def submit_comment(request):
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        article_id = request.POST.get('article_id')  # فرض بر این است که شناسه مقاله در فرم ارسال می‌شود
        
        if comment_text:
            article = Aticel.objects.get(id=article_id)
            comment = ArticelComments(
                article=article,
                user=request.user,
                comment=comment_text
            )
            comment.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'نظر باید پر شود!'})
    return JsonResponse({'success': False, 'message': 'درخواست غیرمجاز'})