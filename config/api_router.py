from django.conf import settings
from django.urls import include, path

from server.cloth.api.views import ClothViewSet
from server.member.api.views import MemberViewset, UserMemberMatchingViewset
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("cloth", ClothViewSet, basename="cloth")
router.register("member", MemberViewset, basename="member")
router.register("matching", UserMemberMatchingViewset, basename="matching")

app_name = "api"
urlpatterns = router.urls
