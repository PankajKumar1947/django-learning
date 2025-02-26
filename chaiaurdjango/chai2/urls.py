from django.urls import path

from . import views

# localhost: 8000/chai2
urlpatterns = [ 
    path('', views.allChai, name="all_chai"), # Home route
    path('<int:chai_id>', views.chaiDetail, name="chai_detail"),
]
