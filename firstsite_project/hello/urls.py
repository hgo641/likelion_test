
from django.urls import path
import hello.views

urlpatterns = [
    path('', hello.views.home, name='home'),
    path('new', hello.views.postnew, name='postnew'),
    path('create', hello.views.postcreate, name='postcreate'),
    path('detail/<int:post_id>',hello.views.detail,name="detail"),
    path('edit/<int:post_id>',hello.views.postedit,name="postedit"),
    path('postupdate/<int:post_id>',hello.views.postupdate,name="postupdate"),
    path('postdelete/<int:post_id>',hello.views.postdelete,name="postdelete"),
    path('commentcreate/<int:post_id>', hello.views.commentcreate, name='commentcreate')
]
