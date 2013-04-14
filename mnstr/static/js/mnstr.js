
var mnstr = {
	init: function() {
		
		function getCookie(name) {
		    var cookieValue = null;
		    if (document.cookie && document.cookie != '') {
		        var cookies = document.cookie.split(';');
		        for (var i = 0; i < cookies.length; i++) {
		            var cookie = jQuery.trim(cookies[i]);
		            // Does this cookie string begin with the name we want?
		            if (cookie.substring(0, name.length + 1) == (name + '=')) {
		                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
		                break;
		            }
		        }
		    }
		    return cookieValue;
		}
		var csrftoken = getCookie('csrftoken');
		
		function csrfSafeMethod(method) {
		    // these HTTP methods do not require CSRF protection
		    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
		}
		$.ajaxSetup({
		    crossDomain: false, // obviates need for sameOrigin test
		    beforeSend: function(xhr, settings) {
		        if (!csrfSafeMethod(settings.type)) {
		            xhr.setRequestHeader("X-CSRFToken", csrftoken);
		        }
		    }
		});
		
		var auto_clicking = false;

		$("body").on("click", ".img-source", function(e) {
			if (!auto_clicking) {
				var link = $(this);
				var source = link.closest(".source");
				auto_clicking = true;
				$.ajax({
					url: source.attr("data-source_click_url"),
					method: "post",
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
		
		$("body").on("mouseover", ".news_displayed_name", function() {
			$(this).tooltip({ title: $(this).find(".real_news_name").text()});
		});
		
	}
}

$(function() {
	mnstr.init();
});