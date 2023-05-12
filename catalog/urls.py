from django.contrib.auth.views import LogoutView
from django.urls import path

from catalog.views import (
    index,
    LoginView,
    SignUpView,
    TaskListView,
    TaskDetailView,
    update_task_status,
    TaskCreateView,
    TaskDeleteView,
    ProfileView,
)

urlpatterns = [
    path("", index, name="index"),
    path("registrate/", SignUpView.as_view(), name="registrate"),
    path("login/", LoginView.as_view(), name="login"),
    path(
        "logout/",
        LogoutView.as_view(next_page="catalog:index"),
        name="logout"
    ),
    path(
        "task/",
        TaskListView.as_view(),
        name="task_url_list"
    ),
    path(
        "task/create/",
        TaskCreateView.as_view(),
        name="task_url_create"
    ),
    path(
        "task/<int:pk>/update_status/",
        update_task_status,
        name="update_task_status"
    ),
    path(
        "task/<int:pk>/",
        TaskDetailView.as_view(),
        name="task_url_detail"
    ),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task_url_delete"
    ),
    path(
        "profile/<int:pk>/",
        ProfileView.as_view(),
        name="profile_url_detail"
    ),
]

app_name = "catalog"
