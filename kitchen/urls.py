from django.urls import path
from kitchen.views import (
       index,
       DishTypeListView,
       DishTypeCreateView,
       DishTypeUpdateView,
       DishTypeDeleteView,
       DishListView,
       DishDetailView,
       DishCreateView,
       DishUpdateView,
       DishAssignmentView,
       DishDeleteView,
       CookListView,
       CookDetailView,
       CookCreateView,
       CookDeleteView
)

urlpatterns = [
       path("", index, name="index"),
       path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
       path("dish-types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
       path("dish-types/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-type-update"),
       path("dish-types/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-type-delete"),
       path("dishes/", DishListView.as_view(), name="dish-list"),
       path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
       path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
       path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
       path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
       path(
              "dishes/<int:pk>/dish-assignment/",
              DishAssignmentView.as_view(),
              name="dish-assignment"),
       path("cooks/", CookListView.as_view(), name="cook-list"),
       path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
       path("cooks/create", CookCreateView.as_view(), name="cook-create"),
       path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),
]

app_name = "kitchen"
