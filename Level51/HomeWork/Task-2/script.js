
// find and get submit button
const formSubmit = document.querySelector('.rate__card .btn');    

const checkIfRated = () => {
    // get form container where radio inputs are located
    const rateForm = document.querySelector('.rate__form');

    // add event click listener on that form
    rateForm.addEventListener('click', (event) => {
        // if click is in the same area where any radio is located, then
        if (event.target.matches('.rate__form-radio')) {
            // get value from that target element(input type radio)
            const radioValue = event.target.value;
            // set it as an hash in url to thankyou page
            formSubmit.setAttribute('href', `./pages/thankyou.html#${radioValue}`);
        } else {
            // if click is not in needed area then no thankyou page
            formSubmit.setAttribute('href', `#!`);
        }
    })
}

// call function
checkIfRated();