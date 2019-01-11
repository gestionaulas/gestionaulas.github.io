$('#InputStartDate').dateDropper();

$('#InputEndDate').dateDropper();

function load() {
    $("#content").load("newUser.html");
  }

function loadReserveClassRom() {
      $("#content").load("classRoomReserve.html");  
}

  $(document).ready(function(){
    $("#login").click(function(){
       $("#content").load("login.html");
    });

    $(".nav-item").click(function(event){
      $(".nav-item").removeClass("active"); 
        $(this).addClass("active");           
      }
    );
  });