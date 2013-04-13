

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
						topic_comments.find(".comments_list").append(res.html);
						loading_lists.topic_id = false;
					}
				});
			}
		});
		
		$("body").on("click", ".show_replies", function() {
			$(this).closest(".comment_container").find(".replies_list").show();
			$(this).closest(".comment_container").find(".comment").show();
		});
		
		$("body").on("click", ".post_comment", function() {
			var button = $(this);
			var topic_comments = button.closest(".topic_comments");
			var comment_box = button.closest(".post_comment_box");
			var username = $.trim(comment_box.find(".post_comment_name").val());
			var content = $.trim(comment_box.find(".post_comment_field").val());
			if (content !== "") {
				if (username === "") {
					username = "anonymous";
				}
				button.attr("disabled", "disabled");
				$.ajax({
					url: comment_box.attr("data-post_comment_url"),
					method: "get",
					dataType: "json",
					data: {
						content: content,
						username: username,
						topic_id: topic_comments.attr("data-topic_id"),
					},
					success: function(res) {
						topic_comments.find(".comments_list").prepend(res.html);
						comment_box.find(".post_comment_name").val("");
						comment_box.find(".post_comment_field").val("");
					},
					complete: function() {
						button.attr("disabled", "");
					}
				});
			}
		});
		
		$("body").on("click", ".reply_button", function() {
			$(this).closest(".comments_list").find(".reply_box").remove();
			var reply_dom = $("#reply_box_sample").find(".reply_box").clone();
			reply_dom.find(".post_reply_field").val("@" + $(this).closest(".comment").find(".commenter_name").html() + " - ");
			$(this).closest(".comment_container").find(".replies_list").show();
			$(this).closest(".comment_container").find(".replies_list_body").append(reply_dom);
			
		});
		
		$("body").on("click", ".post_reply", function() {
			var button = $(this);
			var reply_box = button.closest(".reply_box");
			var username = $.trim(reply_box.find(".post_reply_name").val());
			var content = $.trim(reply_box.find(".post_reply_field").val());
			if (content !== "") {
				if (username === "") {
					username = "anonymous";
				}
				button.attr("disabled", "disabled");
				$.ajax({
					url: reply_box.attr("data-post_reply_url"),
					method: "get",
					dataType: "json",
					data: {
						content: content,
						username: username,
						comment_id: button.closest(".comment_container").attr("data-comment_id"),
					},
					success: function(res) {
						button.closest(".comment_container").find(".replies_list_body").append(res.html);
						reply_box.remove();
					},
					complete: function() {
						button.attr("disabled", "");
					}
				});
			}
		});
	
		
	}
}

$(function() {
	comments.init();
});