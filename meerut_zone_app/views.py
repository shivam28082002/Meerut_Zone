from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from .models import *
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.core import serializers
from django.db.models import Q
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes


# Create your views here.
import logging
logger = logging.getLogger(__name__)


def home(request):
    try:
        user_form = UserForm()
        user_profile_form = UserProfileForm() 
        login_form = LoginForm()
        review = Rating.objects.all()
        if request.user:
            change_password = PasswordChangeForm(request.user)
        return render(request, 'index.html', {'user_form': user_form, 'user_profile_form': user_profile_form, 'login_form':login_form,'change_password':change_password, 'review':review})
    except Exception as e:
        print(e)
        return redirect('home')

    
def login_view(request):
    try:
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                email = login_form.cleaned_data.get('email').lower()
                password = login_form.cleaned_data.get('password')
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Login successfully")
                    return redirect('home')
                else:
                    print('Error Here')
                    return redirect('home')
        else:
            return redirect('home')
    except Exception as e:
        print(e)
        return redirect('home')




def signup(request):
    """
    Allow users to enter their data and save it to the database
    """
    try:
        user = request.user
        if request.method == 'POST':
            user_form = UserForm(request.POST)
            user_profile_form = UserProfileForm(user, request.POST)
            if user_form.is_valid() and user_profile_form.is_valid():       
                email = user_form.cleaned_data.get('email').lower()
                first_name = user_form.cleaned_data.get('first_name')
                last_name = user_form.cleaned_data.get('last_name')
                password = user_form.cleaned_data.get('password') 
                new_user = User.objects.create(
                    username=email,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,  #somaySSS
                )
                new_user.set_password(password) 
                new_user.save() 
                user_profile = user_profile_form.save(commit=False)
                user_profile.user = new_user
                user_profile.is_staff = True
                user_profile.save()
                html_content = render_to_string('email_template.html', {'new_user': new_user})
                plain_content = strip_tags(html_content)
                email = EmailMultiAlternatives(
                    subject=f"Welcome to meerut zone",
                    body=plain_content,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[email]
                )
                email.attach_alternative(html_content, "text/html")
                email.send()
                messages.success(request, "Sign Up Sucessfully")
                return redirect('home') 
        else:
            return  redirect('home')
    except Exception as exc:
        print(exc)
        return redirect('home')
    


def hospital_data(request):
    try:
        hospital_data = Hospital.objects.all().order_by('name')
        return render(request, 'hospital.html',{'hospital_data':hospital_data})
    except Exception as exc:
         print(exc)
         return redirect('home')

def eduction(request):
    try:
        eduction_data = Education.objects.all().order_by('name')
        return render(request, 'eduction.html', {'eduction_data':eduction_data})
    except Exception as exc:
        print(exc)
        return redirect('home')

def cafes(request):
    try:
        cafe_data = Cafes.objects.all().order_by('name')
        return render(request, 'cafes.html', {'cafe_data': cafe_data})
    except Exception as exc:
        print(exc)
        return redirect('home')
    
def bank(request):
    try:
        bank_data = Banks.objects.all().order_by('name')
        return render(request, 'ATM.html',{'bank_data': bank_data})
    except Exception as exc:
        print(exc)
        return redirect('home')
    
def park(request):
    try:
        park_data = Park.objects.all().order_by('name')
        return render(request, 'park.html', {'park_data':park_data})
    except Exception as exc:
        print(exc)
        return redirect('home')
    
def shopping(request):
    try:
        shopping_data = Shopping.objects.all().order_by('name')
        return render(request, 'shopping.html',{'shopping_data': shopping_data})
    except Exception as exc:
        print(exc)
        return redirect('home')
    

def admin_panel(request):
    try:
        pass
    except Exception as e:
        print(e)
        return redirect('home')
    


def contact_us(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            contact = Messages.objects.create(
                name = name,
                email = email,
                subject = subject,
                message = message
            )
            contact.save()
            html_content = render_to_string('contact_us.html', {'new_user': name})
            plain_content = strip_tags(html_content)
            email = EmailMultiAlternatives(
                subject=f"Thank you contact Us",
                body=plain_content,
                from_email=settings.EMAIL_HOST_USER,
                to=[email]
            )
            email.attach_alternative(html_content, "text/html")
            email.send()
            return redirect('home')
    except Exception as e:
        print(e)
        return redirect('home')
    

@login_required
def logout_view(request):
    """se
         Logout view to let the user out of the application
    """
    try:
        logout(request)
        messages.success(request, "Logout Sucessfully")
        return redirect('home')
    except Exception as e:
        print(e)
        return redirect('home')
    

@login_required
def change_password_view(request):
    """
                Change Password to change the password of login user
    """
    try:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                u = User.objects.get(email=request.user.email)
                u.set_password(form['password1'].value())
                u.save()
                messages.success(request, "Password Update Successfully")
                return redirect("home")
    except Exception as exc:
        messages.success(request, "Smething Went Worng")
        return redirect('home')

def check_email(request):
    try:
        email = request.POST.get('email')
        if email:
            email_check = User.objects.filter(email=email).exists()
            return JsonResponse({'success': email_check})
        else:
            return JsonResponse({'success': False})
    except Exception as e:
        print(e)
        return JsonResponse({'failed': True})


@login_required
def profile(request):
    try:
        user = request.user
        profile_data = User.objects.get(id=user.id)
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            profile_data.first_name = first_name
            profile_data.last_name = last_name
            profile_data.email =email
            profile_data.user_profile.phone = phone
            messages.success(request, "Profile Update Successfully")
            profile_data.save()
            return redirect('home')
    except Exception as e:
        return redirect('home')




def data_hospital(request):
    try:
        categories = request.POST.get('categories', '')
        hospital_name = request.POST.get('hospital_name', '')
        hospitals = Hospital.objects.all()
        if hospital_name:
            hospitals = hospitals.filter(Q(name__icontains=hospital_name)).order_by('name')
            print(f"Hospitals after name filter: {hospitals}")
        if categories:
            hospitals = hospitals.filter(category=categories).order_by('name')
        hospital_data = [{
            'id': hospital.id,
            'name': hospital.name,
            'file': hospital.file.url if hospital.file else None,
            'address': hospital.address,
            'category': hospital.category,
            'location': hospital.loction
        } for hospital in hospitals]
        return JsonResponse({'hospital': hospital_data})
    except Exception as e:
        print(f"Exception occurred: {e}")  
        return JsonResponse({'success': False, 'error': str(e)})

def data_eduction(request):
    try:
        categories = request.POST.get('categories', '')
        hospital_name = request.POST.get('hospital_name', '')
        eduction = Education.objects.all()
        if hospital_name:
            hospitals = eduction.filter(Q(name__icontains=hospital_name)).order_by('name')
        if categories:
            hospitals = Education.objects.filter(category=categories).order_by('name')
        hospital_data = [{
            'id': hospital.id,
            'name': hospital.name,
            'file': hospital.file.url if hospital.file else None,
            'address': hospital.address,
            'category': hospital.category,
            'location': hospital.loction
        } for hospital in hospitals]
        return JsonResponse({'hospital': hospital_data})
    except Exception as e:
        print(e)
        return JsonResponse({'success': False, 'error': str(e)})



    
def data_cafes(request):
    try:
        categories = request.POST.get('categories')
        hospital_name = request.POST.get('hospital_name', '')
        hospitals = Cafes.objects.all()
        if hospital_name:
            hospitals = hospitals.filter(Q(name__icontains=hospital_name)).order_by('name')
        if categories:
            hospitals = hospitals.filter(category=categories).order_by('name')
        hospital_data = [{
            'id': hospital.id,
            'name': hospital.name,
            'file': hospital.file.url if hospital.file else None,
            'address': hospital.address,
            'category': hospital.category,
            'location': hospital.loction
        } for hospital in hospitals]
        return JsonResponse({'hospital': hospital_data})
    except Exception as e:
        print(e)
        return JsonResponse({'success': False, 'error': str(e)})



def data_bank(request):
    try:
        categories = request.POST.get('categories')
        hospital_name = request.POST.get('hospital_name', '')
        hospitals = Banks.objects.all()
        if hospital_name:
                    hospitals = hospitals.filter(Q(name__icontains=hospital_name)).order_by('name')
        if categories:
            hospitals = Banks.objects.filter(category=categories).order_by('name')
        hospital_data = [{
            'id': hospital.id,
            'name': hospital.name,
            'file': hospital.file.url if hospital.file else None,
            'address': hospital.address,
            'category': hospital.category,
            'location': hospital.loction
        } for hospital in hospitals]
        return JsonResponse({'hospital': hospital_data})
    except Exception as e:
        print(e)
        return JsonResponse({'success': False, 'error': str(e)})
    

def data_park(request):
    try:
        categories = request.POST.get('categories')
        hospital_name = request.POST.get('hospital_name', '')
        hospitals = Park.objects.all()
        if hospital_name:
            hospitals = hospitals.filter(Q(name__icontains=hospital_name)).order_by('name')
        if categories:
            hospitals = hospitals.filter(category=categories)
        hospital_data = [{
            'id': hospital.id,
            'name': hospital.name,
            'file': hospital.file.url if hospital.file else None,
            'address': hospital.address,
            'category': hospital.category,
            'location': hospital.loction
        } for hospital in hospitals]
        return JsonResponse({'hospital': hospital_data})
    except Exception as e:
        print(e)
        return JsonResponse({'success': False, 'error': str(e)})
    


def data_shopping(request):
    try:
        categories = request.POST.get('categories')
        hospital_name = request.POST.get('hospital_name', '')
        hospitals = Shopping.objects.all()
        if hospital_name:
            hospitals = hospitals.filter(Q(name__icontains=hospital_name)).order_by('name')
        if categories:
            hospitals = hospitals.filter(category=categories)
        hospital_data = [{
            'id': hospital.id,
            'name': hospital.name,
            'file': hospital.file.url if hospital.file else None,
            'address': hospital.address,
            'category': hospital.category,
            'location': hospital.loction
        } for hospital in hospitals]
        return JsonResponse({'hospital': hospital_data})
    except Exception as e:
        print(e)
        return JsonResponse({'success': False, 'error': str(e)})
    



@login_required
def forget_password_view(request):
    """
            Send user an email after email verification to reset their password
    """
    try:
        if request.method == 'POST':
            try:  
                email = request.POST.get('email')
                user = User.objects.filter(email=email).first()
                if user:
                    if user.is_active:
                        user_name = user.first_name + " "+ user.last_name
                        uid = urlsafe_base64_encode(force_bytes(user.id))
                        token = default_token_generator.make_token(user)
                        set_password = f'{request.scheme}://{request.META["HTTP_HOST"]}/reset_password/{uid}/{token}/'
                        html_content = render_to_string('forget_pass.html', {'new_user': user_name, 'set_password': set_password})
                        plain_content = strip_tags(html_content)
                        email = EmailMultiAlternatives(
                            subject=f"Forget your meerut zone password",
                            body=plain_content,
                            from_email=settings.EMAIL_HOST_USER,
                            to=[email]
                        )
                        email.attach_alternative(html_content, "text/html")
                        email.send()
                        messages.success(request, "Resest link will send on your email")
                        return redirect('home')
                    messages.error(request, "Resest link will send on your email")
                    return redirect('home')
                messages.error(request, "Something went Worng")
                return redirect('home')
            except Exception as exc:
                logger.error(exc)
                messages.error(request, "Something went Worng")
                return redirect('home')
    except Exception as exc:
            messages.error(request, "Error occurs")
            return redirect('home') 
    
def reset_password_view(request, uidb64, token):
    """
    Reset the user password and save it into the database
    """
    try:
        if request.method == 'POST':
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.filter(id=uid).first()
            if user is not None:
                username = user.first_name + " " + user.last_name
                new_password = request.POST.get('new_password')
                user.set_password(new_password)
                user.save()
                html_content = render_to_string('reset_email.html', {'new_user': username})
                plain_content = strip_tags(html_content)
                email = EmailMultiAlternatives(
                    subject="Password Reset Successful - Meerut Zone",
                    body=plain_content,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[user.email]  
                )
                email.attach_alternative(html_content, "text/html")
                email.send()
                messages.success(request, "Password reset successfully")
                return redirect('home')
            else:
                messages.error(request, "Invalid user")
                return redirect('home')   
        return render(request, 'reset_password.html', {'uidb64': uidb64, 'token': token})
    except Exception as exc:
        logger.error(exc)
        messages.error(request, "Something went wrong")
        return redirect('reset_password')



from django.http import JsonResponse

FAQ = {
    "hi": "Hi, How are you",
    "what is your name": "I am ChatZone, your assistant.",
    "how can I contact support": "You can contact support via email at meeerutzone@outlook.com",
    "contact support": "You can contact support via email at meeerutzone@outlook.com",
    "what are your working hours?": "Our working hours are from 9 AM to 5 PM, Monday to Friday.",
    "where are you located": "We are located at IIMT Meerut",
    "location": "We are located at IIMT Meerut",
    "fine": "How can I help you?",
    "thank you": "Thanks for chatting with us!",
    "thanks": "Thanks for chatting with us!",
    "thank u": "Thanks for chatting with us!",
    "famous sweet": "Nankhatai is Meerut's favourite sweet.",
    "about meerut": "Meerut is a city in Meerut district of the western part of the Indian state of Uttar Pradesh. The city lies 80 km northeast of the national capital New Delhi, within the National Capital Region and 480 km west of the state capital Lucknow.",
    "more about our services?": "You can go to our services page click here{'/home/'}",
    "ok": "",


    "best time to visit meerut": "The best time to visit Meerut is from October to March when the weather is pleasant.",
    "local cuisine": "Meerut is known for its delicious chaats, kachoris, and sweets like revdi and gajak.",
    "historical places in meerut": "Some famous historical places in Meerut include St. John's Church, Augarnath Temple, and Jama Masjid.",
    "shopping areas in meerut": "Popular shopping areas in Meerut include Abu Lane, Sadar Bazaar, and Central Market.",
    "educational institutions": "Meerut is home to several renowned educational institutions like IIMT University, Chaudhary Charan Singh University, and Shobhit University.",
    "hospitals in meerut": "Major hospitals in Meerut include Anand Hospital, Jaswant Rai Hospital, and Kailashi Hospital.",
    "nearest airport": "The nearest airport to Meerut is Indira Gandhi International Airport in New Delhi, approximately 90 km away.",
    "famous parks": "Famous parks in Meerut include Gandhi Bagh, Suraj Kund Park, and Company Garden.",
    "events in meerut": "Meerut hosts several cultural and religious events throughout the year, including the Nauchandi Mela and Kali Paltan Fair.",
    "transportation in meerut": "Meerut is well-connected by road and rail. Local transportation includes buses, auto-rickshaws, and cycle-rickshaws.",
    "hotels in meerut": "Some popular hotels in Meerut are Hyphen Premier, Bravura Gold Resort, and Hotel Harmony Inn.",
    "weather in meerut": "Meerut experiences a hot and humid climate in summers, while winters are cold and pleasant."
}

QUICK_QUESTIONS = [
    "more about our services?",
    "About Meerut",
    "contact support"
]

MEERUT_QUESTION = [
    "best time to visit meerut",
    "local cuisine",
    "historical places in meerut",
]

def chatbot_view(request):
    try:
        if request.method == 'POST':
            user_message = request.POST.get('message', '').strip().lower()
            selected_quick_question = request.POST.get('selectedQuestion', '').strip().lower()
            response_message = ""
            quick_questions = None    
            if user_message:
                if user_message == 'hi':
                    quick_questions = QUICK_QUESTIONS
                response_message = FAQ.get(user_message, "Sorry, I don't understand that question.")
            if selected_quick_question:
                if selected_quick_question == 'about meerut':
                    response_message = "Meerut is a city in Meerut district of the western part of the Indian state of Uttar Pradesh. The city lies 80 km northeast of the national capital New Delhi, within the National Capital Region and 480 km west of the state capital Lucknow."  
                    quick_questions = MEERUT_QUESTION
                else:
                    response_message = FAQ.get(selected_quick_question, "Sorry, I don't understand that question.")
                    quick_questions = None  
            return JsonResponse({'message': response_message, 'quickQuestions': quick_questions})
    except Exception as e:
        return JsonResponse({'Failed': False, 'error': str(e)})
    

def review(request):
    try:
        if request.method == 'POST':
            user = request.POST.get('user')
            post = request.POST.get('post', 'PostID')
            rating = request.POST.get('rating')
            comment = request.POST.get('comment')
            new_rating = Rating.objects.create(user=user, post=post, rating=rating, comment=comment)
            new_rating.save()
            return JsonResponse({'success': True,})
    except Exception as e:
        print(e)
        return JsonResponse({'success': False, 'message': 'An error occurred'})



