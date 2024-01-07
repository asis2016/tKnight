$(document).ready(function () {

    /**
     * for "tuxPublicIPDetailMap"
     */
    $.ajax({
        url: 'http://ip-api.com/json',
        dataType: 'JSON',
        success: function (data) {

            $("#tuxPublicIPAddress h3").text(data['query']);

            //display block
            $('#tuxPublicIPDetails .ip').text(data['query']);
            $('#tuxPublicIPDetails .zip').text(data['zip']);
            $('#tuxPublicIPDetails .countryInfo .flag-icon').addClass(`flag-icon-${data['countryCode'].toLowerCase()}`);
            $('#tuxPublicIPDetails .countryInfo span').text(
                `${data['regionName']}, ${data['countryCode']}`
            );
            $('#tuxPublicIPDetails .lon').text(data['lon']);
            $('#tuxPublicIPDetails .lat').text(data['lat']);
            $('#tuxPublicIPDetails .isp').text(data['isp']);
            $('#tuxPublicIPDetails .timezone').text(data['timezone']);

            //map
            //var latLon = [data['lon'], data['lat']]

            var latLon = [data['lat'], data['lon']]
            //var latLon = [51.5, -0.09]

            const tuxPublicIPDetailMap = L.map('publicIPMap').setView(latLon, 13);

            const tiles = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
                maxZoom: 19,
                attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
            }).addTo(tuxPublicIPDetailMap);

            const marker = L.marker(latLon).addTo(tuxPublicIPDetailMap);
        },
        error: function () {
            console.error('Failed to fetch external IP address');
        }
    });


    /**
     * for tuxDisk > Disk usage
     */
    // Utils
    function bytesToGB(bytes) {
        if (bytes === 0) return '0 GB';
        const gigabytes = bytes / (1024 * 1024 * 1024);
        return gigabytes.toFixed(2);
    }

    $.ajax({
        url: BASE_API_URL + '/disk-usage/',
        dataType: 'JSON',
        success: function (response) {
            let totalDiskUsageInBytes = bytesToGB(response['total']);
            let usedDiskUsageInBytes = bytesToGB(response['used']);
            let freeDiskUsageInBytes = bytesToGB(response['free']);
            let freeDiskUsageInPercentage = response['percent'];

            // tables
            $('#tuxDisk .diskTotal').text(totalDiskUsageInBytes + ' GB');
            $('#tuxDisk .diskUsed').text(usedDiskUsageInBytes + ' GB');
            $('#tuxDisk .diskFree').text(freeDiskUsageInBytes + ' GB');

            if ($('#diskUsageCanvas').length) {
                const diskUsageChart = document.getElementById('diskUsageCanvas');
                new Chart(diskUsageChart, {
                    type: 'doughnut',
                    data: {
                        labels: ['Total (GB)', 'Used (GB)', 'Free (GB)'],
                        datasets: [{
                            data: [totalDiskUsageInBytes, usedDiskUsageInBytes, freeDiskUsageInBytes],
                            borderWidth: 0,
                            backgroundColor: ['#6610f2', '#ffda6a', '#20c997']
                        }]
                    },
                    options: {
                        plugins: {
                            legend: {
                                display: false
                            },
                            tooltip: {
                                enabled: true
                            }
                        },
                        layout: {
                            padding: {
                                left: 0,
                                right: 0,
                                top: 0,
                                bottom: 0
                            }
                        },
                        responsive: false,
                    }
                });
            }
        },
        error: function () {
            console.error('Error fetching data:', error);
        }
    });


    /**
     * for tuxHomepageProcesses (System processes)
     */
    $.ajax({
        url: BASE_API_URL + '/ps/',
        dataType: 'JSON',
        success: function (response) {
            let status_count = response['status_count'];

            if ($('#tuxHomepageProcesses').length) {
                const diskUsageChart = document.getElementById('processesCanvas');
                new Chart(diskUsageChart, {
                    type: 'bar',
                    data: {
                        labels: [
                            'Sleeping', 'Idle', 'Running'
                        ],
                        datasets: [{
                            data: [status_count['sleeping'], status_count['idle'], status_count['running']],
                            borderWidth: 0,
                            backgroundColor: ['#6610f2', '#ffda6a', '#20c997']
                        }]
                    },
                    options: {
                        indexAxis: 'y',
                        plugins: {
                            legend: {
                                display: false
                            },
                            tooltip: {
                                enabled: true
                            }
                        },
                        layout: {
                            padding: {
                                left: 0,
                                right: 0,
                                top: 0,
                                bottom: 0
                            }
                        },
                        responsive: false,
                    }
                });
            }
        },
        error: function () {
            console.error('Error fetching data:', error);
        }
    });

    /**
     * for "tuxSpeedTest"
     */
    // $("#tuxSpeedTest button").on("click", function () {

    //     $("#tuxSpeedTest .txtPing").text("running speed test ...");

    //     $.ajax({
    //         url: BASE_API_URL + '/speed-test/',
    //         dataType: 'JSON',
    //         success: function (response) {
    //             let ping = response['result'].ping
    //             let upload = response['result'].upload
    //             let download = response['result'].download

    //             $("#tuxSpeedTest .txtUpSpeed span").text(upload);
    //             $("#tuxSpeedTest .txtDownSpeed span").text(download);
    //             $("#tuxSpeedTest .txtPing").text(`Ping took about ${ping}.`);
    //         },
    //         error: function () {
    //             console.error('Failed to fetch external IP address');
    //         }
    //     });
    // });



    /**
     * for tuxHomepageSystemctlServices
     */
    // $.ajax({
    //     url: BASE_API_URL + '/systemctl/services/',
    //     dataType: 'JSON',
    //     success: function (response) {
    //         var tbody = $('#tuxHomepageSystemctlServices tbody');

    //         $.each(response['result'], function (index, item) {
    //             var newRow = $('<tr>');
    //             newRow.append('<td>' + item['unit'] + '</td>');
    //             newRow.append(`<td><div class="badge badge-outline-${item['active']}">${item['active']}</div></td>`);
    //             newRow.append('<td>' + item['sub'] + '</td>');
    //             // Append the row to the tbody
    //             tbody.append(newRow);

    //             // only 10 of it.
    //             if (index >= 7) {
    //                 return false; // This will break out of the $.each loop
    //             }
    //         });
    //     },
    //     error: function () {
    //         console.error('Error fetching data:', error);
    //     }
    // });
    // tuxHomepageSystemctlServices ends
});