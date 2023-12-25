/**
 * CONSTANTS
 */
const BASE_API_URL = 'http://127.0.0.1:8000';


$(document).ready(function () {
    /**
     * Activate tooltip everywhere
     */
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    });


    /**
     * whoami
     */
    $.ajax({
        url: BASE_API_URL + '/whoami/',
        dataType: 'json',
        success: function (response) {
            $('.profile-name h5').text(response['result']);
        },
        error: function () {
            console.error("Error fetching data:", error);
        }
    });

    /**
     * ifconfig
     */
    $.ajax({
        url: BASE_API_URL + '/ifconfig/',
        dataType: 'json',
        success: function (response) {
            let localIp = response['result']['inet'];
            $('.profile-name p').text(localIp);

            // scanPort
            scanPort(localIp);
        },
        error: function () {
            console.error("Error fetching data:", error);
        }
    });


    /**
     * openports
     */
    const scanPort = (hostname) => {
        $.ajax({
            url: BASE_API_URL + '/scan-port/?hostname=' + hostname,
            dataType: 'json',
            success: function (response) {
                console.log(response['result']);
                let tbody = $('#tuxHomepageOpenPorts tbody');

                $.each(response['result'], function (index, item) {
                    let newRow = $('<tr>');
                    if (item['aliveStatus']) {
                        newRow.append(`<td>${item}</td>`);
                        newRow.append(`<td>${item}</td>`);

                        <td><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#46c35f" class="bi bi-circle-fill" viewBox="0 0 16 16"> <circle cx="8" cy="8" r="8" /></svg>1, 5, 7, 8, 10, 12, 20, 200</td>
                    }
                    tbody.append(newRow);
                });




            },
            error: function () {
                console.error("Error fetching data:", error);
            }
        });
    };


    /**
     * for 'tuxBattery'
     */
    $.ajax({
        url: BASE_API_URL + '/sensors/battery/',
        dataType: 'JSON',
        success: function (data) {
            // percent left
            let percent = data['result']['percent'].toFixed(2);
            $('#tuxBattery a').attr('data-bs-original-title', `${percent}% remaining`)

            // If power is plugged
            if (data['result']['power_plugged']) {
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
