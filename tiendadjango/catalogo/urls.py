from django.urls import path

from . import views

app_name = "catalogo"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("detail/<int:prod_id>/", views.detail, name="detail"),
    path("process/ajax/comentario/", views.insert_comment, name="comentar"),
]