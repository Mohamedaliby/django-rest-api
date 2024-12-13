import requests
url = ""
satients =  requests.get(url)

satient = {
        "firstName": "qq",
        "fatherName": "qq",
        "grandfatherName": "q",
        "familyName": "q",
        "gender": "MALE",
        "birthday": "2019-07-16",
        "nationality": "libyan",
        "nationalId": "11212",
        "address": "libya",
        "familyId": "111",
        "workId": "111",
        "institute": "nn",
        "relationship": "EMPLOYEE"
    }
filename = "C:\\Users\\ALWAKEEL-M\\Desktop\\defaultProfilePicture.jpg"
files = {
    'file1': open(filename, 'rb'),
    'file2': open(filename, 'rb'),
    'file3': open(filename, 'rb')
}

response = requests.post('http://127.0.0.1:8000/satients/',data=satient ,files=files)
print(response.status_code)
print(response.text)