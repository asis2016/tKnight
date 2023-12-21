$(document).ready(function () {



    /**
     * for "tuxPublicIPAddress"
     */
    $.ajax({
        url: 'https://ifconfig.me/ip',
        dataType: 'text',
        success: function (data) {
            //display block
            $("#tuxPublicIPAddress").attr('style', 'display: block !important');
            $("#tuxPublicIPAddress h4").text(data.trim());
        },
        error: function () {
            console.error('Failed to fetch external IP address');
        }
    });

    /**
     * for "tuxPublicIPDetails"
     */
    $.ajax({
        url: 'http://ip-api.com/json',
        dataType: 'json',
        success: function (data) {
            //display block
            $("#tuxPublicIPDetails .ip").text(data['query']);
            $("#tuxPublicIPDetails .zip").text(data['zip']);
            $("#tuxPublicIPDetails .countryInfo .flag-icon").addClass(`flag-icon-${data['countryCode'].toLowerCase()}`);
            $("#tuxPublicIPDetails .countryInfo span").text(
                `${data['regionName']}, ${data['countryCode']}`
            );
            $("#tuxPublicIPDetails .lon").text(data['lon']);
            $("#tuxPublicIPDetails .lat").text(data['lat']);
            $("#tuxPublicIPDetails .isp").text(data['isp']);
            $("#tuxPublicIPDetails .timezone").text(data['timezone']);

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
            url: BASE_API_URL + '/speedtestapi/',
            dataType: 'json',
            success: function (data) {
                let ping = data[0].ping
                let upload = data[0].upload
                let download = data[0].download

                $("#tuxSpeedTest .txtUpSpeed span").text(upload);
                $("#tuxSpeedTest .txtDownSpeed span").text(download);
                $("#tuxSpeedTest .txtPing").text(`Ping took about ${ping}.`);
            },
            error: function () {
                console.error('Failed to fetch external IP address');
            }
        });
    });
});