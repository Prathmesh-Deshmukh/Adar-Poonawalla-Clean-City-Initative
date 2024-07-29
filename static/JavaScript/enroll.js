function enroll(eventId) {
    $.ajax({
      type: "POST",
      url: "/enroll/",
      data: {
        'event_id': eventId,
        'csrfmiddlewaretoken': '{{ csrf_token }}'
      },
      dataType: "json",
      success: function(response) {
        if (response.success) {
          alert("Enrolled successfully!");
        } else {
          alert("Error enrolling, please try again later.");
        }
      },
      error: function(xhr, errmsg, err) {
        alert("Error enrolling, please try again later.");
      }
    });
  }
  