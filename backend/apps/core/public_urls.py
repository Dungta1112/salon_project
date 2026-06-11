from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.core.public_views import PublicServiceViewSet, PublicStylistViewSet, PublicArticleViewSet, PublicPromotionViewSet


router = DefaultRouter()
router.register("services", PublicServiceViewSet, basename="public-services")
router.register("stylists", PublicStylistViewSet, basename="public-stylists")
router.register("articles", PublicArticleViewSet, basename="public-articles")
router.register("promotions", PublicPromotionViewSet, basename="public-promotions")


urlpatterns = [
    path("", include(router.urls)),
]
