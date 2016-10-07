$(function () {
	$('.launch.button').click(
      function(event){
        $('.styled.sidebar')
        .sidebar('toggle');
      });

	$('.fade.button').click(
      function(event){
        $('.styled.sidebar')
        .sidebar('toggle');
      });

	$(".launch.button").mouseenter(function(){
		$(this).stop().animate({width: '140px'}, 300, 
             function(){$(this).find('.text').show();});
	}).mouseleave(function (event){
		$(this).find('.text').hide();
		$(this).stop().animate({width: '70px'}, 300);
	});

  $(".teal.fluid.button").on("click", function(){
    $("input[type='submit']").trigger('click');
  });

});

