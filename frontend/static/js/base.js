$(document).ready(function () {
    const BASE_API_URL = 'http://127.0.0.1:8000/';

    /**
     * Activate tooltip everywhere
     */
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    })

    /**
     * for 'tuxBattery'
     */
    $.ajax({
        url: BASE_API_URL + 'sensors/battery',
        dataType: 'JSON',
        success: function (data) {
            // percent left
            let percent = data.data.percent.toFixed(2);
            $('#tuxBattery a').attr('data-bs-original-title', `${percent}% remaining`)

            // If power is plugged
            if (data.data.power_plugged) {
                $('#tuxBattery .mdi').addClass('mdi-battery-charging-80 text-success');
            } else {
                $('#tuxBattery .mdi').addClass('mdi-battery-60');
            }
        },
        error: function () {
            console.error('Failed to fetch battery sensor data');
        }
    });
});
