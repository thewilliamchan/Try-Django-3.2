from django.utils.text import slugify

def slugify_instance_title(instance, save=False):
    slug = f"{slugify(instance.title)}-{instance.id}"
    # qs = Article.objects.filter(slug=slug).exclude(id=instance.id)
    # if qs.exists():
    #     slug = f"{slug}-{qs.count() + 1}"
    Klass = instance.__class__
    instance.slug = slug
    if save:
        instance.save()
    return instance