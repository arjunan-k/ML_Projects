const form = document.getElementById('loan-form');

loadAllEvent();

function loadAllEvent() {
form.addEventListener('submit', function(e){
    document.querySelector('#results').style.display = 'none';
    document.querySelector('#loading').style.display = 'block';
    setTimeout(calculateLoan, 2000);
    e.preventDefault();
});
}

function calculateLoan(){
    // console.log('Calculating');

    const amount = document.querySelector('#amount');
    const interest = document.querySelector('#interest');
    const years = document.querySelector('#years');
    console.log(amount.value + interest.value + years.value);

    const monthlyPayment = document.getElementById('monthly-payment');
    const totalPayment = document.getElementById('total-payment');
    const totalInterest = document.getElementById('total-interest');

    const principal = parseFloat(amount.value);
    const calculatedInterest = parseFloat(interest.value) / 100 / 12;
    const calculatedPayment = parseFloat(years.value) * 12;

    const x = Math.pow(1 + calculatedInterest, calculatedPayment);
    const monthly = (principal*x*calculatedInterest) / (x-1);

    if (isFinite(monthly)) {
        monthlyPayment.value = monthly.toFixed(2);
        totalPayment.value = (monthly*calculatedPayment).toFixed(2)
        totalInterest.value = ((monthly*calculatedPayment)-principal).toFixed(2);
        document.querySelector('#results').style.display = 'block';
        document.querySelector('#loading').style.display = 'none';
    } else {
        // console.log('Please check number');
        showError('Please check your numbers');

    }

}

function showError(error) {
    document.querySelector('#results').style.display = 'none';
    document.querySelector('#loading').style.display = 'none';
    const div = document.createElement('div');
    const card = document.querySelector('.card')
    const heading = document.querySelector('.heading')
    div.className = 'alert alert-danger';
    div.appendChild(document.createTextNode(error));
    card.insertBefore(div, heading);

    setTimeout(clearError, 2000);
}

function clearError(){
    document.querySelector('.alert').remove();
}