// Use each to assign a copy of the voteAmount variable to EACH of the clickUp buttons.
$(".rating").each(function() {
	var voteAmount = 0;

	// Use this to ensure you're attaching the event within EACH of the buttons.
	// Using the classname takes the button you've clicked and continues the number on.

	$(this)
		.find(".rating-up")
		.click(function() {
			if (voteAmount < 100) {
				voteAmount++;
				$(this)
					.siblings(".counter-up")
					.text(voteAmount);
			} else {
				alert("Maximum votes reached! Stop clicking!");
			}
		});

	$(this)
		.find(".rating-down")
		.click(function() {

			if (voteAmount < 100) {
				voteAmount++;
				$(this)
					.siblings(".counter-down")
					.text(voteAmount);
			} else {
				alert("Minimum votes reached! Stop clicking!");
			}
		});
});
// Ends the each();
