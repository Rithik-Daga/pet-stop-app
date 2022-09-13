def userDirectoryPath(instance, filename):
    """
    This is a helper function used to provide the
    right path to store the user images.
    """
    upload_path = f"{instance.user.username}/profile/{filename}"
    return upload_path


def petDirectoryPath(instance, filename):
    """
    This is a helper function used to provide the
    right path to store the user images.
    """
    upload_path = (
        f"{instance.user_profile.user.username}/{instance.username}/{filename}"
    )
    return upload_path


def postDirectoryPath(instance, filename):
    """
    This is a helper function used to provide the
    right path to store the pet profile post.
    """
    upload_path = f"{instance.pet_profile.user_profile.user.username}/{instance.pet_profile.username}/posts/{filename}"
    return upload_path
