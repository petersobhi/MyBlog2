function callEdit(id){
		var subject = $("#post-"+id+" #subject").text();
		var body = $("#post-"+id+" #body").text();
		$("#editModal #subject").val(subject);
		$("#editModal #body").val(body);
		//$("#edit-btn").attr("onclick","editPost("+id+")");
		$("#edit-form").attr("onsubmit","return editPost("+id+")");
	}

	function callDelete(id){
		$("#delete-btn").attr("onclick","deletePost("+id+")");
	}


	function sendPost(){
		var subject = $("#subject").val();
		var body = $("#body").val();
		var data = {'action': 0,
					'subject': subject,
					'body': body };
		socket.send(JSON.stringify(data));
		$("#subject").val('');
		$("#body").val('');
		return false; // to prevent the actual form from making request
	}

	function editPost(id){
		var subject = $("#editModal #subject").val();
		var body = $("#editModal #body").val();
		var data = {'action': 1,
					'post_id': id,
					'subject': subject,
					'body': body };
		socket.send(JSON.stringify(data));
		$('#editModal').modal('hide'); // hide modal
		return false; // to prevent the actual form from making request
	}

	function deletePost(id){
		var data = {'action': 2,
					'post_id': id};
		socket.send(JSON.stringify(data));
	}

	function recieveData(data){
		if (data.action == 0){ // add post
			postHtml = '<div class="post" id="post-'+data.post_id+'">' +
					   '<h2 id="subject">' + data.subject + '</h2>' +
					   '<p id="body">' + data.body + '</p>';
					   

			if (username == data.username){
				postHtml += '<div class="action-buttons">' +
						'<button type="button" id="edit_button" class="btn btn-default btn-md"' +
				  		'data-toggle="modal" data-target="#editModal" onclick="callEdit('+data.post_id+')">' +
				  		'<span class="glyphicon glyphicon-pencil" aria-hidden="true"></span></button>' +
						' <button type="button" class="btn btn-danger btn-md" data-toggle="modal"'+
						'data-target="#deleteModal" +  onclick="callDelete('+data.post_id+')">' +
						'<span class="glyphicon glyphicon-trash" aria-hidden="true"></span></button></div>'
				
			}

			postHtml += '<h4 class="text-right"> by ' + data.username;
			if (username == data.username){
				postHtml += ' (you)';
			}
			postHtml += '</h4><hr></div>'
			$(postHtml).hide().prependTo(".posts").fadeIn();
		}

		else if (data.action == 1){ // edit post
			console.log('data.action = edit')
			$("#post-"+data.post_id+" #subject").text(data.subject);
			$("#post-"+data.post_id+" #body").text(data.body);
		}

		else{ // delete post
			$("#post-"+data.post_id).hide('slow', function(){ $target.remove(); });
		}
	}
		

	socket = new WebSocket("ws://" + window.location.host + "/chat/");
	socket.onmessage = function(e) {
		console.log(e);
	    recieveData(JSON.parse(e.data));
	}
	
	if (socket.readyState == WebSocket.OPEN) socket.onopen();