$(document).ready(function () {
    const ctx = document.getElementById('tuxCpuAsync').getContext('2d');
    const cpuChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: Array.from({ length: 10 }, (_, i) => i), // Assuming initial labels from 0 to 9
            datasets: Array.from({ length: 6 }, (_, index) => ({
                label: `Core ${index + 1}`,
                borderColor: getRandomColor(),
                data: generateRandomWalk(10), // Generate initial random walk data
                fill: false,
            })),
        },
        options: {
            plugins: {
                legend: {
                    display: true,
                    position: 'right',
                }
            },
            scales: {
                x: {
                    type: 'linear',
                    position: 'bottom',
                },
            },
        },
    });

    // Set up periodic updates every 2000 milliseconds (adjust as needed)
    const updateInterval = setInterval(() => {
        updateRandomWalkData(); // Trigger an update by generating new random walk data
    }, 2000);

    // Helper function to generate random walk data
    function generateRandomWalk(length) {
        let data = [Math.random() * 100]; // Initial random value
        for (let i = 1; i < length; i++) {
            data.push(data[i - 1] + (Math.random() - 0.5) * 20); // Increased fluctuation (adjust as needed)
        }
        return data;
    }

    // Function to update random walk data without smoothing
    function updateRandomWalkData() {
        const labels = cpuChart.data.labels;

        labels.push(labels.length);

        cpuChart.data.datasets.forEach((dataset, index) => {
            dataset.data.push(dataset.data[dataset.data.length - 1] + (Math.random() - 0.5) * 20); // Increased fluctuation (adjust as needed)

            if (dataset.data.length > 10) {
                dataset.data.shift();
            }
        });

        cpuChart.update();
    }

    // Helper function to generate random colors
    function getRandomColor() {
        const letters = '0123456789ABCDEF';
        let color = '#';
        for (let i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    }

    // Handle cleanup on document unload
    $(window).on('unload', function () {
        clearInterval(updateInterval); // Stop the update interval on page unload
    });
});
