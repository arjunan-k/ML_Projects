const storage = new Storage();
const weatherLocation = storage.getLocationData();

const weather = new Weathery(weatherLocation.place);
const ui = new UI();


function getWeather() {
    weather.getData()
        .then(results => {
            ui.paint(results);
        })
        .catch(err => console.log(err))
}

document.addEventListener('DOMContentLoaded', getWeather)
document.getElementById('w-change-btn').addEventListener('click', (e) => {
    const place = document.getElementById('place').value;
    // console.log(place)
    weather.changeLocation(place)
    getWeather();

    // To close the modal
    document.getElementById('w-change-btn').setAttribute('data-bs-dismiss', 'modal')
    document.getElementById('w-change-btn').textContent = 'OK'
    storage.setLocationData(place)

    // To close the modal
    // $('#locModal').modal('hide')
})