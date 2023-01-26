class Weathery {

    constructor(place) {
        this.apiKey = "Your API key here"
        this.place = place
    }
    

    async getData() {
        const response = await fetch(`http://api.weatherapi.com/v1/current.json?key=${this.apiKey}&q=${this.place}&aqi=yes`);
        const data = await response.json();
        return data;
    }

    
    changeLocation(newPlace) {
        this.place = newPlace;
    }
}