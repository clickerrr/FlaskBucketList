
$(document).ready(function()
{
  var clicked;
  $(".removeItemButton").click(function()
  {
    clicked = $(this).attr("id");
    req = $.ajax({
      type : 'POST',
      url : "/removePost",
      data : JSON.stringify({'data':clicked}, null, '\t')
    });
    
    $("#item"+$(this).attr("id")).remove();
    
    
  });
  
  
  
  $("#new-post-submit").click(function()
  {
    title = $("#new-post-title").val();
    content = $("#new-post-content").val();
    
    if( !title )
    {
      $("#titleError").css("display", "flex");
    }
    else
    {
      $("#titleError").css("display", "none");
      req = $.ajax({
        type : 'POST',
        url : "/newPost",
        data : JSON.stringify({'title':title, 'content': content}, null, '\t')
      });
      
      req.done(function(data) {
        
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
          req = $.ajax({
            type : 'POST',
            url : "/removePost",
            data : JSON.stringify({'data':clicked}, null, '\t')
          });
          
          $("#item"+$(this).attr("id")).remove();
          
          
        });
        
        $("#new-post-title").val("");
        $("#new-post-content").val("");
        
        
      });
      
      
      
    }
    
    
  });
  
  
  
  
  
  
});