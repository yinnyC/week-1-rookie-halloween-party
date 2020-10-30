
# ------------------------------------
# Import the Libraries
# ------------------------------------
from flask import Flask, render_template, request
from random import choice
from guests import Guest
# ------------------------------------
# Declare Variables and Instances
# ------------------------------------
app = Flask(__name__)  # Instantiate the Flask class

myName = "Yin"
date, time = ("Oct. 31st, Sat", "1pm")

# Generate Guest List
# guestNameList = ["Sid", "Starlight", "Yin",
#                  "Rick", "Jconr", "Merissa", "Logan", "Tian"]
# rsvpList = [choice([True, False]) for _ in range(len(guestNameList))]
guests = []
# for (name, status) in zip(guestNameList, rsvpList):
#     guests.append({'name': name, 'rsvp': status})

# ------------------------------------
# Define Functions for Routes
# ------------------------------------


@app.route('/')
def homepage():
    """Return template and pass name variable for home."""
    return render_template('index.html', myname=myName)


@app.route('/about')
def aboutpage():
    """Return template and date/time info for about."""
    return render_template('about.html', date=date, time=time)


@app.route('/guests', methods=['GET', 'POST'])
def guestspage():
    """Return template and guests' name for guests."""
    if request.method == 'POST':
        guest_name = request.form.get('name')
        guest_email = request.form.get('email')
        guest_plus_one = request.form.get('plus-one')
        guest_phone = request.form.get('phone')
        guest_costume = request.form.get('costume')
        guest = Guest(guest_name, guest_email, guest_plus_one,
                      guest_phone, guest_costume)
        guests.append(guest)
        return render_template('guests.html', guests=guests)


@app.route('/rsvp')
def rsvppage():
    """Return template and guests for rsvp."""
    return render_template('rsvp.html', guests=guests)


if __name__ == '__main__':
    app.run(debug=True)
