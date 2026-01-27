
import os

os.environ.setdefault(
    'SECRET_KEY', 'django-insecure-=h!m@t@bd9=kt6r)m&!bx2t=!sj7k%e&uo&s)gt6790dcnm+-gdcfxfgdffa')

# Set database URL for PostgreSQL
# Example format: 'postgresql://USER:PASSWORD@HOST:PORT/NAME'
os.environ.setdefault(
    "DATABASE_URL", "postgresql://neondb_owner:npg_Icr6fs9nGuOZ@ep-icy-sea-ag9a8dpf.c-2.eu-central-1.aws.neon.tech/jot_yummy_turf_427020")
# Set Cloudinary URL for media storage
# Example format: 'cloudinary://API_KEY:API_SECRET@CLOUD_NAME?secure=true'
# Replace with your actual Cloudinary credentials
os.environ.setdefault(
    "CLOUDINARY_URL", "cloudinary://272974694284733:j6lYm583o11AaAPckqjmPMgRoEQ@dz3tztxgb?secure=true")
