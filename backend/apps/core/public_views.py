from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.services.models import Service
from apps.services.serializers import ServiceSerializer
from apps.employees.models import EmployeeProfile
from apps.employees.serializers import EmployeeProfileSerializer
from apps.promotions.models import Promotion
from apps.promotions.serializers import PromotionSerializer


class PublicPromotionViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = PromotionSerializer
    queryset = Promotion.objects.filter(active=True).order_by("-starts_at")



class PublicServiceViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ServiceSerializer
    queryset = Service.objects.filter(active=True, status="active").order_by("name")


class PublicStylistViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = EmployeeProfileSerializer
    queryset = EmployeeProfile.objects.filter(employment_status="active", role_type="staff").order_by("full_name")


class PublicArticleViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        articles = [
            {
                "id": 1,
                "title": "5 Essential Hair Care Tips for Hot Summer Days",
                "summary": "Keep your hair hydrated, shiny, and fully protected from intense UV rays with these expert-approved summer salon tips.",
                "content": "Summertime brings sun, beach days, and unfortunately, dry, brittle hair. The combination of intense UV rays, chlorine from pools, and salt water can strip hair of its natural moisture and fade color treatments. To keep your locks healthy and vibrant, we recommend deep conditioning treatments twice a week, using heat-protecting sprays, and washing with mineral-free water.",
                "author": "Elena Nguyen",
                "published_at": "2026-06-01",
                "image_url": "https://images.unsplash.com/photo-1562322140-8baeececf3df?auto=format&fit=crop&q=80&w=600",
                "category": "Hair Care",
                "read_time": "3 min read"
            },
            {
                "id": 2,
                "title": "Choosing the Perfect Hair Color for Your Skin Tone",
                "summary": "Struggling to find the right color palette? Consult our gold guidelines to match shades to warm or cool skin tones.",
                "content": "Finding the perfect hair color starts with understanding your skin's undertones. If you have cool undertones, shades like platinum, ash blonde, or cool brown look spectacular. For warm skin tones, golden blondes, rich coppers, and warm chestnut browns create a natural, sun-kissed glow. Our coloring experts specialize in bespoke coloring techniques to bring out your best look.",
                "author": "Elena Nguyen",
                "published_at": "2026-05-15",
                "image_url": "https://images.unsplash.com/photo-1605497746445-97d1b0a9eaf4?auto=format&fit=crop&q=80&w=600",
                "category": "Styling",
                "read_time": "5 min read"
            },
            {
                "id": 3,
                "title": "Understanding Modern Perm and Treatment Techniques",
                "summary": "From soft waves to bouncy digital perms, discover which structure fits your hair texture and structure.",
                "content": "The perm has evolved. Modern techniques like digital perms and cold waves offer soft, natural-looking curls without damaging the hair shaft. Before scheduling a perm, it is crucial to assess your hair structure. If your hair is heavily bleached, a restorative keratin treatment is recommended prior to perming. Our experts use low-chemical perm formulas to protect and style your hair.",
                "author": "Marcus Tran",
                "published_at": "2026-05-10",
                "image_url": "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?auto=format&fit=crop&q=80&w=600",
                "category": "Treatments",
                "read_time": "4 min read"
            }
        ]
        return Response({"results": articles, "count": len(articles)})
