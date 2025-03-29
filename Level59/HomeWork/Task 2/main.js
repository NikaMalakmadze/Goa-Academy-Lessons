
// find and get needed elements from page
const headerNav = document.querySelector('.header__nav');
const headerNavList = document.querySelector('.header__nav-list');
const headerNavItem = document.querySelectorAll('.header__nav-list-item');
const burgerBtn = document.querySelector('.burger');

// functionality for the burger menu
const burgerMenu = () => {
    burgerBtn.addEventListener('click', () => {     // add click event listener on burger button 
        burgerBtn.classList.toggle('active');           // add or remove active class on click

        // hide or show navigation by adding or removing classes
        headerNav.classList.toggle('header__nav--show');
        headerNavList.classList.toggle('header__nav-list--show');

        // feature to close navigation when user clicks on any item of it
        headerNavItem.forEach(item => {                 // for each item of navigation:
            item.addEventListener('click', () => {          // add click event listener
                // remove all classes to hide navigation
                burgerBtn.classList.remove('active');           
                headerNav.classList.remove('header__nav--show');
                headerNavList.classList.remove('header__nav-list--show');
            })
        })
    })
};

// function that will automatically remove neccesery classes on dynamic resizing
const removeShowClasses = () => {
    if (window.innerWidth > 600) {                      // when width of screen is more then 600px
        // find all elements by attribute that have '--show' in their classes
        document.querySelectorAll('[class*="--show"]').forEach((el) => {
            el.classList.forEach((cls) => {                 // for each class name of item
                if (cls.includes('--show')) {                   // if class name includes '--show'
                    el.classList.remove(cls);                       // remove it
                }
            });
        });

        // find active element if it is on page
        //  using querySelectorAll with forEach in case if no such element with active class
        document.querySelectorAll('.active').forEach((el) => {
            el.classList.remove('active');      // remove active class
        });
    }
};

window.addEventListener('resize', removeShowClasses);   // on window resize call specific function

burgerMenu();       // call burger menu function