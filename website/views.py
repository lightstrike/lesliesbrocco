from mezzanine.core.views import direct_to_template

from mezzanine.pages.models import Page, RichTextPage
from mezzanine.forms.models import Form
from mezzanine.blog.models import BlogPost

def base(request):
    pages = Page.objects.all().order_by('content_model').reverse()
    content_pages = pages.filter(content_model='richtextpage')
    form_page = pages.get(content_model='form').form
    blog_posts = BlogPost.objects.all()

    # if request.method == 'POST':
    return direct_to_template(request, "index.html",{"pages":pages, "content_pages":content_pages, "form_page":form_page, "blog_posts":blog_posts})
    
    
