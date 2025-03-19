
// async function to fetch json data file
//  it will return object with data from json file
async function loadData(file) {
    const response = await fetch(file);

    const data = await response.json();

    return data
};

// async arrow function to get and load stats on page
const getStats = async (file) => {
    const stats = await loadData(file);     // await stats to load

    // get needed elements from html page
    const statsDiv = document.querySelector('#stats');
    const statAverage = document.querySelector('#user-average');

    let statSum = statCount = 0         // helper variables to calculate average of stats

    // add each stat with its info in statsDiv using for of loop
    for (const stat of stats) {
        statSum += stat.score
        statCount += 1

        // pasting needed info in right places
        statsDiv.innerHTML += `
            <div class="result__card-stat">
              <div class="result__card-stat-info">
                <div class="result__card-stat-info-img-container">
                  <img src="${stat.icon}" alt="" class="result__card-stat-info-img">
                </div>
                <h5 class="result__card-stat-info-title" style="--color: ${stat.color}">${stat.category}</h5>
              </div>
              <div class="result__card-stat-score">
                <div class="result__card-stat-user-score">${stat.score}</div>
                <div class="result__card-stat-max-score"> / 100</div>
              </div>
            </div>
        `
    }

    // calculate and load stats average on html page
    statAverage.innerHTML = Math.floor(statSum/statCount)
};

getStats('./data.json');        // call function with given argument - path to json file

// for fetch to work open html page using live server