var username_helptext = document.getElementById("id_username_helptext")
var password2_helptext = document.getElementById("id_password2_helptext")
var password1_helptext = document.getElementById("id_password1_helptext")
var labels = document.querySelectorAll('label')
username_helptext.innerText = ""
password2_helptext.innerText = ""
password1_helptext.innerText = ""

labels.forEach(function (label) {
    label.innerText = label.textContent.replace(":","")
})

// The username is required. It should be 150 characters or fewer. Letters, digits and @/./+/-/_ only.
// Your password can’t be too similar to your other personal information.
// Your password must contain at least 8 characters.
// Your password can’t be a commonly used password.
// Your password can’t be entirely numeric.