class UI {
    constructor(data) {
        this.location = document.getElementById('w-location')
        this.desc = document.getElementById('w-desc')
        this.string = document.getElementById('w-string')
        this.details = document.getElementById('w-details')
        this.icon = document.getElementById('w-icon')
        this.humidity = document.getElementById('w-humidity')
        this.feelsLike = document.getElementById('w-feels-like')
        this.dewpoint = document.getElementById('w-dewpoint')
        this.wind = document.getElementById('w-wind')
    }

    paint(weather) {
        this.location.textContent = `${weather.location.name}, ${weather.location.country}`
        this.desc.textContent = weather.location.region;
        this.string.textContent = `${weather.current.temp_c} Celcius`
        this.icon.setAttribute('src', `https://${weather.current.condition.icon}`)
        this.humidity.textContent = `Relative Humidity: ${weather.current.humidity}`
        this.feelsLike.textContent = `Feels Like: ${weather.current.feelslike_c} Celcius`
        this.dewpoint.textContent = `DewPoint: ${weather.current.pressure_in}`
        this.wind.textContent = `Wind: ${weather.current.wind_degree}`
    }
}