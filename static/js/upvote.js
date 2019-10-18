// Make upvote orange
for (const btn of document.querySelectorAll('.vote')) {
	btn.addEventListener('click', event => {
		event.target.classList.toggle('on');
	});
}

var csrftoken = Cookies.get('csrftoken');

$("#upvote-issue").click(function() {
	let pk = window.location.href.split('/').slice(-1)[0]
  $.ajax({
		url: pk + "/upvote-issue",
		type: "POST",
		SameSite: "Strict",
		error: function(error) {
			console.log("Response error: ", error)
		}
	});
});

// Ajax Boilerplate
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
