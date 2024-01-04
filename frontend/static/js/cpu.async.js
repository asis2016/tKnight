$(document).ready(function () {
    const ctx = document.getElementById('tuxCpuAsync').getContext('2d');
    const cpuChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [],
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

    const socket = new WebSocket("ws://127.0.0.1:8000/cpu/async/");

    // Set up periodic updates every 500 milliseconds (adjust as needed)
    const updateInterval = setInterval(() => {
        socket.send("update"); // Trigger an update by sending a message to the server
    }, 2000);

    socket.onmessage = function (event) {
        const data = JSON.parse(event.data);

        const labels = cpuChart.data.labels;

        if (labels.length === 0) {
            cpuChart.data.labels = Array.from({ length: Object.keys(data).length }, (_, i) => i);
        }

        Object.entries(data).forEach(([core, usage], index) => {
            const dataset = cpuChart.data.datasets[index] || {
                label: core,
                borderColor: getRandomColor(),
                data: [],
                fill: false,
            };

            dataset.data.push(usage);

            if (dataset.data.length > 5) {
                dataset.data.shift();
            }

            cpuChart.data.datasets[index] = dataset;
        });

        cpuChart.update();
    };

    // Helper function to generate random colors
    function getRandomColor() {
        const letters = '0123456789ABCDEF';
        let color = '#';
        for (let i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    }

    socket.onerror = function (error) {
        console.error("WebSocket Error: ", error);
    };

    socket.onclose = function (event) {
        clearInterval(updateInterval); // Stop the update interval on connection close
        if (event.wasClean) {
            console.log(`Closed cleanly, code=${event.code}, reason=${event.reason}`);
        } else {
            console.error(`Connection died`);
        }
    };
});