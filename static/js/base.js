for (const btn of document.querySelectorAll('.vote')) {
	btn.addEventListener('click', event => {
		event.target.classList.toggle('on');
	});
}
