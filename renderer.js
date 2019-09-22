// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// All of the Node.js APIs are available in this process.

const serialport = require('serialport')
const createTable = require('data-table')

serialport.list((err, ports) => {
  //port_list = menu.popup(options)
  const headers = Object.keys(ports[0])
  const table = createTable(headers)
  tableHTML = ''
  let usable_ports = []
  for (let x = 0; x < ports.length; x++) {
    if(ports[x]["manufacturer"] == "FTDI"){
      usable_ports.push(ports[x]["comName"])  
    }
  }

  let selected_port = 0;
  usable_ports = ["dsa,mnds,","dsajhdsah"]
  
  if(usable_ports.length>0){
    document.getElementById("port_selected").innerHTML = usable_ports[selected_port];
  }
  else{
    document.getElementById("port_selected").innerHTML = "Connect Robot Cing to PC and make sure that green light is turned on.";
  }

})
