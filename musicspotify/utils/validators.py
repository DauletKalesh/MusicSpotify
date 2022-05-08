import os
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .constants import (
    IMAGE_ALLOWED_FORMATS, MAX_IMAGE_SIZE,
    TRACK_ALLOWED_FORMATS, MAX_TRACK_SIZE    
)

def validate_image_size(value):
    if value.size <= MAX_IMAGE_SIZE:
        return value
    raise ValidationError('The maximum file size that can be uploaded is 10MB')

def validate_image_format(value):
    ext = os.path.splitext(value.name)[1]
    if ext.lower() not in IMAGE_ALLOWED_FORMATS:
        raise ValidationError('Unsupported file extension for image.')


def validate_track_size(value):
    if value.size > MAX_TRACK_SIZE:
        raise ValidationError('The maximum file size that can be uploaded is 15MB')
    return value

def validate_track_format(value):
    ext = os.path.splitext(value.name)[1]
    if ext.lower() not in TRACK_ALLOWED_FORMATS:
        raise ValidationError('Unsupported file extension for track.')

def validate_minimum_time(value):
    if value.hour > 0:
        raise serializers.ValidationError("Invalid time for track")
    minute = value.minute
    second = value.second
    if minute * 60 + second < 30:
        raise serializers.ValidationError("Track duration must not be less than half of minute")

def validate_maximum_time(value):
    minute = value.minute
    second = value.second
    if minute * 60 + second > 5*60:
        raise serializers.ValidationError("Track duration must not be greater than 5 minutes")
