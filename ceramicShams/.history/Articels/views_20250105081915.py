from django.shortcuts import render
from .models import ArticelCategories, Aticel, ArticelComments
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from utils.helpers import show_jalali_date
from django.template.loader 
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
            article_id=articel.id, parent=None).order_by('-created_at').prefetch_related('articelcomments_set')
        context['categories'] = ArticelCategories.objects.all()
        return context


@login_required
def submit_comment(request):
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        article_id = request.POST.get('article_id')
        parent_id = request.POST.get("parent_id")
        # print(request)
        if article_id:
            try:
                article = Aticel.objects.get(id=article_id)
            except Aticel.DoesNotExist:
                return JsonResponse({'success': False, 'message': 'مقاله یافت نشد.'})

            if comment_text:
                comment = ArticelComments(
                    article=article,
                    user=request.user,
                    parent = parent_id,
                    comment=comment_text
                )
                comment.save()
                # ارسال داده‌های نظر به صورت JSON برای رندر در صفحه
                # return JsonResponse({
                #     'success': True,
                #     'comment': {
                #         'created_at': show_jalali_date(comment.created_at),
                #         'parent_id': comment.parent,
                #         'user': comment.user.username,  # نام کاربر
                #         'comment': comment.comment  # متن نظر
                #     }
                # })
                
                context = {
                    'comment': comment,
                    'show_jalali_date': True,  # اگر فیلتر خاصی دارید، از اینجا استفاده کنید
                }
                html = render_to_string('comment.html', context)

                return JsonResponse({
                    'success': True,
                    'html': html,
                    'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M:%S')  # بازگشت زمان ایجاد
                })
                
                
            else:
                return JsonResponse({'success': False, 'message': 'نظر باید پر شود!'})
        else:
            return JsonResponse({'success': False, 'message': 'آیدی مقاله ارسال نشده است.'})

    return JsonResponse({'success': False, 'message': 'درخواست غیرمجاز'})
