var svg = dimple.newSvg("#chartContainer", 590, 400);
d3.csv("corrogated_by_month.csv", function (data) {
  
  var myChart = new dimple.chart(svg, data);

  myChart.setBounds(60, 30, 350, 330);

  var x = myChart.addTimeAxis("x", "date");

  var y = myChart.addMeasureAxis("y", "weight");

  var s = myChart.addSeries("product_name", dimple.plot.bar);
  
  s.addOrderRule(function(cand1,cand2){
    return d3.sum(cand1, 'weight') > d3.sum(cand2, 'weight');
  });

  myChart.addLegend(430, 20, 100, 300, "left");
  myChart.draw();
});