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
	
	$.getJSON('/bar_data',function(data_bar){
	Morris.Bar({
		element: 'bar-charts',
		data: data_bar
		// [
		// 	{ y: data_bar[0][1], a: data_bar[1][1]},
		// 	{ y: data_bar[0][2], a: data_bar[1][2] },
		// 	{ y: data_bar[0][3], a: data_bar[1][3]},
		// 	{ y: data_bar[0][4], a: data_bar[1][4]},
		// 	{ y: data_bar[0][5], a: data_bar[1][5]},
		// 	{ y: data_bar[0][6], a: data_bar[1][6] },
		// 	{ y: data_bar[0][7], a: data_bar[1][7]}
		// ]
		,
		xkey: 'y',
		ykeys: 'a',
		labels: ['Time Spent in %',],
		lineColors: ['#00c5fb','#0253cc'],
		lineWidth: '3px',
		barColors: ['#74AC4A'],
		resize: true,
		redraw: true
	});
	});
	// Line Chart
	
	$.getJSON('/barg_data',function(data_barg){
		Morris.Bar({
			element: 'barg-charts',
			data: data_barg,
			xkey: 'y',
			ykeys: 'a',
			labels: ['count in %'],
			lineColors: ['#00c5fb','#0253cc'],
			lineWidth: '3px',
			barColors: ['#74AC4A'],
			resize: true,
			redraw: true
		});
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