#!/usr/bin/python3
""" This script starts the web Flask """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.city import City
""" Flask class and render template method """
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def hbnb_filters():
    """ Display filters in html page """
    state = sorted(storage.all(State).values(), key=lambda state: state.name)
    city = sorted(storage.all(City).values(), key=lambda city: city.name)
    amenities = sorted(storage.aSll(Amenity).values(),
                       key=lambda amenity: amenity.name)

    return render_template('10-hbnb_filters.html', state=state, city=city, amenities=amenities)


@app.teardown_appcontext
def teardown(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
