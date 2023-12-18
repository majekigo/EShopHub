from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Category, Tag


class Command(BaseCommand):

    def handle(self, *args, **options):
        seller_group, _ = Group.objects.get_or_create(name='Продавец')
        admin_group, _ = Group.objects.get_or_create(name='Админ')
        buyer_group, _ = Group.objects.get_or_create(name='Покупатель')

        product_content_type = ContentType.objects.get_for_model(Product)
        category_content_type = ContentType.objects.get_for_model(Category)
        tag_content_type = ContentType.objects.get_for_model(Tag)

        seller_permissions = Permission.objects.filter(content_type=product_content_type)
        admin_permissions = Permission.objects.filter(
            content_type__in=[product_content_type, category_content_type, tag_content_type]
        )

        seller_users = []
        for i in range(3):
            seller_user = User.objects.create_user(f'seller{i+1}', f'seller{i+1}@example.com', f'seller{i+1}')
            seller_user.groups.add(seller_group)
            seller_user.user_permissions.set(seller_permissions)
            seller_users.append(seller_user)

        admin_users = []
        for i in range(2):
            admin_user = User.objects.create_user(f'admin{i+1}', f'admin{i+1}@example.com', f'admin{i+1}')
            admin_user.groups.add(admin_group)
            admin_user.user_permissions.set(admin_permissions)
            admin_users.append(admin_user)

        buyer_users = []
        for i in range(4):
            buyer_user = User.objects.create_user(f'buyer{i+1}', f'buyer{i+1}@example.com', f'buy{i+1}')
            buyer_user.groups.add(buyer_group)
            buyer_users.append(buyer_user)

        self.stdout.write(self.style.SUCCESS('Работает'))

