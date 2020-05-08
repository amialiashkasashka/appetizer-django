$(document).on('submit', '#contact-form', function(e){
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: "{% url 'contact' %}",
        data: {
            name:$('#name').val(),
            email:$('#email').val(),
            header:$('#header').val(),
            message:$('#messagee').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(){
            
        }
    });
});