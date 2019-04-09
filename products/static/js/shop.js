$(function(){
    $('#calculation').click(function(event) {

        event.preventDefault();

        let userWeight = $("#userWeight").val();
        $.ajax({
            type: 'POST',
            data: {'userWeight': userWeight ,
                    'csrfmiddlewaretoken': getCookie('csrftoken')
                   },

            success: function()
            {
                $( "#CalculationState" ).append('<div class="alert alert-success" role="alert">Your calculation is done</div>');

            },
            error: function() {
                $( "#CalculationState" )
                .append('<div class="alert alert-danger" role="alert">For some reason we can not do calculation!</div>');
            },
            url: './calculate/',
            cache: false
        });
        return false;
    });
}

);

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');