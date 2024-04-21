from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import JsonResponse
from bs4 import BeautifulSoup
import requests
from google.cloud import texttospeech
import tempfile
import os
from dotenv import load_dotenv
# import openai            



# def generate_speech(request):
#     if request.method == 'POST':
#         text = request.POST.get('text')
#         openai.api_key = OPENAI_API_KEY
#         response = openai.TextToSpeech.create(engine="text-davinci-003", text=text)
#         return JsonResponse({'audio': response.url})
#     return JsonResponse({'error': 'Invalid request method'}, status=400)


# Create your views here.

# def scrape_data_view(request):
#     if request.method == 'POST':
#         url = request.POST.get('url')
#         if url:
#             try:
#                 response = requests.get(url)
#                 if response.status_code == 200:
#                     soup = BeautifulSoup(response.content, 'html.parser')
#                     # Here, you can extract the data you need from the soup object
#                     # For example, let's extract all the text from the page
#                     data = soup.get_text()
#                     return render(request, 'home.html', {'data': data})
#                 else:
#                     error_message = f"Failed to fetch data from URL. Status code: {response.status_code}"
#                     return render(request, 'home.html', {'error': error_message})
#             except Exception as e:
#                 error_message = f"An error occurred: {str(e)}"
#                 return render(request, 'home.html', {'error': error_message})
#         else:
#             return render(request, 'home.html', {'error': 'URL is required'})

#     return render(request, 'home.html')


# def scrape_data(request,url):
#     # Send a GET request to the webpage
#     response = requests.get(url)
    
#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         # Parse the HTML content using BeautifulSoup
#         soup = BeautifulSoup(response.content, 'html.parser')
        
#         # Extract the desired information from the webpage
#         # For example, let's extract all the text from <p> tags
#         paragraphs = soup.find_all('p')
        
#         # Print the extracted text
#         for paragraph in paragraphs:
#             print(paragraph.get_text())
#     else:
#         # If the request was not successful, print an error message
#         print(f"Failed to fetch data from {url}. Status code: {response.status_code}")




# def convert_to_speech(request, url):
#     # URL of the webpage to scrape
#     # For demonstration, let's pass the URL as a query parameter in the request
#     url = request.GET.get('url', '')

#     # Send a GET request to the webpage
#     response = requests.get(url)

#     # Create a BeautifulSoup object with the webpage content
#     soup = BeautifulSoup(response.content, "html.parser")

#     # Extract text from the webpage
#     text = soup.get_text()
#     print (text)
#     # Convert text to speech using gTTS
#     texttospeech = texttospeech(text=text, lang='en')

#     # Save the speech to a temporary file
#     with tempfile.NamedTemporaryFile(delete=False) as fp:
#         texttospeech.save(fp.name)
#         file_path = fp.name

#     # Open the temporary file and read its content
#     with open(file_path, 'rb') as fp:
#         speech_data = fp.read()

#     # Delete the temporary file
#     os.unlink(file_path)

#     # Set response headers
#     response = HttpResponse(content_type='audio/mpeg')
#     response['Content-Disposition'] = 'attachment; filename="speech.mp3"'

#     # Return the speech data as an HTTP response
#     response.write(speech_data)

#     return response

def scrape_data_view(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        if url:
            try:
                # Scrape data from the URL
                response = requests.get(url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    # Extract the text from the page
                    data = soup.get_text()
                    load_dotenv()
                    api_key = os.getenv("API_KEY")
                    print("API Key:", api_key)

                    # Convert the scraped text to speech
                    text = data
                    url = "https://cloudlabs-text-to-speech.p.rapidapi.com/synthesize"
                    payload = {
                        "voice_code": "en-US-1",
                        "text": text,
                        "speed": "1.00",
                        "pitch": "1.00",
                        "output_type": "audio_url"
                    }
                    headers = {
                        "X-RapidAPI-Key": api_key,
                        "X-RapidAPI-Host": "cloudlabs-text-to-speech.p.rapidapi.com"
                    }
                    response = requests.post(url, data=payload, headers=headers)
                    
                    if response.status_code == 200:
                        data = response.json()
                        audio_url = data['result']['audio_url']
                        # Redirect the user to the audio URL
                        return redirect(audio_url)
                    else:
                        return HttpResponse("Error: Unable to convert text to speech", status=response.status_code)

                else:
                    error_message = f"Failed to fetch data from URL. Status code: {response.status_code}"
                    return render(request, 'home.html', {'error': error_message})
            except Exception as e:
                error_message = f"An error occurred: {str(e)}"
                return render(request, 'home.html', {'error': error_message})
        else:
            return render(request, 'home.html', {'error': 'URL is required'})

    return render(request, 'home.html')

def base(request):
    user = request.user
    return render(request,'base.html',{'user':user})

def home(request):
    job= jobs.objects.all().order_by('-id')[:3]
    return render(request,'home.html',{"jobs":job})

def index(request):
    job= jobs.objects.all()[:3]
    return render(request,'index.html',{"jobs":job})


def register_candidate(request):
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        mothers_name = request.POST['mothers_name']
        fathers_name = request.POST['fathers_name']
        address = request.POST.get('address', '')
        gender = request.POST['inlineRadioOptions']
        state = request.POST['state']
        city = request.POST['city']
        pincode = request.POST['pincode']
        DOB = request.POST['DOB']
        email = request.POST['email']
        username = request.POST['username']
        qualification = request.POST['qualification']
        stream = request.POST['stream']
        skills = request.POST['skills']
        UDID = request.POST['UDID']
        functional_difficulties = request.POST['functional_difficulties']
        assistive_device = request.POST['assistive_device']
        human_assistance = request.POST['human_assistance']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register_candidate')

        # Check if email or username already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered. Please use a different email address.')
            return redirect('register_candidate')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please try a different username.')
            return redirect('register_candidate')

        # Create user and candidate profile
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        candidate_profile = CandidateProfile.objects.create(user=user, mothers_name=mothers_name, fathers_name=fathers_name, address=address, pincode=pincode, DOB=DOB, stream=stream, skills=skills, UDID=UDID, functional_difficulties=functional_difficulties, assistive_device=assistive_device, human_assistance=human_assistance)
        candidate_profile.save()
        print('candidate_profile:', candidate_profile.user.username)
        messages.success(request, 'You are now registered and can log in')
        return redirect('register_candidate')  # Redirect to login page after successful registration
    else:
        return render(request, 'register_candidate.html')
    

def candidate_profile(request):
    candidate = CandidateProfileNew.objects.filter(user=request.user).first()
    print(candidate)
    return render(request, 'candidate_profile.html', {'candidate': candidate})

def register_employer(request):   

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        organization_name = request.POST['organization_name']
        organization_address = request.POST.get('organization_address', '')
        organization_type = request.POST['inlineRadioOptions']
        # state = request.POST['state']
        # city = request.POST['city']
        pincode = request.POST['pincode']
        DOB = request.POST['DOB']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:

            if User.objects.filter(email=email).exists():
                messages.error(request, 'email is already registered. Please use a different email address.')
                return redirect('register_employer')
            
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'username already exists. Please try different username.')
                return redirect('register_employer')
            
            else:
                user = User.objects.create_user(username=username,email=email,password=password, first_name=first_name, last_name=last_name,)
                user.save()
                
                employer_profile = employerProfile.objects.create(user=user,organization_name=organization_name
                                                ,organization_address=organization_address,organization_type=organization_type,pincode=pincode,DOB=DOB)
                employer_profile.save()
                
                messages.success(request, 'You are now registered and can log in')
                return redirect('register_employer')
            
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register_employer')
    else:
        return render(request, 'register_employer.html')


def candidate_login (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print(f"Username: {username}")
        print(f"Password: {password}")

        user= authenticate(username=username,password=password)

        print (f"user= {user}")
        if user is not None:
            auth.login(request,user)
            return redirect('candidate_home')
        
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('candidate_login')
       
    else:    
        return render(request,'candidate_login.html')

def employer_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print(f"Username: {username}")
        print(f"Password: {password}")

        user= authenticate(username=username,password=password)

        print (f"user= {user}")
        if user is not None:
            auth.login(request,user)
            return redirect('employer_home')
        
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('employer_login')
       
    else:    
        return render(request,'employer_login.html')
@login_required(login_url="employer_login")
def employer_home(request):
    query=None
    posted_job = None
    if request.method == 'POST':
        organization_name = request.POST['organization_name']
        organization_type = request.POST['organization_type']
        job_title = request.POST['job_title']
        job_description = request.POST['job_description']
        openings=request.POST['openings']
        location = request.POST['location']
        
        job= jobs.objects.create(organization_name=organization_name, organization_type=organization_type
                                 ,job_title=job_title,job_description=job_description,
                                 openings=openings,location=location)
        job.save()
        
        posted_job = Posted_job.objects.create(employer=request.user,job=job)
        posted_job.save()
        
        
        messages.success(request, 'Job Posted successfully!!')
        return redirect('employer_home')
    else:
        return render(request, 'employer_home.html',)
    

@login_required(login_url="employer_login")
def posted_job(request):
    posted_jobs = Posted_job.objects.filter(employer=request.user)
    query = []
    applicants =[]
    for posted_job in posted_jobs:
        applications = Application.objects.filter(job=posted_job.job)
        applicant_names = [app.candidate.username for app in applications]
        applicant_emails = [app.candidate.email for app in applications]
        applicants.append({'name': applicant_names, 'email': applicant_emails})
        query.append({'job': posted_job, 'applicants': applicants})

    return render(request, 'posted_job.html', {'posted_job': query})

# def posted_job(request):
   
#     posted_job=None
    
#     posted_job = Posted_job.objects.filter(employer=request.user)
#     query = [job.job for job in posted_job]
    
#     for job in posted_job:
#         applications = Application.objects.filter(job=job.job )
#         applicant_names = [app.candidate.username for app in applications] 
#         query.append({'applicants': applicant_names})


#     return render(request, 'posted_job.html',{'posted_job':query})

@login_required(login_url="employer_login")
def applicants(request,job_id):
   
   job = jobs.objects.get(id=job_id)
   applicants = Application.objects.filter(job=job.id)

   return render(request, 'posted_job.html', {'applicants': applicants, 'job': job})
    

    
@login_required(login_url="candidate_login")    
def apply_job(request, job_id):
    job = jobs.objects.get(id=job_id)
    application = None
    if request.method == 'POST':
        application = Application.objects.create(candidate=request.user, job=job)
        application.save()
        return redirect('jobs_page')
    return render(request, 'apply_job.html', {'job': job})




# @login_required(login_url="candidate_login")
# def applied_jobs(request):
#     # Get all applications for the current candidate
#     applications = Application.objects.filter(candidate=request.user)

#     # Get the jobs associated with the applications
#     applied_jobs = [app.job for app in applications]

#     return render(request, 'applied_jobs.html', {'applied_jobs': applied_jobs})
    
def logout_page(request):
    auth.logout(request)
    return redirect('home')

@login_required(login_url="candidate_login")
def candidate_home (request):
    job= jobs.objects.all().order_by('-id')[:3]
    return render(request, 'candidate_home.html',{"jobs":job})

# @login_required(login_url="candidate_login")
# def candidate_profile(request):
#     candidate = CandidateProfile.objects.filter(user=request.user)
    
#     return render(request, "candidate_profile.html",{"candidate":candidate})

def previous_Year_questions(request):
    PYQ = PYQs.objects.all()
    return render(request,'Previous_Year_questions.html', {"PYQs":PYQ})

def tutorials(request):
    return render(request,'tutorials.html')

def jobs_page(request):
    # applications = Application.objects.filter(candidate=request.user)
    job= jobs.objects.all().order_by('-id')
    # return render(request,'jobs_page.html',{"jobs":job,"applications":applications})
    if request.user.is_authenticated:
        applications = Application.objects.filter(candidate=request.user)
        applied_jobs = [app.job for app in applications]
        return render(request,'jobs_page.html',{"jobs":job , "applied_jobs": applied_jobs})
    else:
        return render(request,'jobs_page.html',{"jobs":job })



def register_candidate_new(request):
    if request.method == 'POST':
        data=request.POST
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register_candidate_new')
        elif User.objects.filter(email=email).exists():
                messages.error(request, 'email is already registered. Please use a different email address.')
                return redirect('register_candidate_new')
        elif User.objects.filter(username=username).exists():
                messages.error(request, 'username already exists. Please try different username.')
                return redirect('register_candidate_new')
        else:
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            user.save()
            mothers_name = data.get('mothers_name')
            fathers_name = data.get('fathers_name')
            # address = data.get('address', '')
            date_of_birth = data.get('date_of_birth')
            gender = data.get('gender')
            address = data.get('address', '')
            pincode = data.get('pincode')
            highest_qualification= data.get('highest_qualification')
            skills= data.get('skills')
            UDID=   data.get('UDID')
            functional_difficulties = data.get('functional_difficulties')
            assistive_device = data.get('assistive_device')
            human_assistance =  data.get('human_assistance')
            candidate_profile = CandidateProfileNew.objects.create(user=user, mothers_name=mothers_name, fathers_name=fathers_name, date_of_birth=date_of_birth,gender=gender
                                                                   ,address=address,pincode=pincode,highest_qualification=highest_qualification,skills=skills,UDID=UDID,
                                                                   functional_difficulties=functional_difficulties,assistive_device=assistive_device,human_assistance=human_assistance)
            candidate_profile.save()
            messages.success(request, 'You are now registered and can log in')
            return redirect('register_candidate_new')
    return render(request,'register_candidate_new.html')