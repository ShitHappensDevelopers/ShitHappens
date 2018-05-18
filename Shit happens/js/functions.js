
function addListener(element, eventName, handler) {
    if (element.addEventListener) {
      element.addEventListener(eventName, handler, false);
    }
    else if (element.attachEvent) {
      element.attachEvent('on' + eventName, handler);
    }
    else {
      element['on' + eventName] = handler;
    }
}


var optbuttns = document.querySelectorAll(".mystoryoptionsbtn");

Array.prototype.forEach.call(optbuttns, function(optbuttn) {
    var element= optbuttn.parentNode.querySelector(".myoptionscon");
            addListener(optbuttn,"click", function() {
                if(element.style.display  == "none"){
                    element.style.display = "block";
                }
                else
                {
                    element.style.display =  "none";
                }
            });
});




// this code helps to toggle window for setting story lifetime
$('#myStoryLife').change(function() {
	$('#mySetStoryLife').toggle(300);
}); 


// for textarea to resize automatically
$('#myWriteStoryTxtAr').on("input", function() {
	// var textArea = $('#myWriteStoryTxtAr');
	this.style.height = 0;
	this.style.height = this.scrollHeight + 'px';
	// this.style.height = this.scrollHeight + (textArea.outerHeight() - textArea.height()) / 2 + 'px';
});