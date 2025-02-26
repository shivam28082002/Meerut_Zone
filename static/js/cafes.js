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



$(document).on('change', '#id_email', function(){
    let email = $('#id_email').val();
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
                if(response.success){
                    $('#emailtext').text('Email is already registered.');
                } else {
                    $('#emailtext').text('Email is available.');
                }
            },
            error: function(){
                $('#emailtext').text('An error occurred. Please try again.');
            }
        });
    }
});




$(document).ready(function(){
    $('#hospital_search').on('click', function(){
        let categories = $('#categories').val();
        let hospital_name = $('#hospital_name').val();
        console.log("Clicked", hospital_name);
        if(categories || hospital_name ){
            $.ajax({
                url: '/data_cafes/',
                type: 'POST',
                data: {
                    hospital_name: hospital_name,
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
