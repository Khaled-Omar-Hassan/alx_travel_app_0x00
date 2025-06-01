from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Listing(models.Model):
    """Represents a travel listing (hotel, apartment, etc)."""
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    """Represents a user's booking for a listing."""
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.user.username} booking {self.listing.title}"


class Review(models.Model):
    """User review for a listing."""
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.rating}/5 by {self.user.username}"
