
function getCookie(cookieName) {
    const cookies = document.cookie.split('; '); // split key value, expire in 2 segments
    console.log(cookies,"\n");
    
    for (const cookie of cookies) { // will run for 2 times as it was split in 2 values 
        const [name, value] = cookie.split('='); // split only the key value pair in 2 values
        if (name === cookieName) { //check cookie names
            return decodeURIComponent(value);
        }
    }
    return null; // ani su requirement ?

}

// start here - create and storing cookie 
document.cookie = "courseName=webDeveopment bootcamp; expires = Thu, 5 March 2030 12:00:00 UTC;" 

// get cookie name here
const courseName = getCookie('courseName');

//prints cookie name here
console.log('Course Name:', courseName);
