from .models import CustomUser
import django_filters


class UserFilter(django_filters.FilterSet):
    home = django_filters.CharFilter(field_name="home__name")
    order = django_filters.OrderingFilter(
        fields=(
            ('created_at', 'created_at'),
            ('name', 'name'),
            ('status', 'status'),
            ('date_of_birth','date_of_birth')
        )
    )
    class Meta:
        model = CustomUser
        fields = ["status", "name", "surname", "email", "document", "date_of_birth", "created_at"]
        #These are exact lookups
