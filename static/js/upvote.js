// Make upvote orange
for (const btn of document.querySelectorAll('.vote')) {
	btn.addEventListener('click', event => {
		event.target.classList.add('on');
	});
}

// ISSUE UPVOTE
$("#issue-upvote").click(function() {
	let pk = window.location.href.split('/')[4]
  $.ajax({
		url: pk + "/issue-upvote",
		type: "POST",
		SameSite: "Strict",
		success: function(data) {
			if (data) {
				$('#issue-upvote-display').text(data.upvotes)
				$('#issue-upvote').attr('data-target', '#casted-vote')
			}
		},
		error: function(error) {
			console.log("Response error: ", error)
		}
	});
});

// SOLUTION UPVOTE
$('#solutions').click(function(e) {
	let id = e.target.parentElement.id
	if (id.includes('solution-upvote')) {
		let pk = id.split('-')[2]
		$.ajax({
			url: pk + "/solution-upvote",
			type: "POST",
			SameSite: "Strict",
			success: function(data) {
				if (data) {
					$('#solution-upvote-display').text(data.upvotes)
					$('#solution-upvote').attr('data-target', '#casted-vote')
				}
			},
			error: function(error) {
				console.log("Response error: ", error)
			}
		});
	}
})

// Ajax Boilerplate
var csrftoken = Cookies.get('csrftoken');
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
