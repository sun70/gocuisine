$(document).ready(function(){
	
	$(".clicable_text").click(function(){
		if($(".clicable_text").hasClass("active")){
			$(".offers").fadeOut();
			$(".offer_zone").animate({"width":"40"});
			$(this).removeClass("active");
		}else{
			$(".offers").fadeIn();
			$(".offer_zone").animate({"width":"550"});
			$(this).addClass("active");
		}
	});
	
	$(".closers").click(function(){
		$(".offers").fadeOut();
		$(".offer_zone").animate({"width":"40"});
		$(this).removeClass("active");
	});
	
	$(".tba_pluss").click(function(){
		$(".multicity_popup").fadeIn();
	});
	
	$(".btna button").click(function(){
		$(".multicity_popup").fadeOut();
	});
	
	// date picker--------------
	
$.datetimepicker.setLocale('en');

$('#datetimepicker,#datetimepicker1,#datetimepicker2,#datetimepicker3').datetimepicker({
dayOfWeekStart : 1,
lang:'en',
disabledDates:['1986/01/08','1986/01/09','1986/01/10'],
startDate:	'1986/01/05'
});
$('#datetimepicker,#datetimepicker1,#datetimepicker2,#datetimepicker3').datetimepicker({value:'2015/04/15 05:03',step:10});

$('.some_class').datetimepicker();

	
	
	
});
	