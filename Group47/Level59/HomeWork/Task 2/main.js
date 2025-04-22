
// HEADER //

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

// MAIN // 

// find needed elements
const favButton = document.querySelector('#fav');
const favButtonText = document.querySelector('#fav-text');

// function to bookmark needed project
const bookMark = () => {
    favButton.addEventListener('click', () => {         // add click listener
        // add or remove active classes
        favButton.classList.toggle('active--fav');          
        favButtonText.classList.toggle('active--fav-green');
    
        const value = favButtonText.dataset.value;      // get dataset value (bookmarked or not)
        
        if (value === 'not-booked') {                       // if not marked make it bookmarked
            favButtonText.dataset.value = 'booked';
            favButtonText.innerHTML = 'Bookmarked';
        } else {                                            // else make it not-bookmarked
            favButtonText.dataset.value = 'not-booked';
            favButtonText.innerHTML = 'Bookmark';
        } 
    });
}

// MODALS

// function to manage modals opening and closing
const ModalControl = () => {
    // find and get needed elements
    const modalBtn = document.querySelector('.riser__card-project-btn');
    const modalOverlay = document.querySelector('.form__modal-overlay');

    const thanksModalOverlay = document.querySelector('.thanks__modal-overlay');
    const thanksModalButton = document.querySelector('.thanks__modal-btn');

    const pledformContinues = document.querySelectorAll('.form__modal-pledge-form-btn'); 

    // not all riser card buttons can open modal
    const riserCardBtns = Array.from(document.querySelectorAll('.riser__card-reward-select-btn')).slice(0,-1);

    // write css properties for modaloverlay to make smooth transitions
    modalOverlay.style.cssText = `
        display: flex;
        visibility: hidden;
        opacity: 0;
        transition: opacity 0.2s ease;
    `
    // write css properties for thanksModalOverlay to make smooth transitions
    thanksModalOverlay.style.cssText = `
        display: flex;
        visibility: hidden;
        opacity: 0;
        transition: opacity 0.2s ease;
    `;

    // function that is working with events
    const closeModal = event => {
        const target = event.target;        // get event from page

        if (
            target === modalOverlay ||                      // if clicked on modal Overlay
            target.closest('.form__modal-close') ||         // if clicked on modal Overlay 'x'(exit) button
            target === thanksModalOverlay ||                // if clicked on thanksModal Overlay
            target === thanksModalButton                    // if clicked on thanksModal close button
            )                                                       // then: 
            {
            // hide both overlays because we dont know with which of them are we dealing
            modalOverlay.style.opacity = 0;
            thanksModalOverlay.style.opacity = 0;

            // after 200 mili seconds: 
            setTimeout(() => {  
                // make their visibility - hidden
                modalOverlay.style.visibility = 'hidden';
                thanksModalOverlay.style.visibility = 'hidden';
            }, 200);
        }
    }

    // function to open modal
    const openModal = () => {
        // just reasign css properties to show it again
        modalOverlay.style.visibility = 'visible';
        modalOverlay.style.opacity = 1;
    }

    // function to open thanks modal
    const openThanksModal = () => {
        modalOverlay.style.opacity = 0;     // hide previous modal
        // after 200 mili seconds: 
        setTimeout(() => {
            // reasign previous modal overlay's visibility to hidden and make thanksModal Overlay visible
            modalOverlay.style.visibility = 'hidden';
            thanksModalOverlay.style.visibility = 'visible';
            thanksModalOverlay.style.opacity = 1;
        }, 200);
    }

    modalBtn.addEventListener('click', openModal);          // call openModal function when clicked on modal Open btn
    modalOverlay.addEventListener('click', closeModal);     // call closeModal function when clicked on modal overlay

    // for each continue in modal form:
    pledformContinues.forEach(pledformContinue => {
        // add event listener and call openThanksModal function on click
        pledformContinue.addEventListener('click', openThanksModal);
    })

    // for each riser card button: 
    riserCardBtns.forEach(riserCardBtn => {
        // add event listener and call openThanksModal function on click
        riserCardBtn.addEventListener('click', openThanksModal);
    })

    thanksModalButton.addEventListener('click', closeModal);    // call closeModal function when clicked on thanksModal open button
    thanksModalOverlay.addEventListener('click', closeModal);   // call closeModal function when clicked on thanksModal overlay
}

// PLEDGE SELECT IN MODAL

// find and get needed elements
const pledgeRadios = document.querySelectorAll('.form__modal-radio');
const pledgeCards = document.querySelectorAll('.form__modal-pledge');
const pledgeForms = document.querySelectorAll('.form__modal-pledge-form');

// function to work with radio inputs in modal
const pledgeSelect = () => {
    // for each radio input add click event listener 
    pledgeRadios.forEach(radio => {
        radio.addEventListener('click', () => {
            // unactive all pledge cards
            pledgeCards.forEach(card => {
                card.classList.remove('form__modal-pledge--active');
            })

            // hide all forms of pledge cards
            pledgeForms.forEach(form => {
                form.style.display = 'none'
            })

            // make all radios unchecked
            pledgeRadios.forEach(item => {
                item.checked = false;
            })

            radio.checked = true;       // make clicked radio checked

            // get info from radio input's dataset
            const pledgeNomer = radio.dataset.pledge;       // id - which pledge card be active
            const pledgeForm = radio.dataset.form;          // id - which form should be opened

            document.querySelector(`#${pledgeForm}`).style.display = 'flex';        // show cliked pledge card's form

            document.querySelector(`#${pledgeNomer}`).classList.add('form__modal-pledge--active');      // make clicked pledge card active
        })
    })
}

// FUNCTION FOR RESPONSIVE LAYOUT

// function that changes pledge cards layout depended on screen width 
const pledgeFormResponsive = (matches450px) => {
    // find and get needed elements
    const pledges = document.querySelectorAll('.form__modal-pledge');
    const neededPledges = Array.from(pledges).slice(1);                     // all pledges except first one

    // for each pledge:
    neededPledges.forEach(pledge => {
        // find and get each pledge card's needed elements
        const pledgeAmount = pledge.querySelector('.form__modal-pledge-amount');
        const pledgeInfo = pledge.querySelector('.form__modal-pledge-info');
        const pledgeLabel = pledge.querySelector('.form__modal-label');

        // if matchmedia statement matches
        if (matches450px.matches) {
            // Move `.form__modal-pledge-amount` to `.form__modal-pledge-info`

            // 1. first remove it from original place
            //      before removing check if it is in original place
            if (pledgeAmount && pledgeAmount.parentElement === pledgeLabel) {
                pledgeLabel.removeChild(pledgeAmount);
            }

            // 2. add it to new place
            //      before adding check if it is not in new place
            if (pledgeInfo && pledgeInfo.lastChild !== pledgeAmount) {
                pledgeInfo.append(pledgeAmount);
            }

        } else {
            // Move `.form__modal-pledge-amount` back to `.form__modal-label`

            // 1. remove it from new place
            //      before removing check if it it in new place
            if (pledgeAmount && pledgeAmount.parentElement === pledgeInfo) {
                pledgeInfo.removeChild(pledgeAmount);
            }

            // 2. add it to original place
            //      before adding check if it is not in original place
            if (pledgeLabel && pledgeLabel.lastChild !== pledgeAmount) {
                pledgeLabel.append(pledgeAmount);
            }
        }
    });
}

const matches450px = window.matchMedia('(max-width: 450px)');   // needed matchMedia statement for pledgeFormResponsive function

pledgeFormResponsive(matches450px);

// call same function again when sreen width is changed(for dynamic resizing)
matches450px.addEventListener('change', () => pledgeFormResponsive(matches450px));

window.addEventListener('resize', removeShowClasses);   // on window resize call specific function

// call all functions
burgerMenu();       
bookMark();        
ModalControl();
pledgeSelect();