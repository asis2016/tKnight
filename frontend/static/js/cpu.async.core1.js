$(document).ready(function () {
    // Initialize Chart.js
    const ctx = document.getElementById('tuxCpuAsync').getContext('2d');
    const cpuChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'CPU Usage',
                borderColor: 'rgba(75, 192, 192, 1)',
                data: [],
                fill: false,
                tension: 0.5,
                pointRadius: 0,
            }],
        },
        options: {
            scales: {
                x: [{
                    type: 'linear',
                    position: 'bottom',
                }],
                y: [{
                    ticks: {
                        beginAtZero: true,
                        max: 100,
                    },
                }],
            },
        },
    });

    // Establish WebSocket connection
    const socket = new WebSocket("ws://127.0.0.1:8000/cpu/async/");

    // Handle incoming messages
    socket.onmessage = function (event) {
        const data = JSON.parse(event.data);

        // Update chart labels and data
        const labels = cpuChart.data.labels;
        const datasets = cpuChart.data.datasets[0].data;

        labels.push(labels.length);
        datasets.push(data["Core 1"]);  // Assuming you want to show the usage of Core 1

        // Remove old data if you want to limit the number of data points
        if (labels.length > 10) {
            labels.shift();
            datasets.shift();
        }

        // Update the chart
        cpuChart.update();
    };

    // Log errors
    socket.onerror = function (error) {
        console.error("WebSocket Error: ", error);
    };

    // Log closures
    socket.onclose = function (event) {
        if (event.wasClean) {
            console.log(`Closed cleanly, code=${event.code}, reason=${event.reason}`);
        } else {
            console.error(`Connection died`);
        }
    };
});