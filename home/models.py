import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django import forms


# from django.dispatch import receiver

# from home.emails import send_account_activation_email



# Create your models here.
  
    
# class UserProfile(models.Model):
#     name = models.CharField(max_length=100)
#     username = models.CharField(max_length=20)
#     dob = models.DateField()
#     gender = models.CharField(max_length=20)
#     phone = models.CharField(max_length=20)
#     emergency_phone = models.CharField(max_length=20)
#     email = models.EmailField()
#     address = models.CharField(max_length=200)
#     blood_group = models.CharField(max_length=10, default='Unknown')
#     area_of_interest = models.TextField()
#     time_volunteering = models.CharField(max_length=100)
#     locations_volunteering = models.CharField(max_length=200)
#     notification_mode = models.CharField(max_length=20)
#     comments = models.TextField()
#     password = models.CharField(max_length=20)
    
    
class UserProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=20)
    dob = models.DateField()
    gender = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    emergency_phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    blood_group = models.CharField(max_length=10, default='Unknown')
    area_of_interest = models.TextField(null=True)
    time_volunteering = models.CharField(max_length=100)
    locations_volunteering = models.CharField(max_length=200)
    notification_mode = models.CharField(max_length=20)
    comments = models.TextField(null=True)
    def __str__(self):
        # return self.name
        return f"{self.first_name} {self.last_name}"
    
    #Events Model
    
class Event(models.Model):
    e_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=200)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_location = models.CharField(max_length=200)

    def __str__(self):
         return f"{self.e_id} - {self.event_name}"
    
# class EnrolledVolunteer(models.Model):
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)


#     def __str__(self):
#         return f"{self.volunteer.username} enrolled in {self.event.event_name}"
    
    
class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    date = models.DateField()
    body = models.TextField()
    author = models.CharField(max_length=255)

    
    def __str__(self):
        return self.title    
    
class Enrollment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, null=True)
    is_present = models.BooleanField(default=False)
    # Add other fields as per your requirements

    def __str__(self):
        return f"Enrollment for {self.event.e_id}-{self.event.event_name} by {self.user.username}"
    
    
    
    
    
    
    
    
    #Email Verification
    
# @receiver(post_save , sender = User)

# def  send_email_token(sender , instance , created , **kwargs):
#     try:
#         if created:
#             email_token = str(uuid.uuid4())
#             Profile.objects.create(user = instance , email_token = email_token)
#             email = instance.email
#             send_account_activation_email(email , email_token)

#     except Exception as e:
#         print(e)



        
        
# class Profile(forms.BaseModelForm):
#     user = models.OneToOneField(User , on_delete=models.CASCADE , related_name="profile")
#     is_email_verified = models.BooleanField(default=False)
#     email_token = models.CharField(max_length=100 , null=True , blank=True)
#     profile_image = models.ImageField(upload_to = 'profile')


    
    