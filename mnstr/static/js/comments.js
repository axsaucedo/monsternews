

var comments = {
	init: function() {
		
		var left_min_height = 50;
		var loading_lists = [];
		var full_lists = [];
		
		$(".topic_comments").on("scroll", function() {
			var topic_comments = $(this);
			var topic_id = topic_comments.attr("data-topic_id");
			if (!loading_lists.topic_id && !full_lists.topic_id && (topic_comments[0].scrollHeight - topic_comments.scrollTop() - topic_comments.height() < left_min_height)) { 	
				loading_lists.topic_id = true;
				$.ajax({
					url : topic_comments.attr("data-load_comments_url"),
					method: "get",
					dataType: "json",
					data: {
						"lower_limit": topic_comments.find(".comment_container").length,
						"topic_id": topic_comments.attr("data-topic_id"),
					},
					success: function(res) {
						if (res.full === true) {
							full_lists.topic_id = true;
						}
						topic_comments.append(res.html);
						loading_lists.topic_id = false;
					}
				});
			}
		});
	}
}

$(function() {
	comments.init();
});