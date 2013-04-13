function getRssFeeds()
{
	return [
		'http://feeds.bbci.co.uk/news/rss.xml',
		'http://news.sky.com/feeds/rss/home.xml',
		'http://www.itv.com/news/index.rss',
		'http://www.channel4.com/news/latest-news/rss',
		
		'http://feeds.guardian.co.uk/theguardian/rss',
		'http://www.independent.co.uk/news/uk/rss',
		'http://www.thetimes.co.uk/tto/news/rss',
		'http://www.telegraph.co.uk/rss'
	];
}

function getRSS(url){

	var urls = {
		'http://feeds.bbci.co.uk/news/rss.xml',
		'http://news.sky.com/feeds/rss/home.xml',
		'http://www.itv.com/news/index.rss',
		'http://www.channel4.com/news/latest-news/rss',
		
		'http://feeds.guardian.co.uk/theguardian/rss',
		'http://www.independent.co.uk/news/uk/rss',
		'http://www.thetimes.co.uk/tto/news/rss',
		'http://www.telegraph.co.uk/rss'
		
	};
	
	$.get(url, function(data) {
	
		var $xml = $(data);
		
		$xml.find("item").each(function() {
			var $this = $(this),
				item = {
					title: $this.find("title").text(),
					link: $this.find("link").text(),
					description: $this.find("description").text(),
					pubDate: $this.find("pubDate").text(),
					author: $this.find("author").text()
			}
			//console.log(item)
		});
	});

}

