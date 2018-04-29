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