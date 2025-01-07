
//find and get elements from page

const PageContainer = document.querySelector('.pages-container');
const Pages = Array.from(document.querySelectorAll('.page'));
const ButtonPrev = document.querySelector('#ButtonPrevious');
const ButtonNext = document.querySelector('#ButtonNext');
const nomer = document.querySelector('#num');

Pages.forEach(function(page, index){

    //hide all images except first image(image with index 0)
    if (index != 0){
        page.classList.add('hidden');
    }

    page.dataset.index = index;                 //add index to every page as a data-attribute

    //add 'active' data attribute to the first page / active page
    
    Pages[0].setAttribute('data-active', '');
})

const ShowPage = function(direction){

    //find and get active image and its index on page
    const CurrentPage = document.querySelector('[data-active]');
    const CurrentPageIndex = +CurrentPage.dataset.index

    // hide current image and remove 'active' data attribute
    CurrentPage.classList.add('hidden');
    CurrentPage.removeAttribute('data-active');

    let NextPageIndex
    if (direction === 'prev'){
        //get index of next image
        // if page is first, start from last page  
        NextPageIndex = CurrentPageIndex === 0 ? Pages.length - 1 : CurrentPageIndex - 1
    }
    else if (direction === 'next'){
        //get index of next page
        // if page is last, start from first page
        NextPageIndex = CurrentPageIndex === Pages.length - 1 ? 0 : CurrentPageIndex + 1
    }

    const NextPage = document.querySelector(`[data-index='${NextPageIndex}']`);     //find next page

    // show next page and make it active
    NextPage.classList.remove('hidden');
    NextPage.setAttribute('data-active', '');

    //assign nomer of next page to the 'nomer label' using data-index attribute value
    nomer.innerHTML = +NextPage.dataset.index + 1;
}

//add function when clicked on next button
ButtonNext.addEventListener('click', function(){
    ShowPage('next');
})

//add function when clicked on previous button

ButtonPrev.addEventListener('click', function(){
    ShowPage('prev');
})