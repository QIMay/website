from django.shortcuts import render
from django.shortcuts import redirect
from block.models import Block
from .models import Article
from .forms import ArticleForm
from django.core.paginator import Paginator


def article_list(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)

    all_articles = Article.objects.filter(block=block, article_status=0).order_by("-id")
    ARTICLE_CNT_1PAGE = 2
    p = Paginator(all_articles, ARTICLE_CNT_1PAGE)
    page_no = int(request.GET.get("page_no", "1"))
    page = p.page(page_no)
    articles_objs = page.object_list

    page_links = [i
                  for i in range(page_no - 2, page_no + 3) if i > 0 and i <= p.num_pages]

    return render(request, "article_list.html",
                  {"articles": articles_objs, "b": block, "page_no": page_no, "page": page,
                   "page_links": page_links, "p": p})


def article_create(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    if request.method == "GET":
        return render(request, "article_create.html", {"b": block})
    else:
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.block = block
            article.article_status = 0
            article.save()
            return redirect("/article/list/%s" % block_id)
        else:
            return render(request, "article_create.html", {"b": block, "form": form})


def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, "article_detail.html", {"article": article})
