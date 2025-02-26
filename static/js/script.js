// id_email


// $(document).on('input', '#id_email',function(){
//     email = $('#id_email').val()
//     console.log(email,"Hiiiii");
//     if (email){
//         $.ajax({
//             url : '/check_email/',
//             type : 'POST',
//             data : email,
//             success : function(response){
//                 $('#emailtext').text()
//             },
//         })
//     }
// })

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
        }
    }
}
return cookieValue;
}



$(document).on('input', '#email_check', function(){
    let email = $('#email_check').val();
    console.log(email, "Hiiiii");
    if (email){
        $.ajax({
            url: '/check_email/',
            type: 'POST',
            data: {
                'email': email,
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function(response){
                console.log(response );
                if(response.success){
                    $('#error_email').text('');
                } else {
                    $('#error_email').text('Email is not registered.');
                }
            },
            error: function(){
                $('#emailtext').text('An error occurred. Please try again.');
            }
        });
    }
});



$(document).on('input', '#id_email_signup', function(){
    let email = $('#id_email_signup').val();
    console.log(email, "Hiiiii");
    if (email){
        $.ajax({
            url: '/check_email/',
            type: 'POST',
            data: {
                'email': email,
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function(response){
                console.log(response );
                if(response.success){
                    $('#emailtext').text('Email is already registered.');
                } else {
                    $('#emailtext').text('');
                }
            },
            error: function(){
                $('#emailtext').text('An error occurred. Please try again.');
            }
        });
    }
});



$(document).ready(function(){
    $('#categories').on('change', function(){
        let categories = $('#categories').val();
        if (categories == 'select'){
            window.location.reload()
        }
        console.log(categories);
        if(categories){
            $.ajax({
                url: '/data_hospital/',
                type: 'POST',
                data: {
                    categories: categories, 
                    "csrfmiddlewaretoken": getCookie("csrftoken"),
                },
                success: function(response){
                    console.log(response);
                    updateHospitalList(response.hospital);
                }
            });
        }
    });
});

function updateHospitalList(hospitals) {
    let appendShow = $('#append_show');
    appendShow.empty(); // Clear existing content

    hospitals.forEach(function(hospital) {
        let hospitalHTML = `
            <div class="col-lg-4 col-md-2">
                <div class="icon-box" style="margin-top: -10%;">
                    <img class="img-fluid-1" src="${hospital.file}" alt="placeholder"> <br>
                    <br>
                    <h4><b>${hospital.name}</b></h4>
                    <p><b>${hospital.address}</b></p>
                    <a href="${hospital.location}" style="margin-right: 10px;">
                        <svg xmlns="http://www.w3.org/2000/svg" style="width: 32px; height: 32px;" fill="currentColor" class="bi bi-geo-alt" viewBox="0 0 16 16">
                            <path d="M12.166 8.94c-.524 1.062-1.234 2.12-1.96 3.07A32 32 0 0 1 8 14.58a32 32 0 0 1-2.206-2.57c-.726-.95-1.436-2.008-1.96-3.07C3.304 7.867 3 6.862 3 6a5 5 0 0 1 10 0c0 .862-.305 1.867-.834 2.94M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10"/>
                            <path d="M8 8a2 2 0 1 1 0-4 2 2 0 0 1 0 4m0 1a3 3 0 1 0 0-6 3 3 0 0 0 0 6"/>
                        </svg>
                    </a>
                </div>            
            </div>`;
        appendShow.append(hospitalHTML);
    });
}




$(document).ready(function () {
  $(".rating-component .star").on("mouseover", function () {
      var onStar = parseInt($(this).data("value"), 10); //
      $(this).parent().children("i.star").each(function (e) {
          if (e < onStar) {
              $(this).addClass("hover");
          } else {
              $(this).removeClass("hover");
          }
      });

  }).on("mouseout", function () {
      $(this).parent().children("i.star").each(function (e) {
          $(this).removeClass("hover");
      });
  });

  // Set rating value on star click
  $(".rating-component .stars-box .star").on("click", function () {
      var onStar = parseInt($(this).data("value"), 10);
      var stars = $(this).parent().children("i.star");
      var ratingMessage = $(this).data("message");

      var msg = "";
      if (onStar > 1) {
          msg = onStar;
      } else {
          msg = onStar;
      }
      $('.rating-component .starrate .ratevalue').val(msg);

      $(".fa-smile-wink").show();

      $(".button-box .done").show();

      if (onStar === 5) {
          $(".button-box .done").removeAttr("disabled");
      } else {
          $(".button-box .done").attr("disabled", "true");
      }

      for (i = 0; i < stars.length; i++) {
          $(stars[i]).removeClass("selected");
      }

      for (i = 0; i < onStar; i++) {
          $(stars[i]).addClass("selected");
      }

      $(".status-msg .rating_msg").val(ratingMessage);
      $(".status-msg").html(ratingMessage);
      $("[data-tag-set]").hide();
      $("[data-tag-set=" + onStar + "]").show();
  });

  // Handle tag selection
  $(".feedback-tags").on("click", function () {
      var choosedTagsLength = $(this).parent("div.tags-box").find("input").length;
      choosedTagsLength = choosedTagsLength + 1;

      if ($(this).hasClass("choosed")) {
          $(this).removeClass("choosed");
          choosedTagsLength = choosedTagsLength - 2;
      } else {
          $(this).addClass("choosed");
          $(".button-box .done").removeAttr("disabled");
      }

      console.log(choosedTagsLength);

      if (choosedTagsLength <= 0) {
          $(".button-box .done").attr("enabled", "false");
      }
  });

  // Show compliment container on click
  $(".compliment-container .fa-smile-wink").on("click", function () {
      $(this).fadeOut("slow", function () {
          $(".list-of-compliment").fadeIn();
      });
  });

  // Submit review data to backend
  $(".done").on("click", function () {
    var formData = {
        'user': $('#name_id').val(),
        'post': 'PostID',
        'rating': $('.ratevalue').val(),
        'comment': $('input[name=comment]').val(),
        'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
    };
    console.log(formData);
    $.ajax({
        type: 'POST',
        url: '/review/',
        data: formData,
        success: function (response) {
            console.log(response);
            if (response.success) {
                window.location.reload()
            } else {
                alert(response.message);
            }
        },
        error: function (xhr, status, error) {
            alert(xhr.responseText);
        }
    });

    return false;
});







});
