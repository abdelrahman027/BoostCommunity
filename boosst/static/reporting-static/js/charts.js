/****************************** Task progress Chart ********************************/
import "https://code.jquery.com/jquery-3.7.1.min.js";

$(".progress_bar").each(function () {

    var $bar = $(this).find(".bar");
    var $val = $(this).find("span");
    var perc = parseInt($val.text(), 10);

    $({ p: 0 }).animate({ p: perc }, {
        duration: 3000,
        easing: "swing",
        step: function (p) {
            $bar.css({
                transform: "rotate(" + (45 + (p * 1.8)) + "deg)", // 100%=180° so: ° = % * 1.8
                // 45 is to add the needed rotation to have the green borders at the bottom
            });
            $val.text(p | 0);
        }
    });
});

/****************************** Progress Chart ********************************/

{
    const xValues = ["completed", "Not completed", "In progress"];
    const yValues = [85, 19, 44];
    const barColors = [
        "#58508D",
        "#00314B",
        "#BC5090",
    ];

    new Chart("progressChart", {
        type: "doughnut",
        data: {
            labels: xValues,
            datasets: [{
                backgroundColor: barColors,
                data: yValues
            }]
        },
    });
}
/****************************** Work load Disruption Chart ********************************/

{
    const xValues = ["Abudabi", "Dubai", "Egypt"];
    const yValues = [55, 24, 15];
    const barColors = [
        "#58508D",
        "#00314B",
        "#BC5090",
    ];

    new Chart("WorkloadDisruptionChart", {
        type: "pie",
        data: {
            labels: xValues,
            datasets: [{
                backgroundColor: barColors,
                data: yValues
            }]
        },
        options: {
            title: {
                display: true,
            }
        }
    });
}
/****************************** Sales Chart ********************************/

var ctx = document.getElementById("myChart").getContext('2d');

var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ["January", "February", "March", "April"],
        datasets: [{
            label: 'Series 1', // Name the series
            data: [5, 87, 120, 66], // Specify the data values array
            fill: true,
            borderColor: '#58508D', // Add custom color border (Line)
            backgroundColor: '#58508D', // Add custom color background (Points and Fill)
            borderWidth: 1 // Specify bar border width
        },
        {
            label: 'Series 2', // Name the series
            data: [12, 54, 35, 77], // Specify the data values array
            fill: true,
            borderColor: '#FFA600', // Add custom color border (Line)
            backgroundColor: '#FFA600', // Add custom color background (Points and Fill)
            borderWidth: 1 // Specify bar border width
        }, {
            label: 'Series 2', // Name the series
            data: [55, 84, 34, 14], // Specify the data values array
            fill: true,
            borderColor: '#FF6361', // Add custom color border (Line)
            backgroundColor: '#FF6361', // Add custom color background (Points and Fill)
            borderWidth: 1 // Specify bar border width
        }]
    },
    options: {
        responsive: true, // Instruct chart js to respond nicely.
        maintainAspectRatio: false, // Add to prevent default behaviour of full-width/height 
    }
});
/**************************************** Department performance ************************************************/
// Sample data for the chart
const departmentData = {
    labels: ['January', 'February', 'March', 'April', 'May'],
    datasets: [
        {
            label: ['Completed', 'Not completed', 'In progress'],
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1,
            data: [120, 150, 180, 90, 200]
        }
    ]
};

// Configuration options for the chart
const departmentOptions = {
    scales: {
        y: {
            beginAtZero: true
        }
    }
};

// Create the chart
const ctx2 = document.getElementById('departmentPerformance').getContext('2d');
new Chart(ctx2, {
    type: 'bar',
    data: departmentData,
    options: departmentOptions
});

/**************************************** highest_reporting_chart ************************/
const highData = [
    { id: 1, region: 'USA', value: 12, image: "../images/employee.jpg" },
    { id: 2, region: 'China', value: 16, image: "../images/employee2.png" },
    { id: 3, region: 'Germany', value: 10, image: "../images/employee3.png" }
];

const margins = { horizontal: 20, vertical: 20 };
const chartWidth = 400 - (margins.horizontal * 2);
const chartHeight = 320 - (margins.vertical * 2);

const chartContainer = d3
    .select('#high_report')
    .attr('width', chartWidth + (margins.horizontal))
    .attr('height', chartHeight + (margins.vertical));

const chart = chartContainer.append('g');

function renderHighChart(chartData) {
    const x = d3
        .scaleBand()
        .rangeRound([margins.horizontal * 2, chartWidth])
        .padding(0.1)
        .domain(chartData.map(d => d.region));
    const y = d3
        .scaleLinear()
        .range([chartHeight, 0])
        .domain([0, d3.max(chartData, d => d.value) + 3]);

    chart.selectAll('g').remove();

    chart
        .append('g')
        .call(d3.axisLeft(y).tickSizeOuter(0))
        .attr('transform', `translate(${margins.horizontal}, -${margins.vertical})`)
        .attr('color', '#4f009e');

    chart.selectAll('.bar').remove();

    chart
        .selectAll('.bar')
        .data(chartData, d => d.id)
        .enter()
        .append('rect')
        .classed('bar', true)
        .attr('width', 20)
        .attr('height', d => chartHeight - y(d.value))
        .attr('x', d => x(d.region) + 10)
        .attr('rx', 5)
        .attr('y', d => y(d.value) - 10);

    chart.selectAll('.label').remove();

    chart
        .selectAll('.label')
        .data(chartData, d => d.id)
        .enter()
        .append('image')
        .attr('xlink:href', d => d.image)
        .attr('width', 20)
        .attr('height', 20)
        .attr('x', d => x(d.region) + 10)
        .attr('y', 275)
    // .attr('text-anchor', 'middle')
    // .classed('label', true);
}

let highUnselectedIds = [];

const highListItems = d3
    .select('#data')
    .select('ul')
    .selectAll('li')
    .data(highData)
    .enter()
    .append('li');

highListItems
    .append('span')
    .text(d => d.region);

highListItems
    .append('input')
    .attr('type', 'checkbox')
    .attr('checked', true)
    .on('change', (data) => {
        if (highUnselectedIds.indexOf(data.id) === -1) {
            highUnselectedIds.push(data.id);
        } else {
            highUnselectedIds = highUnselectedIds.filter(id => id !== data.id);
        }

        const newData = highData.filter(d => !highUnselectedIds.includes(d.id));

        renderHighChart(newData);
    });

renderHighChart(highData);


/**************************************** highest_reporting_chart ************************/
const lowData = [
    { id: 1, region: 'USA', value: 12, image: "../images/employee.jpg" },
    { id: 2, region: 'China', value: 16, image: "../images/employee2.png" },
    { id: 3, region: 'Germany', value: 10, image: "../images/employee3.png" }
];

const lowMargins = { horizontal: 20, vertical: 20 };
const lowChartWidth = 400 - (lowMargins.horizontal * 2);
const lowChartHeight = 320 - (lowMargins.vertical * 2);

const lowChartContainer = d3
    .select('#low_report')
    .attr('width', lowChartWidth + (lowMargins.horizontal))
    .attr('height', lowChartHeight + (lowMargins.vertical));

const lowChart = lowChartContainer.append('g');

function renderLowChart(chartData) {
    const x = d3
        .scaleBand()
        .rangeRound([lowMargins.horizontal * 2, lowChartWidth])
        .padding(0.1)
        .domain(chartData.map(d => d.region));
    const y = d3
        .scaleLinear()
        .range([lowChartHeight, 0])
        .domain([0, d3.max(chartData, d => d.value) + 3]);

    lowChart.selectAll('g').remove();

    lowChart
        .append('g')
        .call(d3.axisLeft(y).tickSizeOuter(0))
        .attr('transform', `translate(${lowMargins.horizontal}, -${lowMargins.vertical})`)
        .attr('color', '#FFA600');

    lowChart.selectAll('.bar').remove();

    lowChart
        .selectAll('.bar')
        .data(chartData, d => d.id)
        .enter()
        .append('rect')
        .classed('bar', true)
        .attr('width', 20)
        .attr('height', d => lowChartHeight - y(d.value))
        .attr('x', d => x(d.region) + 10)
        .attr('ry', 5)
        .attr('y', d => y(d.value) - 10);

    lowChart.selectAll('.label').remove();

    lowChart
        .selectAll('.label')
        .data(chartData, d => d.id)
        .enter()
        .append('image')
        .attr('xlink:href', d => d.image)
        .attr('width', 20)
        .attr('height', 20)
        .attr('x', d => x(d.region) + 10)
        .attr('y', 275)
    // .attr('text-anchor', 'middle')
    // .classed('label', true);
}

let unselectedIds = [];

const lowListItems = d3
    .select('#data')
    .select('ul')
    .selectAll('li')
    .data(lowData)
    .enter()
    .append('li');

lowListItems
    .append('span')
    .text(d => d.region);

lowListItems
    .append('input')
    .attr('type', 'checkbox')
    .attr('checked', true)
    .on('change', (data) => {
        if (unselectedIds.indexOf(data.id) === -1) {
            unselectedIds.push(data.id);
        } else {
            unselectedIds = unselectedIds.filter(id => id !== data.id);
        }

        const newData = lowData.filter(d => !unselectedIds.includes(d.id));

        renderLowChart(newData);
    });

renderLowChart(lowData);
