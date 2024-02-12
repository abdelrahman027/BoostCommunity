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
            borderColor: '#2196f3', // Add custom color border (Line)
            backgroundColor: '#2196f3', // Add custom color background (Points and Fill)
            borderWidth: 1 // Specify bar border width
        },
        {
            label: 'Series 2', // Name the series
            data: [12, 54, 35, 77], // Specify the data values array
            fill: true,
            borderColor: '#4CAF50', // Add custom color border (Line)
            backgroundColor: '#4CAF50', // Add custom color background (Points and Fill)
            borderWidth: 1 // Specify bar border width
        }, {
            label: 'Series 2', // Name the series
            data: [55, 84, 34, 14], // Specify the data values array
            fill: true,
            borderColor: '#888', // Add custom color border (Line)
            backgroundColor: '#888', // Add custom color background (Points and Fill)
            borderWidth: 1 // Specify bar border width
        }]
    },
    options: {
        responsive: true, // Instruct chart js to respond nicely.
        maintainAspectRatio: false, // Add to prevent default behaviour of full-width/height 
    }
});