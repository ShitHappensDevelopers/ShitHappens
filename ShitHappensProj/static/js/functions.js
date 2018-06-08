// function to add eventlisteners on DOM elements 
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


// this code make copy link button work. It add event listeners to buttons 
//to show and hide needed functionality
var optbuttns = document.querySelectorAll(".mystoryoptionsbtn");
Array.prototype.forEach.call(optbuttns, function(optbuttn) {
    var element= optbuttn.parentNode.querySelector(".myoptionscon");
            addListener(optbuttn,"click", function() {
              element.classList.toggle("myoptionsconhidden");
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


var copybuttns = document.querySelectorAll(".mycopylinkbut");
Array.prototype.forEach.call(copybuttns, function(copybuttn) {
    var element= copybuttn.parentNode.parentNode.querySelector(".myidlink");
            addListener(copybuttn,"click", function() {
              element.select();
              document.execCommand('copy');
            });
});