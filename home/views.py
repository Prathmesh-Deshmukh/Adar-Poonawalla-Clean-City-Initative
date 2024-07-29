

import datetime
from django.contrib import admin
from django.db import models
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from home.models import Enrollment, UserProfile, Event, Blog
from django.utils import timezone
#from datetime import datetime
from django.contrib.auth.decorators import login_required
from random import sample
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail,EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.db import IntegrityError





# Create your views here.
def index(request):
    context = {     }
    return render(request, 'index.html')
    #return HttpResponse("this is home page")
    
def about(request):
    context = {     }
    return render(request, 'about.html')

def admin_login(request):
    context = {     }
    return render(request, 'admin_login.html')

def base(request):
    context = {     }
    return render(request, 'base.html')

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})

def change_password(request):
    context = {     }
    return render(request, 'change_password.html')

def contact(request):
    context = {     }
    return render(request, 'contact.html')

def forget_password(request):
    context = {     }
    return render(request, 'forget_password.html')

def gallery(request):
    context = {     }
    return render(request, 'gallery.html')

def home(request):
    context = {     }
    return render(request, 'home.html')

def login(request):
    context = {     }
    return render(request, 'login.html')

def register_2(request):
    context = {     }
    return render(request, 'register_2.html')

def reset_password(request):
    context = {     }
    return render(request, 'reset_password.html')

def team(request):
    context = {     }
    return render(request, 'team.html')

def volunteer(request):
    context = {     }
    return render(request, 'volunteer.html')

def password_reset(request):
    context = {     }
    return render(request, 'password_reset.html')

def password_reset_confirm(request):
    context = {     }
    return render(request, 'password_reset_confirm.html')
    
def password_reset_complete(request):
    context = {     }
    return render(request, 'password_reset_complete.html')

def password_reset_done(request):
    context = {     }
    return render(request, 'password_reset_done.html')

def register_1(request):
    context = {     }
    return render(request, 'register_1.html')

# def profile(request):
#     context = {     }
#     return render(request, 'profile.html')
    

# def about(request):
#     return HttpResponse("this is about page")

# def services(request):
#     return HttpResponse("this is services page")

# def contact(request):
#     context = {
        
#     }
#     return render(request, 'contact.html')





# Registeration

def register_1(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        emergency_phone = request.POST.get('emergency_phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        blood_group = request.POST.get('blood_group')
        area_of_interest = request.POST.get('area_of_interest')
        time_volunteering = request.POST.get('time_volunteering')
        locations_volunteering = request.POST.get('locations_volunteering')
        notification_mode = request.POST.get('notification_mode')
        comments = request.POST.get('comments')
        profile = UserProfile(first_name=first_name,last_name=last_name, username=username, dob=dob, gender=gender, phone=phone, emergency_phone=emergency_phone, email=email, address=address,blood_group=blood_group, area_of_interest=area_of_interest, time_volunteering=time_volunteering, locations_volunteering=locations_volunteering, notification_mode=notification_mode, comments=comments)
        profile.save()
        return redirect('/login')
    else:
        return render(request, 'register_1.html')
    
    
    
    


# def main_register(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')

#         # Check if email is already present in the database
#         if User.objects.filter(email=email).exists():
#             error_message = "Email already exists. Please use a different email."
#             return render(request, 'main_register.html', {'error_message': error_message})

#         user = User.objects.create_user(
#             username=username,
#             email=email,
#             password=password,
#             first_name=first_name,
#             last_name=last_name
#         )
#         user.save()

#         return redirect('/register')
#     return render(request, 'main_register.html')

def main_register(request):
    error_message = {
        'username': '',
        'email': ''
    }
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        try:
            # Check if username is already present in the user profile model
            if User.objects.filter(username=username).exists():
                error_message['username'] = "Username already exists. Please choose a different username."
            else:
                # Check if email is already present in the database
                if User.objects.filter(email=email).exists():
                    error_message['email'] = "Email already exists. Please use a different email."
                else:
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=password,
                        first_name=first_name,
                        last_name=last_name
                    )
                    user.save()
                    return redirect('/register_1')
        except IntegrityError:
            error_message['general'] = "An error occurred while registering. Please try again."
    
    return render(request, 'main_register.html', {'error_message': error_message})





    
    
    
    
    
    # Login


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'login.html')
    
    
    
    
    


# def myview(request):
#   if request.method == "POST":
#     form1 = MyForm(request.POST)
#     form2 = MyForm(request.POST)
#   else:
#     form1 = MyForm()
#     form2 = MyForm()
#   return render(request, "mytemplate.html", {"form1": form1, "form2":form2})
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #Email Verification
    
    
# def activate_email(request , email_token):
#     try:
#         user = Profile.objects.get(email_token= email_token)
#         user.is_email_verified = True
#         user.save()
#         return redirect('/')
#     except Exception as e:
#         return HttpResponse('Invalid Email token')






# def home(request):
#     past_events = Event.objects.filter(event_date__lt=timezone.now().date(), event_time__lt=timezone.now().time()).order_by('event_date', 'event_time')

#     # get all events whose date and time is greater than or equal to today's date
#     upcoming_events = Event.objects.filter(event_date__gte=timezone.now().date(), event_time__gte=timezone.now().time()).order_by('event_date', 'event_time')

#     # create a list of dictionaries to store the event data
#     past_event_data = []
#     for event in past_events:
#         past_event_data.append({
#             'event_name': event.event_name,
#             'event_date': event.event_date,
#             'event_time': event.event_time.strftime('%I:%M %p'),
#             'event_location': event.event_location,
#         })

#     upcoming_event_data = []
#     for event in upcoming_events:
#         upcoming_event_data.append({
#             'event_name': event.event_name,
#             'event_date': event.event_date,
#             'event_time': event.event_time.strftime('%I:%M %p'),
#             'event_location': event.event_location,
#         })








# def home(request):
   
#     # current_date = datetime.now().date()
#     # current_time = datetime.now().time()

#     # # Query the Event objects that meet the condition
#     # events = Event.objects.filter(event_date__gte=current_date, event_time__gte=current_time)
     
#     today = datetime.date.today()
#     past_events = Event.objects.filter(event_date__lt=today).order_by('-event_date')
#     upcoming_events = Event.objects.filter(event_date__gte=today).order_by('event_date')

    


#     all_blogs = Blog.objects.all()
#     random_blogs = sample(list(all_blogs), 2)

#     context = {
#         'past_events': past_events,
#         'upcoming_events': upcoming_events,
#         'random_blogs': random_blogs
#     }
#     return render(request, 'home.html', context)











    # # Get all Blog objects
    # all_blogs = Blog.objects.all()
    # # Choose two random Blog objects
    # random_blogs = sample(list(all_blogs), 2)

    # # render the event list template with the event data
    # return render(request, 'home.html', {'past_event_data': past_event_data, 'upcoming_event_data': upcoming_event_data, 'random_blogs': random_blogs})

    # return render(request, 'home.html', {'past_event_data': past_event_data, 'upcoming_event_data': upcoming_event_data })


# def enroll(request, event_id):
#     event = get_object_or_404(Event, e_id=event_id)
#     enrollments = EnrolledVolunteer.objects.filter(event=event)
#     volunteers = [enrollment.user for enrollment in enrollments]
#     context = {
#         'event': event,
#         'volunteers': volunteers
#     }
#     return render(request, 'home.html', context)







# def enroll(request, e_id):
#     if request.method == 'POST':
#         event = get_object_or_404(Event, e_id=e_id)
#         user = request.user

#         if Enrollment.objects.filter(event=event, user=user).exists():
#             # User has already enrolled for this event
#             messages.warning(request, 'You have already enrolled for this event.')
#             return redirect('home')  # Redirect to the event list page

#         # # Get the UserProfile instance of the logged-in user
#         # user_profile = UserProfile.objects.get(user=user)

#         enrollment = Enrollment(event=event, user=user, email=user.email)
        
#         # # Set the phone field of the enrollment object to the phone field of the UserProfile
#         # enrollment.phone = user_profile.phone
        
#         enrollment.save()

#         messages.success(request, 'You have successfully enrolled for the event.')
#         return redirect('home')  # Redirect to the event list page
#     else:
#         return redirect('login')  # Redirect to the login page if the user is not authenticated


def home(request):
    
    today = datetime.date.today()
    past_events = Event.objects.filter(event_date__lt=today).order_by('-event_date')
    upcoming_events = Event.objects.filter(event_date__gte=today).order_by('event_date')

    enrolled_events = set()

    if request.user.is_authenticated:
        enrollments = Enrollment.objects.filter(event__in=upcoming_events, user=request.user)
        enrolled_events = set(enrollment.event for enrollment in enrollments)

    all_blogs = Blog.objects.all()
    random_blogs = sample(list(all_blogs), 2)

    context = {
        'past_events': past_events,
        'upcoming_events': upcoming_events,
        'random_blogs': random_blogs,
        'enrolled_events': enrolled_events,
    }
    return render(request, 'home.html', context)



def enroll(request, e_id):
    if request.method == 'POST':
        event = get_object_or_404(Event, e_id=e_id)
        user = request.user

        if Enrollment.objects.filter(event=event, user=user).exists():
            # User has already enrolled for this event
            messages.warning(request, 'You have already enrolled for this event.')
            return redirect('home')  # Redirect to the event list page

        enrollment = Enrollment(event=event, user=user, email=user.email)
        enrollment.save()

        messages.success(request, 'You have successfully enrolled for the event.')
        return redirect('home')  # Redirect to the event list page
    else:
        return redirect('login')  # Redirect to the login page if the user is not authenticated



def logout_view(request):
    logout(request)
    return redirect('home') 



# def send_email(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
        
       
#         subject = 'Change Password'
#         body = 'To change your Password click on this link'
#         from_email = '204006.jpscwit@gmail.com'
#         to_email = [email]
#         email = EmailMessage(subject, body, from_email, to_email)
#         csv_filename = os.path.basename("C:/Users/jayas/Downloads/export.csv")

#         with open('export (5).csv', 'rb') as file:
#             email.attach(csv_filename, file.read(), 'text/csv')
#         email.send()
#         return response
        
#     return render(request,'email.html',{'subject': subject})


# def attendance(request, e_id):
#     if request.user == "admin@2023":
#         if request.method == 'POST':
#             toggle_values = request.POST.getlist('toggle')
#             toggle_values = list(map(int, toggle_values))  # Convert toggle values to integers
#             for attendance in Enrollment.objects.filter(event=e_id):
#                 is_present = attendance.id in toggle_values
#                 attendance.is_present = is_present
#                 attendance.save()

#         attendee = Enrollment.objects.filter(event=e_id)
#         return render(request, 'attendance_list.html', {'attendee': attendee,'e_id':e_id})
#     else:
#         return HttpResponse("You are not Authorized to Access this.")
    
    
    
# def profile(request):
#     # Retrieve the user profile from the database
#     user_profile = UserProfile.objects.get(username=request.user.username)
#     # Pass the user profile data to the template context
#     context = {'user_profile': user_profile}

#     return render(request, 'profile.html', context)
def profile(request):
    if request.user.username == "admin@2023" and request.method == 'GET':
        # Redirect to the Django administration
        return redirect('/admin/')
    else:
        # Retrieve the user profile from the database
        user_profile = UserProfile.objects.get(username=request.user.username)
        # Pass the user profile data to the template context
        context = {'user_profile': user_profile}
        return render(request, 'profile.html', context)



@staff_member_required
def attendance(request, e_id):
    event = Event.objects.get(e_id=e_id)  # Fetch the event object using the event ID
    if request.method == 'POST':
        toggle_values = request.POST.getlist('toggle')
        toggle_values = list(map(int, toggle_values))  # Convert toggle values to integers
        for attendance in Enrollment.objects.filter(event=e_id):
            is_present = attendance.id in toggle_values
            attendance.is_present = is_present
            attendance.save()

    attendee = Enrollment.objects.filter(event=e_id)
    return render(request, 'attendance_list.html', {'attendee': attendee, 'e_id': e_id, 'event': event})


# def send_email(request):
#     if request.method == 'POST':
#         name=request.POST.get('name')
#         email = request.POST.get('email')
#         phonenumber=request.POST.get('phonenumber')
#         Query=request.POST.get('Query')
#         print(name)
#         print(email)
#         print(phonenumber)
#         print(Query)
#         print("hello")
#         subject = 'New message on contact from '
#         body = '<br><h1 style="color:#df9d4f !important">New user Contacted from Adar Poonawala Green City Initiative Website...</h1><br> <b>Name:</b> '+name+'<br><b>Email:</b> '+email+' <br><b>Phone Number:</b> '+phonenumber+' <br><b>Query: </b>'+Query+' <br> <h2 style="color:#df9d4f !important">Thanks Regards,</h2><br><h2 style="color:#df9d4f !important">www.analytiqglobalsolution.com</h2><br>'
#         from_email = '204030.psdcwit@gmail.com'
#         to_email = ['204030.psdcwit@gmail.com']
#         email = EmailMessage(subject, body, from_email, to_email)
#         email.send()
        
#     return render(request,'contact.html')





def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        Query = request.POST.get('Query')

        subject = 'New Enquiry from '+name 
        from_email = '204030.psdcwit@gmail.com'
        to_email = ['204030.psdcwit@gmail.com']

        # Render the HTML template with the context data
        html_content = render_to_string('email_template.html', {'name': name, 'email': email, 'phonenumber': phonenumber, 'Query': Query})

        # Create the email message object
        email_message = EmailMultiAlternatives(subject, '', from_email, to_email)
        email_message.attach_alternative(html_content, "text/html")

        # Send the email
        email_message.send()
        
        # Set the message value based on the email send status
        message = 'OK'  # Assuming the email is sent successfully

        # Pass the message as a context variable
        context = {'message': message}
        return render(request, 'contact.html', context)

    return render(request, 'contact.html')



def update_profile(request):
    # Get the user profile object
    user_profile = UserProfile.objects.get(username=request.user.username)
    context = {
        'user_profile': user_profile
    }
    return render(request, 'update_profile.html', context)

def save_profile_changes(request):
    if request.method == 'POST':
        # Get the user profile object
        user_profile = UserProfile.objects.get(username=request.user.username)
        # Update the profile attributes with the submitted form data
        user_profile.phone = request.POST.get('phone')
        user_profile.emergency_phone = request.POST.get('emergency_phone')
        user_profile.address = request.POST.get('address')
         
        
        # Update more profile attributes as per your form fields

        # Save the changes to the database
        user_profile.save()

    return redirect('/profile')