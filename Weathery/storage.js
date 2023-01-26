class Storage {
    constructor() {
        this.place;
        this.defaultPlace = "Spain";
    }

    getLocationData() {
        const place = localStorage.getItem('place');
        if(place === null) {
            this.place = this.defaultPlace
        } else {
            this.place = place
        }

        return {
            place: this.place
        }
    }

    setLocationData(place) {
        localStorage.setItem('place', place)
    }
}