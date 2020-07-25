$(document).ready(function(){

    // scroll bar
    $(window).on('scroll', function(){
        if($(window).scrollTop() > 150){
            $('nav').addClass('navbar-fixed-top')
        }
        else{
            $('nav').removeClass('navbar-fixed-top')
        }
    })

    // owl carousel

    $('.owl-carousel').owlCarousel({
        rtl: false,
        loop: false,
        margin: 5,
        width: 100,
        items: 1,
        nav: true,
        dots: true
    });

        // var messageElement = document.getElementById('messageId')
        setTimeout(() => {
            $('.alert').fadeOut();
        }, 3000);


})

// copy bitcoin address
function copyBTClink(){

    var bitcoin_link = document.getElementById('wallet-id');
    console.log(bitcoin_link);

    bitcoin_link.select();
    bitcoin_link.setSelectionRange(0, 99999);
    document.execCommand('copy');

    var tooltip = document.getElementById('myTooltip');
    tooltip.innerHTML = 'Copied: ' + bitcoin_link.value
}

function outFunc(){
    var tooltip = document.getElementById('myTooltip')
    tooltip.innerHTML = ''
}

// function loader(){
//     $('#loading').show();
// }

// $(
//     $.ajax({
//         url: '/', 
//         type: 'GET', 
//         beforeSend:  $('#loading').show(),
//         complete : $('#loading').hide(), 
//         success : function(){
//             // return null;
//         }
//     })
// )


