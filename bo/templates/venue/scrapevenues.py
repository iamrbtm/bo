# from bo import db
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
from bo import db
from bo.models import *

def scrapevenue():
    URL = "https://concertfix.com/concerts/salem-or+venues"
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    page = driver.get(URL) 

    eventblocks = driver.find_elements(By.CLASS_NAME,'eventblock')

    for ev in eventblocks:
        text = ev.text.replace('Where: ', '').splitlines()
        fulladdress = text[1].split(', ')
        venue = text[0]
        address = fulladdress[0]
        city = fulladdress[1]
        state = fulladdress[2].split(' - ')[0]  
        postalcode = fulladdress[2].split(' - ')[1]
        
        cnt = db.session.query(Venue).filter(Venue.name == venue).count()
        if cnt == 0:
            stateid = db.session.query(States).filter(States.state == state).first().id
            venueid = add_venue(venue=venue, address=address, city=city, state=stateid, postalcode=postalcode)
            
    driver.close() 

def add_venue(venue, address, city, state, postalcode):
    new = Venue(
        name = venue,
        address = address,
        city = city,
        state = state,
        zip = postalcode,
        userid = 1
    )
    db.session.add(new)
    db.session.commit()
    db.session.refresh(new)
    return new.id