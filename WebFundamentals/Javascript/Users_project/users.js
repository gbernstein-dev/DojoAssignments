$(document).ready(function(){
	$("#user_form").submit(function(){

		var form_data = document.getElementById("user_form");
		for(var i=0;i<form_data.elements.length-1;i++){
			console.log(form_data[i].value);
			// if(i=0){
			// 	$("#user_table").last().append("<tr><td>"+form_data[i].value+"</td>");
			// }
			// else if(i=form_data.elements.length-3){
			// 	$("#user_table").last().append("<td>"+form_data[i].value+"</td></tr>");
			// }
			// else{
			// 	$("#user_table").last().append("<td>"+form_data[i].value+"</td>");
			// }
		}

		// lazy way to do it
		// $("#user_table").last().append("<tr><td>"+user_form.first_name.value+"</td><td>"+user_form.last_name.value+"</td><td>"+user_form.email.value+"</td><td>"+user_form.contact.value+"</td></tr>")
		return false;
	});
});