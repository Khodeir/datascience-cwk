d3.csv("stock_data.csv", function (data) {
  var startDate = new Date("2014-06-01");
  var endDate = new Date("2016-01-01");
   data = data.filter(function(d){
    var date = new Date(d.Date);
    return (date<endDate) & (date>startDate);
   });
  var svg = dimple.newSvg('#mainChartContainer', "100%", "50%");
  var chart = new dimple.chart(svg, data);
  chart.setBounds("10%", "10%", "70%", "70%");
  var x = chart.addTimeAxis("x", "Date", "%Y-%m-%d", "%b %Y");
  var z = chart.addMeasureAxis("z", "Tons available at start of month");
  var y = chart.addMeasureAxis("y", "Tons sold all month")
  var line = chart.addSeries(null, dimple.plot.line);
  var bubble = chart.addSeries(null, dimple.plot.bubble);

  line.addEventHandler('mouseover', function(){

  });
  
  chart.draw();

  x.shapes.selectAll("text").attr("transform",
    function (d) {
      return d3.select(this).attr("transform") + " translate(0, 20) rotate(-45)";
    });

});
