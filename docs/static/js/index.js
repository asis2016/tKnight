$(document).ready(function () {
    /**
     * for tuxHomeLsof
     */
    $.ajax({
        url: BASE_API_URL + '/lsof.n.i.json',
        dataType: 'JSON',
        success: function (response) {
            $('#tuxHomeLsof h3').text(response['total'] + ' lsof');
        },
        error: function () {
            console.error('Error fetching data:', error);
        }
    });

    /**
     * for tuxOSRelease
     */
    $.ajax({
        url: BASE_API_URL + '/os-release.json',
        dataType: 'JSON',
        success: function (response) {
            $('#tuxOSRelease h3').text(response['result']['NAME']);
            $('#tuxOSRelease p').text(response['result']['VARIANT'] + ' v' + response['result']['VERSION_ID']);
        },
        error: function () {
            console.error('Error fetching data:', error);
        }
    });

    /**
     * for tuxBoottime
     */
    $.ajax({
        url: BASE_API_URL + '/boottime.json',
        dataType: 'JSON',
        success: function (response) {
            $('#tuxBoottime p').text(response['result']);
        },
        error: function () {
            console.error('Error fetching data:', error);
        }
    });


    /**
     * for tuxHomepageCpuCore
     */
    $.ajax({
        url: BASE_API_URL + '/cpu.count.json',
        dataType: 'JSON',
        success: function (response) {
            $('#tuxHomepageCpuCore a').text(response['result'] + ' core CPUs');
        },
        error: function () {
            console.error('Error fetching data:', error);
        }
    });

    /**
     * for tuxHomepageSensors
     */
    $.ajax({
        url: BASE_API_URL + '/sensors.temperature.json',
        dataType: 'JSON',
        success: function (response) {
            $('#tuxHomepageSensors a').text(response['total'] + ' sensors');
        },
        error: function () {
            console.error('Error fetching data:', error);
        }
    });

    /**
     * for tuxHomepageEnviron
     */
    $.ajax({
        url: BASE_API_URL + '/environ.json',
        dataType: 'JSON',
        success: function (response) {
            $('#tuxHomepageEnviron a').text(response['total'] + ' env found');
        },
        error: function () {
            console.error('Error fetching data:', error);
        }
    });


    

    /**
     * GET users/
     */
    $.ajax({
        url: BASE_API_URL + '/users.json',
        dataType: 'JSON',
        success: function (data) {

            let name = data['result']['name'];
            let terminal = data['result']['terminal'];
            let host = data['result']['host'];
            let started = data['result']['started'];
            let pid = data['result']['pid'];

            //For ifconfig-and-users-stat.html
            $('#ifconfigAndUserStat .name').text(name);
            $('#ifconfigAndUserStat .pid').text(pid);
            $('#ifconfigAndUserStat .terminal').text(terminal);
            $('#ifconfigAndUserStat .host').text(host);
            $('#ifconfigAndUserStat .started').text(started + ' secs.');

        },
        error: function () {
            console.error('Failed to fetch external IP address');
        }
    });


    


    /**
     * for tuxHomepageProcesses
     */
    $.ajax({
        url: BASE_API_URL + '/ps.json',
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
     * for tuxDisk > Disk partition
     */
    $.ajax({
        url: BASE_API_URL + '/disk.partition.json',
        dataType: 'JSON',
        success: function (response) {
            let tbody = $('#tuxDiskPartition tbody');

            $.each(response['result'], function (index, item) {
                var newRow = $('<tr>');

                // Append cells to the row
                newRow.append('<td>' + item['Filesystem'] + '</td>');
                newRow.append('<td>' + item['Size'] + '</td>');
                newRow.append('<td class="only-d-lg">' + item['Used'] + '</td>');
                newRow.append('<td class="only-d-lg">' + item['Avail'] + '</td>');
                //newRow.append('<td>' + item['Use%'] + '</td>');
                newRow.append(`<td><div class="progress"><div class="progress-bar bg-info" role="progressbar" style="width: ${item['Use%']};"></div></div></td>`);
                newRow.append('<td class="only-d-lg">' + item['Mounted on'] + '</td>');
                newRow.append('</tr>');

                // Append the row to the tbody
                tbody.append(newRow);
            });
        },
        error: function () {
            console.error('Error fetching data:', error);
        }
    });

    /**
     * for "tuxSpeedTest"
     */
    $("#tuxSpeedTest button").on("click", function () {

        $("#tuxSpeedTest .txtPing").text("running speed test ...");

        $.ajax({
            url: BASE_API_URL + '/speed-test.json',
            dataType: 'JSON',
            success: function (response) {
                let ping = response['result'].ping
                let upload = response['result'].upload
                let download = response['result'].download

                $("#tuxSpeedTest .txtUpSpeed span").text(upload);
                $("#tuxSpeedTest .txtDownSpeed span").text(download);
                $("#tuxSpeedTest .txtPing").text(`Ping took about ${ping}.`);
            },
            error: function () {
                console.error('Failed to fetch external IP address');
            }
        });
    });

    /**
     * for "tuxPublicIPDetailMap"
     */
    $.ajax({
        url: 'https://raw.githubusercontent.com/asis2016/tKnight/main/backend/dummyJson/ip.api.json',
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
     * for tuxHomepageSystemctlServices
     */
    $.ajax({
        url: BASE_API_URL + '/systemctl.services.json',
        dataType: 'JSON',
        success: function (response) {
            var tbody = $('#tuxHomepageSystemctlServices tbody');

            $.each(response['result'], function (index, item) {
                var newRow = $('<tr>');
                newRow.append('<td>' + item['unit'] + '</td>');
                newRow.append(`<td><div class="badge badge-outline-${item['active']}">${item['active']}</div></td>`);
                newRow.append('<td>' + item['sub'] + '</td>');
                // Append the row to the tbody
                tbody.append(newRow);

                // only 10 of it.
                if (index >= 7) {
                    return false; // This will break out of the $.each loop
                }
            });
        },
        error: function () {
            console.error('Error fetching data:', error);
        }
    });
    // tuxHomepageSystemctlServices ends
});