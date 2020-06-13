$("document").ready(function () {
    var id;
    //console.log("hello world!");
    $(".like").on("click", function () {
        // console.log("click!!!")
        let id = $(this).attr("id");
        // console.log(id);
        $.ajax("/hello/ajax/add_likes",
            {"data":{"id":id},
                    "method":"get",
                    "success":function (data) {
                        //console.log(data);
                        $("#" + id).html("Likes: " + data)

            }})

    })

});
