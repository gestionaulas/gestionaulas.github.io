$('#InputStartDate').dateDropper();

$('#InputEndDate').dateDropper();

function load() {
    $("#content").load("newUser.html");
  }

function cancelReserve(id,modal) {
  $( "#" + id ).empty();
  $( "#" + id ).append( "Cancelado" );
 
}

function loadReserveClassRom() {
      $("#content").load("classRoomReserve.html");  
}


  $(document).ready(function(){
    $("#login").click(function(){
      console.log("reserve");
       $("#content").load("login.html");
    });

    $('#calendar').fullCalendar({
      themeSystem: 'bootstrap4',
      defaultView: 'agendaWeek',
      locale: 'es',
      header: {
        left: 'prev,next today',
        center: 'title',
        right: 'agendaWeek'
      },
      events: 'https://fullcalendar.io/demo-events.json'
    });
    $(".nav-item").click(function(event){
      $(".nav-item").removeClass("active"); 
        $(this).addClass("active");           
      }
    );
  });