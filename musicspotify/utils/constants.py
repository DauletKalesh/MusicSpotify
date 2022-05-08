
GENDER_LIST = [
    (True,  'Male'),
    (False, 'Female'),
    (None, 'Not selected')
]

CATEGORY_LIST = [
    (0, 'At home'),
    (1, 'Gaming'),
    (2, 'Workout'),
    (3, 'Party'),
    (4, 'Kids&Family')
]

# IMAGE VALIDATION VALUES
IMAGE_ALLOWED_FORMATS = ('.png', '.jpg' ,' .jpeg' , '.jfif')
MAX_IMAGE_SIZE = 10485760

#DOCUMENT VALIDATION VALUESS
TRACK_ALLOWED_FORMATS = ('.mp3', '.mp4', '.mpeg', '.wav', '.wma')
MAX_TRACK_SIZE = MAX_IMAGE_SIZE*10 # 15MB LIMIT