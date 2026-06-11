from datetime import date, time, timedelta

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.accounts.roles import Roles
from apps.customers.models import CustomerProfile
from apps.employees.models import EmployeeProfile, StaffAvailability
from apps.promotions.models import Promotion, Voucher
from apps.services.models import Service


class Command(BaseCommand):
    help = "Seed rich, beautiful demo data for the salon backend."

    def handle(self, *args, **options):
        User = get_user_model()

        # 1. Create Managers and Receptionists
        manager, _ = User.objects.get_or_create(username="manager", defaults={"role": Roles.MANAGER, "full_name": "Nguyen Manager"})
        manager.set_password("Password123!")
        manager.save()
        EmployeeProfile.objects.get_or_create(user=manager, defaults={"role_type": Roles.MANAGER, "full_name": "Nguyen Manager", "phone": "0912345678"})

        receptionist, _ = User.objects.get_or_create(username="receptionist", defaults={"role": Roles.RECEPTIONIST, "full_name": "Tran Receptionist"})
        receptionist.set_password("Password123!")
        receptionist.save()
        EmployeeProfile.objects.get_or_create(user=receptionist, defaults={"role_type": Roles.RECEPTIONIST, "full_name": "Tran Receptionist", "phone": "0912345679"})

        # 2. Create Stylists (Staff)
        stylists_data = [
            {"username": "elena", "full_name": "Elena Nguyen", "specialties": "Hair Stylist, Color Expert", "phone": "0901234501"},
            {"username": "marcus", "full_name": "Marcus Tran", "specialties": "Senior Hair Stylist, Perming Specialist", "phone": "0901234502"},
            {"username": "sophie", "full_name": "Sophie Le", "specialties": "Nail Artist & Designer", "phone": "0901234503"},
            {"username": "chloe", "full_name": "Chloe Pham", "specialties": "Spa & Skincare Therapist", "phone": "0901234504"},
        ]

        stylist_profiles = []
        for item in stylists_data:
            user, _ = User.objects.get_or_create(username=item["username"], defaults={"role": Roles.STAFF, "full_name": item["full_name"], "phone": item["phone"]})
            user.set_password("Password123!")
            user.save()
            
            profile, _ = EmployeeProfile.objects.get_or_create(
                user=user, 
                defaults={
                    "role_type": Roles.STAFF, 
                    "full_name": item["full_name"],
                    "phone": item["phone"],
                    "specialties": item["specialties"],
                    "employment_status": "active"
                }
            )
            stylist_profiles.append(profile)

            # Seed availability for the next 14 days (9:00 - 17:00)
            for d_offset in range(14):
                slot_date = date.today() + timedelta(days=d_offset)
                if not StaffAvailability.objects.filter(employee=profile, date=slot_date).exists():
                    StaffAvailability.objects.create(
                        employee=profile,
                        date=slot_date,
                        start_time=time(9, 0),
                        end_time=time(17, 0),
                        availability_type="available"
                    )

        # 3. Create Customers
        customers_data = [
            {"username": "customer1", "full_name": "Customer One", "email": "customer1@gmail.com", "phone": "0987654321"},
            {"username": "dat", "full_name": "dat", "email": "dat0304@gmail.com", "phone": "0987654322"},
            {"username": "Dat", "full_name": "Dat", "email": "dat0304_upper@gmail.com", "phone": "0987654323"},
            {"username": "anmin", "full_name": "anmin", "email": "anmin@gmail.com", "phone": "0987654324"},
        ]

        for item in customers_data:
            user, _ = User.objects.get_or_create(username=item["username"], defaults={"role": Roles.CUSTOMER, "full_name": item["full_name"], "email": item["email"], "phone": item["phone"]})
            user.set_password("Password123!")
            user.save()
            CustomerProfile.objects.get_or_create(
                user=user, 
                defaults={
                    "full_name": item["full_name"], 
                    "email": item["email"],
                    "phone": item["phone"],
                    "status": "active"
                }
            )

        # 4. Create Rich Services
        services_list = [
            # Hair Category
            {"name": "Premium Haircut & Wash", "base_price": 250000, "duration_minutes": 45, "category": "Hair", "description": "High-end scissor cut including hair shampoo, styling and scalp relaxation massage."},
            {"name": "Luxury Hair Coloring", "base_price": 800000, "duration_minutes": 120, "category": "Hair", "description": "Premium hair coloring with organic imports for long-lasting color protection."},
            {"name": "Japanese Perm & Treatment", "base_price": 1200000, "duration_minutes": 150, "category": "Hair", "description": "Volumizing perm including keratin recovery treatment to preserve hair texture."},
            {"name": "Scalp Therapy & Wash", "base_price": 150000, "duration_minutes": 30, "category": "Hair", "description": "Deep hair wash with herbal extracts followed by therapeutic scalp conditioning."},
            # Nail Category
            {"name": "Premium Gel Manicure", "base_price": 180000, "duration_minutes": 60, "category": "Nail", "description": "Luxury gel polish including nail shaping, cuticle care and custom nail art styling."},
            {"name": "Gel Pedicure Care", "base_price": 200000, "duration_minutes": 60, "category": "Nail", "description": "Foot bath in rose petals, cuticle cleanup, scrub and long-lasting gel polish coating."},
            # Spa Category
            {"name": "Therapeutic Facial Spa", "base_price": 350000, "duration_minutes": 75, "category": "Spa", "description": "Deep skin cleaning, facial acupressure, biological essence injection and hydration mask."},
            {"name": "Aromatherapy Massage", "base_price": 500000, "duration_minutes": 90, "category": "Spa", "description": "Whole body massage with hot stones and premium natural essential oils for ultimate relaxation."},
        ]

        services_created = []
        for item in services_list:
            service, _ = Service.objects.get_or_create(
                name=item["name"],
                defaults={
                    "base_price": item["base_price"],
                    "duration_minutes": item["duration_minutes"],
                    "category": item["category"],
                    "description": item["description"],
                    "status": "active",
                    "active": True
                }
            )
            services_created.append(service)

        # 5. Create Vouchers & Promotions
        promo, _ = Promotion.objects.get_or_create(
            name="Grand Opening Promotion",
            defaults={
                "discount_type": "amount",
                "discount_value": 50000,
                "starts_at": timezone.now(),
                "ends_at": timezone.now() + timedelta(days=60),
            },
        )
        for s in services_created:
            promo.service_scope.add(s)

        Voucher.objects.get_or_create(
            code="WELCOME50",
            defaults={
                "promotion": promo,
                "discount_type": "amount",
                "discount_value": 50000,
                "starts_at": timezone.now(),
                "expires_at": timezone.now() + timedelta(days=60),
            },
        )

        Voucher.objects.get_or_create(
            code="SALON100",
            defaults={
                "promotion": promo,
                "discount_type": "amount",
                "discount_value": 100000,
                "starts_at": timezone.now(),
                "expires_at": timezone.now() + timedelta(days=60),
            },
        )

        self.stdout.write(self.style.SUCCESS("Demo database successfully populated with rich data!"))
