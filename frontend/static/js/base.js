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
        dataType: 'JSON',
        success: function (response) {
            $('.tuxProfileName span').text(response['result']);
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
        dataType: 'JSON',
        success: function (response) {
            let localIp = response['result']['inet'];
            $('#tuxPublicIPAddress h3').text(localIp);
        },
        error: function () {
            console.error("Error fetching data:", error);
        }
    });


    /**
     * TODO: REFACTOR openports
     */
    // const scanPort = (hostname) => {
    //     $.ajax({
    //         url: BASE_API_URL + '/scan-port/?hostname=' + hostname,
    //         dataType: 'JSON',
    //         success: function (response) {
    //             console.log(response['result']);
    //             let tbody = $('#tuxHomepageOpenPorts tbody');

    //             $.each(response['result'], function (index, item) {
    //                 let newRow = $('<tr>');

    //                 if (item['aliveStatus']) {
    //                     newRow.append(`<td>${item}</td>`);
    //                     newRow.append(`<td>${item}</td>`);
    //                 }

    //                 tbody.append(newRow);
    //             });
    //         },
    //         error: function () {
    //             console.error("Error fetching data:", error);
    //         }
    //     });
    // };


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
                $('#tuxBattery .bi').addClass('bi-battery-charging');
            } else {
                $('#tuxBattery .bi').addClass('bi-battery-half');
            }
        },
        error: function () {
            console.error('Failed to fetch battery sensor data');
        }
    });


});
