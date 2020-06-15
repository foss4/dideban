from django.db import models
from django.utils.translation import gettext_lazy as _

__all__ = ['TimestampedModelMixin', 'ActivatedModelMixin']


class TimestampedModelMixin(models.Model):
    """Timestamp mixin
    This mixin adds a timestamp to model for create and update events
    """

    created = models.DateTimeField(
        _("created at"),
        auto_now_add=True,
        help_text=_("This is the timestamp of the object creation."),
    )
    updated = models.DateTimeField(
        _("updated at"),
        auto_now=True,
        help_text=_("This is the timestamp of the object update"),
    )

    class Meta:
        ordering = ["-created"]
        abstract = True


class ActivatedModelManager(models.Manager):
    def actives(self):
        return self.get_queryset().filter(is_active=True)


class ActivatedModelMixin(models.Model):
    """Active objects mixin
    This mixin add a is_active field to the model
    which indicated the model active status.
    It also adds a queryset to support
    getting only active objects.
    """

    is_active = models.BooleanField(
        verbose_name=_("active"),
        default=True,
        db_index=True,
        help_text=_(
            "Designates if this object should be considered active or not "
            "or to simulate soft delete behaviour."
        ),
    )

    objects = ActivatedModelManager()

    class Meta:
        abstract = True
