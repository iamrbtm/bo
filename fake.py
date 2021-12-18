import faker

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

if __name__ == "__main__":
    venue(100)