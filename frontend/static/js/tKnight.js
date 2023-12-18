
/**
 * CONSTANTS
 */

BASE_API_URL = 'http://127.0.0.1:8000/api/v1'

/**
 * fetchData
 */
function fetchData(apiUrl) {
  return new Promise(function (resolve, reject) {
    let settings = {
      "url": BASE_API_URL + apiUrl,
      "method": "GET",
      "timeout": 0,
    };

    $.ajax(settings).done(function (response) {
      resolve(response);
    }).fail(function (jqXHR, textStatus, errorThrown) {
      reject(errorThrown);
    });
  });
}


/**
 * Boottime
 */
fetchData("/sysinfo/boottime").then(function (response) {
  $("#rowBoottime h3").text(response);
}).catch(function (error) {
  console.error("Error fetching data:", error);
});

/**
 * whoami
 */
fetchData("/whoami").then(function (response) {
  $(".profile-name h5").text(response["data"]);
}).catch(function (error) {
  console.error("Error fetching data:", error);
});


/**
 * Disk Partition
 */
fetchData("/disks/usage").then(function (response) {

  let totalDiskUsageInBytes = bytesToGB(response[0]['total']);
  let usedDiskUsageInBytes = bytesToGB(response[0]['used']);
  let freeDiskUsageInBytes = bytesToGB(response[0]['free']);
  let freeDiskUsageInPercentage = response[0]['percent'];

  // Utils
  function bytesToGB(bytes) {
    if (bytes === 0) return '0 GB';
    const gigabytes = bytes / (1024 * 1024 * 1024);
    return gigabytes.toFixed(2);
  }


  if ($("#transaction-history").length) {
    var areaData = {
      labels: ["Total (GB)", "Used (GB)", "Free (GB)"],
      datasets: [{
        data: [totalDiskUsageInBytes, usedDiskUsageInBytes, freeDiskUsageInBytes],
        backgroundColor: [
          "#111111", "#00d25b", "#ffab00"
        ]
      }
      ]
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
        ctx.font = fontSize + "rem sans-serif";
        ctx.textAlign = 'left';
        ctx.textBaseline = "middle";
        ctx.fillStyle = "#ffffff";

        var text = freeDiskUsageInPercentage + "% GB",
          textX = Math.round((width - ctx.measureText(text).width) / 2),
          textY = height / 2.4;

        ctx.fillText(text, textX, textY);

        ctx.restore();
        var fontSize = 1.5;
        ctx.font = fontSize + "rem sans-serif";
        ctx.textAlign = 'left';
        ctx.textBaseline = "middle";
        ctx.fillStyle = "#ffffff";

        var texts = "Free",
          textsX = Math.round((width - ctx.measureText(text).width) / 1.7),
          textsY = height / 1.7;

        ctx.fillText(texts, textsX, textsY);
        ctx.save();
      }
    }
    var transactionhistoryChartCanvas = $("#transaction-history").get(0).getContext("2d");
    var transactionhistoryChart = new Chart(transactionhistoryChartCanvas, {
      type: 'doughnut',
      data: areaData,
      options: areaOptions,
      plugins: transactionhistoryChartPlugins
    });
  }

});


/**
 * Disk Partition
 */
fetchData("/disks/partition").then(function (response) {
  var tbody = $("#rowDiskPartition tbody");

  $.each(response["data"], function (index, item) {
    var newRow = $("<tr>");

    // Append cells to the row
    newRow.append("<td>" + item["Filesystem"] + "</td>");
    newRow.append("<td>" + item["Size"] + "</td>");
    newRow.append("<td>" + item["Used"] + "</td>");
    newRow.append("<td>" + item["Avail"] + "</td>");
    newRow.append("<td>" + item["Use%"] + "</td>");
    newRow.append("<td>" + item["Mounted on"] + "</td>");
    newRow.append("</tr>");

    // Append the row to the tbody
    tbody.append(newRow);
  });
});


/**
 * processes
 */
fetchData("/processes/").then(function (response) {
  var tbody = $("#processes tbody");

  $.each(response["data"], function (index, item) {
    var newRow = $("<tr>");

    // Append cells to the row
    newRow.append("<td>" + item["pid"] + "</td>");
    newRow.append("<td>" + item["process_name"] + "</td>");
    newRow.append("<td>" + item["terminal"] + "</td>");
    newRow.append("<td>" + item["num_threads"] + "</td>");
    newRow.append("<td>" + item["created_time"] + "</td>");
    newRow.append("<td>" + item["status"] + "</td>");
    newRow.append("<td>" + item["username"] + "</td>");
    newRow.append("</tr>");

    // Append the row to the tbody
    tbody.append(newRow);
  });
});