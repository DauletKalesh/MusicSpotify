def profile_image_upload(instance, filename):
    return f"user/{instance.user.id}/{filename}"

def track_document_path(instance, filename):
    return f"track/{instance.id}_{filename}"