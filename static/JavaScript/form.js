// function saveFormData() {
//     const formData = {
//       name: document.getElementById('name').value,
//       email: document.getElementById('email').value,
//       message: document.getElementById('message').value
//     };
//     localStorage.setItem('formData', JSON.stringify(formData));
//   }
  
//   window.addEventListener('DOMContentLoaded', (event) => {
//     const formData = JSON.parse(localStorage.getItem('formData'));
//     if (formData) {
//       document.getElementById('name').value = formData.name;
//       document.getElementById('email').value = formData.email;
//       document.getElementById('message').value = formData.message;
//       document.getElementById('name').disabled = true;
//       document.getElementById('email').disabled = true;
//       document.getElementById('message').disabled = true;
//     }
//   });




// Get the form elements
const form1 = document.querySelector("form[name='form1']");
const form2 = document.getElementById('form2');

// Listen for the form submission
form1.addEventListener('submit', (event) => {
	// Prevent the default form submission
	event.preventDefault();
	
	// Get the form data
	const formData = new FormData(form1);
	
	// Store the form data in local storage
	localStorage.setItem('formData', JSON.stringify(Object.fromEntries(formData)));
	
	// Redirect to the second form page
	window.location.href = '/register';
});

// Listen for the page load event
window.addEventListener('DOMContentLoaded', (event) => {
	// Get the data from the previous form submission
	const formData = JSON.parse(localStorage.getItem('formData'));
	
    // Populate the form fields with the data
    document.getElementById('username').value = formData.username;
    document.getElementById('email').value = formData.email;
    document.getElementById('first_name').value = formData.first_name;
    document.getElementById('last_name').value = formData.last_name;



    // Disable the form fields so they can't be changed
    document.getElementById('username1').disabled = true;
    document.getElementById('email1').disabled = true;
    document.getElementById('first_name1').disabled = true;
    document.getElementById('last_name1').disabled = true;
});
