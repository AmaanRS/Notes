from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import User_profile
from .models import Note
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
import random
import datetime
import pytz

timezone = pytz.timezone('Asia/Kolkata')


# Function for sending otp
def send_otp(username,email):
    rand_otp = random.randrange(0,100000)
    html_message = loader.render_to_string(
        'email_sender_app/message.html',
        {
            # TODO: Enter the recipient name
            'name': username,
            # TODO:  Update with your own body
            'body': f'Your OTP is {rand_otp} Dont share this OTP with anyone',
            # TODO: Update the signature
            'sign': 'System',
        })
    send_mail(
        'OTP for Notes Website',
        'You are lucky to receive this mail.',
        'amaan.212124101@vcet.edu.in',  # TODO: Update this with your mail id
        [email],  # TODO: Update this with the recipients mail id
        html_message=html_message,
        fail_silently=False,
    )
    return rand_otp


# Create your views here.
def index(request):
    return render(request,'Notepad/index.html')

def Signup(request):
    return render(request,'Notepad/index.html')

def Login(request):
    return render(request,'Notepad/index.html')

def Logout(request):
    logout(request)
    # del request.session['Login']
    return redirect('/Notepad/')

def OTP(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        image = request.POST['image']
        otp_for_verification = send_otp(username,email)
        params = {'otp_for_verification' : otp_for_verification,'username':username,'email':email,'password':password,'image':image}
        return render(request,'Notepad/otp.html',params)
    else:
        return render(request, 'Notepad/error.html')

def OTP_verify(request):
    if request.method == 'POST':
        otp_for_verification = request.POST['otp_for_verification']
        otp = request.POST['otp']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        image = request.POST['image']
        if otp == otp_for_verification:
            user = User.objects.create_user(username=username,password=password,email=email)
            user.save()
            user_profile,created = User_profile.objects.get_or_create(user=user)
            if created:
                user_profile.Image=image
                user_profile.save()
            messages.success(request,'Signed up successfully, you can Login now')
            return redirect('/Notepad/')
        else:
            messages.success(request,'The OTP entered was wrong')
            return redirect('/Notepad/Signup/')
    else:
        return render(request, 'Notepad/error.html')


def Login_verify(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'You have successfully logged in')
            request.session['Login'] = 'adc63dul'
            return redirect('notepad')
        else:
            messages.success(request,'Enter the correct details')
            return redirect('Login')
    else:
        return render(request, 'Notepad/error.html')

def notepad(request):
    if request.session.get('Login') == 'adc63dul':
        # All the commented lines were written to sort the note in descending order which didnt work
        # It worked by just using order_by
        # date_time_dict = {}
        # timezone = pytz.timezone('Asia/Kolkata')
        # reference_date_time = datetime.datetime.now(timezone)
        # difference_date_time_dict = {}
        # sorted_date_time_list = []
        # sorted_all_notes = {}
        # all_notes_and_values = []
        final_note_id = 0
        try:
            final_note_id = Note.objects.last().id
        except:
            pass
        all_notes = list(Note.objects.filter(user=request.user).order_by('-Last_edited'))
        # There will always be one object because of this if statement
        if len(all_notes) == 0:
            note = Note(id=final_note_id+1,user=request.user,Title="First Note",Text="Write a Note by clicking on the top right + symbol OR edit by clicking on the previously created note")
            note.save()
            all_notes.append(note)
        # for one in all_notes:
        #     date_time_dict[one.id] = one.Last_edited
        # for key,value in date_time_dict.items():
        #     difference_date_time_dict[key] = (reference_date_time - value).total_seconds()/60
        # sorted_date_time_list = sorted(difference_date_time_dict.items() , key=lambda x :x[1])
        # for obj in all_notes:
        #     id = obj.id
        #     Title = obj.Title
        #     Last_edited = obj.Last_edited
        #     Image = obj.Image
        #     Text = obj.Text
        #     user = obj.user
        #     all_notes_and_values = all_notes_and_values.__add__([[id,Title,Last_edited,Image,Text,user]])
        #     i = 0
        # for sublist in sorted_date_time_list:
        #     for item in sublist:
        #         for t in item:
        #             if t == all_notes_and_values[i][0]:
        #                 sorted_all_notes['id']: t
        #                 i = i + 1

        # for i in range(len(sorted_date_time_list)):
        #     if sorted_date_time_list[i][0] in all_notes_and_values[i][0]:
        #         sorted_all_notes[sorted_date_time_list[i][0]] = all_notes_and_values[i][1]
    # for f in range(len(sorted_date_time_dict)):
    #     for i in sorted_date_time_dict[f][0]:
    #         for j in range(len(all_notes_and_values)):
    #             if all_notes_and_values[j][0] == i:
    #                 sorted_all_notes[i] = all_notes_and_values[j]
        # sorted_all_notes = sorted([item[2] for item in all_notes_and_values])
        # param = {'all_notes':sorted_all_notes}
        param = {'all_notes':all_notes}
        return render(request,'Notepad/notepad.html',param)
    else:
        return render(request, 'Notepad/error.html')

def new_note(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            new_note = Note(user=request.user)
            # new_note.save()
            return render(request,'Notepad/write_note.html')
    else:
        return render(request, 'Notepad/error.html')

def edit_note(request):
    if request.method == 'POST':
        note = list(Note.objects.filter(id=request.POST['id']))
        note_id = note[0].id
        Title = note[0].Title
        Text = note[0].Text
        db_note = {'Title':Title,'Text':Text ,'note_id':note_id}
        param = {'db_note':db_note}
        return render(request,'Notepad/write_note.html',param)
    else:
        return render(request, 'Notepad/error.html')

def save_note(request):
    if request.method == 'POST':
        if request.POST['note_id'] == '':
            Title = request.POST['txt_1']
            Text = request.POST['txt_2']
            note = Note(Title=Title,Text=Text,user=request.user)
            note.save()
            return redirect('notepad')
        else:
            note_id = request.POST['note_id']
            Title = request.POST['txt_1']
            Text = request.POST['txt_2']
            Note.objects.filter(id=note_id).update(Title=Title,Text=Text,Last_edited=datetime.datetime.now(timezone))
            return redirect('notepad')
    else:
        return render(request, 'Notepad/error.html')

def delete_note(request):
    note = Note.objects.filter(id=request.POST['id'])
    note.delete()
    return redirect('notepad')