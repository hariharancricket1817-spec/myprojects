function toggleTheme(){
    document.body.classList.toggle("dark");

}

/* LOADER */
function showLoader(){
    document.getElementById("loader").classList.add("active");
}

/* NAVIGATION */
function goStudent(){
    showLoader();
    setTimeout(()=>{
        window.location.href="studentlogin.html";
    },1500);
}

function goStaff(){
    showLoader();
    setTimeout(()=>{
        window.location.href="stafflogin.html";
    },1500);
}