$(document).ready(function () {
    /**
     * for tuxHomeLsof
     */
    $.ajax({
        url: BASE_API_URL + '/lsof/n/i/',
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
        url: BASE_API_URL + '/os-release/',
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
        url: BASE_API_URL + '/boottime/',
        dataType: 'JSON',
        success: function (response) {
            $('#tuxBoottime p').text(response['result']);
        },
        error: function () {
            console.error('Error fetching data:', error);
        }
    });


    /**
     * GET ifconfig
     * And scanMyPorts
     */
    $.ajax({
        url: BASE_API_URL + '/ifconfig/',
        dataType: 'JSON',
        success: function (data) {

            let inet = data['result']['inet'];
            let inet6 = data['result']['inet6'][0];
            let ether = data['result']['ether'];
            let netmask = data['result']['netmask'];
            let broadcast = data['result']['broadcast'];
            let device = data['result']['device'];

            $('#scanMyPorts').attr('href', '/scan-port?hostname=' + inet);

            //For ifconfig-and-users-stat.html
            $('#ifconfigAndUserStat .ipv4').text(inet);
            $('#ifconfigAndUserStat .ipv6').text(inet6);
            $('#ifconfigAndUserStat .netmask').text(netmask);
            $('#ifconfigAndUserStat .broadcast').text(broadcast);
            $('#ifconfigAndUserStat .ether').text(ether);
            $('#ifconfigAndUserStat .device').text(device);

        },
        error: function () {
            console.error('Failed to fetch external IP address');
        }
    });

    /**
     * GET users/
     */
    $.ajax({
        url: BASE_API_URL + '/users/',
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
     * for tuxDisk > Disk usage
     */

    // Utils
    function bytesToGB(bytes) {
        if (bytes === 0) return '0 GB';
        const gigabytes = bytes / (1024 * 1024 * 1024);
        return gigabytes.toFixed(2);
    }

    $.ajax({
        url: BASE_API_URL + '/disk/usage/',
        dataType: 'JSON',
        success: function (response) {
            let totalDiskUsageInBytes = bytesToGB(response['result']['total']);
            let usedDiskUsageInBytes = bytesToGB(response['result']['used']);
            let freeDiskUsageInBytes = bytesToGB(response['result']['free']);
            let freeDiskUsageInPercentage = response['result']['percent'];

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
     * for tuxDisk > Disk partition
     */
    $.ajax({
        url: BASE_API_URL + '/disk/partition/',
        dataType: 'JSON',
        success: function (response) {
            let tbody = $('#tuxDiskPartition tbody');

            $.each(response['result'], function (index, item) {
                var newRow = $('<tr>');

                // Append cells to the row
                newRow.append('<td>' + item['Filesystem'] + '</td>');
                newRow.append('<td>' + item['Size'] + '</td>');
                newRow.append('<td>' + item['Used'] + '</td>');
                newRow.append('<td>' + item['Avail'] + '</td>');
                //newRow.append('<td>' + item['Use%'] + '</td>');
                newRow.append(`<td><div class="progress"><div class="progress-bar bg-info" role="progressbar" style="width: ${item['Use%']};"></div></div></td>`);
                newRow.append('<td>' + item['Mounted on'] + '</td>');
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
     * for 'tuxPublicIPAddress'
     */
    $.ajax({
        url: 'https://ifconfig.me/ip',
        dataType: 'text',
        success: function (data) {
            //display block
            $('#tuxPublicIPAddress').attr('style', 'display: block !important');
            $('#tuxPublicIPAddress h3').text(data.trim());
        },
        error: function () {
            console.error('Failed to fetch external IP address');
        }
    });


    /**
     * for 'tuxPublicIPDetails'
     */
    $.ajax({
        url: 'http://ip-api.com/json',
        dataType: 'JSON',
        success: function (data) {
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
     * for "tuxSpeedTest"
     */
    $("#tuxSpeedTest button").on("click", function () {

        $("#tuxSpeedTest .txtPing").text("running speed test ...");

        $.ajax({
            url: BASE_API_URL + '/speed-test/',
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
     * for "tuxHomepageOpenPorts"
     */
    $.ajax({
        url: 'http://ip-api.com/json',
        dataType: 'JSON',
        success: function (data) {
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
});