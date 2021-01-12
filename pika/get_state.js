    ws = new WebSocket("ws://127.0.0.1:8866")
    //ws = new WebSocket("ws://192.168.11.65:12345/send_graph")
    var request_data_interval

	var dps_xy = [];
    var dps_xz = [];
    var dps_yz = [];
    var dataLength = 30;
    var chart

    ws.onopen = function()
    {
        // Web Socket is connected, send data using send()
        ws.send("Message to send");
		// 500 : millsec
        request_data_interval = window.setInterval(requestData, 50);

    };
		
    ws.onmessage = function (evt) 
    { 
        var received_msg = evt.data;
        //console.log(received_msg)
        data = JSON.parse(evt.data);
        console.log(data)

		dps_xy.push({x: data.x, y:data.y})
        dps_xz.push({x: data.x, y:data.z})
        dps_yz.push({x: data.y, y:data.z})
        
        if (dps_xy.length > dataLength) {
            dps_xy.shift();
            dps_xz.shift();
            dps_yz.shift();
        }
		
		chart_xy.render();
        chart_xz.render();
		chart_yz.render();

		
    };
		
    ws.onclose = function()
    { 
      // websocket is closed.
      window.clearInterval(request_data_interval)
    };
    
    function requestData()
    {
        ws.send("get-data");
    }