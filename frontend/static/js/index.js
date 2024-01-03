$(document).ready(function () {
    /**
     * for tuxHomeLsof
     */
    $.ajax({
        url: BASE_API_URL + '/lsof/n/i/',
        dataType: 'json',
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
        dataType: 'json',
        success: function (response) {
            $('#tuxOSRelease h3').text(response['result']['NAME']);
            $('#tuxOSRelease p').text('v' + response['result']['VERSION_ID']);
            $('#tuxOSRelease .small').text(response['result']['VARIANT']);
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
        dataType: 'json',
        success: function (response) {
            $('#tuxBoottime h6').text(response['result']);
        },
        error: function () {
            console.error('Error fetching data:', error);
        }
    });


    /**
     * for tuxDisk > Disk usage
     */
    $.ajax({
        url: BASE_API_URL + '/disk/usage/',
        dataType: 'json',
        success: function (response) {
            let totalDiskUsageInBytes = bytesToGB(response['result']['total']);
            let usedDiskUsageInBytes = bytesToGB(response['result']['used']);
            let freeDiskUsageInBytes = bytesToGB(response['result']['free']);
            let freeDiskUsageInPercentage = response['result']['percent'];

            // Utils
            function bytesToGB(bytes) {
                if (bytes === 0) return '0 GB';
                const gigabytes = bytes / (1024 * 1024 * 1024);
                return gigabytes.toFixed(2);
            }


            if ($('#diskUsageCanvas').length) {
                var areaData = {
                    labels: ['Total (GB)', 'Used (GB)', 'Free (GB)'],
                    datasets: [{
                        data: [totalDiskUsageInBytes, usedDiskUsageInBytes, freeDiskUsageInBytes],
                        backgroundColor: ['#111111', '#00d25b', '#ffab00']
                    }]
                };
                var areaOptions = {
                    responsive: true,
                    maintainAspectRatio: true,
                    segmentShowStroke: false,
                    cutoutPercentage: 70,
                    elements: {
                        arc: {
                            borderWidth: 0
                        }
                    },
                    legend: {
                        display: false
                    },
                    tooltips: {
                        enabled: true
                    }
                }
                var transactionhistoryChartPlugins = {
                    beforeDraw: function (chart) {
                        var width = chart.chart.width,
                            height = chart.chart.height,
                            ctx = chart.chart.ctx;

                        ctx.restore();
                        var fontSize = 1;
                        ctx.font = fontSize + 'rem sans-serif';
                        ctx.textAlign = 'left';
                        ctx.textBaseline = 'middle';
                        ctx.fillStyle = '#ffffff';

                        var text = freeDiskUsageInPercentage + '% GB',
                            textX = Math.round((width - ctx.measureText(text).width) / 2),
                            textY = height / 2.4;

                        ctx.fillText(text, textX, textY);

                        ctx.restore();
                        var fontSize = 1.5;
                        ctx.font = fontSize + 'rem sans-serif';
                        ctx.textAlign = 'left';
                        ctx.textBaseline = 'middle';
                        ctx.fillStyle = '#ffffff';

                        var texts = 'Free',
                            textsX = Math.round((width - ctx.measureText(text).width) / 1.7),
                            textsY = height / 1.7;

                        ctx.fillText(texts, textsX, textsY);
                        ctx.save();
                    }
                }
                var transactionhistoryChartCanvas = $('#diskUsageCanvas').get(0).getContext('2d');
                var transactionhistoryChart = new Chart(transactionhistoryChartCanvas, {
                    type: 'doughnut',
                    data: areaData,
                    options: areaOptions,
                    plugins: transactionhistoryChartPlugins
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
        dataType: 'json',
        success: function (response) {
            let tbody = $('#rowDiskPartition tbody');

            $.each(response['result'], function (index, item) {
                var newRow = $('<tr>');

                // Append cells to the row
                newRow.append('<td>' + item['Filesystem'] + '</td>');
                newRow.append('<td>' + item['Size'] + '</td>');
                newRow.append('<td>' + item['Used'] + '</td>');
                newRow.append('<td>' + item['Avail'] + '</td>');
                newRow.append('<td>' + item['Use%'] + '</td>');
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
        dataType: 'json',
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
            dataType: 'json',
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
        dataType: 'json',
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