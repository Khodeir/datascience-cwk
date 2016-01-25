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
(This version can be seen here: https://rawgit.com/Khodeir/datascience-cwk/b599a7e6f8381c741c69c4a962fd0f188708df4e/project5/dimple-vis/index.html).

My next attempt was to use a bubble chart with months on the x-axis, total
sales on the y-axis, and the size of the circles encoding the total stock on
hand. This was a much more informative visualization, showing clearly the
relationship between sales and warehouse size over time. I then added a
description and shared this version with the client for feedback.
(This version can be seen here: https://rawgit.com/Khodeir/datascience-cwk/b74ba431296aae90d47d279de20a5dc86974dfde/project5/dimple-vis/index.html).

### Feedback

#### In Company

* (Company Owner) This is great. I had an intuition about this problem, but 
seeing it visually is really useful validation. We really want to be more like
we were back in June (2015).
* (Head of sales) I see the problem. Well, we're in a really good position for
bumping up sales in January, but I don't think we're likely to exceed 1200 tons
this month.
* (Head of purchasing) I'd like to know what products were in stock in these
months, maybe we can do better at stocking the right products.

#### Discussion Boards

* The only thing that took me a while to realize was what the size of the circles means: I guess it is the stock at the beginning of month? Perhaps adding a legend could make this clearer? It also seems to me that it is the radius, rather than the area, which is proportional to the stock... this makes the stock in, for example, September look much bigger than 3-fold the stock in June. It will be exciting to learn if the attempt of increasing the revenue works out... will you keep the visualization up to date? 
(https://discussions.udacity.com/t/feedback-for-p6/45058/2?u=khodeir)

#### Acquaintances

* I think the graph's cool, but I don't think it'd be immediately obvious to people that the circles represent the warehouse stock capacity. I would also add a title to the graph even though you explain it in the first paragraph.

## Final Design

The feedback I got seemed to point first to the fact that circle size encoding needs to be explained. When I showed the visualization to clients in the company, I explained this verbally, but when I simply shared the link on discussion boards and with acquaintances, it was not immediately obvious. I therefore made a simple legend to explain it to the reader.

Second, an astute reader from Udacity's discussion board, pointed out that it was the circle radius that encoded available stock, instead of the circle area. Upon review, I decided it was better to reverse this, to allow more accurate comparisons. (Although this came at the expense of clarity for my main point.)

(This version can be viewed here: https://rawgit.com/Khodeir/datascience-cwk/e652e0fc9b0737ef2185dc9e88faf418d35215ea/project5/dimple-vis/index.html)
