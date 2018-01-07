$(document).ready(function(){

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


    $(document).on('click', '.task-box', function(){
      var t_id = $(this).attr('id');
      var element = this;

      $.ajax({
        type: "POST",
        url: '/chronos/toggle_completion/',
        data: {
          't_id': t_id,
          'csrfmiddlewaretoken': getCookie('csrftoken'),
        },
        dataType: 'json',
      });
    });

    $('.add-task').click(function(){
        var cat_id = $(this).attr('id');
        var element = this;
        var task_name = $(this).parent().prev().children('input').val();

        $.ajax({
            type: "POST",
            url: "/chronos/add_task/",
            data: {
                "cat_id": cat_id,
                "task_name": task_name,
                'csrfmiddlewaretoken': getCookie('csrftoken'),
            },
            dataType: 'json',
            success: function(data){
                if(data.task_added){
                    var taskHTML = document.createElement('div');
                    var taskLabel = document.createElement('label');
                    var checkbox = document.createElement('input');
                    var t_id = 'tid_' + data.t_id;
                    
                    $(taskHTML).addClass('md-checkbox');
                    $(checkbox).attr('type', 'checkbox').attr('id', t_id).addClass('task-box');
                    $(taskLabel).addClass('is-size-6').attr('for', t_id).html(task_name);
                    $(taskHTML).append(checkbox);
                    $(taskHTML).append(taskLabel);
                    $(element).closest('.card-footer').prev().children('.content').append(taskHTML);
                }
            }
        }); 

    });



    $('.navbar-burger').click(function(){
        $(this).toggleClass('is-active');
        $('#navbarMenuHeroB').toggleClass('is-active');
    });

    $('.toggle-add').click(function(){
        $(this).toggleClass('hidden');
        $(this).next().toggleClass('hidden');
    });

    $('.cancel-button').click(function(){
        $(this).closest('.task-form').toggleClass('hidden');
        $(this).closest('.task-form').prev().toggleClass('hidden');
    });

});