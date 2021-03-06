from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room


@login_required
def index(request):
    """
    Root page view. This is essentially a single-page app, if you ignore the
    login and admin parts.
    """
    # Get a list of rooms, ordered alphabetically

    # Render that in the index template
    return render(request, "chat.html", {})
