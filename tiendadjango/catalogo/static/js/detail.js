$(document).ready(function() {
    $(document).on('click', '.btn-comentar', (e) => {
            var rate = 4.5;
            var com = $('#comment').val();
    
            console.log(rate, num_serie, mail, com);
        $.ajax({
            url:url_comentar,
            method:"POST",
            data:{
                csrfmiddlewaretoken: csrf_token,
                rating:rate,
                num_serie:num_serie,
                mail:mail,
                comment:com,
            },
            success: (data) => {   
                // location.reload(true);
            }
        });
    })
});