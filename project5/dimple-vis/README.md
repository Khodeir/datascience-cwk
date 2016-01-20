# Introduction

For my data visualization, I chose to use some real operations data from a 
client whose company sells imported raw materials to local manufacturers of
paper products.

The company operates warehouses, so my visualization will focus on the
relationship between the quantity of their warehoused goods and their sales.

# Design

The data consists of monthly sales for each product, as well as the stock
available for each product at the beginnning of the month.

## Initial Design

I experimented with different chart types. To start off with, I used a stacked
bar chart to show monthly stock on hand. This had months on the x axis, color
indicating product id, and bar size indicating quantity. The resulting graph
was hard to read and the number of colors distracting and uninformative.
Furthermore, the graph was already saturated without even incorporating the
sales data, so I iterated without resorting to external feedback. 
(This version can be seen at commit b599a7e6f8381c741c69c4a962fd0f188708df4e).

My next attempt was to use a bubble chart with months on the x-axis, total
sales on the y-axis, and the size of the circles encoding the total stock on
hand. This was a much more informative visualization, showing clearly the
relationship between sales and warehouse size over time. I then added a
description and shared this version with the client for feedback.
(This version can be seen at commit b74ba431296aae90d47d279de20a5dc86974dfde).

### Feedback

* (Company Owner) This is great. I had an intuition about this problem, but 
seeing it visually is really useful validation. We really want to be more like
we were back in June (2015).
* (Head of sales) I see the problem. Well, we're in a really good position for
bumping up sales in January, but I don't think we're likely to exceed 1200 tons
this month.
* (Head of purchasing) I'd like to know what products were in stock in these
months, maybe we can do better at stocking the right products.