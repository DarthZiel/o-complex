from django.contrib.auth import login, get_user_model

User = get_user_model()


def register_user(email, password1, password2):
    if password1 != password2:
        return None

    if User.objects.filter(email=email).exists():
        return None

    user = User.objects.create_user(email=email, password=password1)
    return user