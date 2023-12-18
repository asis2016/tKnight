
/**
 * fetchData
 */
function fetchData(apiUrl) {
  return new Promise(function (resolve, reject) {
    let settings = {
      "url": "http://127.0.0.1:8000/api/v1" + apiUrl,
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
 * processes
 */
fetchData("/processes/environ").then(function (response) {
  var tbody = $("#environ tbody");

  $.each(response, function (index, item) {

    // Access each item in the array
    $.each(item, function (key, value) {
      var newRow = $("<tr>");
      newRow.append("<td>" + key + "</td>");
      newRow.append("<td>" + value + "</td>");
      newRow.append("</tr>");

      tbody.append(newRow);
    });
  });
});