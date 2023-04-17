$(document).ready(function() {
	
	// Area Chart
	
    Morris.Area({
		element: 'area-charts',
		data: [
			{ y: '2006', a: 100, b: 90 },
			{ y: '2007', a: 75,  b: 65 },
			{ y: '2008', a: 50,  b: 40 },
			{ y: '2009', a: 75,  b: 65 },
			{ y: '2010', a: 50,  b: 40 },
			{ y: '2011', a: 75,  b: 65 },
			{ y: '2012', a: 100, b: 90 }
		],
		xkey: 'y',
		ykeys: ['a', 'b'],
		labels: ['Laptop/computer', 'Phone'],
		lineColors: ['#A6F0C6','#95BDFF'],
		lineWidth: '3px',
		resize: true,
		redraw: true
    });

	// Bar Chart
	
	Morris.Bar({
		element: 'bar-charts',
		data: [
			{ y: 'Football', a: 80},
			{ y: 'Chess', a: 65 },
			{ y: 'Watermelon farm', a: 30},
			{ y: 'Tarak Mehta', a: 75},
			{ y: 'swimming', a: 50},
			{ y: 'Man vs Wild', a: 25 },
			{ y: 'Nike Launches', a: 40}
		],
		xkey: 'y',
		ykeys: ['a'],
		labels: ['Time Spent [mins]',],
		lineColors: ['#00c5fb','#0253cc'],
		lineWidth: '3px',
		barColors: ['#74AC4A'],
		resize: true,
		redraw: true
	});
	
	// Line Chart
	
	Morris.Line({
		element: 'line-charts',
		data: [
			{ y: '2006', a: 50, b: 90 },
			{ y: '2007', a: 75,  b: 65 },
			{ y: '2008', a: 50,  b: 40 },
			{ y: '2009', a: 75,  b: 65 },
			{ y: '2010', a: 50,  b: 40 },
			{ y: '2011', a: 75,  b: 65 },
			{ y: '2012', a: 100, b: 50 }
		],
		xkey: 'y',
		ykeys: ['a', 'b'],
		labels: ['Laptop/computer', 'Phone'],
		lineColors: ['#95BDFF','#74AC4A'],
		lineWidth: '3px',
		resize: true,
		redraw: true
	});
	
	// Donut Chart
		
	Morris.Donut({
		element: 'pie-charts',
		colors: [
			'#50CB93',
			'#74AC4A',
			'#ACFFAD',
			'#71EFA3'
		],
		data: [
			{label: "Youtube.com", value: 40},
			{label: "chess.com", value: 25},
			{label: "Modernfarmer.com", value: 30},
			{label: "Ajioluxe.com", value: 15}
		],
		resize: true,
		redraw: true
	});
		
});