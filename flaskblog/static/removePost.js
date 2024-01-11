
$(document).ready(function()
{
  var clicked;
  $(".removeItemButton").click(function()
  {
    clicked = $(this).attr("id");

    $.post("/removePost", JSON.stringify({'data':clicked}, null, '\t'))
    
    $("#item"+$(this).attr("id")).remove();
    
    
  });
  
  
  
  $("#new-post-submit").click(function()
  {
    title = $("#new-post-title").val();
    content = $("#new-post-content").val();
    
    if( !title )
    {
      $("#titleError").removeClass("d-none");
    }
    else
    {
      $("#titleError").addClass("d-none");

      $.post("/newPost", JSON.stringify({'title':title, 'content': content}, null, '\t')).done( function(data)
      {
        postDiv = document.createElement("div");
        postDiv.classList.add("row");
        postDiv.classList.add("mb-4");
        postDiv.id = "item" + data.id;

        postSubDiv1 = document.createElement("div");
        postSubDiv1.classList.add("p-2");
        postSubDiv1.classList.add("text-center");
        postSubDiv1.classList.add("col-lg-2");
        postSubDiv1.id = "item" + data.id;

        postTitle = document.createElement("h4");
        postTitle.id = "title" + data.id;
        postTitle.classList.add("post-title");

        postContent = document.createElement("p");
        postContent.id = "content" + data.id;
        postContent.classList.add("post-content");


        postContentDiv = document.createElement("div");
        postContentDiv.classList.add("col-lg-6");
        postContentDiv.classList.add("m1");
        postContentDiv.classList.add("p-3");

        button = document.createElement("button");
        button.id = data.id;
        button.classList.add("btn");
        button.classList.add("btn-success");
        button.classList.add("removeItemButton");

        postSubDiv1.append(postTitle);
        postSubDiv1.append(button);
        postContentDiv.append(postContent);

        postDiv.append(postSubDiv1);
        postDiv.append(postContentDiv);

        hr = document.createElement("hr");
        postDiv.append(hr);


        $("#item-list").append(postDiv);
        $("#" + data.id).text("Mark As Done");
        $("#title" + data.id).text(title);
        $("#content" + data.id).text(content);

        console.log($("#item-list").children().length)
        if ($("#item-list").children().length >= 2)
        {
          $("#no-items-yet-container").addClass("d-none");
        }


        var clicked;
        $("#" + data.id).click(function()
        {
          clicked = $(this).attr("id");
          $.post("/removePost", JSON.stringify({'data':clicked}, null, '\t'))
          $("#item"+$(this).attr("id")).remove();

            console.log($("#item-list").children().length)
            if($("#item-list").children().length == 1)
            {
                $("#no-items-yet-container").removeClass("d-none");
            }


        });

        $("#new-post-title").val("");
        $("#new-post-content").val("");

      })

      
      /*req.done(function(data)
      {
        
        postDiv = document.createElement("div");
        postDiv.classList.add("list-item");
        postDiv.id = "item" + data.id;
        
        postTitle = document.createElement("h4");
        postTitle.id = "title" + data.id;
        postTitle.classList.add("post-title");
        
        postContent = document.createElement("p");
        postContent.id = "content" + data.id;
        postContent.classList.add("post-content");
        
        button = document.createElement("button");
        button.id = data.id;
        button.classList.add("removeItemButton");
        
        postDiv.append(button);
        postDiv.append(postTitle);
        postDiv.append(postContent);
        
        $(".bucket-list-container").append(postDiv);
        $("#" + data.id).text("Mark As Done");
        $("#title" + data.id).text(title);
        $("#content" + data.id).text(content);
        
        if ($('.no-items-yet').length)
        {
          $(".no-items-yet").remove();
        }
        
        
        var clicked;
        $("#" + data.id).click(function()
        {
          clicked = $(this).attr("id");
          $.post("/removePost", JSON.stringify({'data':clicked}, null, '\t'))
          $("#item"+$(this).attr("id")).remove();
          
          
        });
        
        $("#new-post-title").val("");
        $("#new-post-content").val("");
        
        
      });*/
      
      
      
    }
    
    
  });
  
  
  
  
  
  
});