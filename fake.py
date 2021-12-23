from random import random
import faker
from datetime import datetime, timedelta

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
        event_venuefk = fake.random_int(min=1, max=2)
        event_promotorfk = fake.random_int(min=1, max=3)
        userid = 1
        data = f"INSERT INTO `events`(`eventname`, `event_start_datetime`, `event_end_datetime`, `event_onsale_datetime`, `event_catagoryfk`, `event_venuefk`, `event_promotorfk`, `userid`) VALUES ('{eventname}','{event_start_datetime}','{event_end_datetime}','{event_onsale_datetime}',{event_catagoryfk},{event_venuefk},{event_promotorfk},{userid});"

        with open(f"venue{quantity}.sql", "a") as file:
            file.write(data+'\n')

        
if __name__ == "__main__":
    # venue(100)
    event(150)