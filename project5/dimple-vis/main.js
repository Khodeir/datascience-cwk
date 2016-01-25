d3.csv("stock_data.csv", function (data) {
  var startDate = new Date("2014-06-01");
  var endDate = new Date("2016-01-01");
   data = data.filter(function(d){
    var date = new Date(d.Date);
    return (date<endDate) & (date>startDate);
   });
  var size_x = 850;
  var size_y = 400;
  var svg = dimple.newSvg('#mainChartContainer', size_x, size_y);
  var chart = new dimple.chart(svg, data);
  chart.setBounds(size_x*.1, size_y*.1,  size_x*.7, size_y*.7);
  var x = chart.addTimeAxis("x", "Date", "%Y-%m-%d", "%b %Y");
  var z = chart.addMeasureAxis("z", "Tons available at start of month");
  var y = chart.addMeasureAxis("y", "Tons sold all month");
  var line = chart.addSeries(null, dimple.plot.line);
  var bubble = chart.addSeries(null, dimple.plot.bubble);

  line.addEventHandler('mouseover', function(){

  });

  chart.draw();

  function scale_z(datum, accessor){
    var r;
    if(accessor===true){
      r = datum;
    }
    else{
      r = datum['r'];
    }
    
    return 20*Math.sqrt(r)/63;
  }

  bubble.shapes.attr('r', scale_z);

  var offset_x = size_x*.88;
  var offset_y = size_y*.3;
  
  var label1 = scale_z(500, true);
  var label2 = scale_z(1500, true);
  var label3 = scale_z(4500, true);

  chart.svg.insert('text')
                .attr('class','legendtext legendtitle')
                .text("Stock at start of month")
                .attr("transform","translate("+(size_x*.86-10) +"," + (offset_y-label1-10) + ")");

  chart.svg.insert('circle')
                .attr('class','legendcircles')
                .attr('r', label1)
                .attr("transform","translate("+offset_x+"," + offset_y + ")");
  chart.svg.insert('text')
                .attr('class','legendtext')
                .text("500 T")
                .attr("transform","translate("+(5+label3+offset_x) +"," + (5+offset_y) + ")");

  chart.svg.insert('circle')
                .attr('class','legendcircles')
                .attr('r', label2)
                .attr("transform","translate("+offset_x+"," + (offset_y+label2+label1+5) + ")");
  chart.svg.insert('text')
                .attr('class','legendtext')
                .text("1500 T")
                .attr("transform","translate("+(5+label3+offset_x) +"," + (offset_y+label2+label1+5+5) + ")");

  chart.svg.insert('circle')
                .attr('class','legendcircles')
                .attr('r', label3)
                .attr("transform","translate("+offset_x+"," + ((offset_y+label2+label1+5) + label3+label2+5) + ")");
  
  chart.svg.insert('text')
                .attr('class','legendtext')
                .text("4500 T")
                .attr("transform","translate("+(5+label3+offset_x) +"," + ((offset_y+label2+label1+5) + label3+label2+5+5) + ")");

  x.shapes.selectAll("text").attr("transform",
    function (d) {
      return d3.select(this).attr("transform") + " translate(0, 20) rotate(-45)";
    });

});
