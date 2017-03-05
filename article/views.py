from django.shortcuts import render
from django.shortcuts import redirect
from block.models import Block
from .models import Article
from .forms import ArticleForm


def article_list(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    articles_objs = Article.objects.filter(block=block, article_status=0).order_by("-id")

    return render(request, "article_list.html", {"articles": articles_objs, "b": block})


def article_create(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = Article(block=block, article_title=form.cleaned_data["title"],
                          article_content=form.cleaned_data["content"], article_status=0)
        article.save()
        return redirect("/article/list/%s" % block_id)
    else:
        return render(request, "article_create.html", {"b": block, "form": form})
