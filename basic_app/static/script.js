window.onload = function(){
    let navActive = false;
    nav_btn = document.querySelector('#nav-btn');
    nav = document.querySelector('#nav');
    nav_btn.addEventListener('click',function () {
        navActive = !navActive;
        if (navActive){
            nav.className ='active';
        }
        else{
            nav.className ='';
        }
    })
};