
var mnstr = {
	init: function() {
		
		var auto_clicking = false;

		$("body").on("click", ".img-source", function(e) {
			if (!auto_clicking) {
				var link = $(this);
				var source = link.closest(".source");
				auto_clicking = true;
				$.ajax({
					url: source.attr("data-source_click_url"),
					method: "get",
					data: {
						source_id: source.attr("data-source_id"),
					},
					complete: function() {
						link.click();
					}
				});
				e.preventDefault();
			}
		});
		
	}
}

$(function() {
	mnstr.init();
});