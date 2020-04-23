from django.urls import include, path
from .views import home, CreateToken, TokenList, TokenDetail, UpdateToken

urlpatterns = [
    path('', home, name='home'),
    path('tokens/', TokenList.as_view(), name='token-list'),
    path('token/', TokenDetail.as_view(), name='token-detail'),
    path('tokens/create/', CreateToken.as_view(), name='create-token'),
    path('tokens/<pk>/update/', UpdateToken.as_view(), name='update-token'),
]
