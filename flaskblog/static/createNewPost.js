window.onload = function()
{


    $("#newPostAcceptButton").click(function() {

        $(".new-post").css('display', 'flex');
        $(".create-new-post-button").css('display','none');

    })

    $("#new-post-submit").click(function() {


        if($("#new-post-title").val())
        {            
            $(".new-post").css('display', 'none');
            $(".create-new-post-button").css('display','flex');
        }
    })

};



