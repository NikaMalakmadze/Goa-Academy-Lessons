
// async function to fetch json data file
//  it will return object with data from json file
async function fetchData(file) {

    response = await fetch(file);

    data = await response.json();

    return data
}

// function to load fetched data on page
const loadData = (periodName, statsData, container) => {

    let last
    // set correct word for each period
    if (periodName==='daily') {last = 'Day'}
    if (periodName==='monthly') {last = 'Month'}
    if (periodName==='weekly') {last = 'Week'}

    // clear container tag's inner Html if it has any child
    if (container.innerHTML) {
        container.innerHTML = ''
    } 

    // add each stat with its info in container using for of loop
    for (const statCard of statsData) {
        container.innerHTML += 
        `<div class="profile__stat-card">
        <div class="profile__stat-card-info">
          <div class="profile__stat-card-info-title-container">
            <h4 class="profile__stat-card-info-title">${statCard.title}</h4>
            <div class="profile__stat-card-info-title-img-container">
              <img src="./assets/images/icon-ellipsis.svg" alt="" class="profile__stat-card-info-title-img">
            </div>
          </div>
          <div class="profile__stat-card-info-text">
            <h3 class="profile__stat-card-info-time">${statCard.timeframes[periodName].current}hrs</h3>
            <p class="profile__stat-card-info-last">Last ${last} - ${statCard.timeframes[periodName].previous}hrs</p>
          </div>
        </div>
      </div>`
    }
}

// main function, combines all staff together
const Main = async (file) => {
    const statsData = await fetchData(file);        // get data from json file

    // get needed elements from page
    const statsContainer = document.querySelector('.profile__stats-container');
    const periodButtons = document.querySelectorAll('.profile__card-option');

    loadData('daily', statsData, statsContainer);           // load daily tasks when page is open

    periodButtons.forEach(periodButton => {                     // for each button
        periodButton.addEventListener('click', () => {              // add click event listener
            // remove active state class from all buttons
            periodButtons.forEach(button => {
                button.classList.remove('profile__card-option--active');
            })    

            periodButton.classList.add('profile__card-option--active');     // add active state class to clicked button

            const period = periodButton.dataset.period;                     // get its period/value from dataset
        
            // call loadData that will load info on page depended on chosen period
            loadData(period, statsData, statsContainer);                    
        })
    })

}

Main('./data.json');    // call main function