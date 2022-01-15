alertify.set('notifier', 'position', 'bottom-right');

if ($('.d-none.message').length) {
    const message = $('.d-none.message');
    alertify.notify(message.text(), message.data('status'), 10)
}


if (window.location.hash == '#cart') {
    $('.cart-btn').click()
}

$('.icofont-logout').on('click', function () {
    $('form.logout-form').submit();
});

var subscribe = function (pk) {
    $.ajax({
        url: $('.news-form').attr('data-url'),
        method: 'POST',
        data: {
            'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val(),
            'email': $('.sub-email').val()
        },
        success: function (data) {
            alertify.alert(data.message);
        }
    })
}