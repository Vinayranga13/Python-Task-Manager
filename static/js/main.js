$(document).ready(function() {
    $('.task-item').each(function(index) {
        $(this).addClass('animate__animated animate__fadeInLeft');
    });

    $('.delete-task').on('click', function(e) {
        e.preventDefault();
        const taskElement = $(this).closest('.task-item');
        taskElement.addClass('animate__fadeOutRight');

        setTimeout(function() {
            taskElement.find('form').submit();
        }, 500); 
    });

    $('a').on('click', function(e) {
        const href = $(this).attr('href');
        if (href && !$(this).hasClass('prevent-default')) {
            e.preventDefault();
            $('body').addClass('animate__fadeOut');
            setTimeout(function() {
                window.location.href = href;
            }, 500); // Delay for animation
        }
    });

    $('.add-task').on('click', function() {
        $('.task-form').addClass('animate__animated animate__bounceIn');
    });
});
