
function time_of_day(hour,minute,am_pm){
	var a = "";
	var b = "";
	if (minute > 30){
		var a = "It's almost ";
	}
	else if (minute == 30){
		var a = "It's";
	}
	else{
		var a = "It's just after ";
	}
	if (am_pm == "am"){
		var b = " in the morning.";
	}
	else if(am_pm == "pm"){
		var b = " in the evening.";
	}
	else{
		return "invalid input."
	}	
	console.log(a+hour+b)
}