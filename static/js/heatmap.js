// set the dimensions and margins of the graph
let buildHeatMap = (data) => {
    let margin = {top: 80, right: 25, bottom: 30, left: 40},
        width = 250 - margin.left - margin.right,
        height = 400 - margin.top - margin.bottom;

// append the svg object to the body of the page
    let svg = d3.select("#svg_heatmap")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

        // Labels of row and columns -> unique identifier of the column called 'group' and 'letiable'
        let myGroups = d3.map(data, function (d) {
            console.log(d)
            return d.team_name;
        })
        let mylets = d3.map(data, function (d) {
            return d.num_players;
        })

        // Build X scales and axis:
        let x = d3.scaleBand()
            .range([0, width])
            .domain(myGroups)
            .paddingInner(0.3) // Adjust the inner padding between bands
    .paddingOuter(0.3);
       svg.append("g")
    .style("font-size", 15)
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x).tickSize(0))
    .selectAll("text")
    .style("text-anchor", "end") // align labels to the end
    .attr("dx", "-.8em") // set x-offset to adjust positioning
    .attr("dy", ".15em") // set y-offset to adjust positioning
    .attr("transform", "rotate(-70)"); // rotate labels by -70 degrees

svg.select(".domain").remove(); // remove the axis line


        // Build Y scales and axis:
        let y = d3.scaleBand()
            .range([height, 0])
            .domain(mylets)
            .padding(0.05);
        svg.append("g")
            .style("font-size", 15)
            .call(d3.axisLeft(y).tickSize(0))
            .select(".domain").remove()



        // Build color scale
        let myColor = d3.scaleSequential()
            .interpolator(d3.interpolateInferno)
            .domain([1, 100])

        // create a tooltip
        let tooltip = d3.select("#svg_heatmap")
            .append("div")
            .style("opacity", 0)
            .attr("class", "tooltip")
            .style("background-color", "white")
            .style("border", "solid")
            .style("border-width", "2px")
            .style("border-radius", "5px")
            .style("padding", "5px")

        // Three function that change the tooltip when user hover / move / leave a cell
        let mouseover = function (d) {
            tooltip
                .style("opacity", 1)
            d3.select(this)
                .style("stroke", "black")
                .style("opacity", 1)
        }
        let mousemove = function (d) {
            tooltip
                .html("The exact value of<br>this cell is: " + d.num_players)
                .style("left", (d3.mouse(this)[0] + 70) + "px")
                .style("top", (d3.mouse(this)[1]) + "px")
        }
        let mouseleave = function (d) {
            tooltip
                .style("opacity", 0)
            d3.select(this)
                .style("stroke", "none")
                .style("opacity", 0.8)
        }

        // add the squares
        svg.selectAll()
            .data(data, function (d) {
                return d.team_name + ':' + d.num_players;
            })
            .enter()
            .append("rect")
            .attr("x", function (d) {
                return x(d.team_name)
            })
            .attr("y", function (d) {
                return y(d.num_players)
            })
            .attr("rx", 4)
            .attr("ry", 4)
            .attr("width", x.bandwidth())
            .attr("height", y.bandwidth())
            .style("fill", function (d) {
                return myColor(d.num_players)
            })
            .style("stroke-width", 4)
            .style("stroke", "none")
            .style("opacity", 0.8)
            .on("mouseover", mouseover)
            .on("mousemove", mousemove)
            .on("mouseleave", mouseleave)
    

// Add title to graph
    svg.append("text")
        .attr("x", 0)
        .attr("y", -50)
        .attr("text-anchor", "left")
        .style("font-size", "22px")
        .text("A d3.js heatmap");

// Add subtitle to graph
    svg.append("text")
        .attr("x", 0)
        .attr("y", -20)
        .attr("text-anchor", "left")
        .style("font-size", "14px")
        .style("fill", "grey")
        .style("max-width", 400)
        .text("A short description of the take-away message of this chart.");
}