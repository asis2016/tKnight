/**
 * CONSTANTS
 */
const BASE_API_URL = 'http://127.0.0.1:9001';
const WS_BASE_API_URL = 'ws://127.0.0.1:8000';

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
    // $.ajax({
    //     url: BASE_API_URL + '/whoami/',
    //     dataType: 'JSON',
    //     success: function (response) {
    //         $('.tuxProfileName span').text(response['result']);
    //     },
    //     error: function () {
    //         console.error("Error fetching data:", error);
    //     }
    // });

    

    /**
     * GET ifconfig
     * And scanMyPorts
     */
    // $.ajax({
    //     url: BASE_API_URL + '/ifconfig/',
    //     dataType: 'JSON',
    //     success: function (data) {

    //         let inet = data['result']['inet'];
    //         let inet6 = data['result']['inet6'][0];
    //         let ether = data['result']['ether'];
    //         let netmask = data['result']['netmask'];
    //         let broadcast = data['result']['broadcast'];
    //         let device = data['result']['device'];

    //         $('#scanMyPorts').attr('href', '/scan-port?hostname=' + inet);

    //         //For ifconfig-and-users-stat.html
    //         $('#ifconfigAndUserStat .ipv4').text(inet);
    //         $('#ifconfigAndUserStat .ipv6').text(inet6);
    //         $('#ifconfigAndUserStat .netmask').text(netmask);
    //         $('#ifconfigAndUserStat .broadcast').text(broadcast);
    //         $('#ifconfigAndUserStat .ether').text(ether);
    //         $('#ifconfigAndUserStat .device').text(device);

    //     },
    //     error: function () {
    //         console.error('Failed to fetch external IP address');
    //     }
    // });

});
