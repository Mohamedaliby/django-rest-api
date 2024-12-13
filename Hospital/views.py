from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.response import Response
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

from Hospital.models import Person, Contact, Institute


def index(request):
    return render(request, 'logout.html')


@login_required(login_url='login')
def home(request):
    if request.user.groups.filter(name='EntryGroup').__len__() > 0:
        return HttpResponse("You don't have permission to enroll to this page")
    return render(request, 'home.html', context={'people': Person.objects.all(), 'title': 'Hospital'})


@login_required(login_url='login')
def entry(request):
    context = {
        'institutes': Institute.objects.all()
    }
    return render(request, 'entry.html', context=context)


@login_required(login_url='login')
def about(request):
    return render(request, 'about.html')


@login_required(login_url='login')
def contact_us(request):
    return render(request, 'contact.html')


@csrf_exempt
def insert(request):
    if request.method == 'POST':
        print(request.POST)

        first_name = request.POST.get("firstName")
        father_name = request.POST.get("fatherName")
        grandfather_name = request.POST.get("grandfatherName")
        family_name = request.POST.get("familyName")

        nationality = request.POST.get("nationality")
        national_id = request.POST.get("nationalId")

        birthday = request.POST.get("birthday")
        gender = request.POST.get("gender")
        institute = request.POST.get("institute")
        work_id = request.POST.get("workId")
        relationship = request.POST.get("relationship")

        address = request.POST.get("ADDRESS")
        mailbox = request.POST.get("MAILBOX")
        phones = request.POST.getlist("PHONE")
        emails = request.POST.getlist("EMAIL")
        facebook_urls = request.POST.getlist("FACEBOOK")
        instagram_urls = request.POST.getlist("INSTAGRAM")
        twitter_urls = request.POST.getlist("TWITTER")
        viber_numbers = request.POST.getlist("VIBER")
        whatsapp_numbers = request.POST.getlist("WHATSAPP")
        other_contacts = request.POST.getlist("CONTACTS")

        right_thumb_fingerprint_template = request.POST.get("rightThumbFinger")
        right_index_fingerprint_template = request.POST.get("rightIndexFinger")
        right_middle_fingerprint_template = request.POST.get("rightMiddleFinger")
        right_ring_fingerprint_template = request.POST.get("rightRingFinger")
        right_pinky_fingerprint_template = request.POST.get("rightPinkyFinger")

        left_thumb_fingerprint_template = request.POST.get("leftThumbFinger")
        left_index_fingerprint_template = request.POST.get("leftIndexFinger")
        left_middle_fingerprint_template = request.POST.get("leftMiddleFinger")
        left_ring_fingerprint_template = request.POST.get("leftRingFinger")
        left_pinky_fingerprint_template = request.POST.get("leftPinkyFinger")

        # Check information validation
        if not (first_name and father_name and family_name):
            return HttpResponse("Fail: First name, father name, grandfather name and family name are required.")

        if not (nationality and national_id):
            return HttpResponse("Fail: Nationality and national id are required.")

        if not (gender and birthday):
            return HttpResponse("Fail: Birthday and gender are required.")

        from datetime import datetime as dt
        birthday_date = dt.strptime(birthday, '%Y-%m-%d').date()
        current_date = dt.now().date()
        if birthday_date > current_date or birthday_date.year > (current_date.year - 150):
            return HttpResponse('Fail: invalid birthday')
        else:
            # TODO: check if birthday in suitable range
            # check father, mother and employee birthday
            if relationship is not None:
                if relationship == "FATHER" or relationship == "MOTHER":
                    Person.objects.all().filter(workId=work_id).first()

        if relationship is None:
            return HttpResponse("Fail: Relationship is required.")

        if not institute:
            return HttpResponse("Fail: Institute is required.")

        # emp = Employee.objects.filter(workId=work_id).first()
        # if emp == relationship:
        #     if emp is not None:
        #         return HttpResponse("Fail: Work id doesn't exist.")
        #     elif institute == emp.institute.name:
        #         return HttpResponse("Fail: Work id is already assigned for other employee.")

        person = Person()

        person.firstName = first_name
        person.fatherName = father_name
        person.grandfatherName = grandfather_name
        person.familyName = family_name

        person.nationality = nationality
        person.nationalId = national_id
        person.birthday = birthday
        person.gender = gender

        person.address = address

        person.workId = work_id
        person.institute = Institute.objects.get(name=institute)

        person.save()

        if mailbox:
            contact = Contact()
            contact.person = person
            contact.label = "MAILBOX"
            contact.contact = mailbox
            contact.save()

        for email in emails:
            contact = Contact()
            contact.person = person
            contact.label = "EMAIL"
            contact.contact = email
            contact.save()

        for phone in phones:
            contact = Contact()
            contact.person = person
            contact.label = "PHONE"
            contact.contact = phone
            contact.save()

        for facebook_url in facebook_urls:
            contact = Contact()
            contact.person = person
            contact.label = "FACEBOOK"
            contact.contact = facebook_url
            contact.save()

        for instagram_url in instagram_urls:
            contact = Contact()
            contact.person = person
            contact.label = "INSTAGRAM"
            contact.contact = instagram_url
            contact.save()

        for twitter_url in twitter_urls:
            contact = Contact()
            contact.person = person
            contact.label = "TWITTER"
            contact.contact = twitter_url
            contact.save()

        for viber_number in viber_numbers:
            contact = Contact()
            contact.person = person
            contact.label = "VIBER"
            contact.contact = viber_number
            contact.save()

        for whatsapp_number in whatsapp_numbers:
            contact = Contact()
            contact.person = person
            contact.label = "WHATSAPP"
            contact.contact = whatsapp_number
            contact.save()

        for other_contact in other_contacts:
            contact = Contact()
            contact.person = person
            contact.label = "OTHER"
            contact.contact = other_contact
            contact.save()

        # ======================= Right hand fingers =======================
        # fingerprint = Fingerprint()
        # fingerprint.person = person
        # fingerprint.finger = "RIGHT_THUMB"
        # fingerprint.fingerprintTemplate = right_thumb_fingerprint_template
        # fingerprint.save()
        #
        # fingerprint = Fingerprint()
        # fingerprint.person = person
        # fingerprint.finger = "RIGHT_INDEX"
        # fingerprint.fingerprintTemplate = right_index_fingerprint_template
        # fingerprint.save()
        #
        # fingerprint = Fingerprint()
        # fingerprint.person = person
        # fingerprint.finger = "RIGHT_MIDDLE"
        # fingerprint.fingerprintTemplate = right_middle_fingerprint_template
        # fingerprint.save()
        #
        # fingerprint = Fingerprint()
        # fingerprint.person = person
        # fingerprint.finger = "RIGHT_RING"
        # fingerprint.fingerprintTemplate = right_ring_fingerprint_template
        # fingerprint.save()
        #
        # fingerprint = Fingerprint()
        # fingerprint.person = person
        # fingerprint.finger = "RIGHT_PINKY"
        # fingerprint.fingerprintTemplate = right_pinky_fingerprint_template
        # fingerprint.save()
        # # ==================================================================
        #
        # # ======================= Right hand fingers =======================
        # fingerprint = Fingerprint()
        # fingerprint.person = person
        # fingerprint.finger = "LEFT_THUMB"
        # fingerprint.fingerprintTemplate = left_thumb_fingerprint_template
        # fingerprint.save()
        #
        # fingerprint = Fingerprint()
        # fingerprint.person = person
        # fingerprint.finger = "LEFT_INDEX"
        # fingerprint.fingerprintTemplate = left_index_fingerprint_template
        # fingerprint.save()
        #
        # fingerprint = Fingerprint()
        # fingerprint.person = person
        # fingerprint.finger = "LEFT_MIDDLE"
        # fingerprint.fingerprintTemplate = left_middle_fingerprint_template
        # fingerprint.save()
        #
        # fingerprint = Fingerprint()
        # fingerprint.person = person
        # fingerprint.finger = "LEFT_RING"
        # fingerprint.fingerprintTemplate = left_ring_fingerprint_template
        # fingerprint.save()
        #
        # fingerprint = Fingerprint()
        # fingerprint.person = person
        # fingerprint.finger = "LEFT_PINKY"
        # fingerprint.fingerprintTemplate = left_pinky_fingerprint_template
        # fingerprint.save()
        # # ==================================================================

        print("Done")

    return HttpResponse("Success")


@csrf_exempt
def check_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return HttpResponse('Yes')
        return HttpResponse('No')


def get_work_ides(request):
    data = []
    for person in Person.objects.all():
        emp = dict(
            workId=person.workId)
        data.append(emp)
    return HttpResponse(data.__str__())


def get_institutes(request):
    data = []
    for institute in Institute.objects.all():
        data.append(institute.name)
    return HttpResponse(data.__str__())


def get_users(request):
    users = User.objects.all()
    data = []
    for user in users:
        u = dict(
            username=user.username,
            password=user.password,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            date_joined=user.date_joined,
            is_active=user.is_active,
        )
        data.append(u)
    return Response(data)
