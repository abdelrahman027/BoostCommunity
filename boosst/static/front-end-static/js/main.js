var toggler = document.getElementById('toggler'),
    sideNav = document.getElementById("side_nav"),
    sideContent = document.getElementById("side_content");


toggler.addEventListener('click', function () {

    [...toggler.children].forEach(sib => sib.classList.toggle('hidden_icon'))


    sideNav.classList.toggle('hide')
    sideContent.classList.toggle('offset_left')
})

function hiddenHandler(index) {
    this.children[index].style.display = 'none'
}

///////////////////////////////////////////
var loadingContainer = document.getElementById('loading_container')

