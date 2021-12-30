import faker, requests, json
from datetime import timedelta
from bo.models import *

def promotors(qty:int):
    fake = faker.Faker(["en_US"])
    
    def formatph():
        import re
        ph = fake.phone_number()
        ph = re.sub('\D', '', ph)
        return str(ph[0:10])
    
    for i in range(qty):
        company = str(fake.unique.company())
        fname = str(fake.first_name())
        lname = str(fake.last_name())
        address = fake.street_address() 
        city = fake.city()
        state = fake.random_int(min=1, max=52)
        zip = fake.postalcode()
        phone = formatph()
        if i == 0: i=1
        if fake.random_int() % i == 0:
            mobile = formatph()
        else:
            mobile = 'Null'
        if fake.random_int() % i == 0:
            fax = formatph()
        else:
            fax = 'Null'
        email = fake.company_email()
        userid = 1
        
        data = f"INSERT INTO `promotors`(`company`, `fname`, `lname`, `address`, `city`, `state`, `zip`, `phone`, `mobile`, `fax`, `email`, `userid`) VALUES ('{company}', '{fname}', '{lname}', '{address}', '{city}', {state}, '{zip}', '{phone}', '{mobile}', '{fax}', '{email}', {userid});"

        with open(f"promotor{qty}.sql", "a") as file:
            file.write(data+'\n')



def venue(quantity:int):
    fake = faker.Faker(["en_US"])

    for _ in range(quantity):
        name = str(fake.unique.company())
        address = str(fake.street_address())
        city = str(fake.city())
        state = fake.random_int(min=0, max=52)
        zip = str(fake.postalcode())
        phone = str(fake.phone_number())
        website = str(fake.url())
        userid = 2
        loadinst = str(fake.paragraph(nb_sentences=5))

        data = f"INSERT INTO venue(name, address, city, state, zip, phone, website, loadinst, userid) VALUES ('{name}','{address}','{city}',{state},'{zip}','{phone}','{website}','{loadinst}',{userid});"

        with open(f"venue{quantity}.sql", "a") as file:
            file.write(data+'\n')


def event(quantity:int):
    fake = faker.Faker(["en_US"])

    for _ in range(quantity):
        eventname = fake.text(max_nb_chars=50)
        event_start_datetime = fake.date_time_this_decade(after_now=True)
        event_end_datetime = event_start_datetime + timedelta(hours=fake.random_int(min=2, max=8))
        event_onsale_datetime = event_start_datetime - timedelta(days=96)
        event_catagoryfk = fake.random_int(min=1, max=3)
        event_venuefk = fake.random_int(min=1, max=1502)
        event_promotorfk = fake.random_int(min=1, max=546)
        userid = 1
        data = f"INSERT INTO `events`(`eventname`, `event_start_datetime`, `event_end_datetime`, `event_onsale_datetime`, `event_catagoryfk`, `event_venuefk`, `event_promotorfk`, `userid`) VALUES ('{eventname}','{event_start_datetime}','{event_end_datetime}','{event_onsale_datetime}',{event_catagoryfk},{event_venuefk},{event_promotorfk},{userid});"
        
        with open(f"event{quantity}.sql", "a") as file:
            file.write(data+'\n')
        

def users(quantity):
    import random
    r = requests.get(f'https://randomuser.me/api/?nat=us&results={quantity}')
    if r.status_code == 200:
        fulljson = json.loads(r.text)
    else:
        print(f"somethig went wrong. try again.  Statuscode = {r.status_code}.")
    
    for item in fulljson['results']:
        firstname = item['name']['first']
        lastname = item['name']['last']
        address = str(item['location']['street']['number']) + " " + item['location']['street']['name']
        city = item['location']['city']
        state = random.randint(1,52)
        zip = item['location']['postcode']
        phone = item['phone']
        email = item['email']
        dob = item['dob']['date']
        avatar_url = item['picture']['medium']
        username = item['login']['username']
        password = 'sha256$fB27alBnOB5dkJNL$a9e0f6a1a7122fd7626508da689e552e703d241c2e180caf08b09c0051a90fb4'
        date_created = item['registered']['date']
        
        data = f"INSERT INTO `user` (`firstname`,`lastname`,`email`,`dob`,`address`,`city`,`state`,`zip`,`phone`,`avatar_url`,`username`,`password`,`date_created`) VALUES ('{firstname}', '{lastname}', '{email}', '{dob}', '{address}','{city}',{state},'{zip}','{phone}','{avatar_url}','{username}','{password}', '{date_created}')"
        with open('fakeuser.sql', 'a') as file:
            file.write(data+";\n")
        
if __name__ == "__main__":
    venue(150)
    # event(10000)
    promotors(54)
    # users(500)