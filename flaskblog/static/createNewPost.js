window.onload = function()
{


    $("#new-post-accept-button").click(function() {

        $("#new-post-container").removeClass("d-none");
        $("#new-post-button-container").addClass("d-none");

    })

    $("#new-post-submit").click(function() {


        if($("#new-post-title").val())
        {            
            $("#new-post-container").addClass("d-none");
            $("#new-post-button-container").removeClass("d-none");
        }
    })

};



