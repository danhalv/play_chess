from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from apps.chessgames.views import ChessGameViewSet


chessgame_list = ChessGameViewSet.as_view({
    'get': 'list'
})
chessgame_detail = ChessGameViewSet.as_view({
    'get': 'retrieve'
})
chessgame_move = ChessGameViewSet.as_view({
    'post': 'move'
})

urlpatterns = format_suffix_patterns([
    path('chessgames/', chessgame_list),
    path('chessgames/<int:pk>/', chessgame_detail),
    path('chessgames/<int:pk>/move/<str:from_square>/<str:to_square>/', chessgame_move),
])